# TMF639 Resource Inventory Management

**FSA status:** Reference  
**Documentation used:** User Guide, version 4.0.0 (Team Approved, pre-production)  
**Base path:** `/tmf-api/resourceInventoryManagement/v4`

## What Film Site Access uses it for

The resources themselves: a door lock, a gate, a card reader, a deployed service. A candidate for the physical side of an access point, which is not itself a resource.

Information objects in Encyclopedia Galactica (ID in brackets): Resource (40), LogicalResource (101).

## Resources and operations

| Resource | Operations |
|---|---|
| Resource | GET, POST /resource; GET, PATCH, DELETE /resource/{id} |

Every API also has `POST /hub` and `DELETE /hub/{id}` to subscribe to its events, and the TM Forum query parameters `fields`, `offset` and `limit`.

## States

Resource has four states: administrativeState (locked, unlocked, shutdown), operationalState (enable, disable), usageState (idle, active, busy) and resourceStatus (standby, alarm, available, reserved, suspended). The document gives these as examples ("such as"), not complete lists.

## Files in this folder

| Path | What it is |
|---|---|
| `postman/TMF639-ResourceInventory-v4.0.0.postman_collection.json` | TM Forum Postman collection, version 4.0.0 (release 19.5, December 2019): Resource, hub and listeners, 11 requests. It uses the variables `{{scheme}}`, `{{host}}`, `{{port}}`, `{{id}}`, `fields`, `offset` and `limit`, and has no test scripts. The listener requests have no example event, only the text "The event data" |
| `postman/TMF639-ResourceInventory-v4.postman_environment.json` | TM Forum Postman environment from 2020. It sets `scheme`, `host` and `port` to a TM Forum sandbox on `mybluemix.net`, which is probably no longer running. To use the reference implementation instead, set `host` to `localhost` and `port` to `8639` |
| `ri/` | TM Forum reference implementation kit for TMF639 version 4.0.0 (image `tmforumorg/tmf639-v4.0.0-ri:1.0.1`, ports 8639 for HTTP and 4639 for HTTPS). It needs a certificate in `ri/certs`; see [running a reference implementation](../README.md#reference-implementations) |

The collection's examples use the four states above with the values unlocked, disable, idle, available and reserved.

## Specification

Not in this folder yet. Add the Swagger or OpenAPI file that TM Forum publishes for this API before generating code or defining FSA resources from it.
