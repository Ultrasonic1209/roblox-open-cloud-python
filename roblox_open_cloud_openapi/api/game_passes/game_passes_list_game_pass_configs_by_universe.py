from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.game_passes_error_response import GamePassesErrorResponse
from ...models.list_game_pass_configs_by_universe_response import ListGamePassConfigsByUniverseResponse
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
        "url": "/game-passes/v1/universes/{universe_id}/game-passes/creator".format(
            universe_id=quote(str(universe_id), safe=""),
        ),
        "params": params,
        "openapi-extensions": {
            "x-roblox-stability": "BETA",
            "x-roblox-rate-limits": {
                "perApiKeyOwner": {"period": "SECOND", "maxInPeriod": 10},
                "perOauth2Authorization": {"period": "SECOND", "maxInPeriod": 10},
            },
            "x-roblox-scopes": [{"name": "game-pass:read", "targetResourceSpecifier": "universes"}],
            "x-roblox-engine-usability": {"apiKeyWithHttpService": True},
        },
        "openapi-id": "GamePasses_ListGamePassConfigsByUniverse",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> GamePassesErrorResponse | ListGamePassConfigsByUniverseResponse | None:
    if response.status_code == 200:
        response_200 = ListGamePassConfigsByUniverseResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GamePassesErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GamePassesErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GamePassesErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GamePassesErrorResponse.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[GamePassesErrorResponse | ListGamePassConfigsByUniverseResponse]:
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
) -> Response[GamePassesErrorResponse | ListGamePassConfigsByUniverseResponse]:
    """List game passes by universe with configuration details

    Args:
        universe_id (int):
        page_size (int | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GamePassesErrorResponse | ListGamePassConfigsByUniverseResponse]
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
) -> GamePassesErrorResponse | ListGamePassConfigsByUniverseResponse | None:
    """List game passes by universe with configuration details

    Args:
        universe_id (int):
        page_size (int | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GamePassesErrorResponse | ListGamePassConfigsByUniverseResponse
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
) -> Response[GamePassesErrorResponse | ListGamePassConfigsByUniverseResponse]:
    """List game passes by universe with configuration details

    Args:
        universe_id (int):
        page_size (int | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GamePassesErrorResponse | ListGamePassConfigsByUniverseResponse]
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
) -> GamePassesErrorResponse | ListGamePassConfigsByUniverseResponse | None:
    """List game passes by universe with configuration details

    Args:
        universe_id (int):
        page_size (int | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GamePassesErrorResponse | ListGamePassConfigsByUniverseResponse
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            client=client,
            page_size=page_size,
            page_token=page_token,
        )
    ).parsed
