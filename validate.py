#!/usr/bin/env python3
from pathlib import Path
import sys, json, hashlib, yaml

try:
    from jsonschema import Draft202012Validator
    from referencing import Registry, Resource
except Exception as exc:
    print("EF CANON VALIDATION: FAIL")
    print("- required validation dependency unavailable:", exc)
    sys.exit(1)

ROOT = Path(__file__).resolve().parent
errors = []
parsed_docs = {}
resolved_locators = set()
resource_docs_validated = set()

def relpath(path):
    return Path(path).relative_to(ROOT).as_posix()

def parse_active(rel):
    if rel in parsed_docs:
        return parsed_docs[rel]
    p = ROOT / rel
    if not p.exists():
        errors.append(f"missing active file: {rel}")
        return None
    try:
        if p.suffix.lower() == ".json":
            obj = json.loads(p.read_text(encoding="utf-8"))
        elif p.suffix.lower() in (".yaml", ".yml"):
            obj = yaml.safe_load(p.read_text(encoding="utf-8"))
        else:
            obj = None
        parsed_docs[rel] = obj
        return obj
    except Exception as exc:
        errors.append(f"{rel}: parse error: {exc}")
        return None

# Bootstrap parse.
manifest = parse_active("manifest.yaml")
registry = parse_active("registry.yaml")
if not isinstance(manifest, dict) or not isinstance(registry, dict):
    print("EF CANON VALIDATION: FAIL")
    for e in errors:
        print("-", e)
    sys.exit(1)

active = manifest.get("active_files", [])
active_set = set(active)

# Parse every active YAML/JSON declaration (EF-R4-001).
for rel in active:
    p = ROOT / rel
    if p.suffix.lower() in (".json", ".yaml", ".yml"):
        parse_active(rel)

# Load canonical schemas into a local registry.
schema_registry = Registry()
schema_objs = {}
for p in sorted((ROOT / "schemas").glob("*.json")):
    rel = relpath(p)
    obj = parsed_docs.get(rel)
    if obj is None:
        obj = parse_active(rel)
    if not isinstance(obj, dict):
        continue
    schema_objs[rel] = obj
    rid = obj.get("$id")
    try:
        resource = Resource.from_contents(obj)
        if rid:
            schema_registry = schema_registry.with_resource(rid, resource)
        schema_registry = schema_registry.with_resource(p.name, resource)
        schema_registry = schema_registry.with_resource(rel, resource)
    except Exception as exc:
        errors.append(f"{rel}: cannot register schema: {exc}")

def validate_instance(instance, schema_rel, label):
    schema = schema_objs.get(schema_rel)
    if schema is None:
        errors.append(f"{label}: missing canonical schema {schema_rel}")
        return
    try:
        validator = Draft202012Validator(schema, registry=schema_registry)
        for err in sorted(validator.iter_errors(instance), key=lambda e: list(e.absolute_path)):
            path = ".".join(str(x) for x in err.absolute_path)
            errors.append(f"{label}: schema error at {path or '<root>'}: {err.message}")
    except Exception as exc:
        errors.append(f"{label}: schema validation failure: {exc}")

# Local schema validation.
validate_instance(registry, "schemas/registry.schema.json", "registry.yaml")

contracts = {}
for rel in sorted(x for x in active if x.startswith("contracts/") and x.endswith(".yaml")):
    c = parsed_docs.get(rel)
    if isinstance(c, dict):
        contracts[rel] = c
        validate_instance(c, "schemas/contract.schema.json", rel)

# Validate typed normative resource documents.
resource_type_schemas = manifest.get("resource_type_schemas", {})
for rel, schema_rel in resource_type_schemas.items():
    obj = parsed_docs.get(rel)
    if obj is None:
        obj = parse_active(rel)
    if obj is not None:
        validate_instance(obj, schema_rel, rel)
        resource_docs_validated.add(rel)

# Generic resource-descriptor uniqueness + recursive locator resolution.
def resolve_locator(source_rel, locator):
    if not locator:
        errors.append(f"{source_rel}: empty locator")
        return None
    target = ROOT / locator
    resolved_locators.add((source_rel, locator))
    if not target.exists():
        errors.append(f"{source_rel}: dangling locator {locator}")
        return None
    if locator not in active_set:
        errors.append(f"{source_rel}: locator target is not active: {locator}")
    if target.suffix.lower() in (".json", ".yaml", ".yml"):
        obj = parse_active(locator)
        if obj is None:
            errors.append(f"{source_rel}: unparseable locator target {locator}")
        return obj
    return None

