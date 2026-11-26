# ActivityAssignment and TMF713 Work Management

ActivityAssignment is modelled after TM Forum Work Management (TMF713). This document maps the information object to the TMF713 resources, so the FSA API can expose activity assignments as `Work` instead of a resource of its own.

This is a **proposal**. The mapping isn't in Encyclopedia Galactica yet, and the open questions at the end need an answer from the model owner before the API is defined.

## Sources

- Information object ActivityAssignment (ID 23): *who should be at a location and an access point at a certain time period, with optional resources.* Status Verified. Its `Standard` column is `Falskt` and has no TM Forum reference (see question 1).
- Information objects Activity (90) and ActivityAssignmentSpecification (91), both with the reference *TMF713 / SID GB922*.
- Semantic relations 15 (ActivityAssignment occurs at Place), 18 (uses AccessPoint), 19 (involves Resource) and 20 (relates to ActivityAssignment).
- Decision by the model owner, 2026-11-26: an ActivityAssignment relates to **Place, Individual, AccessPoint, Resource and equipment (Product)**. The relations to Individual and Product are not in `semantic-relations.csv` yet (see question 3).
- Business terms with information object ActivityAssignment and boundary Film Site Access: access pass (1225), access request (1226), all day (1246), period (1244), time slot (1245), recurrence (1248), weekday (1247), and the statuses pending (1257), approved (1258), declined (1259) and revoked (1260).
- Use cases UC-FSA-3 (List activities), UC-FSA-4a (Request access to a home and unlock door) and UC-FSA-4b (Request access for cast or crew to a filming location).
- [`tmf/TMF713-work-management/TMF713.json`](../tmf/TMF713-work-management/TMF713.json), version 4.0.0 beta.

## Resources

| Film Site Access | TMF713 | How |
|---|---|---|
| ActivityAssignment | `Work` | `@type: ActivityAssignment`, `@baseType: Work` |
| ActivityAssignmentSpecification | `WorkSpecification` | `@type: ActivityAssignmentSpecification`, `@baseType: WorkSpecification` |

TM Forum allows a sub-class to be named with `@type` and `@baseType`, and its extra attributes to be described in a JSON Schema referenced by `@schemaLocation`. The paths stay `/work` and `/workSpecification`.

## Related objects

An ActivityAssignment relates to five kinds of object. TMF713 `Work` has a place for two of them. The other three need an FSA extension of `Work`.

| Related object | Information object | Work attribute | TM Forum resource |
|---|---|---|---|
| Place | Place (49) | `place[]` (RelatedPlaceRefOrValue), `role: location` | TMF674 GeographicSite |
| Individual | Individual (31) | `relatedParty[]` (RelatedParty), `@referredType: Individual`, `role: assignee` | TMF632 Individual |
| AccessPoint | AccessPoint (22) | Extension: `accessPoint[]` (EntityRef, `@referredType: AccessPoint`) | None; FSA API |
| Resource | Resource (40) | Extension: `resource[]` (EntityRef, `@referredType: Resource`) | TMF639 Resource |
| Equipment | Product (36) | Extension: `product[]` (EntityRef, `@referredType: Product`) | TMF637 Product |

The extension is the TM Forum sub-class mechanism: `@type: ActivityAssignment`, `@baseType: Work`, and a JSON Schema at `@schemaLocation` that adds `accessPoint`, `resource` and `product`. Each is a list of references, with the cardinality 0..n of relations 18 and 19.

- **Individual uses `relatedParty`, not `workforceEmployeeAssignment`.** TMF713 writes WorkforceEmployeeAssignment for a company's own workforce. In FSA the individual is often a visitor or crew from another company, and the relation is to the Individual, not to a role.
- **AccessPoint is not put in `place[]`.** AccessPoint is not a subtype of Place (remark on relation 9), so it gets its own list instead of a place with a role.
- **Equipment is the UX term; Product is the API term.** The API says `product`. The app says *equipment*.

## Attributes

| ActivityAssignment | Work attribute | Note |
|---|---|---|
| Period (1244) | `deliveryTimeSlot` (TimePeriod) | Start and end of the whole assignment. |
| Time slot (1245), all day (1246) | `workCharacteristic[]` | `Work` has no time slots of its own outside WorkforceEmployeeAssignment. All day is a time slot that covers the day. |
| Recurrence (1248), weekday (1247) | `workCharacteristic[]` | The characteristic pattern of quality rule 09-05, defined in the WorkSpecification's `specCharacteristic`. |
| Parent activity and child access request (relation 20) | `work[]` for the children, `workRelationship[]` for other relations | A WorkRelationship needs `relationshipType`. |
| Specification | `workSpecification` (WorkSpecificationRef) | |
| Agreement behind it | `agreement[]` (AgreementRef) | TMF651. |
| Status | `state` (WorkStateType) | See below. |

## Status

TMF713 has one state type, WorkStateType, for both `Work.state` and `WorkforceEmployeeAssignment.state`: acknowledged, rejected, pending, held, inProgress, cancelled, completed, failed, partial.

*Pending*, *approved*, *declined* and *revoked* are UX language (decision by the model owner, 2026-11-26). The API uses WorkStateType, and the app shows the UX term:

| WorkStateType (API) | UX term |
|---|---|
| `pending` | pending (1257) |
| `acknowledged` | approved (1258) |
| `rejected` | declined (1259) |
| `cancelled` | revoked (1260) |

The other WorkStateType values (`held`, `inProgress`, `completed`, `failed`, `partial`) have no UX term yet.

## Presence is not part of this

Presence (24) is *whether an individual or a resource is at a geographical location*: the actual outcome, not the plan. TMF713 doesn't cover it, so Presence stays an FSA API, as before.

## Model questions

1. **Information object 23 has no TM Forum reference.** ActivityAssignment has `Standard: Falskt` and an empty `Standard reference`, while Activity (90) and ActivityAssignmentSpecification (91) refer to TMF713. Should row 23 say TMF713 (Work)?
2. **Status terms are marked as business terms.** Terms 1257–1260 have information object ActivityAssignment and boundary Film Site Access, but they are UX language. Should they be marked as UX terms, so the API isn't expected to use them?
3. **Relations to Individual and Product are missing.** `semantic-relations.csv` has ActivityAssignment to Place (15), AccessPoint (18), Resource (19) and ActivityAssignment (20), but not to Individual or Product.
4. **Equipment has no Film Site Access row.** Business term *equipment* (93) maps to Product, but its Boundary is empty and its capability is *Film and TV production*.
5. **Access point.** AccessPoint (22) has no TM Forum reference and no data entity, so `accessPoint[]` refers to a resource of the FSA API that isn't defined yet.
6. **No data entity.** `data-entities.csv` has no entity for ActivityAssignment, so the fields above can't be checked against `data-elements.csv` yet.
7. **FSA definition overlaps.** `fsa/film-site-access.yaml` defines `GET /activityAssignmentSpecification` with its own schema (`resourceSpecification[]`, `productSpecification[]`). If the mapping is accepted, it becomes `GET /workSpecification` with `@type: ActivityAssignmentSpecification`.
