from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v1_game_localization_status_translation_counts_for_language_or_locale_language_or_locale_type import (
    GetV1GameLocalizationStatusTranslationCountsForLanguageOrLocaleLanguageOrLocaleType,
)
from ...models.roblox_game_internationalization_api_get_translation_counts_for_language_or_locale_response import (
    RobloxGameInternationalizationApiGetTranslationCountsForLanguageOrLocaleResponse,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    game_ids: list[int],
    language_or_locale_code: str,
    language_or_locale_type: GetV1GameLocalizationStatusTranslationCountsForLanguageOrLocaleLanguageOrLocaleType,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_game_ids = game_ids

    params["gameIds"] = json_game_ids

    params["languageOrLocaleCode"] = language_or_locale_code

    json_language_or_locale_type = language_or_locale_type.value
    params["languageOrLocaleType"] = json_language_or_locale_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://gameinternationalization.roblox.com/v1/game-localization-status/translation-counts-for-language-or-locale",
        "params": params,
        "extensions": {
            "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
            "openapi-id": "get_v1_game-localization-status_translation-counts-for-language-or-locale",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxGameInternationalizationApiGetTranslationCountsForLanguageOrLocaleResponse | None:
    if response.status_code == 200:
        response_200 = RobloxGameInternationalizationApiGetTranslationCountsForLanguageOrLocaleResponse.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxGameInternationalizationApiGetTranslationCountsForLanguageOrLocaleResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    game_ids: list[int],
    language_or_locale_code: str,
    language_or_locale_type: GetV1GameLocalizationStatusTranslationCountsForLanguageOrLocaleLanguageOrLocaleType,
) -> Response[Any | RobloxGameInternationalizationApiGetTranslationCountsForLanguageOrLocaleResponse]:
    """Gets the language translation counts for the specified table.
    The languages to retrieve must be provided.

    Args:
        game_ids (list[int]):
        language_or_locale_code (str):
        language_or_locale_type
            (GetV1GameLocalizationStatusTranslationCountsForLanguageOrLocaleLanguageOrLocaleType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxGameInternationalizationApiGetTranslationCountsForLanguageOrLocaleResponse]
    """

    kwargs = _get_kwargs(
        game_ids=game_ids,
        language_or_locale_code=language_or_locale_code,
        language_or_locale_type=language_or_locale_type,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    game_ids: list[int],
    language_or_locale_code: str,
    language_or_locale_type: GetV1GameLocalizationStatusTranslationCountsForLanguageOrLocaleLanguageOrLocaleType,
) -> Any | RobloxGameInternationalizationApiGetTranslationCountsForLanguageOrLocaleResponse | None:
    """Gets the language translation counts for the specified table.
    The languages to retrieve must be provided.

    Args:
        game_ids (list[int]):
        language_or_locale_code (str):
        language_or_locale_type
            (GetV1GameLocalizationStatusTranslationCountsForLanguageOrLocaleLanguageOrLocaleType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxGameInternationalizationApiGetTranslationCountsForLanguageOrLocaleResponse
    """

    return sync_detailed(
        client=client,
        game_ids=game_ids,
        language_or_locale_code=language_or_locale_code,
        language_or_locale_type=language_or_locale_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    game_ids: list[int],
    language_or_locale_code: str,
    language_or_locale_type: GetV1GameLocalizationStatusTranslationCountsForLanguageOrLocaleLanguageOrLocaleType,
) -> Response[Any | RobloxGameInternationalizationApiGetTranslationCountsForLanguageOrLocaleResponse]:
    """Gets the language translation counts for the specified table.
    The languages to retrieve must be provided.

    Args:
        game_ids (list[int]):
        language_or_locale_code (str):
        language_or_locale_type
            (GetV1GameLocalizationStatusTranslationCountsForLanguageOrLocaleLanguageOrLocaleType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxGameInternationalizationApiGetTranslationCountsForLanguageOrLocaleResponse]
    """

    kwargs = _get_kwargs(
        game_ids=game_ids,
        language_or_locale_code=language_or_locale_code,
        language_or_locale_type=language_or_locale_type,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    game_ids: list[int],
    language_or_locale_code: str,
    language_or_locale_type: GetV1GameLocalizationStatusTranslationCountsForLanguageOrLocaleLanguageOrLocaleType,
) -> Any | RobloxGameInternationalizationApiGetTranslationCountsForLanguageOrLocaleResponse | None:
    """Gets the language translation counts for the specified table.
    The languages to retrieve must be provided.

    Args:
        game_ids (list[int]):
        language_or_locale_code (str):
        language_or_locale_type
            (GetV1GameLocalizationStatusTranslationCountsForLanguageOrLocaleLanguageOrLocaleType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxGameInternationalizationApiGetTranslationCountsForLanguageOrLocaleResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            game_ids=game_ids,
            language_or_locale_code=language_or_locale_code,
            language_or_locale_type=language_or_locale_type,
        )
    ).parsed
