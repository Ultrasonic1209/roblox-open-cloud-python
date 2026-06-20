from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.list_developer_product_configs_v2_response import ListDeveloperProductConfigsV2Response
from ...types import UNSET, Response, Unset


def _get_kwargs(
    universe_id: int,
    *,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["pageSize"] = page_size

    params["pageToken"] = page_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/developer-products/v2/universes/{universe_id}/developer-products/creator".format(
            universe_id=quote(str(universe_id), safe=""),
        ),
        "params": params,
        "extensions": {
            "openapi-extensions": {
                "x-roblox-stability": "BETA",
                "x-roblox-rate-limits": {
                    "perApiKeyOwner": {"period": "SECOND", "maxInPeriod": 10},
                    "perOauth2Authorization": {"period": "SECOND", "maxInPeriod": 10},
                },
                "x-roblox-scopes": [{"name": "developer-product:read", "targetResourceSpecifier": "universes"}],
                "x-roblox-engine-usability": {"apiKeyWithHttpService": True},
            },
            "openapi-id": "DeveloperProducts_ListDeveloperProductConfigsByUniverseV2",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ErrorResponse | ListDeveloperProductConfigsV2Response | None:
    if response.status_code == 200:
        response_200 = ListDeveloperProductConfigsV2Response.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ErrorResponse | ListDeveloperProductConfigsV2Response]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> Response[ErrorResponse | ListDeveloperProductConfigsV2Response]:
    """List developer products by universe with configuration details

    Args:
        universe_id (int):
        page_size (int | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ListDeveloperProductConfigsV2Response]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        page_size=page_size,
        page_token=page_token,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> ErrorResponse | ListDeveloperProductConfigsV2Response | None:
    """List developer products by universe with configuration details

    Args:
        universe_id (int):
        page_size (int | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ListDeveloperProductConfigsV2Response
    """

    return sync_detailed(
        universe_id=universe_id,
        client=client,
        page_size=page_size,
        page_token=page_token,
    ).parsed


async def asyncio_detailed(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> Response[ErrorResponse | ListDeveloperProductConfigsV2Response]:
    """List developer products by universe with configuration details

    Args:
        universe_id (int):
        page_size (int | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ListDeveloperProductConfigsV2Response]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        page_size=page_size,
        page_token=page_token,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> ErrorResponse | ListDeveloperProductConfigsV2Response | None:
    """List developer products by universe with configuration details

    Args:
        universe_id (int):
        page_size (int | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ListDeveloperProductConfigsV2Response
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            client=client,
            page_size=page_size,
            page_token=page_token,
        )
    ).parsed
