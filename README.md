# fsa-open-api

API definitions for Film Site Access: the TM Forum Open API specifications that Film Site
Access uses, and code generated from them. The specification comes first; code follows from
it (quality rule 09-05, *contract first*).

## Contents

| Path | What it is |
|---|---|
| `tmf` | TM Forum Open API specifications, as published by TM Forum |
| `generated/Tmf674.Server` | ASP.NET Core 8 server generated from TMF674 Geographic Site |
| `generated/Contracts` | A second generator output from TMF674, moved from `src/Contracts/Generated` in fsa-backend |
| `package.json`, `openapitools.json` | OpenAPI Generator, pinned to version 7.21.0 |

| Specification | Release | Used for |
|---|---|---|
| TMF674 Geographic Site Management | 19.5 | Locations (version 0.4 in the MVP roadmap) |

Moved from fsa-backend, where they were in `openapi/tmf`, `src/Tmf674.Server` and
`src/Contracts`. The backend doesn't reference the generated code yet.

## Generate

Requires Node.js and Java (for OpenAPI Generator).

```bash
npm install
npx openapi-generator-cli generate -i tmf/TMF674.yaml -g aspnetcore \
  --additional-properties aspnetCoreVersion=8.0 -o generated/Tmf674.Server
```

Don't edit generated files by hand; change the specification or the generator settings and
generate again. Files listed in a folder's `.openapi-generator-ignore` are kept.

## Build the generated server

Requires the .NET 8 SDK.

```bash
dotnet build generated/Tmf674.Server/src/Org.OpenAPITools
```

## Film Site Access API

`fsa/film-site-access.yaml` (OpenAPI 3.0.3) defines the API that Film Site Access defines
itself, where no TM Forum Open API covers the resource: sign-up, email verification, login
and logout, emergencies, a location's emergency area, and customer onboarding. It follows
TM Forum conventions (`@type`, `@referredType`, the TM Forum `Error`). The decisions behind
it are the ADRs in fsa-backend, `doc/decisions`.

The backend implements it in `src/Api/Endpoints`. Change the definition here first, then the
backend and the app.

### Check the definition

```bash
pip install openapi-spec-validator openapi-core
openapi-spec-validator fsa/film-site-access.yaml
```

### Check the backend against it

`tools/check_exchanges.py` checks recorded requests and responses against the definition:
every response's status and body, and the request of every successful exchange. Record the
exchanges by running the backend's tests with a middleware that appends each request and
response to a file as one JSON line (`method`, `path`, `query`, `requestContentType`,
`requestBody`, `status`, `responseContentType`, `responseBody`), then:

```bash
python tools/check_exchanges.py fsa/film-site-access.yaml exchanges.jsonl
```

The recording middleware is not part of the backend, because it would write passwords to
disk. On 2026-11-25 all 357 exchanges from the backend's 250 tests matched the definition,
across every operation except a successful `GET /customer/{id}`, which no test makes.
