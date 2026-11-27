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

## Files in this folder

| Path | What it is |
|---|---|
| `postman/tmf632-postman-collection-5.0.0.json` | TM Forum Postman collection, version 5.0.0 (release 22.5): Individual, Organization, hub and listeners. Base URL variable `{{baseUrl}}`, set to `https://serverRoot/partyManagement/v5` |
| `ri/` | TM Forum reference implementation kit for TMF632 version 5.0.0 (image `tmforumorg/tmf632-v5.0.0-ri:1.0.1`, port 8632). See [running a reference implementation](../README.md#reference-implementations) |

## Specification

Not in this folder yet. The documentation above is version 4; the Postman collection and the reference implementation are version 5. Add the OpenAPI file that TM Forum publishes for version 5 before generating code or defining FSA resources from it.
