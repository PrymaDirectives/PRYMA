# PRYMA Core Axioms and Models

## PRYMA Core Axioms and Invariants

### 1. Scope of the Specification
1.1 This specification applies to all PRYMA subsystems that issue, interpret, enforce, or audit authority, intent, memory, and proof semantics.
1.2 These constraints cover human-operated interfaces, agent runtimes, protocol services, and storage layers that process PRYMA artifacts.
1.3 Implementation details, optimizations, and deployment-specific configurations are explicitly out of scope for this section.
1.4 Boundary conditions include interoperation points with external systems; where PRYMA artifacts transit untrusted domains, the invariants in this specification remain mandatory.

### 2. Definitions and Terminology
2.1 **Authority**: A bounded, non-transferable capability to act within declared scope and duration.  
2.2 **Intent**: An explicit expression of desired action tied to a specific authority and scope.  
2.3 **Scope**: The explicit spatial, temporal, and resource boundaries within which authority is valid.  
2.4 **Proof**: A verifiable, time-bounded statement asserting origin, authority, and scope without asserting truth or legitimacy.  
2.5 **Memory**: An append-only, content-addressed record that is globally observable and non-ownable.  
2.6 **Revocation**: An explicit act or condition that terminates authority, proofs, or sentences within their scope.  
2.7 **Sentence**: A structured statement expressing authority, scope, duration, resources, and revocation path.  
2.8 **Gate**: The mediation layer that classifies, normalizes, and associates inputs with scope and authority.  
2.9 **Modality**: The form of representation for intent or input (e.g., text, speech, transcription, summarization, agent relay).  
2.10 **Invariant**: A property that must hold for all system states and operations.
2.11 **Violation**: Any detectable state that contradicts a declared invariant or introduces a prohibited collapse.
2.12 Undefined terms MUST NOT be introduced elsewhere in this document.
2.13 Where external standards are referenced, terminology mapping MUST be explicit to avoid ambiguity.
2.14 **Composite Input**: An input assembled from multiple modalities or actors that MUST retain linkage to each constituent component.
2.15 **Downgrade**: An explicit reduction in permitted authority due to ambiguity, degradation, or missing verification evidence.

### 3. Foundational Axioms
Each axiom is expressed as a single declarative constraint.  

#### 3.1 Authority
Authority is non-transferable, inheres only to its issuer, and is valid solely within the issuer-declared scope and duration.

#### 3.2 Intent
Intent binds authorized action to the exact expression provided by the authorized actor and MUST NOT be expanded without reaffirmation.  

#### 3.3 Scope
Authority is constrained to explicitly bounded scope and ceases to exist outside those bounds.
3.3.1 Scope definitions MUST enumerate actors, actions, spatial/temporal limits, and resource ceilings to prevent implicit gaps.

#### 3.4 Proof
Proof establishes verifiable origin, authority, and scope but cannot establish truth, correctness, or legitimacy of the underlying action.  

#### 3.5 Memory
Memory is non-ownable, append-only, and any annotation MUST NOT mutate existing records.  

#### 3.6 Revocation
Revocation is always possible, observable, and MUST terminate further use of associated authority or proof.
3.6.1 Revocation MUST propagate to all dependent proofs, sentences, and delegations without requiring additional confirmation.

### 4. System Invariants

#### 4.1 Conditions That Must Always Remain True
- All authority is bound to declared scope, duration, and resources.  
- Every action consuming authority references a valid, non-expired proof or sentence.  
- Memory entries are immutable after append and are content-addressed.  
- Revocation states are publicly observable and auditable.  
- Inputs are classified and normalized before interpretation.  
- Delegated authority never exceeds the granting scope.  
- Proof verification is deterministic and reproducible.  
- Audit trails exist for all authority-bearing actions.  
- Scope escalation requires explicit authorization and leaves an auditable record.
- Emergency handling preserves all invariants.
- Compliance levels (Minimal, Standard, Strict) are declared and discoverable for every participating subsystem.

