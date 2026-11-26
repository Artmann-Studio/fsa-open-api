# TMF771 Resource Usage Management

**FSA status:** Reference  
**Documentation used:** Postman collection, version 5  
**Base path:** `/tmf-api/resourceUsageManagement/v5`

## What Film Site Access uses it for

A record of a resource being used, for example a gate opened or a card reader used, with characteristics that describe the use. It can feed billing. Not in the MVP.

No information object in Encyclopedia Galactica refers to TMF771 yet.

## Resources and operations

| Resource | Operations |
|---|---|
| ResourceUsage | GET, POST /resourceUsage; GET, PATCH, DELETE /resourceUsage/{id} |
| ResourceUsageSpecification | GET, POST /resourceUsageSpecification; GET, PATCH, DELETE /resourceUsageSpecification/{id} |

Every API also has `POST /hub` and `DELETE /hub/{id}` to subscribe to its events (this collection also has `GET /hub/{id}`), and the TM Forum query parameters `fields`, `offset` and `limit`.

## Files in this folder

| Path | What it is |
|---|---|
| `postman/TMF771-Resource_Usage_Management.postman_collection.json` | TM Forum Postman collection, 19 requests, downloaded as `Resource Usage Management.postman_collection.json` and renamed to carry the API number and no spaces. Base URL variable `{{baseUrl}}`, set to `{{apiRoot}}/tmf-api/resourceUsageManagement/v5/` |
| `ri/` | TM Forum reference implementation kit for TMF771 version 5.0.0 (image `tmforumorg/tmf771-v5.0.0-ri:1.0.1`, port 8771). See [running a reference implementation](../README.md#reference-implementations) |

## Specification

Not in this folder yet. Add the OpenAPI file that TM Forum publishes for this API before generating code or defining FSA resources from it.
