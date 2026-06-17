import sys
from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response

if sys.version_info >= (3, 13):
    from warnings import deprecated
else:
    from typing_extensions import deprecated

from ...models.roblox_web_web_api_models_api_array_response_roblox_game_internationalization_api_universe_display_info_automatic_translation_settings import (
    RobloxWebWebAPIModelsApiArrayResponseRobloxGameInternationalizationApiUniverseDisplayInfoAutomaticTranslationSettings,
)


def _get_kwargs(
    game_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://gameinternationalization.roblox.com/v1/supported-languages/games/{game_id}/universe-display-info-automatic-translation-settings".format(
            game_id=quote(str(game_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> (
    Any
    | RobloxWebWebAPIModelsApiArrayResponseRobloxGameInternationalizationApiUniverseDisplayInfoAutomaticTranslationSettings
    | None
):
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIModelsApiArrayResponseRobloxGameInternationalizationApiUniverseDisplayInfoAutomaticTranslationSettings.from_dict(
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

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[
    Any
    | RobloxWebWebAPIModelsApiArrayResponseRobloxGameInternationalizationApiUniverseDisplayInfoAutomaticTranslationSettings
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/localization#gameinternationalization_get_v1_supported_languages_games__gameId__universe_display_info_automatic_translation_settings"
)
def sync_detailed(
    game_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[
    Any
    | RobloxWebWebAPIModelsApiArrayResponseRobloxGameInternationalizationApiUniverseDisplayInfoAutomaticTranslationSettings
]:
    """Get UniverseDisplayInfo automatic translation settings.

    Args:
        game_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGameInternationalizationApiUniverseDisplayInfoAutomaticTranslationSettings]
    """

    kwargs = _get_kwargs(
        game_id=game_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/localization#gameinternationalization_get_v1_supported_languages_games__gameId__universe_display_info_automatic_translation_settings"
)
def sync(
    game_id: int,
    *,
    client: AuthenticatedClient,
) -> (
    Any
    | RobloxWebWebAPIModelsApiArrayResponseRobloxGameInternationalizationApiUniverseDisplayInfoAutomaticTranslationSettings
    | None
):
    """Get UniverseDisplayInfo automatic translation settings.

    Args:
        game_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGameInternationalizationApiUniverseDisplayInfoAutomaticTranslationSettings
    """

    return sync_detailed(
        game_id=game_id,
        client=client,
    ).parsed


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/localization#gameinternationalization_get_v1_supported_languages_games__gameId__universe_display_info_automatic_translation_settings"
)
async def asyncio_detailed(
    game_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[
    Any
    | RobloxWebWebAPIModelsApiArrayResponseRobloxGameInternationalizationApiUniverseDisplayInfoAutomaticTranslationSettings
]:
    """Get UniverseDisplayInfo automatic translation settings.

    Args:
        game_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGameInternationalizationApiUniverseDisplayInfoAutomaticTranslationSettings]
    """

    kwargs = _get_kwargs(
        game_id=game_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/localization#gameinternationalization_get_v1_supported_languages_games__gameId__universe_display_info_automatic_translation_settings"
)
async def asyncio(
    game_id: int,
    *,
    client: AuthenticatedClient,
) -> (
    Any
    | RobloxWebWebAPIModelsApiArrayResponseRobloxGameInternationalizationApiUniverseDisplayInfoAutomaticTranslationSettings
    | None
):
    """Get UniverseDisplayInfo automatic translation settings.

    Args:
        game_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGameInternationalizationApiUniverseDisplayInfoAutomaticTranslationSettings
    """

    return (
        await asyncio_detailed(
            game_id=game_id,
            client=client,
        )
    ).parsed
