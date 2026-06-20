from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v1_universes_universe_id_badges_limit import GetV1UniversesUniverseIdBadgesLimit
from ...models.get_v1_universes_universe_id_badges_sort_by import GetV1UniversesUniverseIdBadgesSortBy
from ...models.get_v1_universes_universe_id_badges_sort_order import GetV1UniversesUniverseIdBadgesSortOrder
from ...models.roblox_web_web_api_models_api_page_response_roblox_badges_api_badge_response import (
    RobloxWebWebAPIModelsApiPageResponseRobloxBadgesApiBadgeResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    universe_id: int,
    *,
    sort_by: GetV1UniversesUniverseIdBadgesSortBy | Unset = UNSET,
    limit: GetV1UniversesUniverseIdBadgesLimit | Unset = GetV1UniversesUniverseIdBadgesLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1UniversesUniverseIdBadgesSortOrder | Unset = GetV1UniversesUniverseIdBadgesSortOrder.ASC,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_sort_by: str | Unset = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = sort_by.value

    params["sortBy"] = json_sort_by

    json_limit: int | Unset = UNSET
    if not isinstance(limit, Unset):
        json_limit = limit.value

    params["limit"] = json_limit

    params["cursor"] = cursor

    json_sort_order: str | Unset = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value

    params["sortOrder"] = json_sort_order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://badges.roblox.com/v1/universes/{universe_id}/badges".format(
            universe_id=quote(str(universe_id), safe=""),
        ),
        "params": params,
        "extensions": {
            "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
            "openapi-id": "get_v1_universes_universeId_badges",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxBadgesApiBadgeResponse | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIModelsApiPageResponseRobloxBadgesApiBadgeResponse.from_dict(response.json())

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
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxBadgesApiBadgeResponse]:
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
    sort_by: GetV1UniversesUniverseIdBadgesSortBy | Unset = UNSET,
    limit: GetV1UniversesUniverseIdBadgesLimit | Unset = GetV1UniversesUniverseIdBadgesLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1UniversesUniverseIdBadgesSortOrder | Unset = GetV1UniversesUniverseIdBadgesSortOrder.ASC,
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxBadgesApiBadgeResponse]:
    """Gets badges by their awarding game.

    Args:
        universe_id (int):
        sort_by (GetV1UniversesUniverseIdBadgesSortBy | Unset):
        limit (GetV1UniversesUniverseIdBadgesLimit | Unset):  Default:
            GetV1UniversesUniverseIdBadgesLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV1UniversesUniverseIdBadgesSortOrder | Unset):  Default:
            GetV1UniversesUniverseIdBadgesSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxBadgesApiBadgeResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        sort_by=sort_by,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    sort_by: GetV1UniversesUniverseIdBadgesSortBy | Unset = UNSET,
    limit: GetV1UniversesUniverseIdBadgesLimit | Unset = GetV1UniversesUniverseIdBadgesLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1UniversesUniverseIdBadgesSortOrder | Unset = GetV1UniversesUniverseIdBadgesSortOrder.ASC,
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxBadgesApiBadgeResponse | None:
    """Gets badges by their awarding game.

    Args:
        universe_id (int):
        sort_by (GetV1UniversesUniverseIdBadgesSortBy | Unset):
        limit (GetV1UniversesUniverseIdBadgesLimit | Unset):  Default:
            GetV1UniversesUniverseIdBadgesLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV1UniversesUniverseIdBadgesSortOrder | Unset):  Default:
            GetV1UniversesUniverseIdBadgesSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiPageResponseRobloxBadgesApiBadgeResponse
    """

    return sync_detailed(
        universe_id=universe_id,
        client=client,
        sort_by=sort_by,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
    ).parsed


async def asyncio_detailed(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    sort_by: GetV1UniversesUniverseIdBadgesSortBy | Unset = UNSET,
    limit: GetV1UniversesUniverseIdBadgesLimit | Unset = GetV1UniversesUniverseIdBadgesLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1UniversesUniverseIdBadgesSortOrder | Unset = GetV1UniversesUniverseIdBadgesSortOrder.ASC,
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxBadgesApiBadgeResponse]:
    """Gets badges by their awarding game.

    Args:
        universe_id (int):
        sort_by (GetV1UniversesUniverseIdBadgesSortBy | Unset):
        limit (GetV1UniversesUniverseIdBadgesLimit | Unset):  Default:
            GetV1UniversesUniverseIdBadgesLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV1UniversesUniverseIdBadgesSortOrder | Unset):  Default:
            GetV1UniversesUniverseIdBadgesSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxBadgesApiBadgeResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        sort_by=sort_by,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    sort_by: GetV1UniversesUniverseIdBadgesSortBy | Unset = UNSET,
    limit: GetV1UniversesUniverseIdBadgesLimit | Unset = GetV1UniversesUniverseIdBadgesLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1UniversesUniverseIdBadgesSortOrder | Unset = GetV1UniversesUniverseIdBadgesSortOrder.ASC,
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxBadgesApiBadgeResponse | None:
    """Gets badges by their awarding game.

    Args:
        universe_id (int):
        sort_by (GetV1UniversesUniverseIdBadgesSortBy | Unset):
        limit (GetV1UniversesUniverseIdBadgesLimit | Unset):  Default:
            GetV1UniversesUniverseIdBadgesLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV1UniversesUniverseIdBadgesSortOrder | Unset):  Default:
            GetV1UniversesUniverseIdBadgesSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiPageResponseRobloxBadgesApiBadgeResponse
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            client=client,
            sort_by=sort_by,
            limit=limit,
            cursor=cursor,
            sort_order=sort_order,
        )
    ).parsed
