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

from ...models.roblox_game_internationalization_api_edit_automatic_translation_status_for_game_and_language_response import (
    RobloxGameInternationalizationApiEditAutomaticTranslationStatusForGameAndLanguageResponse,
)


def _get_kwargs(
    game_id: int,
    language_code: str,
    *,
    body: bool | bool | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "https://gameinternationalization.roblox.com/v1/supported-languages/games/{game_id}/languages/{language_code}/automatic-translation-status".format(
            game_id=quote(str(game_id), safe=""),
            language_code=quote(str(language_code), safe=""),
        ),
        "openapi-extensions": {
            "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            "x-roblox-recommended-alternatives": [
                {
                    "url": "https://apis.roblox.com/legacy-game-internationalization/v1/supported-languages/games/{gameId}/languages/{languageCode}/automatic-translation-status",
                    "httpMethod": "PATCH",
                    "documentationUrl": "https://create.roblox.com/docs/cloud/reference/features/localization#patch_legacy_game_internationalization_v1_supported_languages_games__gameId__languages__languageCode__automatic_translation_status",
                }
            ],
        },
        "openapi-id": "patch_v1_supported-languages_games_gameId_languages_languageCode_automatic-translation-status",
    }

    if isinstance(body, bool):
        _kwargs["json"] = body

        headers["Content-Type"] = "application/json"
    if isinstance(body, bool):
        _kwargs["json"] = body

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxGameInternationalizationApiEditAutomaticTranslationStatusForGameAndLanguageResponse | None:
    if response.status_code == 200:
        response_200 = (
            RobloxGameInternationalizationApiEditAutomaticTranslationStatusForGameAndLanguageResponse.from_dict(
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
) -> Response[Any | RobloxGameInternationalizationApiEditAutomaticTranslationStatusForGameAndLanguageResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/localization#gameinternationalization_patch_v1_supported_languages_games__gameId__languages__languageCode__automatic_translation_status"
)
def sync_detailed(
    game_id: int,
    language_code: str,
    *,
    client: AuthenticatedClient,
    body: bool | bool | Unset = UNSET,
) -> Response[Any | RobloxGameInternationalizationApiEditAutomaticTranslationStatusForGameAndLanguageResponse]:
    """Enable or disable automatic translation for a game and language.

    Args:
        game_id (int):
        language_code (str):
        body (bool):
        body (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxGameInternationalizationApiEditAutomaticTranslationStatusForGameAndLanguageResponse]
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
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/localization#gameinternationalization_patch_v1_supported_languages_games__gameId__languages__languageCode__automatic_translation_status"
)
def sync(
    game_id: int,
    language_code: str,
    *,
    client: AuthenticatedClient,
    body: bool | bool | Unset = UNSET,
) -> Any | RobloxGameInternationalizationApiEditAutomaticTranslationStatusForGameAndLanguageResponse | None:
    """Enable or disable automatic translation for a game and language.

    Args:
        game_id (int):
        language_code (str):
        body (bool):
        body (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxGameInternationalizationApiEditAutomaticTranslationStatusForGameAndLanguageResponse
    """

    return sync_detailed(
        game_id=game_id,
        language_code=language_code,
        client=client,
        body=body,
    ).parsed


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/localization#gameinternationalization_patch_v1_supported_languages_games__gameId__languages__languageCode__automatic_translation_status"
)
async def asyncio_detailed(
    game_id: int,
    language_code: str,
    *,
    client: AuthenticatedClient,
    body: bool | bool | Unset = UNSET,
) -> Response[Any | RobloxGameInternationalizationApiEditAutomaticTranslationStatusForGameAndLanguageResponse]:
    """Enable or disable automatic translation for a game and language.

    Args:
        game_id (int):
        language_code (str):
        body (bool):
        body (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxGameInternationalizationApiEditAutomaticTranslationStatusForGameAndLanguageResponse]
    """

    kwargs = _get_kwargs(
        game_id=game_id,
        language_code=language_code,
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/localization#gameinternationalization_patch_v1_supported_languages_games__gameId__languages__languageCode__automatic_translation_status"
)
async def asyncio(
    game_id: int,
    language_code: str,
    *,
    client: AuthenticatedClient,
    body: bool | bool | Unset = UNSET,
) -> Any | RobloxGameInternationalizationApiEditAutomaticTranslationStatusForGameAndLanguageResponse | None:
    """Enable or disable automatic translation for a game and language.

    Args:
        game_id (int):
        language_code (str):
        body (bool):
        body (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxGameInternationalizationApiEditAutomaticTranslationStatusForGameAndLanguageResponse
    """

    return (
        await asyncio_detailed(
            game_id=game_id,
            language_code=language_code,
            client=client,
            body=body,
        )
    ).parsed
