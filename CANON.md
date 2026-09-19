# EF CANON
## r5 CURRENT
### Single Active LLM-First Canon for the ExpoFlamenco Software Ecosystem

```yaml
canon:
  id: ef-canon
  status: CURRENT
  revision: 5
  orientation: LLM_FIRST
  legacy_dependency: NONE
  historical_context_required: false
  platform_family: WORDPRESS_7_PLUS
  multisite: FIRST_CLASS
```

# 0. Mission

EF Canon is the **single active architectural and engineering source of truth** for the ExpoFlamenco software ecosystem.

A fresh LLM or agent with no prior ExpoFlamenco context must be able to receive:

```text
EF CANON CURRENT
+
PRODUCT / BUSINESS REQUIREMENTS
+
REPOSITORY WHEN RELEVANT
```

and deterministically resolve how to build, modify, integrate and validate EF software without historical documentation, tacit knowledge or architectural inference.

Required path:

```text
BUSINESS REQUIREMENT
→ DOMAIN RESPONSIBILITY
→ REQUIRED CAPABILITIES
→ UNIQUE OWNER
→ PUBLIC CONTRACT
→ WORDPRESS / EF IMPLEMENTATION PATH
→ VALIDATION
```

If a required architectural decision cannot be resolved from CURRENT EF Canon:

```text
BLOCKED
```

Never guess. Never infer from legacy. Never inspect implementation internals to reconstruct architecture.

# 1. Canon Invariants

```yaml
EF_CANON_INVARIANTS:
  ONE_ACTIVE_TRUTH:
    rule: "EF Canon CURRENT is the single active source of architectural truth."

  ZERO_ACTIVE_LEGACY:
    rule: "Historical or superseded material has no active authority and is not required for normal reasoning."

  ONE_CAPABILITY_ONE_OWNER:
    rule: "Every admitted shared capability has exactly one active owner."

  PUBLIC_CONTRACTS_ONLY:
    rule: "Components cross ownership boundaries only through public contracts."

  DOMAIN_LOGIC_STAYS_WITH_CONSUMER:
    rule: "Consumers own product-domain semantics and behavior; admitted shared transversal capabilities are consumed, not reimplemented."

  BLOCK_DONT_INFER:
    rule: "If a required decision cannot be deterministically resolved from CURRENT Canon, the result is BLOCKED."

  WORDPRESS_NATIVE_FIRST:
    rule: "Use WordPress public primitives unless EF adds real transversal semantics, ownership, determinism, portability, operational guarantees or machine-consumable contracts."

  CURRENT_NOT_HISTORY:
    rule: "Normal operation resolves CURRENT only."

  CAPABILITY_FIRST:
    rule: "Architecture is modeled by capability, ownership and contract before Provider packaging."

  MACHINE_DISCOVERABLE:
    rule: "Required architectural routes must be resolvable without source-code inspection."
```

# 2. Minimality Rule

Every active Canon fact must materially help an LLM make or validate a required decision.

> If removing a rule, field or section does not materially increase architectural or implementation uncertainty, it does not belong in the active Canon.

# 3. Canon vs CURRENT State

The Canon contains two kinds of truth inside one product:

```text
CANON MODEL
= what must be true

CURRENT REGISTRY
= what is true now
```

`registry.yaml` is the only active machine-readable CURRENT projection.

Registry projects Canon truth. It does not originate architecture.

# 4. EF Architecture

```text
                          EF
                          │
                          ▼
                      EF CANON
                single active truth
                          │
              ┌───────────┴───────────┐
              │                       │
         CANON MODEL             CURRENT REGISTRY
              │                       │
              └───────────┬───────────┘
                          │
                     CAPABILITIES
                          │
                      OWNERS
                          │
                  PUBLIC CONTRACTS
                          │
                     EF STACK
                          │
                     PROVIDERS
                          │
                     CONSUMERS
                          │
                          ▼
                     WORDPRESS
```

