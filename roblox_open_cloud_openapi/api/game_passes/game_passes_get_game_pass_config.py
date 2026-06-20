from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.game_pass_config_v2 import GamePassConfigV2
from ...models.game_passes_error_response import GamePassesErrorResponse
from ...types import Response


def _get_kwargs(
    universe_id: int,
    game_pass_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/game-passes/v1/universes/{universe_id}/game-passes/{game_pass_id}/creator".format(
            universe_id=quote(str(universe_id), safe=""),
            game_pass_id=quote(str(game_pass_id), safe=""),
        ),
        "extensions": {
            "openapi-extensions": {
                "x-roblox-stability": "BETA",
                "x-roblox-rate-limits": {
                    "perApiKeyOwner": {"period": "SECOND", "maxInPeriod": 10},
                    "perOauth2Authorization": {"period": "SECOND", "maxInPeriod": 10},
                },
                "x-roblox-scopes": [{"name": "game-pass:read", "targetResourceSpecifier": "universes"}],
                "x-roblox-engine-usability": {"apiKeyWithHttpService": True},
            },
            "openapi-id": "GamePasses_GetGamePassConfig",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> GamePassConfigV2 | GamePassesErrorResponse | None:
    if response.status_code == 200:
        response_200 = GamePassConfigV2.from_dict(response.json())

        return response_200

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
) -> Response[GamePassConfigV2 | GamePassesErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    universe_id: int,
    game_pass_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[GamePassConfigV2 | GamePassesErrorResponse]:
    """Get game pass with configuration details

    Args:
        universe_id (int):
        game_pass_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GamePassConfigV2 | GamePassesErrorResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        game_pass_id=game_pass_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: int,
    game_pass_id: int,
    *,
    client: AuthenticatedClient,
) -> GamePassConfigV2 | GamePassesErrorResponse | None:
    """Get game pass with configuration details

    Args:
        universe_id (int):
        game_pass_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GamePassConfigV2 | GamePassesErrorResponse
    """

    return sync_detailed(
        universe_id=universe_id,
        game_pass_id=game_pass_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    universe_id: int,
    game_pass_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[GamePassConfigV2 | GamePassesErrorResponse]:
    """Get game pass with configuration details

    Args:
        universe_id (int):
        game_pass_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GamePassConfigV2 | GamePassesErrorResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        game_pass_id=game_pass_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: int,
    game_pass_id: int,
    *,
    client: AuthenticatedClient,
) -> GamePassConfigV2 | GamePassesErrorResponse | None:
    """Get game pass with configuration details

    Args:
        universe_id (int):
        game_pass_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GamePassConfigV2 | GamePassesErrorResponse
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            game_pass_id=game_pass_id,
            client=client,
        )
    ).parsed
