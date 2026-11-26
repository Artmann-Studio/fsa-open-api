# TMF674 Geographic Site Management

**FSA status:** Specification in this folder  
**Documentation used:** User Guide, version 4.0.0 (Team Approved, pre-production)  
**Base path:** `/tmf-api/geographicSiteManagement/v4`

## What Film Site Access uses it for

Locations: a film site, a studio lot, a stage, with their addresses and opening hours. Locations are version 0.4 in the MVP roadmap.

Information objects in Encyclopedia Galactica (ID in brackets): Place (49), GeographicSite (102), GeographicalPlace (99), GeographiclLocation (98).

## Resources and operations

| Resource | Operations |
|---|---|
| GeographicSite | GET, POST /geographicSite; GET, PATCH, DELETE /geographicSite/{id} |

Every API also has `POST /hub` and `DELETE /hub/{id}` to subscribe to its events, and the TM Forum query parameters `fields`, `offset` and `limit`.

## States

GeographicSite.status is a string.

## Specification

`TMF674.yaml`, Swagger 2.0, version 4.0.0. The ASP.NET Core server in `generated/Tmf674.Server` is generated from it.