```yaml
EF:
  definition: "ExpoFlamenco software ecosystem."

EF_CANON:
  definition: "Single active machine-first architectural and engineering source of truth."

EF_STACK:
  definition: "Architecture of admitted reusable shared capabilities."

EF_COMPONENT:
  definition: "Software conforming to EF Canon."

PROVIDER:
  definition: "Component role that owns and implements one or more bounded shared capabilities through public contracts."

CONSUMER:
  definition: "Component role that owns product/domain behavior and consumes shared capabilities through public contracts."

INSTITUTIONAL_CONTROLLER:
  definition: "Non-Stack role that accepts evidence and makes conformity, lifecycle, release or certification decisions where such decisions are required."
```

# 5. Capability Is the Architectural Unit

```text
CAPABILITY
→ UNIQUE OWNER
→ PUBLIC CONTRACT
→ PROVIDER
→ IMPLEMENTATION STATE
→ RUNTIME AVAILABILITY
```

```text
CAPABILITY ≠ PROVIDER ≠ PLUGIN
```

- Capability = architectural responsibility.
- Owner = authority responsible for the capability.
- Provider = implementation role.
- Plugin = optional physical packaging/runtime form.

# 6. Capability Admission

```text
NEED X
  ↓
Is X product/domain-specific?
  ├─ YES → Consumer owns it
  └─ NO
       ↓
Does WordPress already provide a sufficient public primitive?
  ├─ YES → use WordPress directly
  └─ NO
       ↓
Does an admitted EF capability already exist?
  ├─ YES → consume its public contract
  └─ NO
       ↓
Is X genuinely transversal?
  ├─ NO → Consumer/domain owner
  └─ YES
       ↓
Admit shared capability
       ↓
Assign one owner
       ↓
Define public contract
       ↓
Choose Provider implementation
```

A new plugin is justified only when an independent runtime/lifecycle boundary is required.

# 7. Initial Shared Capability Owners

The initial greenfield Canon admits five shared owner domains:

```yaml
shared_owner_domains:
  foundation:
    provider_id: ef-foundation
  data:
    provider_id: ef-data
  presentation:
    provider_id: ef-presentation
  observability:
    provider_id: ef-observability
  operations:
    provider_id: ef-operations
```

These Provider IDs are architectural identities. They do not require one historical plugin to map one-to-one to them.

# 8. Foundation

Purpose: shared cross-ecosystem semantic primitives.

```yaml
foundation:
  owns:
    - component_identity
    - capability_identity
    - shared_types
    - shared_schemas
    - descriptors
    - result_semantics
    - error_semantics
    - contract_primitives
    - operation_context_schema
    - correlation_identifier_semantics
    - multisite_context_semantics
    - configuration_schema_primitives

  does_not_own:
    - product_domain_semantics
    - persistence_mechanics
    - presentation
    - telemetry_storage
    - jobs
    - integration_execution
    - institutional_governance
```

Foundation defines correlation identifiers and context semantics. Observability consumes those primitives for telemetry correlation.

Foundation must remain small. It is not a generic utilities bucket.

# 9. Data

Purpose: persistence architecture and mechanics.

```yaml
data:
  owns:
    - storage_classification
    - placement_resolution
    - storage_schema
    - migrations
    - repository_mechanics
    - persistence_runtime
    - transaction_mechanics
    - query_mechanics
    - index_mechanics
    - data_lifecycle_mechanics

  does_not_own:
    - business_semantics
    - domain_validation
    - product_rules
    - reporting_meaning
    - institutional_evidence_meaning
```

```text
DATA MEANING → DOMAIN OWNER
SHARED CROSS-ECOSYSTEM SEMANTIC PRIMITIVE → FOUNDATION
PERSISTENCE PLACEMENT / MECHANICS → DATA
PHYSICAL INFRASTRUCTURE → WORDPRESS / OPERATOR
```

## 9.1 Data Classes

```yaml
data_classes:
  CONFIGURATION:
  WP_CONTENT:
  ENTITY_METADATA:
  DOMAIN_DURABLE:
  OPERATIONAL:
  EVENT:
  SEARCH:
  CACHE:
  AUDIT:
  EVIDENCE_CANDIDATE:
```

## 9.2 Data Scope

