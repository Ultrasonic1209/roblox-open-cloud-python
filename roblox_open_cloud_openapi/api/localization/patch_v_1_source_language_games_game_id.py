import sys
from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response

if sys.version_info >= (3, 13):
    from warnings import deprecated
else:
    from typing_extensions import deprecated

from ...models.roblox_web_web_api_api_empty_response_model import RobloxWebWebAPIApiEmptyResponseModel


def _get_kwargs(
    game_id: int,
    *,
    language_code: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["languageCode"] = language_code

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "https://gameinternationalization.roblox.com/v1/source-language/games/{game_id}".format(
            game_id=quote(str(game_id), safe=""),
        ),
        "params": params,
        "extensions": {
            "openapi-extensions": {
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
                "x-roblox-recommended-alternatives": [
                    {
                        "url": "https://apis.roblox.com/legacy-game-internationalization/v1/source-language/games/{gameId}",
                        "httpMethod": "PATCH",
                        "documentationUrl": "https://create.roblox.com/docs/cloud/reference/features/localization#patch_legacy_game_internationalization_v1_source_language_games__gameId_",
                    }
                ],
            },
            "openapi-id": "patch_v1_source-language_games_gameId",
        },
    }

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
) -> Response[Any | RobloxWebWebAPIApiEmptyResponseModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/localization#gameinternationalization_patch_v1_source_language_games__gameId_"
)
def sync_detailed(
    game_id: int,
    *,
    client: AuthenticatedClient,
    language_code: str,
) -> Response[Any | RobloxWebWebAPIApiEmptyResponseModel]:
    """Sets the source language of a game

    Args:
        game_id (int):
        language_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIApiEmptyResponseModel]
    """

    kwargs = _get_kwargs(
        game_id=game_id,
        language_code=language_code,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/localization#gameinternationalization_patch_v1_source_language_games__gameId_"
)
def sync(
    game_id: int,
    *,
    client: AuthenticatedClient,
    language_code: str,
) -> Any | RobloxWebWebAPIApiEmptyResponseModel | None:
    """Sets the source language of a game

    Args:
        game_id (int):
        language_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIApiEmptyResponseModel
    """

    return sync_detailed(
        game_id=game_id,
        client=client,
        language_code=language_code,
    ).parsed


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/localization#gameinternationalization_patch_v1_source_language_games__gameId_"
)
async def asyncio_detailed(
    game_id: int,
    *,
    client: AuthenticatedClient,
    language_code: str,
) -> Response[Any | RobloxWebWebAPIApiEmptyResponseModel]:
    """Sets the source language of a game

    Args:
        game_id (int):
        language_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIApiEmptyResponseModel]
    """

    kwargs = _get_kwargs(
        game_id=game_id,
        language_code=language_code,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/localization#gameinternationalization_patch_v1_source_language_games__gameId_"
)
async def asyncio(
    game_id: int,
    *,
    client: AuthenticatedClient,
    language_code: str,
) -> Any | RobloxWebWebAPIApiEmptyResponseModel | None:
    """Sets the source language of a game

    Args:
        game_id (int):
        language_code (str):

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
            language_code=language_code,
        )
    ).parsed
