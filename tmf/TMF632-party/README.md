# TMF632 Party Management

**FSA status:** Shapes the FSA definition  
**Documentation used:** REST API Specification, release 19.0.0, version 4.0.0 (Member Evaluation)  
**Base path:** `/tmf-api/party/v4`

## What Film Site Access uses it for

People and organisations: crew, visitors, production companies, studios. The FSA definition uses `Individual`, `Organization` and `ContactMedium` from this API in sign-up.

Information objects in Encyclopedia Galactica (ID in brackets): Party (54), Individual (31), Organization (33), IndividualIdentification (60), PartyIdentification (59), ContactMedium (6).

## Resources and operations

| Resource | Operations |
|---|---|
| Individual | GET, POST /individual; GET, PATCH, DELETE /individual/{id} |
| Organization | GET, POST /organization; GET, PATCH, DELETE /organization/{id} |

Every API also has `POST /hub` and `DELETE /hub/{id}` to subscribe to its events, and the TM Forum query parameters `fields`, `offset` and `limit`.

## States

Individual.status and Organization.status are strings; the examples use initialized and validated.

## Specification

Not in this folder yet. Only the TM Forum document was available. Add the Swagger or OpenAPI file that TM Forum publishes for this API before generating code or defining FSA resources from it.
