from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_web_web_api_models_api_array_response_roblox_game_internationalization_api_get_game_thumbnails_response import (
    RobloxWebWebAPIModelsApiArrayResponseRobloxGameInternationalizationApiGetGameThumbnailsResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    game_id: int,
    *,
    width: int | Unset = 768,
    height: int | Unset = 432,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["width"] = width

    params["height"] = height

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/game-thumbnails/games/{game_id}/images".format(
            game_id=quote(str(game_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGameInternationalizationApiGetGameThumbnailsResponse | None:
    if response.status_code == 200:
        response_200 = (
            RobloxWebWebAPIModelsApiArrayResponseRobloxGameInternationalizationApiGetGameThumbnailsResponse.from_dict(
                response.json()
            )
        )

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

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
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGameInternationalizationApiGetGameThumbnailsResponse]:
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
    width: int | Unset = 768,
    height: int | Unset = 432,
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGameInternationalizationApiGetGameThumbnailsResponse]:
    """Get the localized image ids in all languages for a game.

    Args:
        game_id (int):
        width (int | Unset):  Default: 768.
        height (int | Unset):  Default: 432.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGameInternationalizationApiGetGameThumbnailsResponse]
    """

    kwargs = _get_kwargs(
        game_id=game_id,
        width=width,
        height=height,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    game_id: int,
    *,
    client: AuthenticatedClient,
    width: int | Unset = 768,
    height: int | Unset = 432,
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGameInternationalizationApiGetGameThumbnailsResponse | None:
    """Get the localized image ids in all languages for a game.

    Args:
        game_id (int):
        width (int | Unset):  Default: 768.
        height (int | Unset):  Default: 432.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGameInternationalizationApiGetGameThumbnailsResponse
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
    width: int | Unset = 768,
    height: int | Unset = 432,
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGameInternationalizationApiGetGameThumbnailsResponse]:
    """Get the localized image ids in all languages for a game.

    Args:
        game_id (int):
        width (int | Unset):  Default: 768.
        height (int | Unset):  Default: 432.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGameInternationalizationApiGetGameThumbnailsResponse]
    """

    kwargs = _get_kwargs(
        game_id=game_id,
        width=width,
        height=height,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    game_id: int,
    *,
    client: AuthenticatedClient,
    width: int | Unset = 768,
    height: int | Unset = 432,
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGameInternationalizationApiGetGameThumbnailsResponse | None:
    """Get the localized image ids in all languages for a game.

    Args:
        game_id (int):
        width (int | Unset):  Default: 768.
        height (int | Unset):  Default: 432.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGameInternationalizationApiGetGameThumbnailsResponse
    """

    return (
        await asyncio_detailed(
            game_id=game_id,
            client=client,
            width=width,
            height=height,
        )
    ).parsed
