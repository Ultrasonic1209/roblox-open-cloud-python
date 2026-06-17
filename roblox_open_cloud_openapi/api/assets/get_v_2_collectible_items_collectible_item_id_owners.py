from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v2_collectible_items_collectible_item_id_owners_sort_order import (
    GetV2CollectibleItemsCollectibleItemIdOwnersSortOrder,
)
from ...models.roblox_web_web_api_models_api_page_response_roblox_inventory_api_v2_collectible_item_owner_response import (
    RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiV2CollectibleItemOwnerResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    collectible_item_id: str,
    *,
    limit: int | Unset = 10,
    cursor: str | Unset = "",
    sort_order: GetV2CollectibleItemsCollectibleItemIdOwnersSortOrder
    | Unset = GetV2CollectibleItemsCollectibleItemIdOwnersSortOrder.VALUE_1,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    json_sort_order: int | Unset = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value

    params["sortOrder"] = json_sort_order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://inventory.roblox.com/v2/collectible-items/{collectible_item_id}/owners".format(
            collectible_item_id=quote(str(collectible_item_id), safe=""),
        ),
        "params": params,
        "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
        "openapi-id": "get_v2_collectible-items_collectibleItemId_owners",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiV2CollectibleItemOwnerResponse | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiV2CollectibleItemOwnerResponse.from_dict(
            response.json()
        )

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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiV2CollectibleItemOwnerResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    collectible_item_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 10,
    cursor: str | Unset = "",
    sort_order: GetV2CollectibleItemsCollectibleItemIdOwnersSortOrder
    | Unset = GetV2CollectibleItemsCollectibleItemIdOwnersSortOrder.VALUE_1,
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiV2CollectibleItemOwnerResponse]:
    """Gets a list of owners of a collectible item.

    Args:
        collectible_item_id (str):
        limit (int | Unset):  Default: 10.
        cursor (str | Unset):  Default: ''.
        sort_order (GetV2CollectibleItemsCollectibleItemIdOwnersSortOrder | Unset):  Default:
            GetV2CollectibleItemsCollectibleItemIdOwnersSortOrder.VALUE_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiV2CollectibleItemOwnerResponse]
    """

    kwargs = _get_kwargs(
        collectible_item_id=collectible_item_id,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    collectible_item_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 10,
    cursor: str | Unset = "",
    sort_order: GetV2CollectibleItemsCollectibleItemIdOwnersSortOrder
    | Unset = GetV2CollectibleItemsCollectibleItemIdOwnersSortOrder.VALUE_1,
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiV2CollectibleItemOwnerResponse | None:
    """Gets a list of owners of a collectible item.

    Args:
        collectible_item_id (str):
        limit (int | Unset):  Default: 10.
        cursor (str | Unset):  Default: ''.
        sort_order (GetV2CollectibleItemsCollectibleItemIdOwnersSortOrder | Unset):  Default:
            GetV2CollectibleItemsCollectibleItemIdOwnersSortOrder.VALUE_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiV2CollectibleItemOwnerResponse
    """

    return sync_detailed(
        collectible_item_id=collectible_item_id,
        client=client,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
    ).parsed


async def asyncio_detailed(
    collectible_item_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 10,
    cursor: str | Unset = "",
    sort_order: GetV2CollectibleItemsCollectibleItemIdOwnersSortOrder
    | Unset = GetV2CollectibleItemsCollectibleItemIdOwnersSortOrder.VALUE_1,
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiV2CollectibleItemOwnerResponse]:
    """Gets a list of owners of a collectible item.

    Args:
        collectible_item_id (str):
        limit (int | Unset):  Default: 10.
        cursor (str | Unset):  Default: ''.
        sort_order (GetV2CollectibleItemsCollectibleItemIdOwnersSortOrder | Unset):  Default:
            GetV2CollectibleItemsCollectibleItemIdOwnersSortOrder.VALUE_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiV2CollectibleItemOwnerResponse]
    """

    kwargs = _get_kwargs(
        collectible_item_id=collectible_item_id,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    collectible_item_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 10,
    cursor: str | Unset = "",
    sort_order: GetV2CollectibleItemsCollectibleItemIdOwnersSortOrder
    | Unset = GetV2CollectibleItemsCollectibleItemIdOwnersSortOrder.VALUE_1,
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiV2CollectibleItemOwnerResponse | None:
    """Gets a list of owners of a collectible item.

    Args:
        collectible_item_id (str):
        limit (int | Unset):  Default: 10.
        cursor (str | Unset):  Default: ''.
        sort_order (GetV2CollectibleItemsCollectibleItemIdOwnersSortOrder | Unset):  Default:
            GetV2CollectibleItemsCollectibleItemIdOwnersSortOrder.VALUE_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiV2CollectibleItemOwnerResponse
    """

    return (
        await asyncio_detailed(
            collectible_item_id=collectible_item_id,
            client=client,
            limit=limit,
            cursor=cursor,
            sort_order=sort_order,
        )
    ).parsed
