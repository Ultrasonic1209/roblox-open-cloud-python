from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.game_passes_error_response import GamePassesErrorResponse
from ...models.game_passes_update_game_pass_body import GamePassesUpdateGamePassBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    universe_id: int,
    game_pass_id: int,
    *,
    body: GamePassesUpdateGamePassBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/game-passes/v1/universes/{universe_id}/game-passes/{game_pass_id}".format(
            universe_id=quote(str(universe_id), safe=""),
            game_pass_id=quote(str(game_pass_id), safe=""),
        ),
        "openapi-extensions": {
            "x-roblox-stability": "BETA",
            "x-roblox-rate-limits": {
                "perApiKeyOwner": {"period": "SECOND", "maxInPeriod": 5},
                "perOauth2Authorization": {"period": "SECOND", "maxInPeriod": 5},
            },
            "x-roblox-scopes": [{"name": "game-pass:write", "targetResourceSpecifier": "universes"}],
            "x-roblox-engine-usability": {"apiKeyWithHttpService": True},
        },
        "openapi-id": "GamePasses_UpdateGamePass",
    }

    if not isinstance(body, Unset):
        _kwargs["files"] = body.to_multipart()

    headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | GamePassesErrorResponse | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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

    if response.status_code == 409:
        response_409 = GamePassesErrorResponse.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | GamePassesErrorResponse]:
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
    body: GamePassesUpdateGamePassBody | Unset = UNSET,
) -> Response[Any | GamePassesErrorResponse]:
    """Update game pass

     Updates a game pass with the provided configuration details.
    Note that only fields provided in the request will be updated.

    Args:
        universe_id (int):
        game_pass_id (int):
        body (GamePassesUpdateGamePassBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GamePassesErrorResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        game_pass_id=game_pass_id,
        body=body,
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
    body: GamePassesUpdateGamePassBody | Unset = UNSET,
) -> Any | GamePassesErrorResponse | None:
    """Update game pass

     Updates a game pass with the provided configuration details.
    Note that only fields provided in the request will be updated.

    Args:
        universe_id (int):
        game_pass_id (int):
        body (GamePassesUpdateGamePassBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GamePassesErrorResponse
    """

    return sync_detailed(
        universe_id=universe_id,
        game_pass_id=game_pass_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    universe_id: int,
    game_pass_id: int,
    *,
    client: AuthenticatedClient,
    body: GamePassesUpdateGamePassBody | Unset = UNSET,
) -> Response[Any | GamePassesErrorResponse]:
    """Update game pass

     Updates a game pass with the provided configuration details.
    Note that only fields provided in the request will be updated.

    Args:
        universe_id (int):
        game_pass_id (int):
        body (GamePassesUpdateGamePassBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GamePassesErrorResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        game_pass_id=game_pass_id,
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: int,
    game_pass_id: int,
    *,
    client: AuthenticatedClient,
    body: GamePassesUpdateGamePassBody | Unset = UNSET,
) -> Any | GamePassesErrorResponse | None:
    """Update game pass

     Updates a game pass with the provided configuration details.
    Note that only fields provided in the request will be updated.

    Args:
        universe_id (int):
        game_pass_id (int):
        body (GamePassesUpdateGamePassBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GamePassesErrorResponse
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            game_pass_id=game_pass_id,
            client=client,
            body=body,
        )
    ).parsed