#### 4.2 Conditions That Must Never Occur
- Authority without defined scope or duration.  
- Proof asserting truth or legitimacy beyond origin, authority, and scope.  
- Silent revocation failures or undiscoverable revocation events.  
- Mutation of memory entries after creation.  
- Implicit escalation of scope, modality-based authority gain, or laundering of intent.  
- Gate bypass or unclassified input execution.  
- Irrevocable authority states.  
- Delegation that exceeds original scope or duration.  
- Reuse of expired or revoked proof.
- Collapsing role, authority, or memory into a single primitive.
- Delegation pooling that silently widens effective scope.

### 5. Prohibited Collapses (Role, Authority, Memory)
5.1 Role MUST NOT be treated as authority; possessing a role does not convey actionable capability without explicit sentence or proof.  
5.2 Authority MUST NOT be conflated with ownership of memory; records remain non-ownable regardless of authority state.  
5.3 Memory MUST NOT be used as a proxy for authority or role; append-only history cannot instantiate capability.  
5.4 Any detected collapse is a critical violation requiring immediate response.

### 6. Invariant Violation Handling
6.1 Violations MUST trigger immediate revocation or isolation of implicated authority and proofs.
6.2 Systems MUST emit auditable events detailing the violation, scope, actor, and remediation status.
6.3 Recovery procedures MUST restore invariant compliance before resuming affected operations.
6.4 Silent failure or suppression of violation signals is prohibited.
6.5 Violations MUST be triaged with severity levels and response windows that are documented and testable.

### 7. Non-Goals and Explicit Exclusions
7.1 This specification does not guarantee correctness of user intent, ethical evaluation, or external legitimacy.
7.2 Performance optimizations, UI/UX patterns, and transport-level encoding details are excluded.
7.3 Exclusions MUST NOT be reintroduced by extension or implementation shortcuts.
7.4 Out-of-band trust establishment is out of scope; integrations MUST treat external authority as untrusted until verified via PRYMA sentences or proofs.

---

## PRYMA Sentence Model Specification

### 1. Sentence Purpose and Scope
1.1 Sentences define the canonical vehicle for expressing and constraining authority within PRYMA systems.

### 2. Formal Definition of a Sentence
2.1 A sentence is a structured record that binds an author, scope, duration, resources, and revocation path into a cryptographically addressable object.
2.2 Sentences MAY include typed extensions provided they do not alter required semantics or relax constraints on scope, duration, or revocation.

### 3. Required Fields
Each field listed MUST be present in a valid sentence.  
- Author  
- Scope  
- Duration  
- Resources  
- Revocation Path  

### 4. Optional Fields
4.1 Optional fields MAY include Extensions that add metadata without altering required semantics.

### 5. Cryptographic Addressability Requirements
5.1 Sentences MUST be content-addressable via cryptographic digest over canonicalized fields.
5.2 Addressability MUST be stable across replication and serialization formats.
5.3 Canonicalization MUST include deterministic field ordering, normalization of optional fields, and unambiguous encoding of nested structures to prevent hash mismatches.
5.4 Systems MUST publish reference test vectors for address derivation so independent implementations can verify compatibility.

### 6. Sentence Lifecycle
- **Creation**: Author constructs the sentence with all required fields and signs it.
- **Validation**: Systems verify signatures, field completeness, scope consistency, and revocation path availability.
- **Activation**: Upon successful validation, the sentence becomes usable for actions within its scope.
- **Expiration**: Duration lapse automatically renders the sentence inactive.
- **Revocation**: Explicit triggers or violations invalidate the sentence and propagate observable events.
- **Archival**: Expired or revoked sentences MUST remain addressable for audit and replay prevention.

### 7. Invalid Sentence Conditions
7.1 Missing required fields, failed signature verification, malformed scope, absent revocation path, expired duration at evaluation time, or conflicting resource declarations render a sentence invalid.
7.2 Nested or composed sentences that expand scope beyond any parent sentence are invalid.

### 8. Sentence Composition and Nesting Rules
8.1 Nested sentences MUST NOT extend scope beyond the parent and MUST inherit or further restrict duration and resources.
8.2 Composition MAY aggregate multiple sentences only when aggregate scope equals the intersection of member scopes.
8.3 Composition MUST preserve independent revocation paths; a revoked member invalidates the aggregate.

