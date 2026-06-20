from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v2_users_user_id_tradable_items_item_target_types_item import (
    GetV2UsersUserIdTradableItemsItemTargetTypesItem,
)
from ...models.get_v2_users_user_id_tradable_items_sort_by import GetV2UsersUserIdTradableItemsSortBy
from ...models.get_v2_users_user_id_tradable_items_sort_order import GetV2UsersUserIdTradableItemsSortOrder
from ...models.roblox_trades_api_models_v2_get_user_tradable_items_response import (
    RobloxTradesApiModelsV2GetUserTradableItemsResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: int,
    *,
    search: str | Unset = UNSET,
    item_target_types: list[GetV2UsersUserIdTradableItemsItemTargetTypesItem] | Unset = UNSET,
    sort_by: GetV2UsersUserIdTradableItemsSortBy | Unset = GetV2UsersUserIdTradableItemsSortBy.CREATIONTIME,
    sort_order: GetV2UsersUserIdTradableItemsSortOrder | Unset = GetV2UsersUserIdTradableItemsSortOrder.VALUE_2,
    limit: int | Unset = 25,
    cursor: str | Unset = "",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["search"] = search

    json_item_target_types: list[str] | Unset = UNSET
    if not isinstance(item_target_types, Unset):
        json_item_target_types = []
        for item_target_types_item_data in item_target_types:
            item_target_types_item = item_target_types_item_data.value
            json_item_target_types.append(item_target_types_item)

    params["itemTargetTypes"] = json_item_target_types

    json_sort_by: str | Unset = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = sort_by.value

    params["sortBy"] = json_sort_by

    json_sort_order: int | Unset = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value

    params["sortOrder"] = json_sort_order

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://trades.roblox.com/v2/users/{user_id}/tradableItems".format(
            user_id=quote(str(user_id), safe=""),
        ),
        "params": params,
        "extensions": {
            "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
            "openapi-id": "get_v2_users_userId_tradableItems",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxTradesApiModelsV2GetUserTradableItemsResponse | None:
    if response.status_code == 200:
        response_200 = RobloxTradesApiModelsV2GetUserTradableItemsResponse.from_dict(response.json())

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

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxTradesApiModelsV2GetUserTradableItemsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: int,
    *,
    client: AuthenticatedClient,
    search: str | Unset = UNSET,
    item_target_types: list[GetV2UsersUserIdTradableItemsItemTargetTypesItem] | Unset = UNSET,
    sort_by: GetV2UsersUserIdTradableItemsSortBy | Unset = GetV2UsersUserIdTradableItemsSortBy.CREATIONTIME,
    sort_order: GetV2UsersUserIdTradableItemsSortOrder | Unset = GetV2UsersUserIdTradableItemsSortOrder.VALUE_2,
    limit: int | Unset = 25,
    cursor: str | Unset = "",
) -> Response[Any | RobloxTradesApiModelsV2GetUserTradableItemsResponse]:
    """Gets tradable items for a user.

    Args:
        user_id (int):
        search (str | Unset):
        item_target_types (list[GetV2UsersUserIdTradableItemsItemTargetTypesItem] | Unset):
        sort_by (GetV2UsersUserIdTradableItemsSortBy | Unset):  Default:
            GetV2UsersUserIdTradableItemsSortBy.CREATIONTIME.
        sort_order (GetV2UsersUserIdTradableItemsSortOrder | Unset):  Default:
            GetV2UsersUserIdTradableItemsSortOrder.VALUE_2.
        limit (int | Unset):  Default: 25.
        cursor (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxTradesApiModelsV2GetUserTradableItemsResponse]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        search=search,
        item_target_types=item_target_types,
        sort_by=sort_by,
        sort_order=sort_order,
        limit=limit,
        cursor=cursor,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: int,
    *,
    client: AuthenticatedClient,
    search: str | Unset = UNSET,
    item_target_types: list[GetV2UsersUserIdTradableItemsItemTargetTypesItem] | Unset = UNSET,
    sort_by: GetV2UsersUserIdTradableItemsSortBy | Unset = GetV2UsersUserIdTradableItemsSortBy.CREATIONTIME,
    sort_order: GetV2UsersUserIdTradableItemsSortOrder | Unset = GetV2UsersUserIdTradableItemsSortOrder.VALUE_2,
    limit: int | Unset = 25,
    cursor: str | Unset = "",
) -> Any | RobloxTradesApiModelsV2GetUserTradableItemsResponse | None:
    """Gets tradable items for a user.

    Args:
        user_id (int):
        search (str | Unset):
        item_target_types (list[GetV2UsersUserIdTradableItemsItemTargetTypesItem] | Unset):
        sort_by (GetV2UsersUserIdTradableItemsSortBy | Unset):  Default:
            GetV2UsersUserIdTradableItemsSortBy.CREATIONTIME.
        sort_order (GetV2UsersUserIdTradableItemsSortOrder | Unset):  Default:
            GetV2UsersUserIdTradableItemsSortOrder.VALUE_2.
        limit (int | Unset):  Default: 25.
        cursor (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxTradesApiModelsV2GetUserTradableItemsResponse
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        search=search,
        item_target_types=item_target_types,
        sort_by=sort_by,
        sort_order=sort_order,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    user_id: int,
    *,
    client: AuthenticatedClient,
    search: str | Unset = UNSET,
    item_target_types: list[GetV2UsersUserIdTradableItemsItemTargetTypesItem] | Unset = UNSET,
    sort_by: GetV2UsersUserIdTradableItemsSortBy | Unset = GetV2UsersUserIdTradableItemsSortBy.CREATIONTIME,
    sort_order: GetV2UsersUserIdTradableItemsSortOrder | Unset = GetV2UsersUserIdTradableItemsSortOrder.VALUE_2,
    limit: int | Unset = 25,
    cursor: str | Unset = "",
) -> Response[Any | RobloxTradesApiModelsV2GetUserTradableItemsResponse]:
    """Gets tradable items for a user.

    Args:
        user_id (int):
        search (str | Unset):
        item_target_types (list[GetV2UsersUserIdTradableItemsItemTargetTypesItem] | Unset):
        sort_by (GetV2UsersUserIdTradableItemsSortBy | Unset):  Default:
            GetV2UsersUserIdTradableItemsSortBy.CREATIONTIME.
        sort_order (GetV2UsersUserIdTradableItemsSortOrder | Unset):  Default:
            GetV2UsersUserIdTradableItemsSortOrder.VALUE_2.
        limit (int | Unset):  Default: 25.
        cursor (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxTradesApiModelsV2GetUserTradableItemsResponse]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        search=search,
        item_target_types=item_target_types,
        sort_by=sort_by,
        sort_order=sort_order,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: int,
    *,
    client: AuthenticatedClient,
    search: str | Unset = UNSET,
    item_target_types: list[GetV2UsersUserIdTradableItemsItemTargetTypesItem] | Unset = UNSET,
    sort_by: GetV2UsersUserIdTradableItemsSortBy | Unset = GetV2UsersUserIdTradableItemsSortBy.CREATIONTIME,
    sort_order: GetV2UsersUserIdTradableItemsSortOrder | Unset = GetV2UsersUserIdTradableItemsSortOrder.VALUE_2,
    limit: int | Unset = 25,
    cursor: str | Unset = "",
) -> Any | RobloxTradesApiModelsV2GetUserTradableItemsResponse | None:
    """Gets tradable items for a user.

    Args:
        user_id (int):
        search (str | Unset):
        item_target_types (list[GetV2UsersUserIdTradableItemsItemTargetTypesItem] | Unset):
        sort_by (GetV2UsersUserIdTradableItemsSortBy | Unset):  Default:
            GetV2UsersUserIdTradableItemsSortBy.CREATIONTIME.
        sort_order (GetV2UsersUserIdTradableItemsSortOrder | Unset):  Default:
            GetV2UsersUserIdTradableItemsSortOrder.VALUE_2.
        limit (int | Unset):  Default: 25.
        cursor (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxTradesApiModelsV2GetUserTradableItemsResponse
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            search=search,
            item_target_types=item_target_types,
            sort_by=sort_by,
            sort_order=sort_order,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
