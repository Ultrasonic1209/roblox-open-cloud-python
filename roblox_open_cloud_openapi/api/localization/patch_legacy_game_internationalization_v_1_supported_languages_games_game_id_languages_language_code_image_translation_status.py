from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_game_internationalization_api_edit_image_translation_status_for_game_and_language_response import (
    RobloxGameInternationalizationApiEditImageTranslationStatusForGameAndLanguageResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    game_id: int,
    language_code: str,
    *,
    body: bool | bool | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/legacy-game-internationalization/v1/supported-languages/games/{game_id}/languages/{language_code}/image-translation-status".format(
            game_id=quote(str(game_id), safe=""),
            language_code=quote(str(language_code), safe=""),
        ),
        "openapi-extensions": {
            "x-roblox-rate-limits": {
                "perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 100},
                "perOauth2Authorization": {"period": "MINUTE", "maxInPeriod": 100},
            },
            "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
        },
        "openapi-id": "patch_legacy-game-internationalization_v1_supported-languages_games_gameId_languages_languageCode_image-translation-status",
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
) -> Any | RobloxGameInternationalizationApiEditImageTranslationStatusForGameAndLanguageResponse | None:
    if response.status_code == 200:
        response_200 = RobloxGameInternationalizationApiEditImageTranslationStatusForGameAndLanguageResponse.from_dict(
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

    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxGameInternationalizationApiEditImageTranslationStatusForGameAndLanguageResponse]:
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
    body: bool | bool | Unset = UNSET,
) -> Response[Any | RobloxGameInternationalizationApiEditImageTranslationStatusForGameAndLanguageResponse]:
    """Enable or disable image translation for a game and language.

    Args:
        game_id (int):
        language_code (str):
        body (bool):
        body (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxGameInternationalizationApiEditImageTranslationStatusForGameAndLanguageResponse]
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
    body: bool | bool | Unset = UNSET,
) -> Any | RobloxGameInternationalizationApiEditImageTranslationStatusForGameAndLanguageResponse | None:
    """Enable or disable image translation for a game and language.

    Args:
        game_id (int):
        language_code (str):
        body (bool):
        body (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxGameInternationalizationApiEditImageTranslationStatusForGameAndLanguageResponse
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
    body: bool | bool | Unset = UNSET,
) -> Response[Any | RobloxGameInternationalizationApiEditImageTranslationStatusForGameAndLanguageResponse]:
    """Enable or disable image translation for a game and language.

    Args:
        game_id (int):
        language_code (str):
        body (bool):
        body (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxGameInternationalizationApiEditImageTranslationStatusForGameAndLanguageResponse]
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
    body: bool | bool | Unset = UNSET,
) -> Any | RobloxGameInternationalizationApiEditImageTranslationStatusForGameAndLanguageResponse | None:
    """Enable or disable image translation for a game and language.

    Args:
        game_id (int):
        language_code (str):
        body (bool):
        body (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxGameInternationalizationApiEditImageTranslationStatusForGameAndLanguageResponse
    """

    return (
        await asyncio_detailed(
            game_id=game_id,
            language_code=language_code,
            client=client,
            body=body,
        )
    ).parsed
