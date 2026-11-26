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

## Specification

Not in this folder yet. Only the TM Forum document was available. Add the Swagger or OpenAPI file that TM Forum publishes for this API before generating code or defining FSA resources from it.
