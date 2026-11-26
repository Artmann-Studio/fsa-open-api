# TMF669 Party Role Management

**FSA status:** Reference  
**Documentation used:** REST API Specification, release 19.0, version 4.0.0 (Member Evaluation)  
**Base path:** `/tmf-api/partyRoleManagement/v4`

## What Film Site Access uses it for

The roles a party plays in FSA: the person assigned to an activity assignment, an approver, a site manager. System roles and permissions themselves are TMF672, which is not in this set.

Information objects in Encyclopedia Galactica (ID in brackets): PartyRole (46), PartyRoleSpecification (67), RelatedPartyRole (47).

## Resources and operations

| Resource | Operations |
|---|---|
| PartyRole | GET, POST /partyRole; GET, PATCH, DELETE /partyRole/{id} |

Every API also has `POST /hub` and `DELETE /hub/{id}` to subscribe to its events, and the TM Forum query parameters `fields`, `offset` and `limit`.

## States

PartyRole.status is a free string with a statusReason, for example Approved.

## Specification

Not in this folder yet. Only the TM Forum document was available. Add the Swagger or OpenAPI file that TM Forum publishes for this API before generating code or defining FSA resources from it.
