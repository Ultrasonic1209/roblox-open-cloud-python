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

from ...models.get_v2_users_user_id_inventory_asset_types_item import GetV2UsersUserIdInventoryAssetTypesItem
from ...models.get_v2_users_user_id_inventory_limit import GetV2UsersUserIdInventoryLimit
from ...models.get_v2_users_user_id_inventory_sort_order import GetV2UsersUserIdInventorySortOrder
from ...models.roblox_web_web_api_models_api_page_response_roblox_inventory_api_v2_user_asset_item_model_v2 import (
    RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiV2UserAssetItemModelV2,
)


def _get_kwargs(
    user_id: int,
    *,
    asset_types: list[GetV2UsersUserIdInventoryAssetTypesItem],
    filter_disapproved_assets: bool | Unset = False,
    show_approved_only: bool | Unset = False,
    limit: GetV2UsersUserIdInventoryLimit | Unset = GetV2UsersUserIdInventoryLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV2UsersUserIdInventorySortOrder | Unset = GetV2UsersUserIdInventorySortOrder.ASC,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_asset_types = []
    for asset_types_item_data in asset_types:
        asset_types_item = asset_types_item_data.value
        json_asset_types.append(asset_types_item)

    params["assetTypes"] = json_asset_types

    params["filterDisapprovedAssets"] = filter_disapproved_assets

    params["showApprovedOnly"] = show_approved_only

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
        "url": "https://inventory.roblox.com/v2/users/{user_id}/inventory".format(
            user_id=quote(str(user_id), safe=""),
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
        "openapi-id": "get_v2_users_userId_inventory",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiV2UserAssetItemModelV2 | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiV2UserAssetItemModelV2.from_dict(
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
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiV2UserAssetItemModelV2]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/assets#inventory_get_v2_users__userId__inventory"
)
def sync_detailed(
    user_id: int,
    *,
    client: AuthenticatedClient,
    asset_types: list[GetV2UsersUserIdInventoryAssetTypesItem],
    filter_disapproved_assets: bool | Unset = False,
    show_approved_only: bool | Unset = False,
    limit: GetV2UsersUserIdInventoryLimit | Unset = GetV2UsersUserIdInventoryLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV2UsersUserIdInventorySortOrder | Unset = GetV2UsersUserIdInventorySortOrder.ASC,
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiV2UserAssetItemModelV2]:
    """Get user's inventory by multiple Roblox.Platform.Assets.AssetType.

     GamePass and Badges not allowed.

    Args:
        user_id (int):
        asset_types (list[GetV2UsersUserIdInventoryAssetTypesItem]):
        filter_disapproved_assets (bool | Unset):  Default: False.
        show_approved_only (bool | Unset):  Default: False.
        limit (GetV2UsersUserIdInventoryLimit | Unset):  Default:
            GetV2UsersUserIdInventoryLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV2UsersUserIdInventorySortOrder | Unset):  Default:
            GetV2UsersUserIdInventorySortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiV2UserAssetItemModelV2]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        asset_types=asset_types,
        filter_disapproved_assets=filter_disapproved_assets,
        show_approved_only=show_approved_only,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/assets#inventory_get_v2_users__userId__inventory"
)
def sync(
    user_id: int,
    *,
    client: AuthenticatedClient,
    asset_types: list[GetV2UsersUserIdInventoryAssetTypesItem],
    filter_disapproved_assets: bool | Unset = False,
    show_approved_only: bool | Unset = False,
    limit: GetV2UsersUserIdInventoryLimit | Unset = GetV2UsersUserIdInventoryLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV2UsersUserIdInventorySortOrder | Unset = GetV2UsersUserIdInventorySortOrder.ASC,
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiV2UserAssetItemModelV2 | None:
    """Get user's inventory by multiple Roblox.Platform.Assets.AssetType.

     GamePass and Badges not allowed.

    Args:
        user_id (int):
        asset_types (list[GetV2UsersUserIdInventoryAssetTypesItem]):
        filter_disapproved_assets (bool | Unset):  Default: False.
        show_approved_only (bool | Unset):  Default: False.
        limit (GetV2UsersUserIdInventoryLimit | Unset):  Default:
            GetV2UsersUserIdInventoryLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV2UsersUserIdInventorySortOrder | Unset):  Default:
            GetV2UsersUserIdInventorySortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiV2UserAssetItemModelV2
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        asset_types=asset_types,
        filter_disapproved_assets=filter_disapproved_assets,
        show_approved_only=show_approved_only,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
    ).parsed


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/assets#inventory_get_v2_users__userId__inventory"
)
async def asyncio_detailed(
    user_id: int,
    *,
    client: AuthenticatedClient,
    asset_types: list[GetV2UsersUserIdInventoryAssetTypesItem],
    filter_disapproved_assets: bool | Unset = False,
    show_approved_only: bool | Unset = False,
    limit: GetV2UsersUserIdInventoryLimit | Unset = GetV2UsersUserIdInventoryLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV2UsersUserIdInventorySortOrder | Unset = GetV2UsersUserIdInventorySortOrder.ASC,
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiV2UserAssetItemModelV2]:
    """Get user's inventory by multiple Roblox.Platform.Assets.AssetType.

     GamePass and Badges not allowed.

    Args:
        user_id (int):
        asset_types (list[GetV2UsersUserIdInventoryAssetTypesItem]):
        filter_disapproved_assets (bool | Unset):  Default: False.
        show_approved_only (bool | Unset):  Default: False.
        limit (GetV2UsersUserIdInventoryLimit | Unset):  Default:
            GetV2UsersUserIdInventoryLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV2UsersUserIdInventorySortOrder | Unset):  Default:
            GetV2UsersUserIdInventorySortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiV2UserAssetItemModelV2]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        asset_types=asset_types,
        filter_disapproved_assets=filter_disapproved_assets,
        show_approved_only=show_approved_only,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/assets#inventory_get_v2_users__userId__inventory"
)
async def asyncio(
    user_id: int,
    *,
    client: AuthenticatedClient,
    asset_types: list[GetV2UsersUserIdInventoryAssetTypesItem],
    filter_disapproved_assets: bool | Unset = False,
    show_approved_only: bool | Unset = False,
    limit: GetV2UsersUserIdInventoryLimit | Unset = GetV2UsersUserIdInventoryLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV2UsersUserIdInventorySortOrder | Unset = GetV2UsersUserIdInventorySortOrder.ASC,
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiV2UserAssetItemModelV2 | None:
    """Get user's inventory by multiple Roblox.Platform.Assets.AssetType.

     GamePass and Badges not allowed.

    Args:
        user_id (int):
        asset_types (list[GetV2UsersUserIdInventoryAssetTypesItem]):
        filter_disapproved_assets (bool | Unset):  Default: False.
        show_approved_only (bool | Unset):  Default: False.
        limit (GetV2UsersUserIdInventoryLimit | Unset):  Default:
            GetV2UsersUserIdInventoryLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV2UsersUserIdInventorySortOrder | Unset):  Default:
            GetV2UsersUserIdInventorySortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiV2UserAssetItemModelV2
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            asset_types=asset_types,
            filter_disapproved_assets=filter_disapproved_assets,
            show_approved_only=show_approved_only,
            limit=limit,
            cursor=cursor,
            sort_order=sort_order,
        )
    ).parsed
