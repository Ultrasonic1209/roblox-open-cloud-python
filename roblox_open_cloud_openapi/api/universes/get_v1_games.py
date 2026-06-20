from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_web_web_api_models_api_array_response_roblox_games_api_models_response_game_detail_response import (
    RobloxWebWebAPIModelsApiArrayResponseRobloxGamesApiModelsResponseGameDetailResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    universe_ids: list[int],
    fields: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_universe_ids = universe_ids

    params["universeIds"] = json_universe_ids

    params["fields"] = fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://games.roblox.com/v1/games",
        "params": params,
        "extensions": {
            "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
            "openapi-id": "get_v1_games",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGamesApiModelsResponseGameDetailResponse | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIModelsApiArrayResponseRobloxGamesApiModelsResponseGameDetailResponse.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGamesApiModelsResponseGameDetailResponse]:
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
    fields: str | Unset = UNSET,
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGamesApiModelsResponseGameDetailResponse]:
    """Gets a list of games' detail

    Args:
        universe_ids (list[int]):
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGamesApiModelsResponseGameDetailResponse]
    """

    kwargs = _get_kwargs(
        universe_ids=universe_ids,
        fields=fields,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    universe_ids: list[int],
    fields: str | Unset = UNSET,
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGamesApiModelsResponseGameDetailResponse | None:
    """Gets a list of games' detail

    Args:
        universe_ids (list[int]):
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGamesApiModelsResponseGameDetailResponse
    """

    return sync_detailed(
        client=client,
        universe_ids=universe_ids,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    universe_ids: list[int],
    fields: str | Unset = UNSET,
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGamesApiModelsResponseGameDetailResponse]:
    """Gets a list of games' detail

    Args:
        universe_ids (list[int]):
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGamesApiModelsResponseGameDetailResponse]
    """

    kwargs = _get_kwargs(
        universe_ids=universe_ids,
        fields=fields,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    universe_ids: list[int],
    fields: str | Unset = UNSET,
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGamesApiModelsResponseGameDetailResponse | None:
    """Gets a list of games' detail

    Args:
        universe_ids (list[int]):
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGamesApiModelsResponseGameDetailResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            universe_ids=universe_ids,
            fields=fields,
        )
    ).parsed
