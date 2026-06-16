from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_web_web_api_models_api_array_response_roblox_games_api_models_response_game_product_response import (
    RobloxWebWebAPIModelsApiArrayResponseRobloxGamesApiModelsResponseGameProductResponse,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    universe_ids: list[int],
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_universe_ids = universe_ids

    params["universeIds"] = json_universe_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/games/games-product-info",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGamesApiModelsResponseGameProductResponse | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIModelsApiArrayResponseRobloxGamesApiModelsResponseGameProductResponse.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGamesApiModelsResponseGameProductResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    universe_ids: list[int],
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGamesApiModelsResponseGameProductResponse]:
    """Gets a list of games' product info, used to purchase a game

    Args:
        universe_ids (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGamesApiModelsResponseGameProductResponse]
    """

    kwargs = _get_kwargs(
        universe_ids=universe_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    universe_ids: list[int],
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGamesApiModelsResponseGameProductResponse | None:
    """Gets a list of games' product info, used to purchase a game

    Args:
        universe_ids (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGamesApiModelsResponseGameProductResponse
    """

    return sync_detailed(
        client=client,
        universe_ids=universe_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    universe_ids: list[int],
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGamesApiModelsResponseGameProductResponse]:
    """Gets a list of games' product info, used to purchase a game

    Args:
        universe_ids (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGamesApiModelsResponseGameProductResponse]
    """

    kwargs = _get_kwargs(
        universe_ids=universe_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    universe_ids: list[int],
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGamesApiModelsResponseGameProductResponse | None:
    """Gets a list of games' product info, used to purchase a game

    Args:
        universe_ids (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGamesApiModelsResponseGameProductResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            universe_ids=universe_ids,
        )
    ).parsed
