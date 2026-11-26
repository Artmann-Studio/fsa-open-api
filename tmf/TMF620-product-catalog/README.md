# TMF620 Product Catalog Management

**FSA status:** Reference  
**Documentation used:** Postman collection, version 5.0.0  
**Base path:** `/productCatalogManagement/v5` (the collection's base URL is `https://serverRoot/productCatalogManagement/v5/`)

## What Film Site Access uses it for

The catalogue of what FSA's customer offers: product specifications and product offerings, for example the equipment a production can book at a location. Not in the MVP.

Information objects in Encyclopedia Galactica (ID in brackets): ProductSpecification (28), ProductOffering (27), MarketSegment (26).

## Resources and operations

| Resource | Operations |
|---|---|
| ProductCatalog | GET, POST /productCatalog; GET, PATCH, DELETE /productCatalog/{id} |
| Category | GET, POST /category; GET, PATCH, DELETE /category/{id} |
| ProductOffering | GET, POST /productOffering; GET, PATCH, DELETE /productOffering/{id} |
| ProductOfferingPrice | GET, POST /productOfferingPrice; GET, PATCH, DELETE /productOfferingPrice/{id} |
| ProductSpecification | GET, POST /productSpecification; GET, PATCH, DELETE /productSpecification/{id} |
| ImportJob, ExportJob | GET, POST /importJob, /exportJob; GET, DELETE /{job}/{id} |

Every API also has `POST /hub` and `DELETE /hub/{id}` to subscribe to its events, and the TM Forum query parameters `fields`, `offset` and `limit`.

## States

Catalogue items carry lifecycleStatus and validFor. ImportJob and ExportJob have a status; the collection's examples use Not Started, Running, Succeeded and Failed.

## Files in this folder

| Path | What it is |
|---|---|
| `postman/tmf620-postman-collection-5.0.0.json` | TM Forum Postman collection, version 5.0.0, 59 requests. It was downloaded three times, under the names `tmf629-…`, `tmf634-…` and `tmf638-…-postman-collection-5.0.0.json`. All three are this TMF620 collection and differ only in Postman's generated ids, so one copy is kept, renamed after the API it holds |

There is no reference implementation kit for TMF620 here.

## Specification

Not in this folder yet. Add the OpenAPI file that TM Forum publishes for this API before generating code or defining FSA resources from it.
