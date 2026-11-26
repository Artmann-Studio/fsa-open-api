# TMF633 Service Catalog Management

**FSA status:** Shapes the FSA definition  
**Documentation used:** User Guide, version 4.0.0 (TM Forum Approved)  
**Base path:** `/tmf-api/serviceCatalogManagement/v4`

## What Film Site Access uses it for

The kinds of service a customer can have, for example *Basic for individual*. Tenant 0 holds FSA's own catalogue. The FSA definition already has `GET /serviceSpecification`.

Information objects in Encyclopedia Galactica (ID in brackets): ServiceSpecification (100), Category (3), Characteristic (5).

## Resources and operations

| Resource | Operations |
|---|---|
| ServiceCatalog | GET, POST /serviceCatalog; GET, PATCH, DELETE /serviceCatalog/{id} |
| ServiceCategory | GET, POST /serviceCategory; GET, PATCH, DELETE /serviceCategory/{id} |
| ServiceCandidate | GET, POST /serviceCandidate; GET, PATCH, DELETE /serviceCandidate/{id} |
| ServiceSpecification | GET, POST /serviceSpecification; GET, PATCH, DELETE /serviceSpecification/{id} |
| ImportJob, ExportJob | GET, POST /importJob, /exportJob; GET, DELETE /{job}/{id} |

Every API also has `POST /hub` and `DELETE /hub/{id}` to subscribe to its events, and the TM Forum query parameters `fields`, `offset` and `limit`.

## States

Catalogue items carry lifecycleStatus and validFor. Versioned catalogue items are addressed by id and version.

## Specification

Not in this folder yet. Only the TM Forum document was available. Add the Swagger or OpenAPI file that TM Forum publishes for this API before generating code or defining FSA resources from it.