```yaml
data_scope:
  SITE:
  NETWORK:
  EXTERNAL_GLOBAL:
```

## 9.3 WordPress-Native Placement

```text
configuration?
→ Options / Site Options

metadata of WordPress entity?
→ Metadata API

content naturally represented by WordPress?
→ Posts / Terms / Comments / native object model

temporary/cache?
→ Transients / Object Cache

independent / high-volume / query-specific justified data?
→ specialized persistence
```

A custom table, external store or specialized persistence substrate requires an explicit reason why the appropriate WordPress-native substrate is insufficient.

# 10. Presentation

Purpose: reusable shared presentation.

```yaml
presentation:
  owns:
    - admin_shell
    - layouts
    - navigation
    - reusable_components
    - forms
    - tables
    - notices
    - design_tokens
    - accessibility_patterns
    - responsive_patterns
    - shared_assets

  does_not_own:
    - business_meaning
    - persistence
    - authorization_meaning
    - domain_workflows
```

Consumer owns what a screen means and which product workflow it executes.

# 11. Observability

Purpose: operational observation and diagnostics.

```yaml
observability:
  owns:
    - operational_logging
    - telemetry_correlation
    - metrics
    - tracing
    - health
    - readiness
    - diagnostics
    - redaction
    - operational_export

  consumes:
    - foundation.operation_context_schema
    - foundation.correlation_identifier_semantics

  does_not_own:
    - evidence_acceptance
    - conformity
    - release_authorization
    - certification
```

```text
OBSERVATION ≠ ACCEPTED EVIDENCE
LOG ≠ CONFORMITY
```

# 12. Operations

Purpose: controlled deterministic operational execution.

```yaml
operations:
  owns:
    - jobs
    - scheduling_semantics
    - retries
    - locking
    - idempotency
    - execution_status
    - deterministic_cli_execution
    - maintenance_operations
    - technical_validation_execution
    - dry_run_execution

  consumes:
    - foundation.result_semantics
    - foundation.operation_context_schema

  does_not_own:
    - result_semantics
    - business_workflows
    - institutional_governance
    - architectural_authority
```

```text
OPERATIONS EXECUTES
INSTITUTIONAL CONTROL DECIDES
```

WP-Cron may be a scheduling substrate. Precision must never be inferred from WP-Cron alone.

# 13. Institutional Control Boundary

Institutional control is part of EF architecture but outside EF Stack.

It owns, where required:

```yaml
institutional_control:
  owns:
    - evidence_acceptance
    - conformity_decision
    - drift_decision
    - lifecycle_decision
    - release_authorization
    - certification_decision
```

The initial implementation identity is `ef-governance`, with conformance/adoption state recorded in CURRENT Registry. It is not a Stack Provider.

Institutional Control does NOT own:

```yaml
institutional_control:
  does_not_own:
    - canon_truth
    - capability_admission
    - capability_ownership
    - public_contract_definition
    - provider_architecture
```

Canon evolution is the only route by which architectural truth changes.

Hard boundaries:

```text
OBSERVATION ≠ EVIDENCE
EVIDENCE CANDIDATE ≠ ACCEPTED EVIDENCE
EXECUTION SUCCESS ≠ CONFORMITY
CONFORMITY ≠ RELEASE AUTHORIZATION
```

# 14. Capabilities Not Separate Providers Initially

```yaml
not_separate_providers_initially:
  events:
    policy: "Typed event contracts over WordPress Hooks first."

  security:
    policy: "WordPress security primitives first; EF shared semantics only where required."

  configuration:
    policy: "WordPress Settings/Options first; Foundation owns only shared schema primitives."

  cache:
    policy: "WordPress Transients/Object Cache first."

  integration:
    policy: "WordPress HTTP/REST/Connectors first; admit a shared Provider only if repeated transversal semantics justify it."

  notifications:
    policy: "Admit only when common delivery mechanics are demonstrated."

  files_media:
    policy: "Use WordPress native APIs until reusable mechanics justify abstraction."

  search:
    policy: "Admit only when transversal search infrastructure is demonstrated."

  agent_runtime:
    policy: "Do not create a monolithic agent Provider by default."

  mcp:
    policy: "Optional external Consumer/adapter; never an EF dependency."
```

