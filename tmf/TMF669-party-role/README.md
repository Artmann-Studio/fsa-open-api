# TMF669 Party Role Management

**FSA status:** Reference  
**Documentation used:** REST API Specification, release 19.0, version 4.0.0 (Member Evaluation)  
**Base path:** `/tmf-api/partyRoleManagement/v4`

## What Film Site Access uses it for

The roles a party plays in FSA: the person assigned to an activity assignment, an approver, a site manager. System roles and permissions themselves are [TMF672](../TMF672-user-roles-permissions).

Information objects in Encyclopedia Galactica (ID in brackets): PartyRole (46), PartyRoleSpecification (67), RelatedPartyRole (47).

## Resources and operations

| Resource | Operations |
|---|---|
| PartyRole | GET, POST /partyRole; GET, PATCH, DELETE /partyRole/{id} |

Every API also has `POST /hub` and `DELETE /hub/{id}` to subscribe to its events, and the TM Forum query parameters `fields`, `offset` and `limit`.

## States

PartyRole.status is a free string with a statusReason, for example Approved.

## Files in this folder

| Path | What it is |
|---|---|
| `postman/tmf669-postman-collection-5.0.0.json` | TM Forum Postman collection, version 5.0.0 (release 23.0, June 2023): PartyRole, PartyRoleSpecification, hub and listeners. The base URL variable is only `https://serverRoot`; set it to the full API root when you use it |
| `ri/` | TM Forum reference implementation kit for TMF669 version 5.0.0 (image `tmforumorg/tmf669-v5.0.0-ri:1.0.1`, port 8669). See [running a reference implementation](../README.md#reference-implementations) |

Version 5 adds the PartyRoleSpecification resource (`/partyRoleSpecification`), which matches the information object PartyRoleSpecification (67). In version 5 the examples use status and lifecycleStatus values such as validationInProgress and validated.

## Specification

Not in this folder yet. The documentation above is version 4; the Postman collection and the reference implementation are version 5. Add the OpenAPI file that TM Forum publishes for version 5 before generating code or defining FSA resources from it.
