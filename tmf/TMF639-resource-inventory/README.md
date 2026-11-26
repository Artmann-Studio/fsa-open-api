# TMF639 Resource Inventory Management

**FSA status:** Reference  
**Documentation used:** User Guide, version 4.0.0 (Team Approved, pre-production)  
**Base path:** `/tmf-api/resourceInventoryManagement/v4`

## What Film Site Access uses it for

The resources themselves: a door lock, a gate, a card reader, a deployed service. A candidate for the physical side of an access point, which is not itself a resource.

Information objects in Encyclopedia Galactica (ID in brackets): Resource (40), LogicalResource (101).

## Resources and operations

| Resource | Operations |
|---|---|
| Resource | GET, POST /resource; GET, PATCH, DELETE /resource/{id} |

Every API also has `POST /hub` and `DELETE /hub/{id}` to subscribe to its events, and the TM Forum query parameters `fields`, `offset` and `limit`.

## States

Resource has four states: administrativeState (locked, unlocked, shutdown), operationalState (enable, disable), usageState (idle, active, busy) and resourceStatus (standby, alarm, available, reserved, suspended). The document gives these as examples ("such as"), not complete lists.

## Specification

Not in this folder yet. Only the TM Forum document was available. Add the Swagger or OpenAPI file that TM Forum publishes for this API before generating code or defining FSA resources from it.
