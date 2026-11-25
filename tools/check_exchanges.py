"""Check recorded API exchanges against an OpenAPI definition.

Each line of the input is one exchange as JSON: method, path, query, requestContentType,
requestBody, status, responseContentType and responseBody. Every response is checked
against the definition: its status must be listed, and its body must match the schema.
The request is checked too when the response is a success (2xx), since failing requests
are often sent on purpose by tests.

Security is not checked, because the backend's tests sign in with a test scheme instead of
a bearer token.

Usage:
    python tools/check_exchanges.py fsa/film-site-access.yaml exchanges.jsonl

Needs: pip install openapi-core
"""

import json
import sys
from collections import Counter
from urllib.parse import parse_qs

from openapi_core import OpenAPI
from openapi_core.testing import MockRequest, MockResponse
from openapi_core.validation.request.validators import (
    V30RequestBodyValidator,
    V30RequestParametersValidator,
)

HOST = "http://localhost:5080"


def main(definition_path: str, exchanges_path: str) -> int:
    openapi = OpenAPI.from_file_path(definition_path)
    problems: list[str] = []
    checked: Counter[str] = Counter()
    skipped: Counter[str] = Counter()

    with open(exchanges_path, encoding="utf-8") as lines:
        for number, line in enumerate(lines, start=1):
            exchange = json.loads(line)
            path = exchange["path"] or ""
            if not path.startswith("/v1/"):
                skipped[path] += 1
                continue
            label = f"{exchange['method']} {path} -> {exchange['status']}"
            request = MockRequest(
                HOST,
                exchange["method"].lower(),
                path,
                args={k: v[0] for k, v in parse_qs((exchange.get("query") or "").lstrip("?")).items()},
                data=(exchange.get("requestBody") or "").encode(),
                content_type=(exchange.get("requestContentType") or "application/json").split(";")[0],
            )
            body = exchange.get("responseBody") or ""
            response = MockResponse(
                body.encode(),
                status_code=exchange["status"],
                content_type=(exchange.get("responseContentType") or "application/json").split(";")[0],
            )
            try:
                openapi.validate_response(request, response)
            except Exception as error:  # noqa: BLE001 - report every kind of mismatch
                problems.append(f"line {number}: response of {template(label)}: {describe(error)}")
            if 200 <= exchange["status"] < 300:
                for validator in (V30RequestParametersValidator, V30RequestBodyValidator):
                    try:
                        validator(openapi.spec).validate(request)
                    except Exception as error:  # noqa: BLE001
                        problems.append(f"line {number}: request of {template(label)}: {describe(error)}")
            checked[f"{exchange['method']} {template(path)} {exchange['status']}"] += 1

    print(f"Checked {sum(checked.values())} exchanges, {len(checked)} kinds:")
    for key in sorted(checked):
        print(f"  {checked[key]:4}  {key}")
    if skipped:
        print(f"Not in the definition's base path, skipped: {dict(skipped)}")
    unique = sorted(set(problem.split(": ", 1)[1] for problem in problems))
    print(f"\n{len(problems)} problems, {len(unique)} distinct:")
    for problem in unique:
        print(f"  {problem}")
    return 1 if problems else 0


def template(path: str) -> str:
    """Replaces ids in the path, so exchanges group by operation."""
    parts = path.split("/")
    return "/".join("{id}" if len(part) == 36 and part.count("-") == 4 else part for part in parts)


def describe(error: Exception) -> str:
    details = [str(error)]
    cause = error.__cause__
    while cause is not None:
        details.append(str(cause))
        for inner in getattr(cause, "schema_errors", []) or []:
            details.append(f"{list(inner.absolute_path)}: {inner.message}")
        cause = cause.__cause__
    return " | ".join(details)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2]))