### 9. Constraints on Sentence Mutation
9.1 Sentences MUST NOT be mutable; changes require issuance of a new sentence or invocation of the revocation path.
9.2 Amendments MUST reference the prior sentence address to preserve lineage.

### Table: Sentence Fields

| Field            | Required | Optional |
|------------------|----------|----------|
| Author           | Yes      | No       |
| Scope            | Yes      | No       |
| Duration         | Yes      | No       |
| Resources        | Yes      | No       |
| Revocation Path  | Yes      | No       |
| Extensions       | No       | Yes      |

---

## PRYMA Scope and Authority Bounding Specification

### 1. Scope Definition Model
1.1 Scope MUST be explicitly defined by domain, resources, actors, temporal bounds, and permissible actions.

### 2. Authority–Scope Relationship
2.1 Authority MUST NOT exist outside of defined scope and is evaluated against scope before execution.

### 3. Time-Bounded Authority
3.1 Authority MUST expire when temporal bounds are exceeded; expired authority cannot be reactivated without reissuance.

### 4. Resource-Bounded Authority
4.1 Authority MUST be constrained to declared resources and quantities; overuse constitutes violation.

### 5. Delegated Authority Constraints
5.1 Delegation MUST NOT exceed original scope and MUST inherit equal or shorter duration.
5.2 Delegations MUST reference the originating sentence or proof for auditability.
5.3 Delegation MUST NOT bypass revocation chains of the origin and MUST respect resource ceilings.

### 6. Scope Escalation Rules
6.1 Escalation MUST require explicit authorization and produce a new sentence documenting the expanded scope.
6.2 Automatic or implicit escalation is prohibited.
6.3 Escalation attempts MUST be logged even when denied to ensure auditability of repeated probes.

### 7. Scope Reduction and Contraction
7.1 Scope MAY be reduced without escalation and SHOULD emit an audit event documenting the contraction.

### 8. Forbidden Scope Patterns
8.1 Undefined boundaries, unlimited resources, perpetual duration, or implicit actor sets are invalid scope constructions.

### 9. Authority Without Scope (Invalid State)
9.1 Authority without scope MUST be treated as invalid and immediately revoked or refused.
9.2 Systems MUST surface this condition as a high-severity violation with remediation guidance.

---

## PRYMA Proof-of-Permission Specification

### 1. Proof Purpose and Limits
1.1 Proof asserts that an action request originates from an authorized source within declared scope and duration but does not assert truth, correctness, or legitimacy.
1.2 Proof MAY attest to freshness (e.g., nonce or timestamp binding) but MUST NOT be interpreted as intent expansion.

### 2. Proof Components
- Origin
- Authority
- Scope
- Freshness or nonce binding
- Verifier version and supported serialization profile

### 3. Proof Verification Requirements
3.1 Verification MUST be deterministic, reproducible, and based on public parameters.
3.2 Verification MUST fail on expired or revoked authority.
3.3 Verification procedures MUST be versioned; verifiers MUST publish supported versions for interoperability.
3.4 Verification MUST operate over canonicalized encodings; ambiguous serialization MUST be rejected rather than inferred.
3.5 Verifiers MUST emit structured results (pass/fail, downgrade applied, reason codes) suitable for automated audit.

### 4. Proof Non-Assertions
4.1 Proof DOES NOT assert truth.  
4.2 Proof DOES NOT assert correctness of execution.  
4.3 Proof DOES NOT assert legitimacy beyond authenticated origin and bounded scope.

### 5. Proof Lifespan and Expiration
5.1 Proof MUST be time-bounded and invalid after expiration regardless of unused capacity.
5.2 Proof lifespans MUST be discoverable for audit and enforced uniformly across replicas.

### 6. Proof Revocation
6.1 Proof MUST be revocable independently of action outcome and MUST propagate revocation to dependent actions.

