from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_web_web_api_models_api_array_response_roblox_game_internationalization_api_get_game_icon_response import (
    RobloxWebWebAPIModelsApiArrayResponseRobloxGameInternationalizationApiGetGameIconResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    game_id: int,
    *,
    width: int | Unset = 512,
    height: int | Unset = 512,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["width"] = width

    params["height"] = height

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/legacy-game-internationalization/v1/game-icon/games/{game_id}".format(
            game_id=quote(str(game_id), safe=""),
        ),
        "params": params,
        "openapi-extensions": {
            "x-roblox-rate-limits": {
                "perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 100},
                "perOauth2Authorization": {"period": "MINUTE", "maxInPeriod": 100},
            },
            "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            "x-roblox-scopes": [{"name": "legacy-universe:manage"}],
        },
        "openapi-id": "get_legacy-game-internationalization_v1_game-icon_games_gameId",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGameInternationalizationApiGetGameIconResponse | None:
    if response.status_code == 200:
        response_200 = (
            RobloxWebWebAPIModelsApiArrayResponseRobloxGameInternationalizationApiGetGameIconResponse.from_dict(
                response.json()
            )
        )

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGameInternationalizationApiGetGameIconResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    game_id: int,
    *,
    client: AuthenticatedClient,
    width: int | Unset = 512,
    height: int | Unset = 512,
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGameInternationalizationApiGetGameIconResponse]:
    """Get all icons for a game

    Args:
        game_id (int):
        width (int | Unset):  Default: 512.
        height (int | Unset):  Default: 512.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGameInternationalizationApiGetGameIconResponse]
    """

    kwargs = _get_kwargs(
        game_id=game_id,
        width=width,
        height=height,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    game_id: int,
    *,
    client: AuthenticatedClient,
    width: int | Unset = 512,
    height: int | Unset = 512,
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGameInternationalizationApiGetGameIconResponse | None:
    """Get all icons for a game

    Args:
        game_id (int):
        width (int | Unset):  Default: 512.
        height (int | Unset):  Default: 512.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGameInternationalizationApiGetGameIconResponse
    """

    return sync_detailed(
        game_id=game_id,
        client=client,
        width=width,
        height=height,
    ).parsed


async def asyncio_detailed(
    game_id: int,
    *,
    client: AuthenticatedClient,
    width: int | Unset = 512,
    height: int | Unset = 512,
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGameInternationalizationApiGetGameIconResponse]:
    """Get all icons for a game

    Args:
        game_id (int):
        width (int | Unset):  Default: 512.
        height (int | Unset):  Default: 512.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGameInternationalizationApiGetGameIconResponse]
    """

    kwargs = _get_kwargs(
        game_id=game_id,
        width=width,
        height=height,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    game_id: int,
    *,
    client: AuthenticatedClient,
    width: int | Unset = 512,
    height: int | Unset = 512,
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGameInternationalizationApiGetGameIconResponse | None:
    """Get all icons for a game

    Args:
        game_id (int):
        width (int | Unset):  Default: 512.
        height (int | Unset):  Default: 512.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGameInternationalizationApiGetGameIconResponse
    """

    return (
        await asyncio_detailed(
            game_id=game_id,
            client=client,
            width=width,
            height=height,
        )
    ).parsed
