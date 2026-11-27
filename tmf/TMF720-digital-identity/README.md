# TMF720 Digital Identity Management

**FSA status:** Reference  
**Documentation used:** Specification, version 4.0.0 (TM Forum Approved)  
**Base path:** `/tmf-api/digitalIdentityManagement/v4`

## What Film Site Access uses it for

A person's digital identity and its credentials (password, passkey, authenticator). It covers what the identity is, not the sign-in exchange: sign-in, email verification and sign-out stay in the FSA definition.

Information objects in Encyclopedia Galactica (ID in brackets): DigitalIdentity (92), Credential (93), UserAccount (88), AuthenticationEntity (71).

## Resources and operations

| Resource | Operations |
|---|---|
| DigitalIdentity | GET, POST /digitalIdentity; GET, PATCH, DELETE /digitalIdentity/{id} |

Every API also has `POST /hub` and `DELETE /hub/{id}` to subscribe to its events, and the TM Forum query parameters `fields`, `offset` and `limit`.

## States

DigitalIdentity.status, for example active or pending. Credential.state: active, inactive, expired. Credential has a trustLevel.

## Files in this folder

| Path | What it is |
|---|---|
| `postman/TMF720-DigitalIdentity-v4.0.0.postman_collection.json` | TM Forum Postman collection, version 4.0.0 (January 2021): DigitalIdentity, hub and listeners. It uses the variables `{{scheme}}`, `{{host}}`, `{{port}}`, `{{id}}`, `fields`, `offset` and `limit`, and has no test scripts. The examples contain a sample login and password; they are TM Forum sample values, not FSA credentials |
| `ri/` | TM Forum reference implementation kit for TMF720 version 4.0.0 (image `tmforumorg/tmf720-v4.0.0-ri:1.0.2`, ports 8720 for HTTP and 4720 for HTTPS). It needs a certificate in `ri/certs`; see [running a reference implementation](../README.md#reference-implementations) |

## Specification

Not in this folder yet. Add the Swagger file that TM Forum publishes for this API before generating code or defining FSA resources from it.