### 7. Proof Replay and Reuse Constraints
7.1 Reuse MUST be explicitly constrained; absent reuse allowances, proof is single-use.
7.2 Replay outside temporal or scope bounds is invalid.
7.3 Proofs MUST bind to specific actions or resource ceilings when reuse is permitted to prevent scope creep.

### 8. Invalid Proof Conditions
8.1 Altered signatures, mismatched scope, expired duration, revoked authority, or missing origin metadata render proof invalid.
8.2 Proofs with ambiguous or conflicting serialization are invalid and MUST be rejected.

### 9. Observability and Audit Requirements
9.1 Proof evaluation MUST be auditable with traceable logs linking origin, scope, verification result, and revocation state.
9.2 Audits MUST capture verifier version, timestamps, and any downgrades applied during evaluation.

---

## PRYMA Gate and Input Mediation Specification

### 1. Gate Purpose
1.1 The gate mediates all inbound inputs, ensuring classification, normalization, scope association, and authority enforcement.

### 2. Input Classification
- Human  
- Agent  
- Composite  

### 3. Proposal Normalization Rules
3.1 Inputs MUST be normalized before interpretation, preserving semantic intent while removing ambiguity.
3.2 Normalization steps MUST be logged for audit.
3.3 Normalization MUST reject inputs that lack associated scope metadata.

### 4. Scope Association Requirements
4.1 All inputs MUST be associated with scope before execution, linking to sentences or proofs.
4.2 Inputs lacking valid scope association MUST be rejected with an auditable denial.

### 5. Authority Downgrading Conditions
5.1 Downgrades MUST be explicit when ambiguity, degradation, or partial verification occurs and MUST be visible to downstream handlers.

### 6. Modality Provenance Tracking
6.1 Provenance MUST be preserved across handling; modality transitions MUST retain origin metadata and transformation history.
6.2 Provenance MUST include any authority downgrades or reaffirmations performed during handling.

### 7. Disallowed Input Transitions
7.1 Execution of unclassified inputs, implicit escalation during transformation, or bypass of normalization is forbidden.

### 8. Emergency and Urgent Inputs
8.1 Emergency handling MUST NOT bypass invariants and MUST document all deviations and justifications.
8.2 Emergency inputs MUST default to the minimal authority necessary and expire rapidly unless reaffirmed.

### 9. Gate Failure Modes
9.1 Failure modes MUST be enumerated (e.g., classification failure, normalization error, unavailable scope data) and handled via safe denial with logging.
9.2 Failure handling MUST differentiate transient (retryable) from permanent errors and SHOULD rate-limit retries to prevent abuse.
9.3 Gate subsystems MUST expose health signals that surface back-pressure, queue saturation, or degraded classification quality.

### 10. Gate Bypass Prohibitions
10.1 Gate bypass MUST NOT be permitted; attempted bypass is treated as violation.
10.2 Bypass attempts MUST trigger rate-limited alerts and automated containment responses.

---

## PRYMA Intent Integrity and Modality Boundary Specification

### 1. Definition of Intent vs Representation
1.1 Intent is the actor’s desired action; representation is any modality expressing that intent. They MUST be tracked separately.

### 2. Modality Types
- Text  
- Speech  
- Transcription  
- Summarization  
- Agent Relay  

### 3. Modality Transformation Rules
3.1 Transformations MUST preserve intent or explicitly mark degradation, including lost context or uncertainty.
3.2 Transformed outputs MUST inherit or reduce authority, never expand it.
3.3 Transformations MUST preserve ordering and linkage to original sentences or proofs to prevent intent laundering.
3.4 Transformation chains MUST be reproducible from recorded metadata so downstream evaluators can replay or challenge them.

### 4. Authority Across Modality Boundaries
4.1 Authority MUST NOT increase across modality boundaries; any change defaults to downgrade.

### 5. Intent Reaffirmation Requirements
5.1 Reaffirmation MUST be required after degradation or significant transformation before execution.

### 6. Intent Laundering Attack Class
6.1 Systems MUST detect and block attempts to obscure, reinterpret, or expand intent through modality shifts.
6.2 Laundering detection MUST consider aggregation across multiple small transformations that cumulatively expand scope.

