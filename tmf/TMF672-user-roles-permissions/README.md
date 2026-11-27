# TMF672 User Role Permission Management

**FSA status:** Shapes the FSA definition  
**Documentation used:** Postman collection, version 5.1.0  
**Base path:** `/rolesAndPermissionsManagement/v5` (the collection's `apiRoot` is `https://serverRoot/rolesAndPermissionsManagement/v5`)

## What Film Site Access uses it for

What a party may do: the permissions on a type of place, resource or other asset, grouped into sets and assigned to a party role. It is the authorization side of sign-in; TMF720 is the identity side and TMF669 the roles.

The FSA definition has `/permissionSpecification` and `/permissionSet` in the shape of version 5.1 (ADR 0008 in fsa-backend), with these restrictions:

- The permission specifications are fixed: `managePrivacyPolicy`, `manageTermsOfUse` and `actOnBehalfOf`.
- A permission set holds exactly one permission, assigned to a user account (`user.securityPrincipal`).
- The only `managedAssetGroup` is one party, as a `FilterAssetGroup` with `entityType` `Party` and the filter `id=<party id>`.
- PATCH changes only `validFor.endDateTime`, and only to bring it forward. That is how a permission is revoked.

Information objects in Encyclopedia Galactica (ID in brackets): PermissionSpecification (94), PermissionSet (95), PermissionSpecificationSet (96).

## Resources and operations

| Resource | Operations |
|---|---|
| PermissionSpecification | GET, POST /permissionSpecification; GET, PATCH, DELETE /permissionSpecification/{id} |
| PermissionSpecificationSet | GET, POST /permissionSpecificationSet; GET, PATCH, DELETE /permissionSpecificationSet/{id} |
| PermissionSet | GET, POST /permissionSet; GET, PATCH, DELETE /permissionSet/{id} |
| CheckPermission | GET, POST /checkPermission; GET /checkPermission/{id} |

Every API also has `POST /hub` and `DELETE /hub/{id}` to subscribe to its events (this collection also has `GET /hub/{id}`), and the TM Forum query parameters `fields`, `offset` and `limit`.

CheckPermission asks whether a party may perform an action; it is a task resource, created and then read.

## States

CheckPermission.state, from the collection's examples: inProgress, done, terminatedWithError.

## Files in this folder

| Path | What it is |
|---|---|
| `postman/TMF672-User_Role_Permission_Management_API-v5.1.0.postman_collection.json` | TM Forum Postman collection, version 5.1.0, 32 requests |
| `ri/` | TM Forum reference implementation kit for TMF672 version 5.1.0 (image `tmforumorg/tmf672-v5.1.0-ri:1.0.1`, port 8672). See [running a reference implementation](../README.md#reference-implementations) |

## Specification

Not in this folder yet. Add the OpenAPI file that TM Forum publishes for this API before generating code or defining FSA resources from it.
