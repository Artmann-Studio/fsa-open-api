# TMF651 Agreement Management

**FSA status:** Shapes the FSA definition  
**Documentation used:** REST API Specification, release 19.0.1, version 4.0.1 (TM Forum Approved)  
**Base path:** `/tmf-api/agreementManagement/v4`

## What Film Site Access uses it for

Agreements between FSA and its customer, and between the customer and their own customers, for example terms of use and privacy consent. The FSA definition has `/agreementSpecification`.

Information objects in Encyclopedia Galactica (ID in brackets): Agreement (42), AgreementSpecification (103), AgreementAuthorization (69), PartyPrivacyAgreement (61).

## Resources and operations

| Resource | Operations |
|---|---|
| Agreement | GET, POST /agreement; GET, PATCH, DELETE /agreement/{id} |
| AgreementSpecification | GET, POST /agreementSpecification; GET, PATCH, DELETE /agreementSpecification/{id} |

Every API also has `POST /hub` and `DELETE /hub/{id}` to subscribe to its events, and the TM Forum query parameters `fields`, `offset` and `limit`.

## States

Agreement.status is a string; typical values are in process, approved and rejected. AgreementAuthorization.state is a string with similar values.

## Specification

Not in this folder yet. Only the TM Forum document was available. Add the Swagger or OpenAPI file that TM Forum publishes for this API before generating code or defining FSA resources from it.
