from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_api_avatar_models_game_start_info_response import RobloxApiAvatarModelsGameStartInfoResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    universe_id: int,
    roblox_place_id: int | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(roblox_place_id, Unset):
        headers["Roblox-Place-Id"] = str(roblox_place_id)

    params: dict[str, Any] = {}

    params["universeId"] = universe_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://avatar.roblox.com/v1/game-start-info",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> RobloxApiAvatarModelsGameStartInfoResponse | None:
    if response.status_code == 200:
        response_200 = RobloxApiAvatarModelsGameStartInfoResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[RobloxApiAvatarModelsGameStartInfoResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    universe_id: int,
    roblox_place_id: int | Unset = UNSET,
) -> Response[RobloxApiAvatarModelsGameStartInfoResponse]:
    """The server will call this on game server start to request general information about the universe
    This is version 1.1, which returns an entry from the UniverseAvatarType enum.
    During mixed mode this may return unreliable results.

    Args:
        universe_id (int):
        roblox_place_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RobloxApiAvatarModelsGameStartInfoResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        roblox_place_id=roblox_place_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    universe_id: int,
    roblox_place_id: int | Unset = UNSET,
) -> RobloxApiAvatarModelsGameStartInfoResponse | None:
    """The server will call this on game server start to request general information about the universe
    This is version 1.1, which returns an entry from the UniverseAvatarType enum.
    During mixed mode this may return unreliable results.

    Args:
        universe_id (int):
        roblox_place_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RobloxApiAvatarModelsGameStartInfoResponse
    """

    return sync_detailed(
        client=client,
        universe_id=universe_id,
        roblox_place_id=roblox_place_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    universe_id: int,
    roblox_place_id: int | Unset = UNSET,
) -> Response[RobloxApiAvatarModelsGameStartInfoResponse]:
    """The server will call this on game server start to request general information about the universe
    This is version 1.1, which returns an entry from the UniverseAvatarType enum.
    During mixed mode this may return unreliable results.

    Args:
        universe_id (int):
        roblox_place_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RobloxApiAvatarModelsGameStartInfoResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        roblox_place_id=roblox_place_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    universe_id: int,
    roblox_place_id: int | Unset = UNSET,
) -> RobloxApiAvatarModelsGameStartInfoResponse | None:
    """The server will call this on game server start to request general information about the universe
    This is version 1.1, which returns an entry from the UniverseAvatarType enum.
    During mixed mode this may return unreliable results.

    Args:
        universe_id (int):
        roblox_place_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RobloxApiAvatarModelsGameStartInfoResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            universe_id=universe_id,
            roblox_place_id=roblox_place_id,
        )
    ).parsed
