from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_games_api_models_response_game_recommendations_response import (
    RobloxGamesApiModelsResponseGameRecommendationsResponse,
)
from ...types import UNSET, Response


def _get_kwargs(
    universe_id: int,
    *,
    pagination_key: str,
    max_rows: int,
    is_truncated_results_enabled: bool,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["PaginationKey"] = pagination_key

    params["MaxRows"] = max_rows

    params["IsTruncatedResultsEnabled"] = is_truncated_results_enabled

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://games.roblox.com/v1/games/recommendations/game/{universe_id}".format(
            universe_id=quote(str(universe_id), safe=""),
        ),
        "params": params,
        "extensions": {
            "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
            "openapi-id": "get_v1_games_recommendations_game_universeId",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxGamesApiModelsResponseGameRecommendationsResponse | None:
    if response.status_code == 200:
        response_200 = RobloxGamesApiModelsResponseGameRecommendationsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxGamesApiModelsResponseGameRecommendationsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    pagination_key: str,
    max_rows: int,
    is_truncated_results_enabled: bool,
) -> Response[Any | RobloxGamesApiModelsResponseGameRecommendationsResponse]:
    """Get games recommendations based on a given universe

    Args:
        universe_id (int):
        pagination_key (str):
        max_rows (int):
        is_truncated_results_enabled (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxGamesApiModelsResponseGameRecommendationsResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        pagination_key=pagination_key,
        max_rows=max_rows,
        is_truncated_results_enabled=is_truncated_results_enabled,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    pagination_key: str,
    max_rows: int,
    is_truncated_results_enabled: bool,
) -> Any | RobloxGamesApiModelsResponseGameRecommendationsResponse | None:
    """Get games recommendations based on a given universe

    Args:
        universe_id (int):
        pagination_key (str):
        max_rows (int):
        is_truncated_results_enabled (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxGamesApiModelsResponseGameRecommendationsResponse
    """

    return sync_detailed(
        universe_id=universe_id,
        client=client,
        pagination_key=pagination_key,
        max_rows=max_rows,
        is_truncated_results_enabled=is_truncated_results_enabled,
    ).parsed


async def asyncio_detailed(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    pagination_key: str,
    max_rows: int,
    is_truncated_results_enabled: bool,
) -> Response[Any | RobloxGamesApiModelsResponseGameRecommendationsResponse]:
    """Get games recommendations based on a given universe

    Args:
        universe_id (int):
        pagination_key (str):
        max_rows (int):
        is_truncated_results_enabled (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxGamesApiModelsResponseGameRecommendationsResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        pagination_key=pagination_key,
        max_rows=max_rows,
        is_truncated_results_enabled=is_truncated_results_enabled,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    pagination_key: str,
    max_rows: int,
    is_truncated_results_enabled: bool,
) -> Any | RobloxGamesApiModelsResponseGameRecommendationsResponse | None:
    """Get games recommendations based on a given universe

    Args:
        universe_id (int):
        pagination_key (str):
        max_rows (int):
        is_truncated_results_enabled (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxGamesApiModelsResponseGameRecommendationsResponse
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            client=client,
            pagination_key=pagination_key,
            max_rows=max_rows,
            is_truncated_results_enabled=is_truncated_results_enabled,
        )
    ).parsed
