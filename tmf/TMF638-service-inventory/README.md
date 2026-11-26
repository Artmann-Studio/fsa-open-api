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

## Files in this folder

| Path | What it is |
|---|---|
| `ri/` | TM Forum reference implementation kit for TMF638 version 5.0.0 (image `tmforumorg/tmf638-v5.0.0-ri:1.0.1`, port 8638). See [running a reference implementation](../README.md#reference-implementations) |

The Postman collection downloaded as `tmf638-postman-collection-5.0.0.json` turned out to be TMF620 Product Catalog Management, so it is in [`../TMF620-product-catalog`](../TMF620-product-catalog). The TMF638 collection is still missing.

## Specification

Not in this folder yet. The documentation above is version 4; the reference implementation is version 5. Add the OpenAPI file that TM Forum publishes for version 5 before generating code or defining FSA resources from it.
