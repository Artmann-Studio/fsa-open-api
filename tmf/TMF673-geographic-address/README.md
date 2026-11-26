# TMF673 Geographic Address Management

**FSA status:** Reference  
**Documentation used:** REST API Specification, release 17.5.0, version 1.2.2 (Member Evaluation)  
**Base path:** /geographicAddressManagement (release 17 style, without the /tmf-api/.../v4 prefix)

## What Film Site Access uses it for

The address of a location, as part of a geographic site.

Information objects in Encyclopedia Galactica (ID in brackets): GeographicAddress (48).

> This document is an older generation than the others (release 17.5, version 1). Check with TM Forum which version 4 release to use before defining anything from it.

## Resources and operations

| Resource | Operations |
|---|---|
| GeographicAddress | GET /geographicAddress; GET /geographicAddress/{id}; GET /geographicAddress/{id}/geographicSubAddress |
| GeographicAddressValidation | GET, POST /geographicAddressValidation; GET, PATCH, DELETE /geographicAddressValidation/{id} |
| Area, Street, StreetSegment | GET /area, /street, /street/{id}/streetSegment |

Every API also has `POST /hub` and `DELETE /hub/{id}` to subscribe to its events, and the TM Forum query parameters `fields`, `offset` and `limit`.

## States

GeographicAddressValidation.status: rejected, inProgress, done, terminatedWithError.

## Specification

Not in this folder yet. Only the TM Forum document was available. Add the Swagger or OpenAPI file that TM Forum publishes for this API before generating code or defining FSA resources from it.
