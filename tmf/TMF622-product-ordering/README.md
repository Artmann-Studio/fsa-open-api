# TMF622 Product Ordering Management

**FSA status:** Reference  
**Documentation used:** REST API Specification, release 19.0.0, version 4.0.0 (Member Evaluation)  
**Base path:** `/tmf-api/productOrderingManagement/v4`

## What Film Site Access uses it for

A customer's order for an FSA service, for example *Basic for individual*. Not in the MVP; the app signs a customer up through `POST /signUp` in the FSA definition.

Information objects in Encyclopedia Galactica (ID in brackets): ProductOrder (29), Product (36), ProductOffering (27).

## Resources and operations

| Resource | Operations |
|---|---|
| ProductOrder | GET, POST /productOrder; GET, PATCH, DELETE /productOrder/{id} |
| CancelProductOrder | GET, POST /cancelProductOrder; GET /cancelProductOrder/{id} |

Every API also has `POST /hub` and `DELETE /hub/{id}` to subscribe to its events, and the TM Forum query parameters `fields`, `offset` and `limit`.

## States

ProductOrder.state and ProductOrderItem.state: acknowledged, rejected, pending, inProgress, held, assessingCancellation, cancelled, completed, failed, partial (from the state definitions in the document).

## Specification

Not in this folder yet. Only the TM Forum document was available. Add the Swagger or OpenAPI file that TM Forum publishes for this API before generating code or defining FSA resources from it.