# Resolve resource descriptors recursively.
for rel in ("resources/foundation-resources.yaml", "resources/presentation-resources.yaml"):
    obj = parsed_docs.get(rel)
    if not isinstance(obj, dict):
        continue
    ids = []
    for item in obj.get("resources", []):
        if isinstance(item, dict):
            rid = item.get("id")
            if rid:
                ids.append(rid)
            resolve_locator(rel, item.get("locator"))
    if len(ids) != len(set(ids)):
        errors.append(f"{rel}: duplicate resource id")

# Cross-document component/capability/contract invariants.
components = registry.get("components", {})
capabilities = registry.get("capabilities", {})

for comp_id, comp in components.items():
    for cap_id in comp.get("capabilities", []):
        if cap_id not in capabilities:
            errors.append(f"{comp_id}: unknown capability {cap_id}")

for cap_id, cap in capabilities.items():
    provider = cap.get("provider")
    if provider not in components:
        errors.append(f"{cap_id}: missing provider {provider}")
    elif cap_id not in components[provider].get("capabilities", []):
        errors.append(f"{cap_id}: not declared by provider {provider}")

    loc = cap.get("contract")
    if not loc:
        errors.append(f"{cap_id}: missing contract locator")
        continue
    contract = resolve_locator(f"registry:{cap_id}", loc)
    if not isinstance(contract, dict):
        continue

    for field, expected in (
        ("capability", cap_id),
        ("owner", cap.get("owner")),
        ("provider", provider),
    ):
        if contract.get(field) != expected:
            errors.append(
                f"{cap_id}: contract {field} mismatch: "
                f"{contract.get(field)!r} != {expected!r}"
            )

    # Resolve contract resources.
    for res in contract.get("resources", []):
        resolve_locator(loc, res.get("locator"))

    # Resolve operation input/output schemas.
    for op in contract.get("operations", []):
        for field in ("input_schema", "output_schema"):
            oloc = op.get(field)
            if oloc:
                resolve_locator(f"{loc}:{op.get('id')}", oloc)

# Contract IDs unique.
contract_ids = {}
for rel, c in contracts.items():
    cid = c.get("id")
    if cid in contract_ids:
        errors.append(f"duplicate contract id {cid}: {contract_ids[cid]}, {rel}")
    contract_ids[cid] = rel

# Checksum coverage and integrity.
checksum_path = ROOT / "SHA256SUMS"
checksum_entries = {}
if not checksum_path.exists():
    errors.append("missing SHA256SUMS")
else:
    for line in checksum_path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            digest, rel = line.split("  ", 1)
        except ValueError:
            errors.append(f"SHA256SUMS malformed line: {line}")
            continue
        checksum_entries[rel] = digest

expected_covered = active_set - {"SHA256SUMS"}
actual_covered = set(checksum_entries)
if expected_covered != actual_covered:
    missing = sorted(expected_covered - actual_covered)
    extra = sorted(actual_covered - expected_covered)
    if missing:
        errors.append("SHA256SUMS missing active files: " + ", ".join(missing))
    if extra:
        errors.append("SHA256SUMS contains non-active files: " + ", ".join(extra))

for rel, expected in checksum_entries.items():
    p = ROOT / rel
    if not p.exists():
        errors.append(f"SHA256SUMS target missing: {rel}")
        continue
    actual = hashlib.sha256(p.read_bytes()).hexdigest()
    if actual != expected:
        errors.append(f"checksum mismatch: {rel}")

if errors:
    print("EF CANON VALIDATION: FAIL")
    for e in errors:
        print("-", e)
    sys.exit(1)

print("EF CANON VALIDATION: PASS")
print(f"- active files: {len(active)}")
print(f"- parsed YAML/JSON declarations: {len(parsed_docs)}")
print(f"- contracts validated: {len(contracts)}")
print(f"- schemas loaded: {len(schema_objs)}")
print(f"- capabilities validated: {len(capabilities)}")
print(f"- normative resource documents validated: {len(resource_docs_validated)}")
print(f"- normative locators resolved: {len(resolved_locators)}")
print(f"- checksum entries verified: {len(checksum_entries)}")
