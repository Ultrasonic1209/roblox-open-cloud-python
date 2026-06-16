from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v1_favorites_users_user_id_favorites_asset_type_id_assets_limit import (
    GetV1FavoritesUsersUserIdFavoritesAssetTypeIdAssetsLimit,
)
from ...models.get_v1_favorites_users_user_id_favorites_asset_type_id_assets_sort_order import (
    GetV1FavoritesUsersUserIdFavoritesAssetTypeIdAssetsSortOrder,
)
from ...models.roblox_web_web_api_models_api_page_response_roblox_catalog_api_catalog_search_detailed_response_item import (
    RobloxWebWebAPIModelsApiPageResponseRobloxCatalogApiCatalogSearchDetailedResponseItem,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: int,
    asset_type_id: int,
    *,
    limit: GetV1FavoritesUsersUserIdFavoritesAssetTypeIdAssetsLimit
    | Unset = GetV1FavoritesUsersUserIdFavoritesAssetTypeIdAssetsLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1FavoritesUsersUserIdFavoritesAssetTypeIdAssetsSortOrder
    | Unset = GetV1FavoritesUsersUserIdFavoritesAssetTypeIdAssetsSortOrder.DESC,
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
        "url": "/v1/favorites/users/{user_id}/favorites/{asset_type_id}/assets".format(
            user_id=quote(str(user_id), safe=""),
            asset_type_id=quote(str(asset_type_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxCatalogApiCatalogSearchDetailedResponseItem | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIModelsApiPageResponseRobloxCatalogApiCatalogSearchDetailedResponseItem.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxCatalogApiCatalogSearchDetailedResponseItem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: int,
    asset_type_id: int,
    *,
    client: AuthenticatedClient,
    limit: GetV1FavoritesUsersUserIdFavoritesAssetTypeIdAssetsLimit
    | Unset = GetV1FavoritesUsersUserIdFavoritesAssetTypeIdAssetsLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1FavoritesUsersUserIdFavoritesAssetTypeIdAssetsSortOrder
    | Unset = GetV1FavoritesUsersUserIdFavoritesAssetTypeIdAssetsSortOrder.DESC,
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxCatalogApiCatalogSearchDetailedResponseItem]:
    """Lists the marketplace assets favorited by a given user with the given assetTypeId.

    Args:
        user_id (int):
        asset_type_id (int):
        limit (GetV1FavoritesUsersUserIdFavoritesAssetTypeIdAssetsLimit | Unset):  Default:
            GetV1FavoritesUsersUserIdFavoritesAssetTypeIdAssetsLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV1FavoritesUsersUserIdFavoritesAssetTypeIdAssetsSortOrder | Unset):
            Default: GetV1FavoritesUsersUserIdFavoritesAssetTypeIdAssetsSortOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxCatalogApiCatalogSearchDetailedResponseItem]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        asset_type_id=asset_type_id,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: int,
    asset_type_id: int,
    *,
    client: AuthenticatedClient,
    limit: GetV1FavoritesUsersUserIdFavoritesAssetTypeIdAssetsLimit
    | Unset = GetV1FavoritesUsersUserIdFavoritesAssetTypeIdAssetsLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1FavoritesUsersUserIdFavoritesAssetTypeIdAssetsSortOrder
    | Unset = GetV1FavoritesUsersUserIdFavoritesAssetTypeIdAssetsSortOrder.DESC,
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxCatalogApiCatalogSearchDetailedResponseItem | None:
    """Lists the marketplace assets favorited by a given user with the given assetTypeId.

    Args:
        user_id (int):
        asset_type_id (int):
        limit (GetV1FavoritesUsersUserIdFavoritesAssetTypeIdAssetsLimit | Unset):  Default:
            GetV1FavoritesUsersUserIdFavoritesAssetTypeIdAssetsLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV1FavoritesUsersUserIdFavoritesAssetTypeIdAssetsSortOrder | Unset):
            Default: GetV1FavoritesUsersUserIdFavoritesAssetTypeIdAssetsSortOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiPageResponseRobloxCatalogApiCatalogSearchDetailedResponseItem
    """

    return sync_detailed(
        user_id=user_id,
        asset_type_id=asset_type_id,
        client=client,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
    ).parsed


async def asyncio_detailed(
    user_id: int,
    asset_type_id: int,
    *,
    client: AuthenticatedClient,
    limit: GetV1FavoritesUsersUserIdFavoritesAssetTypeIdAssetsLimit
    | Unset = GetV1FavoritesUsersUserIdFavoritesAssetTypeIdAssetsLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1FavoritesUsersUserIdFavoritesAssetTypeIdAssetsSortOrder
    | Unset = GetV1FavoritesUsersUserIdFavoritesAssetTypeIdAssetsSortOrder.DESC,
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxCatalogApiCatalogSearchDetailedResponseItem]:
    """Lists the marketplace assets favorited by a given user with the given assetTypeId.

    Args:
        user_id (int):
        asset_type_id (int):
        limit (GetV1FavoritesUsersUserIdFavoritesAssetTypeIdAssetsLimit | Unset):  Default:
            GetV1FavoritesUsersUserIdFavoritesAssetTypeIdAssetsLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV1FavoritesUsersUserIdFavoritesAssetTypeIdAssetsSortOrder | Unset):
            Default: GetV1FavoritesUsersUserIdFavoritesAssetTypeIdAssetsSortOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxCatalogApiCatalogSearchDetailedResponseItem]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        asset_type_id=asset_type_id,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: int,
    asset_type_id: int,
    *,
    client: AuthenticatedClient,
    limit: GetV1FavoritesUsersUserIdFavoritesAssetTypeIdAssetsLimit
    | Unset = GetV1FavoritesUsersUserIdFavoritesAssetTypeIdAssetsLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1FavoritesUsersUserIdFavoritesAssetTypeIdAssetsSortOrder
    | Unset = GetV1FavoritesUsersUserIdFavoritesAssetTypeIdAssetsSortOrder.DESC,
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxCatalogApiCatalogSearchDetailedResponseItem | None:
    """Lists the marketplace assets favorited by a given user with the given assetTypeId.

    Args:
        user_id (int):
        asset_type_id (int):
        limit (GetV1FavoritesUsersUserIdFavoritesAssetTypeIdAssetsLimit | Unset):  Default:
            GetV1FavoritesUsersUserIdFavoritesAssetTypeIdAssetsLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV1FavoritesUsersUserIdFavoritesAssetTypeIdAssetsSortOrder | Unset):
            Default: GetV1FavoritesUsersUserIdFavoritesAssetTypeIdAssetsSortOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiPageResponseRobloxCatalogApiCatalogSearchDetailedResponseItem
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
