# TM Forum Open APIs

The TM Forum Open APIs that Film Site Access uses or may use, one folder per API. Film Site Access uses a TM Forum Open API wherever one fits, and defines its own API in [`../fsa`](../fsa) only where none does.

Each folder has a README: what FSA uses the API for, the information objects it covers in Encyclopedia Galactica, its resources, operations and states. A folder holds the API's Swagger or OpenAPI file when we have one. For the others only the TM Forum PDF was available, and the PDFs are not in this repository: they are TM Forum documents, and this repository is public.

## Catalogue

**FSA status** says how far each API is used:

- **Specification in this folder**: the Swagger file is here and code can be generated from it.
- **Shapes the FSA definition**: `fsa/film-site-access.yaml` has resources shaped after this API.
- **Reference**: documented for later; nothing uses it yet.

**In the folder** lists the TM Forum files kept there: the specification (Spec), a Postman collection (Postman) and a reference implementation kit (RI), with their versions.

| API | Name | Documentation | In the folder | FSA status | Information objects |
|---|---|---|---|---|---|
| [TMF620](TMF620-product-catalog) | Product Catalog Management | Postman v5.0.0 | Postman v5.0.0 | Reference | ProductSpecification, ProductOffering, MarketSegment |
| [TMF622](TMF622-product-ordering) | Product Ordering Management | R19.0.0, v4.0.0 | | Reference | ProductOrder, Product, ProductOffering |
| [TMF629](TMF629-customer) | Customer Management | R19.0, v4.0.1 | RI v5.0.0 | Shapes the FSA definition | Customer |
| [TMF632](TMF632-party) | Party Management | R19.0.0, v4.0.0 | Postman v5.0.0, RI v5.0.0 | Shapes the FSA definition | Party, Individual, Organization, ContactMedium |
| [TMF633](TMF633-service-catalog) | Service Catalog Management | v4.0.0 | | Shapes the FSA definition | ServiceSpecification |
| [TMF634](TMF634-resource-catalog) | Resource Catalog Management | R17.0.1, v2.0.2 | RI v5.0.0 | Shapes the FSA definition | ResourceSpecification |
| [TMF638](TMF638-service-inventory) | Service Inventory Management | v4.0.2 | RI v5.0.0 | Shapes the FSA definition | Service |
| [TMF639](TMF639-resource-inventory) | Resource Inventory Management | v4.0.0 | Postman v4.0.0, RI v4.0.0 | Reference | Resource, LogicalResource |
| [TMF640](TMF640-service-activation) | Service Activation and Configuration | v4.0.2 | | Reference | Service, Resource |
| [TMF641](TMF641-service-ordering) | Service Ordering Management | RI v4.2.0 | RI v4.2.0 | Reference | none yet (data entities ServiceOrder, ServiceOrderLine) |
| [TMF651](TMF651-agreement) | Agreement Management | R19.0.1, v4.0.1 | | Shapes the FSA definition | Agreement, AgreementSpecification |
| [TMF669](TMF669-party-role) | Party Role Management | R19.0, v4.0.0 | Postman v5.0.0, RI v5.0.0 | Reference | PartyRole, PartyRoleSpecification |
| [TMF672](TMF672-user-roles-permissions) | User Role Permission Management | Postman v5.1.0 | Postman v5.1.0, RI v5.1.0 | Shapes the FSA definition | PermissionSpecification, PermissionSet, PermissionSpecificationSet |
| [TMF673](TMF673-geographic-address) | Geographic Address Management | R17.5.0, v1.2.2 | | Reference | GeographicAddress |
| [TMF674](TMF674-geographic-site) | Geographic Site Management | v4.0.0 | Spec v4.0.0 | Specification in this folder | Place, GeographicSite |
| [TMF713](TMF713-work-management) | Work Management | v4.0.0 beta | Spec v4.0.0 beta | Specification in this folder | ActivityAssignment, ActivityAssignmentSpecification, Activity |
| [TMF720](TMF720-digital-identity) | Digital Identity Management | v4.0.0 | Postman v4.0.0, RI v4.0.0 | Reference | DigitalIdentity, Credential |
| [TMF771](TMF771-resource-usage) | Resource Usage Management | Postman v5 | Postman v5, RI v5.0.0 | Reference | none yet |

