# TM Forum Open APIs

The TM Forum Open APIs that Film Site Access uses or may use, one folder per API. Film Site Access uses a TM Forum Open API wherever one fits, and defines its own API in [`../fsa`](../fsa) only where none does.

Each folder has a README: what FSA uses the API for, the information objects it covers in Encyclopedia Galactica, its resources, operations and states. A folder holds the API's Swagger or OpenAPI file when we have one. For the others only the TM Forum PDF was available, and the PDFs are not in this repository: they are TM Forum documents, and this repository is public.

## Catalogue

**FSA status** says how far each API is used:

- **Specification in this folder**: the Swagger file is here and code can be generated from it.
- **Shapes the FSA definition**: `fsa/film-site-access.yaml` has resources shaped after this API.
- **Reference**: documented for later; nothing uses it yet.

| API | Name | Documentation | FSA status | Information objects |
|---|---|---|---|---|
| [TMF622](TMF622-product-ordering) | Product Ordering Management | R19.0.0, v4.0.0 | Reference | ProductOrder, Product, ProductOffering |
| [TMF629](TMF629-customer) | Customer Management | R19.0, v4.0.1 | Shapes the FSA definition | Customer |
| [TMF632](TMF632-party) | Party Management | R19.0.0, v4.0.0 | Shapes the FSA definition | Party, Individual, Organization, ContactMedium |
| [TMF633](TMF633-service-catalog) | Service Catalog Management | v4.0.0 | Shapes the FSA definition | ServiceSpecification |
| [TMF634](TMF634-resource-catalog) | Resource Catalog Management | R17.0.1, v2.0.2 | Shapes the FSA definition | ResourceSpecification |
| [TMF638](TMF638-service-inventory) | Service Inventory Management | v4.0.2 | Shapes the FSA definition | Service |
| [TMF639](TMF639-resource-inventory) | Resource Inventory Management | v4.0.0 | Reference | Resource, LogicalResource |
| [TMF640](TMF640-service-activation) | Service Activation and Configuration | v4.0.2 | Reference | Service, Resource |
| [TMF651](TMF651-agreement) | Agreement Management | R19.0.1, v4.0.1 | Shapes the FSA definition | Agreement, AgreementSpecification |
| [TMF669](TMF669-party-role) | Party Role Management | R19.0, v4.0.0 | Reference | PartyRole, PartyRoleSpecification |
| [TMF673](TMF673-geographic-address) | Geographic Address Management | R17.5.0, v1.2.2 | Reference | GeographicAddress |
| [TMF674](TMF674-geographic-site) | Geographic Site Management | v4.0.0 | Specification in this folder | Place, GeographicSite |
| [TMF713](TMF713-work-management) | Work Management | v4.0.0 beta | Specification in this folder | ActivityAssignment, ActivityAssignmentSpecification, Activity |
| [TMF720](TMF720-digital-identity) | Digital Identity Management | v4.0.0 | Reference | DigitalIdentity, Credential |

TMF634 and TMF673 are documented in older releases (version 2 and version 1) than the rest. Their paths start at `/api/...` instead of `/tmf-api/<api>/v4`. Choose a version 4 release before defining anything from them.

## Referenced by the model, not in this set

`information-objects.csv` refers to these APIs, but there is no documentation for them here yet:

| API | Name | Information objects |
|---|---|---|
| TMF620 | Product Catalog Management | ProductSpecification, ProductOffering, MarketSegment |
| TMF637 | Product Inventory Management | Product, ProductCharacteristic, ProductInventory |
| TMF648 | Quote Management | Quote |
| TMF666 | Account Management | FinancialAccount |
| TMF667 | Document Management | Document, Attachment |
| TMF672 | User Roles and Permissions | PermissionSet, PermissionSpecification, PermissionSpecificationSet |
| TMF675 | Geographic Location Management | Place |
| TMF681 | Communication Management | Communication |
| TMF699 | Sales Management | SalesLead, SalesOpportunity, MarketingCampaign |

## No TM Forum API

These stay in the FSA definition, because no TM Forum Open API covers them:

- **Presence** (24): whether an individual or a resource is at a location.
- **AccessPoint** (22): a point of entry or exit at a location.
- **Search**.
- **Sign-in exchange**: sign-up, email verification, sign-in and sign-out. TMF720 describes the digital identity and its credentials, not the exchange.
- **Emergency**: declaring and listing emergencies at a location.

**Activity** was on this list. ActivityAssignment is now modelled after TMF713 Work Management: see [`../docs/activity-assignment.md`](../docs/activity-assignment.md).

## Adding an API

1. Create a folder `TMFnnn-short-name` and a README in the same layout as the others.
2. Add the Swagger or OpenAPI file exactly as TM Forum publishes it. Don't edit it. FSA extensions go in `fsa/film-site-access.yaml` or in a JSON Schema referenced by `@schemaLocation`.
3. Add the API to the catalogue above.
