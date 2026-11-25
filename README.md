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

## Film Site Access APIs

The API that Film Site Access defines itself (sign-up, email verification, login and
emergencies) has no OpenAPI definition yet. Its shapes are the contract records in
fsa-backend, `src/Api/Endpoints/*/*Contract.cs`, and are described in its ADRs. Where a TM
Forum API covers a resource, that API is used; otherwise the shapes follow TM Forum
conventions (`@type`, `Error`).
