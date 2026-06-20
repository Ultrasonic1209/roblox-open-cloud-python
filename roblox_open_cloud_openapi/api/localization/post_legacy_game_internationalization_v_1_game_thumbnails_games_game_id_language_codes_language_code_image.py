from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_legacy_game_internationalization_v1_game_thumbnails_games_game_id_language_codes_language_code_image_body import (
    PostLegacyGameInternationalizationV1GameThumbnailsGamesGameIdLanguageCodesLanguageCodeImageBody,
)
from ...models.roblox_game_internationalization_api_models_response_upload_image_for_game_thumbnail_response import (
    RobloxGameInternationalizationApiModelsResponseUploadImageForGameThumbnailResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    game_id: int,
    language_code: str,
    *,
    body: PostLegacyGameInternationalizationV1GameThumbnailsGamesGameIdLanguageCodesLanguageCodeImageBody
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/legacy-game-internationalization/v1/game-thumbnails/games/{game_id}/language-codes/{language_code}/image".format(
            game_id=quote(str(game_id), safe=""),
            language_code=quote(str(language_code), safe=""),
        ),
        "extensions": {
            "openapi-extensions": {
                "x-roblox-rate-limits": {
                    "perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 100},
                    "perOauth2Authorization": {"period": "MINUTE", "maxInPeriod": 100},
                },
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
                "x-roblox-scopes": [{"name": "legacy-universe:manage"}],
            },
            "openapi-id": "post_legacy-game-internationalization_v1_game-thumbnails_games_gameId_language-codes_languageCode_image",
        },
    }

    if not isinstance(body, Unset):
        _kwargs["files"] = body.to_multipart()

    headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxGameInternationalizationApiModelsResponseUploadImageForGameThumbnailResponse | None:
    if response.status_code == 200:
        response_200 = RobloxGameInternationalizationApiModelsResponseUploadImageForGameThumbnailResponse.from_dict(
            response.json()
        )

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

    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429

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
) -> Response[Any | RobloxGameInternationalizationApiModelsResponseUploadImageForGameThumbnailResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    game_id: int,
    language_code: str,
    *,
    client: AuthenticatedClient,
    body: PostLegacyGameInternationalizationV1GameThumbnailsGamesGameIdLanguageCodesLanguageCodeImageBody
    | Unset = UNSET,
) -> Response[Any | RobloxGameInternationalizationApiModelsResponseUploadImageForGameThumbnailResponse]:
    """Uploads the game thumbnail.

    Args:
        game_id (int):
        language_code (str):
        body (PostLegacyGameInternationalizationV1GameThumbnailsGamesGameIdLanguageCodesLanguageCo
            deImageBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxGameInternationalizationApiModelsResponseUploadImageForGameThumbnailResponse]
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


def sync(
    game_id: int,
    language_code: str,
    *,
    client: AuthenticatedClient,
    body: PostLegacyGameInternationalizationV1GameThumbnailsGamesGameIdLanguageCodesLanguageCodeImageBody
    | Unset = UNSET,
) -> Any | RobloxGameInternationalizationApiModelsResponseUploadImageForGameThumbnailResponse | None:
    """Uploads the game thumbnail.

    Args:
        game_id (int):
        language_code (str):
        body (PostLegacyGameInternationalizationV1GameThumbnailsGamesGameIdLanguageCodesLanguageCo
            deImageBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxGameInternationalizationApiModelsResponseUploadImageForGameThumbnailResponse
    """

    return sync_detailed(
        game_id=game_id,
        language_code=language_code,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    game_id: int,
    language_code: str,
    *,
    client: AuthenticatedClient,
    body: PostLegacyGameInternationalizationV1GameThumbnailsGamesGameIdLanguageCodesLanguageCodeImageBody
    | Unset = UNSET,
) -> Response[Any | RobloxGameInternationalizationApiModelsResponseUploadImageForGameThumbnailResponse]:
    """Uploads the game thumbnail.

    Args:
        game_id (int):
        language_code (str):
        body (PostLegacyGameInternationalizationV1GameThumbnailsGamesGameIdLanguageCodesLanguageCo
            deImageBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxGameInternationalizationApiModelsResponseUploadImageForGameThumbnailResponse]
    """

    kwargs = _get_kwargs(
        game_id=game_id,
        language_code=language_code,
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    game_id: int,
    language_code: str,
    *,
    client: AuthenticatedClient,
    body: PostLegacyGameInternationalizationV1GameThumbnailsGamesGameIdLanguageCodesLanguageCodeImageBody
    | Unset = UNSET,
) -> Any | RobloxGameInternationalizationApiModelsResponseUploadImageForGameThumbnailResponse | None:
    """Uploads the game thumbnail.

    Args:
        game_id (int):
        language_code (str):
        body (PostLegacyGameInternationalizationV1GameThumbnailsGamesGameIdLanguageCodesLanguageCo
            deImageBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxGameInternationalizationApiModelsResponseUploadImageForGameThumbnailResponse
    """

    return (
        await asyncio_detailed(
            game_id=game_id,
            language_code=language_code,
            client=client,
            body=body,
        )
    ).parsed