# 15. WordPress Platform Contract

WordPress is the platform substrate, not an EF Provider.

```yaml
wordpress_policy:
  baseline_family: "7+"
  public_apis_first: true
  feature_detection: required
  private_core_apis: forbidden
  exact_minor_version_coupling: discouraged
```

Rules:

- Prefer public WordPress APIs.
- Feature-detect optional/new platform primitives.
- Do not couple EF architecture to exact WordPress patch/minor versions when a capability check is sufficient.
- Do not wrap WordPress solely for stylistic uniformity.
- Create EF abstraction only when it adds real shared semantics, ownership, deterministic behavior, operational guarantees, or a machine-consumable public contract.

Canonical native substrates include:

```text
plugin lifecycle → Plugin APIs
events → Actions / Filters
configuration → Settings / Options / Site Options
entity metadata → Metadata API
content → native WordPress content model
cache → Object Cache / Transients
HTTP → HTTP API
REST → REST API
authentication → WordPress authentication
authorization → Roles / Capabilities
CSRF → Nonces
scheduling → WP-Cron as best-effort substrate
multisite → Network / Site APIs
physical plugin dependencies → Plugin Dependencies / headers where appropriate
i18n → WordPress i18n
UI → WordPress admin / blocks / supported UI primitives where appropriate
executable discovery → Abilities API when suitable and available
AI invocation → WordPress AI Client when suitable and available
external/AI connector setup → Connectors API when suitable and available
```

# 16. WordPress Abilities

```text
EF CAPABILITY = architectural responsibility
PUBLIC CONTRACT = authorized consumption semantics
WORDPRESS ABILITY = optionally exposed executable operation
```

```text
CAPABILITY ADMITTED ≠ OPERATION EXECUTABLE
ABILITY REGISTERED ≠ EXTERNALLY EXPOSED
REST EXPOSED ≠ MCP EXPOSED
```

Each exposure surface is explicit and independently authorized.

# 17. MCP Boundary

MCP is an optional Consumer/adapter.

```yaml
mcp:
  required_for_ef_operation: false

  may_consume:
    - ef_canon
    - current_registry
    - public_contracts
    - wordpress_rest
    - wordpress_abilities
    - other_authorized_public_surfaces

  does_not_own:
    - ef_architecture
    - capability_ownership
    - provider_semantics
    - canon
    - institutional_control
    - wordpress_lifecycle
```

EF must function completely without MCP.

# 18. Multisite & Context

Every admitted Provider and Institutional Controller MUST declare:

```yaml
multisite_scope: SITE|NETWORK|BOTH
```

When the component can persist data or be activated at more than one WordPress scope, CURRENT MUST also declare:

```yaml
storage_scope: SITE|NETWORK|BOTH|NOT_APPLICABLE
activation_scope: SITE|NETWORK|BOTH
```

These are CURRENT facts, not inferred from implementation.

The canonical context schema lives in `schemas/context.schema.json`.

# 19. Public Contracts

Cross-owner integration occurs only through public contracts.

A public contract must define the minimum stable information required for deterministic consumption.

Provider internals are not contracts.

Missing required contract:

```text
BLOCKED
```

Concrete contract definitions live under `contracts/`.

Every executable contract operation MUST conform to `schemas/operation.schema.json`.
A contract may expose zero operations when it is a declarative/resource contract, but any executable operation must explicitly declare its input/output contract (or explicit `NONE`), authorization semantics, side-effect class and allowed execution surfaces.

A declarative/resource contract with zero operations MUST expose stable machine-readable `resources` locators. Consumers MUST NOT inspect Provider internals to discover those resources.

# 19.1 Authorization Resolution

Authorization MUST be resolved per execution surface and MUST NOT be inferred from a label alone.

