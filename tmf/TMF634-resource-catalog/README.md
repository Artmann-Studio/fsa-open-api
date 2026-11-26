# TMF634 Resource Catalog Management

**FSA status:** Shapes the FSA definition  
**Documentation used:** REST API Specification, release 17.0.1, version 2.0.2 (TM Forum Approved)  
**Base path:** /catalogManagement (release 17 style, without the /tmf-api/.../v4 prefix)

## What Film Site Access uses it for

The kinds of resource used to deliver a service: physical (locks, gates, card readers) and logical (software, deployed services). The split into physical and logical specifications matches FSA's PhysicalResource and LogicalResource. The FSA definition has `GET /resourceSpecification`.

Information objects in Encyclopedia Galactica (ID in brackets): ResourceSpecification (35), Resource (40), LogicalResource (101).

> This document is an older generation than the others (release 17, version 2). Its paths and conventions differ from the version 4 APIs. Check with TM Forum which version 4 release to use before defining anything from it.

## Resources and operations

| Resource | Operations |
|---|---|
| ResourceCatalog, ResourceCategory, ResourceCandidate | GET, POST, PATCH, DELETE |
| ResourceSpecification | GET, POST /resourceSpecification; GET, PATCH, DELETE /resourceSpecification/{id} |
| PhysicalResourceSpec | GET, POST /physicalResourceSpec; GET, PATCH, DELETE /physicalResourceSpec/{id} |
| LogicalResourceSpec | GET, POST /logicalResourceSpec; GET, PATCH, DELETE /logicalResourceSpec/{id} |
| ImportJob, ExportJob | GET, POST; GET, DELETE by id |

Every API also has `POST /hub` and `DELETE /hub/{id}` to subscribe to its events, and the TM Forum query parameters `fields`, `offset` and `limit`.

## States

Catalogue items carry lifecycleStatus and validFor.

## Specification

Not in this folder yet. Only the TM Forum document was available. Add the Swagger or OpenAPI file that TM Forum publishes for this API before generating code or defining FSA resources from it.
