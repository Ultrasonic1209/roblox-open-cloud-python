from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_universe_regex_http_request import CreateUniverseRegexHttpRequest
from ...models.universe_regex_mutation_http_response import UniverseRegexMutationHttpResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CreateUniverseRegexHttpRequest
    | CreateUniverseRegexHttpRequest
    | CreateUniverseRegexHttpRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/log-attribute-http-service/v1/universe-regexes",
        "extensions": {
            "openapi-extensions": {
                "x-roblox-stability": "EXPERIMENTAL",
                "x-roblox-rate-limits": {
                    "perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 60},
                    "perOauth2Authorization": {"period": "MINUTE", "maxInPeriod": 60},
                },
                "x-roblox-scopes": [{"name": "universe.analytics:write", "targetResourceSpecifier": ""}],
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            },
            "openapi-id": "LogAttributeService_Create",
        },
    }

    if isinstance(body, CreateUniverseRegexHttpRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CreateUniverseRegexHttpRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"
    if isinstance(body, CreateUniverseRegexHttpRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> UniverseRegexMutationHttpResponse | None:
    if response.status_code == 200:
        response_200 = UniverseRegexMutationHttpResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[UniverseRegexMutationHttpResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateUniverseRegexHttpRequest
    | CreateUniverseRegexHttpRequest
    | CreateUniverseRegexHttpRequest
    | Unset = UNSET,
) -> Response[UniverseRegexMutationHttpResponse]:
    """
    Args:
        body (CreateUniverseRegexHttpRequest | Unset):
        body (CreateUniverseRegexHttpRequest | Unset):
        body (CreateUniverseRegexHttpRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UniverseRegexMutationHttpResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: CreateUniverseRegexHttpRequest
    | CreateUniverseRegexHttpRequest
    | CreateUniverseRegexHttpRequest
    | Unset = UNSET,
) -> UniverseRegexMutationHttpResponse | None:
    """
    Args:
        body (CreateUniverseRegexHttpRequest | Unset):
        body (CreateUniverseRegexHttpRequest | Unset):
        body (CreateUniverseRegexHttpRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UniverseRegexMutationHttpResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateUniverseRegexHttpRequest
    | CreateUniverseRegexHttpRequest
    | CreateUniverseRegexHttpRequest
    | Unset = UNSET,
) -> Response[UniverseRegexMutationHttpResponse]:
    """
    Args:
        body (CreateUniverseRegexHttpRequest | Unset):
        body (CreateUniverseRegexHttpRequest | Unset):
        body (CreateUniverseRegexHttpRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UniverseRegexMutationHttpResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateUniverseRegexHttpRequest
    | CreateUniverseRegexHttpRequest
    | CreateUniverseRegexHttpRequest
    | Unset = UNSET,
) -> UniverseRegexMutationHttpResponse | None:
    """
    Args:
        body (CreateUniverseRegexHttpRequest | Unset):
        body (CreateUniverseRegexHttpRequest | Unset):
        body (CreateUniverseRegexHttpRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UniverseRegexMutationHttpResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
