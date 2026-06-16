from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_game_internationalization_api_get_allowed_automatic_translation_status_for_languages_response import (
    RobloxGameInternationalizationApiGetAllowedAutomaticTranslationStatusForLanguagesResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    language_code: str,
    *,
    target_languages: list[str] | Unset = UNSET,
    game_id: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_target_languages: list[str] | Unset = UNSET
    if not isinstance(target_languages, Unset):
        json_target_languages = target_languages

    params["targetLanguages"] = json_target_languages

    params["gameId"] = game_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/automatic-translation/languages/{language_code}/target-languages".format(
            language_code=quote(str(language_code), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxGameInternationalizationApiGetAllowedAutomaticTranslationStatusForLanguagesResponse | None:
    if response.status_code == 200:
        response_200 = (
            RobloxGameInternationalizationApiGetAllowedAutomaticTranslationStatusForLanguagesResponse.from_dict(
                response.json()
            )
        )

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RobloxGameInternationalizationApiGetAllowedAutomaticTranslationStatusForLanguagesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    language_code: str,
    *,
    client: AuthenticatedClient,
    target_languages: list[str] | Unset = UNSET,
    game_id: int | Unset = UNSET,
) -> Response[Any | RobloxGameInternationalizationApiGetAllowedAutomaticTranslationStatusForLanguagesResponse]:
    """Checks if the requested target languages are allowed for automatic translation based on the source
    language.
    If there are no requested target languages, then all allowed target languages for the source
    language will be returned.

    Args:
        language_code (str):
        target_languages (list[str] | Unset):
        game_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxGameInternationalizationApiGetAllowedAutomaticTranslationStatusForLanguagesResponse]
    """

    kwargs = _get_kwargs(
        language_code=language_code,
        target_languages=target_languages,
        game_id=game_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    language_code: str,
    *,
    client: AuthenticatedClient,
    target_languages: list[str] | Unset = UNSET,
    game_id: int | Unset = UNSET,
) -> Any | RobloxGameInternationalizationApiGetAllowedAutomaticTranslationStatusForLanguagesResponse | None:
    """Checks if the requested target languages are allowed for automatic translation based on the source
    language.
    If there are no requested target languages, then all allowed target languages for the source
    language will be returned.

    Args:
        language_code (str):
        target_languages (list[str] | Unset):
        game_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxGameInternationalizationApiGetAllowedAutomaticTranslationStatusForLanguagesResponse
    """

    return sync_detailed(
        language_code=language_code,
        client=client,
        target_languages=target_languages,
        game_id=game_id,
    ).parsed


async def asyncio_detailed(
    language_code: str,
    *,
    client: AuthenticatedClient,
    target_languages: list[str] | Unset = UNSET,
    game_id: int | Unset = UNSET,
) -> Response[Any | RobloxGameInternationalizationApiGetAllowedAutomaticTranslationStatusForLanguagesResponse]:
    """Checks if the requested target languages are allowed for automatic translation based on the source
    language.
    If there are no requested target languages, then all allowed target languages for the source
    language will be returned.

    Args:
        language_code (str):
        target_languages (list[str] | Unset):
        game_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxGameInternationalizationApiGetAllowedAutomaticTranslationStatusForLanguagesResponse]
    """

    kwargs = _get_kwargs(
        language_code=language_code,
        target_languages=target_languages,
        game_id=game_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    language_code: str,
    *,
    client: AuthenticatedClient,
    target_languages: list[str] | Unset = UNSET,
    game_id: int | Unset = UNSET,
) -> Any | RobloxGameInternationalizationApiGetAllowedAutomaticTranslationStatusForLanguagesResponse | None:
    """Checks if the requested target languages are allowed for automatic translation based on the source
    language.
    If there are no requested target languages, then all allowed target languages for the source
    language will be returned.

    Args:
        language_code (str):
        target_languages (list[str] | Unset):
        game_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxGameInternationalizationApiGetAllowedAutomaticTranslationStatusForLanguagesResponse
    """

    return (
        await asyncio_detailed(
            language_code=language_code,
            client=client,
            target_languages=target_languages,
            game_id=game_id,
        )
    ).parsed
