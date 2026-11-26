# TMF640 Service Activation and Configuration

**FSA status:** Reference  
**Documentation used:** User Guide, version 4.0.2 (TM Forum Approved)  
**Base path:** `/tmf-api/ServiceActivationAndConfiguration/v4`

## What Film Site Access uses it for

Activating a service on the resources that deliver it, for example opening a lock for an approved access request. Not in the MVP.

Information objects in Encyclopedia Galactica (ID in brackets): Service (39), Resource (40).

## Resources and operations

| Resource | Operations |
|---|---|
| Service | GET, POST /service; GET, PATCH, DELETE /service/{id} |
| Monitor | GET /monitor; GET /monitor/{id} |

Every API also has `POST /hub` and `DELETE /hub/{id}` to subscribe to its events, and the TM Forum query parameters `fields`, `offset` and `limit`.

## States

Service.state as in TMF638. Monitor.state tracks an asynchronous request: InProgress, InError, Completed.

## Specification

Not in this folder yet. Only the TM Forum document was available. Add the Swagger or OpenAPI file that TM Forum publishes for this API before generating code or defining FSA resources from it.
