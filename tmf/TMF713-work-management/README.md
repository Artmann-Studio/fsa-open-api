# TMF713 Work Management

**FSA status:** Specification in this folder  
**Documentation used:** Swagger, version 4.0.0 beta  
**Base path:** `/tmf-api/workManagement/v4`

## What Film Site Access uses it for

**ActivityAssignment is modelled after Work Management.** An activity assignment is a `Work`; its specification is a `WorkSpecification`. See [the mapping](../../docs/activity-assignment.md).

Information objects in Encyclopedia Galactica (ID in brackets): ActivityAssignment (23), ActivityAssignmentSpecification (91), Activity (90).

## Resources and operations

| Resource | Operations |
|---|---|
| Work | GET, POST /work; GET, PATCH, DELETE /work/{id} |
| WorkSpecification | GET, POST /workSpecification; GET, PATCH, DELETE /workSpecification/{id} |

Every API also has `POST /hub` and `DELETE /hub/{id}` to subscribe to its events, and the TM Forum query parameters `fields`, `offset` and `limit`.

## States

Work.state and WorkforceEmployeeAssignment.state (WorkStateType): acknowledged, rejected, pending, held, inProgress, cancelled, completed, failed, partial.

## Specification

`TMF713.json`, Swagger 2.0, version 4.0.0 beta. It was rebuilt from the swagger printed in `TMF713_Work_Management_v4.0.0_beta_swagger.pdf`: the PDF repeats a line or two at each page break, and those repeats were removed. The result passes `openapi-spec-validator`. Replace it with the file TM Forum publishes when you have it.