### 7. Prohibited Authority Escalations
7.1 Escalation via modality transformations MUST NOT occur and MUST trigger violation handling.

### 8. Required Metadata for Transformed Input
8.1 Metadata MUST include source modality, transformation chain, detected degradation, and associated scope.
8.2 Metadata MUST explicitly flag downgraded authority and the rationale for any reaffirmation requirements.

### 9. Invalid Intent States
9.1 Ambiguous, unverifiable, or modality-expanded intents are invalid and MUST be rejected or downgraded.

---

## PRYMA De-Institutionalized Memory Specification

### 1. Memory Purpose
1.1 Memory exists to provide auditable, append-only context for actions, authority, and proofs without implying ownership.

### 2. Append-Only Constraints
2.1 Memory MUST be append-only; modifications require annotations that do not alter prior bytes.
2.2 Append operations MUST be sequenced and timestamped to support tamper-evident verification.

### 3. Content Addressing Requirements
3.1 Entries MUST be content-addressed, enabling tamper evidence and deduplication.
3.2 Address derivation MUST be deterministic across replicas and serialization formats.

### 4. Replication and Retention Rules
4.1 Replication MUST NOT imply ownership; replicas retain the same address and invariants.
4.2 Retention policies MUST be explicit and auditable.
4.3 Retention enforcement MUST be observable; attempted unauthorized retention changes are violations.

### 5. Memory Ownership Prohibitions
5.1 Ownership claims over memory entries MUST NOT exist; access policies govern interaction without conferring title.

### 6. Annotation vs Mutation
6.1 Annotations MUST NOT mutate records and MUST reference the original entry by address.

### 7. Memory Framing Risks
7.1 Systems MUST identify framing risks where selective replication or ordering could misrepresent history and log mitigations.
7.2 Framing countermeasures MUST include ordering proofs or checkpoints that allow reconstruction of intended sequence.

### 8. Memory Auditability
8.1 Memory MUST be auditable with verifiable chains of custody and replication events.

### 9. Forgetting, Pruning, and Exit
9.1 Forgetting MUST be explicit, bounded, and recorded; pruning MAY remove access without altering historical addresses.
9.2 Exit procedures MUST document custody transfer, ensuring subsequent holders accept the same append-only and non-ownership constraints.

---

## PRYMA Revocation and Interruptibility Specification

### 1. Revocation Principles
1.1 Revocation MUST always be possible, explicitly signaled, and enforceable across modalities and replicas.

### 2. Revocation Triggers
2.1 Triggers MUST include explicit request, scope violation, expiry, proof misuse, detection of laundering, and policy-defined anomalies.
2.2 Revocation triggers MUST be machine-evaluable and regularly tested for coverage.

### 3. Revocation Scope
3.1 Revocation MUST respect scope boundaries, invalidating only the affected authority, proof, or sentence and its delegations.
3.2 Revocation responses MUST include guidance on downstream dependency invalidation.

### 4. Time-Bounded Authority Expiry
4.1 Expiry MUST be enforced automatically and logged as a revocation event.

### 5. Collective Revocation
5.1 Collective mechanisms MUST be defined to allow multiple stakeholders to revoke shared authority with quorum policies.
5.2 Quorum parameters MUST be auditable, and any changes to quorum thresholds MUST themselves require a revocable, scoped authority.

### 6. Emergency Interrupts
6.1 Emergency interrupts MUST be observable, preemptive, and revert systems to a safe state while preserving audit data.
6.2 Emergency interrupts MUST default to the narrowest viable authority to prevent scope creep during recovery.

### 7. Revocation Observability
7.1 Revocation events MUST be recorded in memory with timestamps, actors, triggers, and affected scopes.
7.2 Observability MUST distinguish between proactive revocation and post-incident revocation to support forensic timelines.

### 8. Irrevocable States (Prohibited)
8.1 Irrevocable authority MUST NOT exist; any attempt to create it is invalid and MUST be rejected.

