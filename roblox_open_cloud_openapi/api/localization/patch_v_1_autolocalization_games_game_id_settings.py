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

from ...models.roblox_game_internationalization_api_set_autolocalization_settings_for_game_request import (
    RobloxGameInternationalizationApiSetAutolocalizationSettingsForGameRequest,
)
from ...models.roblox_web_web_api_api_empty_response_model import RobloxWebWebAPIApiEmptyResponseModel


def _get_kwargs(
    game_id: int,
    *,
    body: RobloxGameInternationalizationApiSetAutolocalizationSettingsForGameRequest
    | RobloxGameInternationalizationApiSetAutolocalizationSettingsForGameRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "https://gameinternationalization.roblox.com/v1/autolocalization/games/{game_id}/settings".format(
            game_id=quote(str(game_id), safe=""),
        ),
        "openapi-extensions": {
            "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            "x-roblox-recommended-alternatives": [
                {
                    "url": "https://apis.roblox.com/legacy-localization-tables/v1/autolocalization/games/{gameId}/settings",
                    "httpMethod": "PATCH",
                    "documentationUrl": "https://create.roblox.com/docs/cloud/reference/features/localization#patch_legacy_localization_tables_v1_autolocalization_games__gameId__settings",
                }
            ],
        },
        "openapi-id": "patch_v1_autolocalization_games_gameId_settings",
    }

    if isinstance(body, RobloxGameInternationalizationApiSetAutolocalizationSettingsForGameRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxGameInternationalizationApiSetAutolocalizationSettingsForGameRequest):
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
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/localization#gameinternationalization_patch_v1_autolocalization_games__gameId__settings"
)
def sync_detailed(
    game_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxGameInternationalizationApiSetAutolocalizationSettingsForGameRequest
    | RobloxGameInternationalizationApiSetAutolocalizationSettingsForGameRequest
    | Unset = UNSET,
) -> Response[Any | RobloxWebWebAPIApiEmptyResponseModel]:
    """Sets a game's auto-localization related settings

     Use the Autolocalization controller in LocalizationTables API

    Args:
        game_id (int):
        body (RobloxGameInternationalizationApiSetAutolocalizationSettingsForGameRequest):
        body (RobloxGameInternationalizationApiSetAutolocalizationSettingsForGameRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIApiEmptyResponseModel]
    """

    kwargs = _get_kwargs(
        game_id=game_id,
        body=body,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/localization#gameinternationalization_patch_v1_autolocalization_games__gameId__settings"
)
def sync(
    game_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxGameInternationalizationApiSetAutolocalizationSettingsForGameRequest
    | RobloxGameInternationalizationApiSetAutolocalizationSettingsForGameRequest
    | Unset = UNSET,
) -> Any | RobloxWebWebAPIApiEmptyResponseModel | None:
    """Sets a game's auto-localization related settings

     Use the Autolocalization controller in LocalizationTables API

    Args:
        game_id (int):
        body (RobloxGameInternationalizationApiSetAutolocalizationSettingsForGameRequest):
        body (RobloxGameInternationalizationApiSetAutolocalizationSettingsForGameRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIApiEmptyResponseModel
    """

    return sync_detailed(
        game_id=game_id,
        client=client,
        body=body,
    ).parsed


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/localization#gameinternationalization_patch_v1_autolocalization_games__gameId__settings"
)
async def asyncio_detailed(
    game_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxGameInternationalizationApiSetAutolocalizationSettingsForGameRequest
    | RobloxGameInternationalizationApiSetAutolocalizationSettingsForGameRequest
    | Unset = UNSET,
) -> Response[Any | RobloxWebWebAPIApiEmptyResponseModel]:
    """Sets a game's auto-localization related settings

     Use the Autolocalization controller in LocalizationTables API

    Args:
        game_id (int):
        body (RobloxGameInternationalizationApiSetAutolocalizationSettingsForGameRequest):
        body (RobloxGameInternationalizationApiSetAutolocalizationSettingsForGameRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIApiEmptyResponseModel]
    """

    kwargs = _get_kwargs(
        game_id=game_id,
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/localization#gameinternationalization_patch_v1_autolocalization_games__gameId__settings"
)
async def asyncio(
    game_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxGameInternationalizationApiSetAutolocalizationSettingsForGameRequest
    | RobloxGameInternationalizationApiSetAutolocalizationSettingsForGameRequest
    | Unset = UNSET,
) -> Any | RobloxWebWebAPIApiEmptyResponseModel | None:
    """Sets a game's auto-localization related settings

     Use the Autolocalization controller in LocalizationTables API

    Args:
        game_id (int):
        body (RobloxGameInternationalizationApiSetAutolocalizationSettingsForGameRequest):
        body (RobloxGameInternationalizationApiSetAutolocalizationSettingsForGameRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIApiEmptyResponseModel
    """

    return (
        await asyncio_detailed(
            game_id=game_id,
            client=client,
            body=body,
        )
    ).parsed