```yaml
authorization_modes:
  PUBLIC: {resolver: NONE}
  INTERNAL_ONLY: {resolver: TRUSTED_INTERNAL_CALL_PATH}
  WORDPRESS_CAPABILITY: {resolver: WORDPRESS_CURRENT_USER, cli_policy: EXPLICIT_ACTOR_REQUIRED}
  INSTITUTIONAL: {resolver: INSTITUTIONAL_ACTOR_POLICY, cli_policy: EXPLICIT_ACTOR_REQUIRED}
```

`WORDPRESS_CAPABILITY` MUST name the required WordPress capability. CLI privileged execution requires an explicit authorized actor or is `BLOCKED`. `INSTITUTIONAL` MUST name an actor-policy identifier. SITE/NETWORK authorization differences MUST be explicit in the operation contract.

`INTERNAL_ONLY` with `cli: true` is permitted only for non-privileged read/validation operations whose contract explicitly declares `cli_trust: LOCAL_TRUSTED_OPERATOR`. CLI itself does not create trust. If an INTERNAL_ONLY CLI operation can mutate state or cross an authorization boundary, it MUST use `WORDPRESS_CAPABILITY` or `INSTITUTIONAL` authorization instead.

This does not create a Security Provider.

# 20. Operation & Result Semantics

Operation semantics are defined by `schemas/operation.schema.json`.

Result semantics are defined by `schemas/result.schema.json` and owned by Foundation.

Operation idempotency and reversibility use explicit `YES|NO|UNKNOWN|NOT_APPLICABLE` states. `UNKNOWN` is never permission to infer.

Execution surfaces may include PHP, REST, CLI and WordPress Ability. An optional MCP adapter may map an authorized surface but is not a canonical execution requirement.

# 21. Provider & Consumer Declarations

Provider and Consumer machine declarations conform to their respective schemas under `schemas/`.

Provider declaration describes boundaries and current integration surfaces. It does not create authority by itself.

Consumer declaration identifies domain ownership and consumed capabilities. Consumers must not reimplement admitted shared capabilities.

# 22. WordPress Engineering Minimum

A fresh LLM must apply these minimum rules when creating or modifying an EF WordPress component:

```yaml
wordpress_engineering:
  plugin_bootstrap:
    minimal_entry_file: required
    load_at_wordpress_runtime: required

  identifiers:
    stable_component_id: required
    namespace_or_equivalent_collision_avoidance: required

  lifecycle:
    activation_deactivation_uninstall_distinct: required
    destructive_data_deletion_on_deactivation: forbidden

  security:
    validate_input: required
    sanitize_when_applicable: required
    escape_output_late: required
    authorization_checks: required
    nonce_or_equivalent_csrf_protection_when_applicable: required
    rest_permission_callback: required_for_rest_routes

  dependencies:
    architectural: "capability + public contract"
    physical: "WordPress/plugin/package mechanism"

  multisite:
    scope_declaration: required_when_relevant

  persistence:
    direct_storage_design_outside_data_contract: forbidden_for_shared_or_nontrivial_persistence

  integration:
    public_wordpress_api_first: required

  i18n:
    wordpress_i18n_primitives: required_for_user_facing_strings
```

Exact packaging/release metadata may evolve independently and must not become architectural glue.

# 23. CURRENT Registry

`registry.yaml` is the only active CURRENT projection and MUST validate against `schemas/registry.schema.json`.

It must resolve:

```text
capability
→ owner
→ Provider / platform substrate
→ public contract
→ implementation state
→ conformance state
→ runtime availability
```

Distinguish:

```text
ADMITTED ≠ IMPLEMENTED
IMPLEMENTED ≠ CONFORMANT
CONFORMANT ≠ AVAILABLE NOW
```

# 24. Conformance and Runtime States

Canonical decision/conformance states:

```text
PASS
FAIL
BLOCKED
DEGRADED
```

Capability status:

```text
ADMITTED
RETIRED
```

Implementation state:

```text
ADOPTION_PENDING
IMPLEMENTED
RETIRED
```

Runtime availability:

```text
UNKNOWN
AVAILABLE
UNAVAILABLE
DEGRADED
```

A capability is consumable only when:

