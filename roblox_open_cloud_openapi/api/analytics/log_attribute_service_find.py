from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.find_universe_regexes_http_response import FindUniverseRegexesHttpResponse
from ...models.regex_status import RegexStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    universe_id: int | Unset = UNSET,
    status: RegexStatus | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["universeId"] = universe_id

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/log-attribute-http-service/v1/universe-regexes",
        "params": params,
        "extensions": {
            "openapi-extensions": {
                "x-roblox-stability": "EXPERIMENTAL",
                "x-roblox-rate-limits": {
                    "perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 60},
                    "perOauth2Authorization": {"period": "MINUTE", "maxInPeriod": 60},
                },
                "x-roblox-scopes": [{"name": "universe.analytics:read", "targetResourceSpecifier": ""}],
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            },
            "openapi-id": "LogAttributeService_Find",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> FindUniverseRegexesHttpResponse | None:
    if response.status_code == 200:
        response_200 = FindUniverseRegexesHttpResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[FindUniverseRegexesHttpResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    universe_id: int | Unset = UNSET,
    status: RegexStatus | Unset = UNSET,
) -> Response[FindUniverseRegexesHttpResponse]:
    """
    Args:
        universe_id (int | Unset):
        status (RegexStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FindUniverseRegexesHttpResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        status=status,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    universe_id: int | Unset = UNSET,
    status: RegexStatus | Unset = UNSET,
) -> FindUniverseRegexesHttpResponse | None:
    """
    Args:
        universe_id (int | Unset):
        status (RegexStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FindUniverseRegexesHttpResponse
    """

    return sync_detailed(
        client=client,
        universe_id=universe_id,
        status=status,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    universe_id: int | Unset = UNSET,
    status: RegexStatus | Unset = UNSET,
) -> Response[FindUniverseRegexesHttpResponse]:
    """
    Args:
        universe_id (int | Unset):
        status (RegexStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FindUniverseRegexesHttpResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        status=status,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    universe_id: int | Unset = UNSET,
    status: RegexStatus | Unset = UNSET,
) -> FindUniverseRegexesHttpResponse | None:
    """
    Args:
        universe_id (int | Unset):
        status (RegexStatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FindUniverseRegexesHttpResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            universe_id=universe_id,
            status=status,
        )
    ).parsed
