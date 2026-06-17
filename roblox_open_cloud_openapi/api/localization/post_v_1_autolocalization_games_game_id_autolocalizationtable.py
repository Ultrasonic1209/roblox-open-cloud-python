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

from ...models.roblox_game_internationalization_api_game_autolocalization_information_response import (
    RobloxGameInternationalizationApiGameAutolocalizationInformationResponse,
)


def _get_kwargs(
    game_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "https://gameinternationalization.roblox.com/v1/autolocalization/games/{game_id}/autolocalizationtable".format(
            game_id=quote(str(game_id), safe=""),
        ),
        "openapi-extensions": {
            "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            "x-roblox-recommended-alternatives": [
                {
                    "url": "https://apis.roblox.com/legacy-localization-tables/v1/autolocalization/games/{gameId}/autolocalizationtable",
                    "httpMethod": "POST",
                    "documentationUrl": "https://create.roblox.com/docs/cloud/reference/features/localization#post_legacy_localization_tables_v1_autolocalization_games__gameId__autolocalizationtable",
                }
            ],
        },
        "openapi-id": "post_v1_autolocalization_games_gameId_autolocalizationtable",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxGameInternationalizationApiGameAutolocalizationInformationResponse | None:
    if response.status_code == 200:
        response_200 = RobloxGameInternationalizationApiGameAutolocalizationInformationResponse.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxGameInternationalizationApiGameAutolocalizationInformationResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/localization#gameinternationalization_post_v1_autolocalization_games__gameId__autolocalizationtable"
)
def sync_detailed(
    game_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxGameInternationalizationApiGameAutolocalizationInformationResponse]:
    """Use the Autolocalization controller in LocalizationTables API

    Args:
        game_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxGameInternationalizationApiGameAutolocalizationInformationResponse]
    """

    kwargs = _get_kwargs(
        game_id=game_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/localization#gameinternationalization_post_v1_autolocalization_games__gameId__autolocalizationtable"
)
def sync(
    game_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxGameInternationalizationApiGameAutolocalizationInformationResponse | None:
    """Use the Autolocalization controller in LocalizationTables API

    Args:
        game_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxGameInternationalizationApiGameAutolocalizationInformationResponse
    """

    return sync_detailed(
        game_id=game_id,
        client=client,
    ).parsed


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/localization#gameinternationalization_post_v1_autolocalization_games__gameId__autolocalizationtable"
)
async def asyncio_detailed(
    game_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxGameInternationalizationApiGameAutolocalizationInformationResponse]:
    """Use the Autolocalization controller in LocalizationTables API

    Args:
        game_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxGameInternationalizationApiGameAutolocalizationInformationResponse]
    """

    kwargs = _get_kwargs(
        game_id=game_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/localization#gameinternationalization_post_v1_autolocalization_games__gameId__autolocalizationtable"
)
async def asyncio(
    game_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxGameInternationalizationApiGameAutolocalizationInformationResponse | None:
    """Use the Autolocalization controller in LocalizationTables API

    Args:
        game_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxGameInternationalizationApiGameAutolocalizationInformationResponse
    """

    return (
        await asyncio_detailed(
            game_id=game_id,
            client=client,
        )
    ).parsed