TMF673 is documented in an older release (version 1) than the rest. Its paths start at `/api/...` instead of `/tmf-api/<api>/v4`. Choose a newer release before defining anything from it. TMF634 is also documented in version 2, but its reference implementation is version 5: define from version 5.

### Version 5

The TM Forum files for TMF629, TMF632, TMF634, TMF638, TMF669, TMF672 and TMF771 are version 5, while the documentation summarised in the older READMEs is version 4. Version 5 paths end in `/v5` instead of `/v4`. Before FSA defines a resource from one of these APIs, add its version 5 OpenAPI file and check the README against it.

The Postman collections downloaded as TMF629, TMF634 and TMF638 were all TMF620 Product Catalog Management. One copy is kept in [`TMF620-product-catalog`](TMF620-product-catalog); the real TMF629, TMF634 and TMF638 collections are still missing.

## Reference implementations

A folder's `ri/` holds a TM Forum reference implementation kit, as TM Forum supplies it: `docker-compose.yaml`, launcher scripts and TM Forum's own README. A reference implementation is a mock of the API, backed by MongoDB (and Kafka for version 5), used by the TM Forum conformance test kit (CTK) and for trying a client before a real implementation exists. Don't edit the files. The launcher scripts carry TM Forum's Apache 2.0 licence header.

Requires Docker Desktop. The images are `linux/amd64` and run under emulation on Apple silicon.

```bash
./tmf/TMF672-user-roles-permissions/ri/run.sh
```

`run.sh` creates the shared Docker network `tmf` if needed and starts the API. Each API has its own port: 8 followed by the API number, for example 8672 for TMF672. The version 5 kits' `run.sh` also deletes the API's database volume first (`docker compose down -v`), and `cleanup.sh` removes the images, volumes and the `tmf` network.

To empty a running reference implementation's database:

```bash
curl -X DELETE http://127.0.0.1:8672/tmf-ri-admin/v1/clear-all-data
```

The version 4 kits (TMF639, TMF641, TMF720) also serve HTTPS (port 4 followed by the API number) and mount a certificate that is not in the kit: `ri/certs/api-ri.key` and `ri/certs/api-ri.cert`. Create a self-signed one before the first run; the `certs` folders are ignored by git:

```bash
mkdir -p tmf/TMF720-digital-identity/ri/certs
openssl req -x509 -newkey rsa:2048 -nodes -days 365 -subj /CN=localhost -keyout tmf/TMF720-digital-identity/ri/certs/api-ri.key -out tmf/TMF720-digital-identity/ri/certs/api-ri.cert
```

The reference implementation serves its API documentation: `http://localhost:<port>/tmf-api/<api>/v5/api-docs/` for version 5, `http://localhost:<port>/docs` for version 4.

## Referenced by the model, not in this set

`information-objects.csv` refers to these APIs, but there is no documentation for them here yet:

| API | Name | Information objects |
|---|---|---|
| TMF637 | Product Inventory Management | Product, ProductCharacteristic, ProductInventory |
| TMF648 | Quote Management | Quote |
| TMF666 | Account Management | FinancialAccount |
| TMF667 | Document Management | Document, Attachment |
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
2. Add the Swagger or OpenAPI file exactly as TM Forum publishes it, and the Postman collection in `postman/` and the reference implementation kit in `ri/` when there are any. Don't edit them. FSA extensions go in `fsa/film-site-access.yaml` or in a JSON Schema referenced by `@schemaLocation`.
3. Add the API to the catalogue above.
