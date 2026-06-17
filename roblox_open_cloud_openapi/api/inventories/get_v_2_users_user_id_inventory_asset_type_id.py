import sys
from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset

if sys.version_info >= (3, 13):
    from warnings import deprecated
else:
    from typing_extensions import deprecated

from ...models.get_v2_users_user_id_inventory_asset_type_id_limit import GetV2UsersUserIdInventoryAssetTypeIdLimit
from ...models.get_v2_users_user_id_inventory_asset_type_id_sort_order import (
    GetV2UsersUserIdInventoryAssetTypeIdSortOrder,
)
from ...models.roblox_web_web_api_models_api_page_response_roblox_inventory_api_models_inventory_item_model import (
    RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiModelsInventoryItemModel,
)


def _get_kwargs(
    user_id: int,
    asset_type_id: int,
    *,
    limit: GetV2UsersUserIdInventoryAssetTypeIdLimit | Unset = GetV2UsersUserIdInventoryAssetTypeIdLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV2UsersUserIdInventoryAssetTypeIdSortOrder
    | Unset = GetV2UsersUserIdInventoryAssetTypeIdSortOrder.ASC,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

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
        "url": "https://inventory.roblox.com/v2/users/{user_id}/inventory/{asset_type_id}".format(
            user_id=quote(str(user_id), safe=""),
            asset_type_id=quote(str(asset_type_id), safe=""),
        ),
        "params": params,
        "openapi-extensions": {
            "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            "x-roblox-recommended-alternatives": [
                {
                    "url": "https://apis.roblox.com/cloud/v2/users/{user_id}/inventory-items",
                    "httpMethod": "GET",
                    "documentationUrl": "https://create.roblox.com/docs/cloud/reference/features/inventories#Cloud_ListInventoryItems",
                }
            ],
        },
        "openapi-id": "get_v2_users_userId_inventory_assetTypeId",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiModelsInventoryItemModel | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiModelsInventoryItemModel.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiModelsInventoryItemModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/inventories#inventory_get_v2_users__userId__inventory__assetTypeId_"
)
def sync_detailed(
    user_id: int,
    asset_type_id: int,
    *,
    client: AuthenticatedClient,
    limit: GetV2UsersUserIdInventoryAssetTypeIdLimit | Unset = GetV2UsersUserIdInventoryAssetTypeIdLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV2UsersUserIdInventoryAssetTypeIdSortOrder
    | Unset = GetV2UsersUserIdInventoryAssetTypeIdSortOrder.ASC,
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiModelsInventoryItemModel]:
    """Gets user's inventory based on specific asset type

    Args:
        user_id (int):
        asset_type_id (int):
        limit (GetV2UsersUserIdInventoryAssetTypeIdLimit | Unset):  Default:
            GetV2UsersUserIdInventoryAssetTypeIdLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV2UsersUserIdInventoryAssetTypeIdSortOrder | Unset):  Default:
            GetV2UsersUserIdInventoryAssetTypeIdSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiModelsInventoryItemModel]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        asset_type_id=asset_type_id,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/inventories#inventory_get_v2_users__userId__inventory__assetTypeId_"
)
def sync(
    user_id: int,
    asset_type_id: int,
    *,
    client: AuthenticatedClient,
    limit: GetV2UsersUserIdInventoryAssetTypeIdLimit | Unset = GetV2UsersUserIdInventoryAssetTypeIdLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV2UsersUserIdInventoryAssetTypeIdSortOrder
    | Unset = GetV2UsersUserIdInventoryAssetTypeIdSortOrder.ASC,
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiModelsInventoryItemModel | None:
    """Gets user's inventory based on specific asset type

    Args:
        user_id (int):
        asset_type_id (int):
        limit (GetV2UsersUserIdInventoryAssetTypeIdLimit | Unset):  Default:
            GetV2UsersUserIdInventoryAssetTypeIdLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV2UsersUserIdInventoryAssetTypeIdSortOrder | Unset):  Default:
            GetV2UsersUserIdInventoryAssetTypeIdSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiModelsInventoryItemModel
    """

    return sync_detailed(
        user_id=user_id,
        asset_type_id=asset_type_id,
        client=client,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
    ).parsed


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/inventories#inventory_get_v2_users__userId__inventory__assetTypeId_"
)
async def asyncio_detailed(
    user_id: int,
    asset_type_id: int,
    *,
    client: AuthenticatedClient,
    limit: GetV2UsersUserIdInventoryAssetTypeIdLimit | Unset = GetV2UsersUserIdInventoryAssetTypeIdLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV2UsersUserIdInventoryAssetTypeIdSortOrder
    | Unset = GetV2UsersUserIdInventoryAssetTypeIdSortOrder.ASC,
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiModelsInventoryItemModel]:
    """Gets user's inventory based on specific asset type

    Args:
        user_id (int):
        asset_type_id (int):
        limit (GetV2UsersUserIdInventoryAssetTypeIdLimit | Unset):  Default:
            GetV2UsersUserIdInventoryAssetTypeIdLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV2UsersUserIdInventoryAssetTypeIdSortOrder | Unset):  Default:
            GetV2UsersUserIdInventoryAssetTypeIdSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiModelsInventoryItemModel]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        asset_type_id=asset_type_id,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/inventories#inventory_get_v2_users__userId__inventory__assetTypeId_"
)
async def asyncio(
    user_id: int,
    asset_type_id: int,
    *,
    client: AuthenticatedClient,
    limit: GetV2UsersUserIdInventoryAssetTypeIdLimit | Unset = GetV2UsersUserIdInventoryAssetTypeIdLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV2UsersUserIdInventoryAssetTypeIdSortOrder
    | Unset = GetV2UsersUserIdInventoryAssetTypeIdSortOrder.ASC,
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiModelsInventoryItemModel | None:
    """Gets user's inventory based on specific asset type

    Args:
        user_id (int):
        asset_type_id (int):
        limit (GetV2UsersUserIdInventoryAssetTypeIdLimit | Unset):  Default:
            GetV2UsersUserIdInventoryAssetTypeIdLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV2UsersUserIdInventoryAssetTypeIdSortOrder | Unset):  Default:
            GetV2UsersUserIdInventoryAssetTypeIdSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiModelsInventoryItemModel
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            asset_type_id=asset_type_id,
            client=client,
            limit=limit,
            cursor=cursor,
            sort_order=sort_order,
        )
    ).parsed
