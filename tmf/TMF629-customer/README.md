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

## Files in this folder

| Path | What it is |
|---|---|
| `ri/` | TM Forum reference implementation kit for TMF629 version 5.0.0 (image `tmforumorg/tmf629-v5.0.0-ri:1.0.1`, port 8629). See [running a reference implementation](../README.md#reference-implementations) |

The Postman collection downloaded as `tmf629-postman-collection-5.0.0.json` turned out to be TMF620 Product Catalog Management, so it is in [`../TMF620-product-catalog`](../TMF620-product-catalog). The TMF629 collection is still missing.

## Specification

Not in this folder yet. The documentation above is version 4; the reference implementation is version 5. Add the OpenAPI file that TM Forum publishes for version 5 before generating code or defining FSA resources from it. The running reference implementation serves its API documentation, which shows the version 5 contract until then.