### 9. Revocation Failure Handling
9.1 Failures MUST be surfaced immediately, trigger compensating controls, and block further actions until resolved.
9.2 Post-incident reviews MUST be recorded in memory to improve future detection and handling.

---

## PRYMA Threat Model and Adversarial Classes

### 1. Threat Modeling Philosophy
1.1 Threat modeling focuses on structural misuse of authority, scope, memory, and proof rather than actor identity alone.

### 2. Authority-Based Attacks
2.1 Structural authority abuses MUST be defined, including over-delegation, unauthorized escalation, and perpetual grants.

### 3. Legitimacy Attacks
3.1 Attacks on perceived legitimacy MUST be listed, including forged provenance, misrepresented endorsements, and manipulated metadata.

### 4. Delegation Pooling Attacks
4.1 Pooling behaviors MUST be constrained to prevent aggregation of narrow authorities into broader unauthorized scope.

### 5. Emotional Capture Attacks
5.1 Emotional leverage MUST be treated as a threat when it coerces intent or bypasses reaffirmation requirements.
5.2 Mitigations MUST include reaffirmation prompts, cooling-off periods, or downgraded execution paths when emotional capture is suspected.

### 6. Proof Gaming Attacks
6.1 Proof misuse patterns MUST be identified, including replay, partial reassembly, and context stripping.

### 7. Memory Framing Attacks
7.1 Framing manipulations MUST be described, including selective replication, reorderings, and omission of annotations.
7.2 Systems MUST provide verifiable ordering proofs or checkpoints to counter framing attacks.

### 8. Intent Laundering Attacks
8.1 Laundering vectors MUST be enumerated, such as modality switching to expand scope or hiding downgrades.  

### 9. Non-Threats and Explicit Assumptions
9.1 Non-threats MUST be explicitly stated (e.g., honest use within constrained test networks) to avoid misapplied controls.

### 10. Structural Mitigations
10.1 Mitigations MUST map to threat classes, including revocation hooks, deterministic proof checks, scope validation, and audit enforcement.
10.2 Mitigations MUST be testable with adversarial scenarios that simulate each enumerated threat class.

---

## PRYMA Compliance and Conformance Specification

### 1. Levels of Compliance
1.1 Compliance levels MUST be defined (e.g., Minimal, Standard, Strict) with progressively stronger enforcement and audit guarantees.
1.2 Each level MUST enumerate mandatory self-tests and evidence artifacts to demonstrate conformance before integration.

### 2. Mandatory vs Optional Components
2.1 Mandatory components MUST include sentences, scope enforcement, proof verification, revocation handling, and memory auditability.  
2.2 Optional components MAY include UI affordances, extended analytics, or alternative serialization formats.

### 3. Invariant Enforcement Requirements
3.1 Enforcement MUST be demonstrable through reproducible tests and auditable logs.
3.2 Enforcement status MUST be machine-readable for integration into higher-level governance or automation.

### 4. Audit and Verification Criteria
4.1 Audit criteria MUST be objective, covering sentence validity, scope adherence, revocation propagation, and proof verification outcomes.
4.2 Audit evidence MUST include timestamps, verifier identity, software versions, and hashes of evaluated artifacts.

### 5. Non-Compliance Conditions
5.1 Non-compliance MUST be detectable when invariants are violated, proofs are unverifiable, revocation fails, or scope is unbounded.
5.2 Non-compliance MUST trigger remediation workflows aligned with the severity of impacted invariants.

### 6. Partial Compliance Scenarios
6.1 Partial compliance MUST be explicitly scoped, enumerating which components meet Minimal vs Standard vs Strict levels.
6.2 Partial compliance declarations MUST be versioned and accompanied by compensating controls for deferred items.
6.3 Deferred items MUST include remediation timelines and ownership for closing gaps.

### 7. Interoperability Constraints
7.1 Interoperability MUST NOT weaken invariants; cross-system bridges MUST preserve scope, proof validity, and revocation semantics.

### 8. Versioning and Evolution Rules
8.1 Evolution MUST preserve core axioms, and versioned changes MUST document impacts on compliance levels and invariants.
