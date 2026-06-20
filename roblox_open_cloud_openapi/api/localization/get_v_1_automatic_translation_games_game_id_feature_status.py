from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_game_internationalization_api_get_automatic_translation_feature_status_for_game_response import (
    RobloxGameInternationalizationApiGetAutomaticTranslationFeatureStatusForGameResponse,
)
from ...types import Response


def _get_kwargs(
    game_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://gameinternationalization.roblox.com/v1/automatic-translation/games/{game_id}/feature-status".format(
            game_id=quote(str(game_id), safe=""),
        ),
        "extensions": {
            "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
            "openapi-id": "get_v1_automatic-translation_games_gameId_feature-status",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxGameInternationalizationApiGetAutomaticTranslationFeatureStatusForGameResponse | None:
    if response.status_code == 200:
        response_200 = RobloxGameInternationalizationApiGetAutomaticTranslationFeatureStatusForGameResponse.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxGameInternationalizationApiGetAutomaticTranslationFeatureStatusForGameResponse]:
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
) -> Response[Any | RobloxGameInternationalizationApiGetAutomaticTranslationFeatureStatusForGameResponse]:
    """Checks if automatic translation can be enabled for a game.
    The user must still have proper permissions for the game to get this info.

    Args:
        game_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxGameInternationalizationApiGetAutomaticTranslationFeatureStatusForGameResponse]
    """

    kwargs = _get_kwargs(
        game_id=game_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    game_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxGameInternationalizationApiGetAutomaticTranslationFeatureStatusForGameResponse | None:
    """Checks if automatic translation can be enabled for a game.
    The user must still have proper permissions for the game to get this info.

    Args:
        game_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxGameInternationalizationApiGetAutomaticTranslationFeatureStatusForGameResponse
    """

    return sync_detailed(
        game_id=game_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    game_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxGameInternationalizationApiGetAutomaticTranslationFeatureStatusForGameResponse]:
    """Checks if automatic translation can be enabled for a game.
    The user must still have proper permissions for the game to get this info.

    Args:
        game_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxGameInternationalizationApiGetAutomaticTranslationFeatureStatusForGameResponse]
    """

    kwargs = _get_kwargs(
        game_id=game_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    game_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxGameInternationalizationApiGetAutomaticTranslationFeatureStatusForGameResponse | None:
    """Checks if automatic translation can be enabled for a game.
    The user must still have proper permissions for the game to get this info.

    Args:
        game_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxGameInternationalizationApiGetAutomaticTranslationFeatureStatusForGameResponse
    """

    return (
        await asyncio_detailed(
            game_id=game_id,
            client=client,
        )
    ).parsed
