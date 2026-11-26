# TMF638 Service Inventory Management

**FSA status:** Shapes the FSA definition  
**Documentation used:** User Guide, version 4.0.2 (TM Forum Approved)  
**Base path:** `/tmf-api/serviceInventory/v4`

## What Film Site Access uses it for

The services a customer has: an instance of a service specification, for example access to a film site for a period. The FSA definition already has `/service` and `/service/{id}`, shaped after this API.

Information objects in Encyclopedia Galactica (ID in brackets): Service (39).

## Resources and operations

| Resource | Operations |
|---|---|
| Service | GET, POST /service; GET, PATCH, DELETE /service/{id} |

Every API also has `POST /hub` and `DELETE /hub/{id}` to subscribe to its events, and the TM Forum query parameters `fields`, `offset` and `limit`.

## States

Service.state (ServiceStateType): feasibilityChecked (spelled feasabilityChecked in the document), designed, reserved, inactive, active, terminated.

## Specification

Not in this folder yet. Only the TM Forum document was available. Add the Swagger or OpenAPI file that TM Forum publishes for this API before generating code or defining FSA resources from it.
