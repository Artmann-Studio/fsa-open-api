# TMF629 Customer Management

**FSA status:** Shapes the FSA definition  
**Documentation used:** REST API Specification, release 19.0, version 4.0.1 (Member Evaluation)  
**Base path:** `/tmf-api/customerManagement/v4`

## What Film Site Access uses it for

FSA's customer (a studio or site owner) and individuals who buy directly from FSA in tenant 0. The FSA definition already has `/customer` and `/customer/{id}`, shaped after this API.

Information objects in Encyclopedia Galactica (ID in brackets): Customer (30).

## Resources and operations

| Resource | Operations |
|---|---|
| Customer | GET, POST /customer; GET, PATCH, DELETE /customer/{id} |

Every API also has `POST /hub` and `DELETE /hub/{id}` to subscribe to its events, and the TM Forum query parameters `fields`, `offset` and `limit`.

## States

Customer.status is a free string with a statusReason, for example Approved.

## Specification

Not in this folder yet. Only the TM Forum document was available. Add the Swagger or OpenAPI file that TM Forum publishes for this API before generating code or defining FSA resources from it.
