# TMF634 Resource Catalog Management

**FSA status:** Shapes the FSA definition  
**Documentation used:** REST API Specification, release 17.0.1, version 2.0.2 (TM Forum Approved)  
**Base path:** /catalogManagement (release 17 style, without the /tmf-api/.../v4 prefix)

## What Film Site Access uses it for

The kinds of resource used to deliver a service: physical (locks, gates, card readers) and logical (software, deployed services). The split into physical and logical specifications matches FSA's PhysicalResource and LogicalResource. The FSA definition has `GET /resourceSpecification`.

Information objects in Encyclopedia Galactica (ID in brackets): ResourceSpecification (35), Resource (40), LogicalResource (101).

> This document is an older generation than the others (release 17, version 2). Its paths and conventions differ from the version 4 APIs. A version 5 reference implementation is now in `ri/`: define FSA resources from version 5, not from this document.

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

## Files in this folder

| Path | What it is |
|---|---|
| `ri/` | TM Forum reference implementation kit for TMF634 version 5.0.0 (image `tmforumorg/tmf634-v5.0.0-ri:1.0.1`, port 8634). See [running a reference implementation](../README.md#reference-implementations) |

The Postman collection downloaded as `tmf634-postman-collection-5.0.0.json` turned out to be TMF620 Product Catalog Management, so it is in [`../TMF620-product-catalog`](../TMF620-product-catalog). The TMF634 collection is still missing.

## Specification

Not in this folder yet. The documentation above is release 17 (version 2); the reference implementation is version 5, which is the release to define FSA resources from. Add the OpenAPI file that TM Forum publishes for version 5 first.
