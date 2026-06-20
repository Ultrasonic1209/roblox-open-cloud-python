from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v1_users_user_id_assets_collectibles_asset_type import GetV1UsersUserIdAssetsCollectiblesAssetType
from ...models.get_v1_users_user_id_assets_collectibles_limit import GetV1UsersUserIdAssetsCollectiblesLimit
from ...models.get_v1_users_user_id_assets_collectibles_sort_order import GetV1UsersUserIdAssetsCollectiblesSortOrder
from ...models.roblox_web_web_api_models_api_page_response_roblox_inventory_api_models_collectible_user_asset_model import (
    RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiModelsCollectibleUserAssetModel,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: int,
    *,
    asset_type: GetV1UsersUserIdAssetsCollectiblesAssetType | Unset = UNSET,
    limit: GetV1UsersUserIdAssetsCollectiblesLimit | Unset = GetV1UsersUserIdAssetsCollectiblesLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1UsersUserIdAssetsCollectiblesSortOrder | Unset = GetV1UsersUserIdAssetsCollectiblesSortOrder.ASC,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_asset_type: int | Unset = UNSET
    if not isinstance(asset_type, Unset):
        json_asset_type = asset_type.value

    params["assetType"] = json_asset_type

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
        "url": "https://inventory.roblox.com/v1/users/{user_id}/assets/collectibles".format(
            user_id=quote(str(user_id), safe=""),
        ),
        "params": params,
        "extensions": {
            "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
            "openapi-id": "get_v1_users_userId_assets_collectibles",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiModelsCollectibleUserAssetModel | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiModelsCollectibleUserAssetModel.from_dict(
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
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiModelsCollectibleUserAssetModel]:
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
    asset_type: GetV1UsersUserIdAssetsCollectiblesAssetType | Unset = UNSET,
    limit: GetV1UsersUserIdAssetsCollectiblesLimit | Unset = GetV1UsersUserIdAssetsCollectiblesLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1UsersUserIdAssetsCollectiblesSortOrder | Unset = GetV1UsersUserIdAssetsCollectiblesSortOrder.ASC,
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiModelsCollectibleUserAssetModel]:
    """Gets all collectible assets owned by the specified user.

    Args:
        user_id (int):
        asset_type (GetV1UsersUserIdAssetsCollectiblesAssetType | Unset):
        limit (GetV1UsersUserIdAssetsCollectiblesLimit | Unset):  Default:
            GetV1UsersUserIdAssetsCollectiblesLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV1UsersUserIdAssetsCollectiblesSortOrder | Unset):  Default:
            GetV1UsersUserIdAssetsCollectiblesSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiModelsCollectibleUserAssetModel]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        asset_type=asset_type,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: int,
    *,
    client: AuthenticatedClient,
    asset_type: GetV1UsersUserIdAssetsCollectiblesAssetType | Unset = UNSET,
    limit: GetV1UsersUserIdAssetsCollectiblesLimit | Unset = GetV1UsersUserIdAssetsCollectiblesLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1UsersUserIdAssetsCollectiblesSortOrder | Unset = GetV1UsersUserIdAssetsCollectiblesSortOrder.ASC,
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiModelsCollectibleUserAssetModel | None:
    """Gets all collectible assets owned by the specified user.

    Args:
        user_id (int):
        asset_type (GetV1UsersUserIdAssetsCollectiblesAssetType | Unset):
        limit (GetV1UsersUserIdAssetsCollectiblesLimit | Unset):  Default:
            GetV1UsersUserIdAssetsCollectiblesLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV1UsersUserIdAssetsCollectiblesSortOrder | Unset):  Default:
            GetV1UsersUserIdAssetsCollectiblesSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiModelsCollectibleUserAssetModel
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        asset_type=asset_type,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
    ).parsed


async def asyncio_detailed(
    user_id: int,
    *,
    client: AuthenticatedClient,
    asset_type: GetV1UsersUserIdAssetsCollectiblesAssetType | Unset = UNSET,
    limit: GetV1UsersUserIdAssetsCollectiblesLimit | Unset = GetV1UsersUserIdAssetsCollectiblesLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1UsersUserIdAssetsCollectiblesSortOrder | Unset = GetV1UsersUserIdAssetsCollectiblesSortOrder.ASC,
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiModelsCollectibleUserAssetModel]:
    """Gets all collectible assets owned by the specified user.

    Args:
        user_id (int):
        asset_type (GetV1UsersUserIdAssetsCollectiblesAssetType | Unset):
        limit (GetV1UsersUserIdAssetsCollectiblesLimit | Unset):  Default:
            GetV1UsersUserIdAssetsCollectiblesLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV1UsersUserIdAssetsCollectiblesSortOrder | Unset):  Default:
            GetV1UsersUserIdAssetsCollectiblesSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiModelsCollectibleUserAssetModel]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        asset_type=asset_type,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: int,
    *,
    client: AuthenticatedClient,
    asset_type: GetV1UsersUserIdAssetsCollectiblesAssetType | Unset = UNSET,
    limit: GetV1UsersUserIdAssetsCollectiblesLimit | Unset = GetV1UsersUserIdAssetsCollectiblesLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1UsersUserIdAssetsCollectiblesSortOrder | Unset = GetV1UsersUserIdAssetsCollectiblesSortOrder.ASC,
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiModelsCollectibleUserAssetModel | None:
    """Gets all collectible assets owned by the specified user.

    Args:
        user_id (int):
        asset_type (GetV1UsersUserIdAssetsCollectiblesAssetType | Unset):
        limit (GetV1UsersUserIdAssetsCollectiblesLimit | Unset):  Default:
            GetV1UsersUserIdAssetsCollectiblesLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV1UsersUserIdAssetsCollectiblesSortOrder | Unset):  Default:
            GetV1UsersUserIdAssetsCollectiblesSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiModelsCollectibleUserAssetModel
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            asset_type=asset_type,
            limit=limit,
            cursor=cursor,
            sort_order=sort_order,
        )
    ).parsed
