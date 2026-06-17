from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_localization_tables_api_game_autolocalization_information_response import (
    RobloxLocalizationTablesApiGameAutolocalizationInformationResponse,
)
from ...types import Response


def _get_kwargs(
    game_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/legacy-localization-tables/v1/autolocalization/games/{game_id}/autolocalizationtable".format(
            game_id=quote(str(game_id), safe=""),
        ),
        "openapi-extensions": {
            "x-roblox-rate-limits": {
                "perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 100},
                "perOauth2Authorization": {"period": "MINUTE", "maxInPeriod": 100},
            },
            "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            "x-roblox-scopes": [{"name": "legacy-universe:manage"}],
        },
        "openapi-id": "post_legacy-localization-tables_v1_autolocalization_games_gameId_autolocalizationtable",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxLocalizationTablesApiGameAutolocalizationInformationResponse | None:
    if response.status_code == 200:
        response_200 = RobloxLocalizationTablesApiGameAutolocalizationInformationResponse.from_dict(response.json())

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
) -> Response[Any | RobloxLocalizationTablesApiGameAutolocalizationInformationResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    game_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxLocalizationTablesApiGameAutolocalizationInformationResponse]:
    """
    Args:
        game_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxLocalizationTablesApiGameAutolocalizationInformationResponse]
    """

    kwargs = _get_kwargs(
        game_id=game_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    game_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxLocalizationTablesApiGameAutolocalizationInformationResponse | None:
    """
    Args:
        game_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxLocalizationTablesApiGameAutolocalizationInformationResponse
    """

    return sync_detailed(
        game_id=game_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    game_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxLocalizationTablesApiGameAutolocalizationInformationResponse]:
    """
    Args:
        game_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxLocalizationTablesApiGameAutolocalizationInformationResponse]
    """

    kwargs = _get_kwargs(
        game_id=game_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    game_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxLocalizationTablesApiGameAutolocalizationInformationResponse | None:
    """
    Args:
        game_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxLocalizationTablesApiGameAutolocalizationInformationResponse
    """

    return (
        await asyncio_detailed(
            game_id=game_id,
            client=client,
        )
    ).parsed