```text
status = ADMITTED
AND public contract resolves
AND conformance_state = PASS
AND (
  runtime_availability = AVAILABLE
  OR (
    runtime_availability = DEGRADED
    AND public contract explicitly permits degraded consumption
  )
)
```

No other state value may be invented in CURRENT.

# 24.1 Cross-Document Validation

Local JSON Schema validation is insufficient for invariants spanning active files. The canonical validator declared by `manifest.yaml` MUST validate Registry→component→capability→contract identity, locator resolution, active-file resolution and resource/schema locator resolution. A package is not mechanically conformant merely because each file validates independently.

The canonical mechanical acceptance path is a single execution of `validate.py`. A PASS means:
1. every active YAML/JSON declaration parses;
2. Registry validates against its canonical schema;
3. every public contract validates against `contract.schema.json`;
4. every operation validates through the canonical operation schema;
5. every normative resource document validates against its declared/minimum machine shape;
6. every normative resource/schema locator is recursively resolved to an existing parseable active target;
7. cross-document identities/locators resolve;
8. checksum coverage equals the active-file set excluding `SHA256SUMS`;
9. every covered checksum verifies.

Any failure MUST return a non-zero exit status.

# 25. Validation

Minimum rules:

```text
duplicate active owner for an exclusive capability → BLOCKED
missing required owner → BLOCKED
missing required public contract → BLOCKED
Consumer reimplements admitted shared capability → FAIL
Consumer depends on Provider internals → FAIL
runtime presence used as architectural authority → FAIL
WordPress private API used without explicit authorized exception → FAIL
multisite scope omitted where relevant → FAIL
custom persistence chosen without native-substrate justification → FAIL
unauthorized execution-surface exposure → FAIL
historical source used to override CURRENT → FAIL
```

# 26. Evolution

EF has no generational identity in active operation.

```yaml
canon:
  id: ef-canon
  revision: integer
  status: CURRENT
```

Normal architectural references use stable IDs and CURRENT locators.

Do not use exact document filenames, historical freezes, artifact hashes, release labels or informational SemVer as routine architectural glue.

# 27. Change Propagation

Review downstream impact when semantics change:

```text
public contract semantics
capability ownership
compatibility boundary
required capability availability
security/permission semantics
material degradation semantics
```

Do not globally resynchronize architecture for:

```text
filename
informational SemVer
hash
package label
internal implementation
non-semantic wording
```

# 28. History

```yaml
history:
  retained_externally: true
  active_authority: false
  required_for_normal_reasoning: false
  backward_documentary_compatibility: false
```

> There is no active legacy. There is only CURRENT.

# 29. Acceptance Test

A fresh LLM receives only:

```text
EF CANON CURRENT
+
BUSINESS REQUIREMENTS
+
REPOSITORY WHEN RELEVANT
```

It must resolve:

```text
domain ownership
required capabilities
WordPress-native primitives
shared EF capabilities
unique owners
public contracts
multisite scope
security boundaries
data placement
execution surfaces
validation
BLOCKED conditions
```

It must not inspect Provider internals to infer architecture, consult historical documentation, invent owners/contracts, reimplement admitted capabilities or bypass WordPress security.

Pass condition:

```text
ZERO-CONTEXT LLM
→ ARCHITECTURALLY CORRECT EF SOFTWARE
```

# 30. Growth Guard

```text
product-specific → Consumer
WordPress-native sufficient → use WordPress
existing admitted capability → consume contract
genuine transversal unmet need → evaluate admission
```

New Provider only after bounded ownership and transversal value are proven.

New plugin only when an independent runtime/lifecycle boundary is justified.

# 31. Adoption

Existing software conforms to Canon; Canon does not conform to historical software.

```text
CURRENT COMPONENT
→ AUDIT AGAINST CANON
→ ADOPT | REFACTOR | MERGE | SPLIT | REPLACE | RETIRE
```

# 32. Final Rule

> **One active truth. One capability, one owner. Public contracts only. Consumers own product-domain logic. WordPress-native first. If the Canon cannot resolve a required decision, BLOCK rather than infer.**

> **EF exists to reduce uncertainty and repeated implementation, not to create a second framework inside WordPress.**
