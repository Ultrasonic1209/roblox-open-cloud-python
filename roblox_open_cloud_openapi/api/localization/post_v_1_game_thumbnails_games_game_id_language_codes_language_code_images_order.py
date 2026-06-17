import sys
from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset

if sys.version_info >= (3, 13):
    from warnings import deprecated
else:
    from typing_extensions import deprecated

from ...models.roblox_game_internationalization_api_sort_image_ids_request import (
    RobloxGameInternationalizationApiSortImageIdsRequest,
)
from ...models.roblox_web_web_api_api_empty_response_model import RobloxWebWebAPIApiEmptyResponseModel


def _get_kwargs(
    game_id: int,
    language_code: str,
    *,
    body: RobloxGameInternationalizationApiSortImageIdsRequest
    | RobloxGameInternationalizationApiSortImageIdsRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "https://gameinternationalization.roblox.com/v1/game-thumbnails/games/{game_id}/language-codes/{language_code}/images/order".format(
            game_id=quote(str(game_id), safe=""),
            language_code=quote(str(language_code), safe=""),
        ),
        "openapi-extensions": {
            "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            "x-roblox-recommended-alternatives": [
                {
                    "url": "https://apis.roblox.com/legacy-game-internationalization/v1/game-thumbnails/games/{gameId}/language-codes/{languageCode}/images/order",
                    "httpMethod": "POST",
                    "documentationUrl": "https://create.roblox.com/docs/cloud/reference/features/localization#post_legacy_game_internationalization_v1_game_thumbnails_games__gameId__language_codes__languageCode__images_order",
                }
            ],
        },
        "openapi-id": "post_v1_game-thumbnails_games_gameId_language-codes_languageCode_images_order",
    }

    if isinstance(body, RobloxGameInternationalizationApiSortImageIdsRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxGameInternationalizationApiSortImageIdsRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxWebWebAPIApiEmptyResponseModel | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIApiEmptyResponseModel.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

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
) -> Response[Any | RobloxWebWebAPIApiEmptyResponseModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/localization#gameinternationalization_post_v1_game_thumbnails_games__gameId__language_codes__languageCode__images_order"
)
def sync_detailed(
    game_id: int,
    language_code: str,
    *,
    client: AuthenticatedClient,
    body: RobloxGameInternationalizationApiSortImageIdsRequest
    | RobloxGameInternationalizationApiSortImageIdsRequest
    | Unset = UNSET,
) -> Response[Any | RobloxWebWebAPIApiEmptyResponseModel]:
    """Orders the specified image Ids for the game thumbnails.

    Args:
        game_id (int):
        language_code (str):
        body (RobloxGameInternationalizationApiSortImageIdsRequest): A request model for sorting
            of image Ids for game thumbnails
        body (RobloxGameInternationalizationApiSortImageIdsRequest): A request model for sorting
            of image Ids for game thumbnails

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIApiEmptyResponseModel]
    """

    kwargs = _get_kwargs(
        game_id=game_id,
        language_code=language_code,
        body=body,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/localization#gameinternationalization_post_v1_game_thumbnails_games__gameId__language_codes__languageCode__images_order"
)
def sync(
    game_id: int,
    language_code: str,
    *,
    client: AuthenticatedClient,
    body: RobloxGameInternationalizationApiSortImageIdsRequest
    | RobloxGameInternationalizationApiSortImageIdsRequest
    | Unset = UNSET,
) -> Any | RobloxWebWebAPIApiEmptyResponseModel | None:
    """Orders the specified image Ids for the game thumbnails.

    Args:
        game_id (int):
        language_code (str):
        body (RobloxGameInternationalizationApiSortImageIdsRequest): A request model for sorting
            of image Ids for game thumbnails
        body (RobloxGameInternationalizationApiSortImageIdsRequest): A request model for sorting
            of image Ids for game thumbnails

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIApiEmptyResponseModel
    """

    return sync_detailed(
        game_id=game_id,
        language_code=language_code,
        client=client,
        body=body,
    ).parsed


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/localization#gameinternationalization_post_v1_game_thumbnails_games__gameId__language_codes__languageCode__images_order"
)
async def asyncio_detailed(
    game_id: int,
    language_code: str,
    *,
    client: AuthenticatedClient,
    body: RobloxGameInternationalizationApiSortImageIdsRequest
    | RobloxGameInternationalizationApiSortImageIdsRequest
    | Unset = UNSET,
) -> Response[Any | RobloxWebWebAPIApiEmptyResponseModel]:
    """Orders the specified image Ids for the game thumbnails.

    Args:
        game_id (int):
        language_code (str):
        body (RobloxGameInternationalizationApiSortImageIdsRequest): A request model for sorting
            of image Ids for game thumbnails
        body (RobloxGameInternationalizationApiSortImageIdsRequest): A request model for sorting
            of image Ids for game thumbnails

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIApiEmptyResponseModel]
    """

    kwargs = _get_kwargs(
        game_id=game_id,
        language_code=language_code,
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/localization#gameinternationalization_post_v1_game_thumbnails_games__gameId__language_codes__languageCode__images_order"
)
async def asyncio(
    game_id: int,
    language_code: str,
    *,
    client: AuthenticatedClient,
    body: RobloxGameInternationalizationApiSortImageIdsRequest
    | RobloxGameInternationalizationApiSortImageIdsRequest
    | Unset = UNSET,
) -> Any | RobloxWebWebAPIApiEmptyResponseModel | None:
    """Orders the specified image Ids for the game thumbnails.

    Args:
        game_id (int):
        language_code (str):
        body (RobloxGameInternationalizationApiSortImageIdsRequest): A request model for sorting
            of image Ids for game thumbnails
        body (RobloxGameInternationalizationApiSortImageIdsRequest): A request model for sorting
            of image Ids for game thumbnails

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIApiEmptyResponseModel
    """

    return (
        await asyncio_detailed(
            game_id=game_id,
            language_code=language_code,
            client=client,
            body=body,
        )
    ).parsed
