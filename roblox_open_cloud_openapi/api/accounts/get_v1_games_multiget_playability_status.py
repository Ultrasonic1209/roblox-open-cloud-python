from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_games_api_models_response_playability_status_response import (
    RobloxGamesApiModelsResponsePlayabilityStatusResponse,
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
        "url": "https://games.roblox.com/v1/games/multiget-playability-status",
        "params": params,
        "extensions": {
            "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
            "openapi-id": "get_v1_games_multiget-playability-status",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | list[RobloxGamesApiModelsResponsePlayabilityStatusResponse] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = RobloxGamesApiModelsResponsePlayabilityStatusResponse.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | list[RobloxGamesApiModelsResponsePlayabilityStatusResponse]]:
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
) -> Response[Any | list[RobloxGamesApiModelsResponsePlayabilityStatusResponse]]:
    """Gets a list of universe playability statuses for the authenticated user

    Args:
        universe_ids (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[RobloxGamesApiModelsResponsePlayabilityStatusResponse]]
    """

    kwargs = _get_kwargs(
        universe_ids=universe_ids,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    universe_ids: list[int],
) -> Any | list[RobloxGamesApiModelsResponsePlayabilityStatusResponse] | None:
    """Gets a list of universe playability statuses for the authenticated user

    Args:
        universe_ids (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[RobloxGamesApiModelsResponsePlayabilityStatusResponse]
    """

    return sync_detailed(
        client=client,
        universe_ids=universe_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    universe_ids: list[int],
) -> Response[Any | list[RobloxGamesApiModelsResponsePlayabilityStatusResponse]]:
    """Gets a list of universe playability statuses for the authenticated user

    Args:
        universe_ids (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[RobloxGamesApiModelsResponsePlayabilityStatusResponse]]
    """

    kwargs = _get_kwargs(
        universe_ids=universe_ids,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    universe_ids: list[int],
) -> Any | list[RobloxGamesApiModelsResponsePlayabilityStatusResponse] | None:
    """Gets a list of universe playability statuses for the authenticated user

    Args:
        universe_ids (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[RobloxGamesApiModelsResponsePlayabilityStatusResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            universe_ids=universe_ids,
        )
    ).parsed
