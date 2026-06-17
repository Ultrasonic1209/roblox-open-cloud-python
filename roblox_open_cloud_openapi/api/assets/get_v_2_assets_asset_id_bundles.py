from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v2_assets_asset_id_bundles_limit import GetV2AssetsAssetIdBundlesLimit
from ...models.get_v2_assets_asset_id_bundles_sort_order import GetV2AssetsAssetIdBundlesSortOrder
from ...models.roblox_web_web_api_models_api_page_response_roblox_catalog_api_catalog_search_detailed_response_item import (
    RobloxWebWebAPIModelsApiPageResponseRobloxCatalogApiCatalogSearchDetailedResponseItem,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    asset_id: int,
    *,
    limit: GetV2AssetsAssetIdBundlesLimit | Unset = GetV2AssetsAssetIdBundlesLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV2AssetsAssetIdBundlesSortOrder | Unset = GetV2AssetsAssetIdBundlesSortOrder.ASC,
    roblox_place_id: int,
    roblox_game_id: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Roblox-Place-Id"] = str(roblox_place_id)

    headers["Roblox-Game-Id"] = roblox_game_id

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
        "url": "https://catalog.roblox.com/v2/assets/{asset_id}/bundles".format(
            asset_id=quote(str(asset_id), safe=""),
        ),
        "params": params,
        "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
        "openapi-id": "get_v2_assets_assetId_bundles",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxCatalogApiCatalogSearchDetailedResponseItem | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIModelsApiPageResponseRobloxCatalogApiCatalogSearchDetailedResponseItem.from_dict(
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
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxCatalogApiCatalogSearchDetailedResponseItem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    asset_id: int,
    *,
    client: AuthenticatedClient,
    limit: GetV2AssetsAssetIdBundlesLimit | Unset = GetV2AssetsAssetIdBundlesLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV2AssetsAssetIdBundlesSortOrder | Unset = GetV2AssetsAssetIdBundlesSortOrder.ASC,
    roblox_place_id: int,
    roblox_game_id: str,
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxCatalogApiCatalogSearchDetailedResponseItem]:
    """Lists bundles that contain the given asset (hydrated search-detail shape for marketplace).

    Args:
        asset_id (int):
        limit (GetV2AssetsAssetIdBundlesLimit | Unset):  Default:
            GetV2AssetsAssetIdBundlesLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV2AssetsAssetIdBundlesSortOrder | Unset):  Default:
            GetV2AssetsAssetIdBundlesSortOrder.ASC.
        roblox_place_id (int):
        roblox_game_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxCatalogApiCatalogSearchDetailedResponseItem]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
        roblox_place_id=roblox_place_id,
        roblox_game_id=roblox_game_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: int,
    *,
    client: AuthenticatedClient,
    limit: GetV2AssetsAssetIdBundlesLimit | Unset = GetV2AssetsAssetIdBundlesLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV2AssetsAssetIdBundlesSortOrder | Unset = GetV2AssetsAssetIdBundlesSortOrder.ASC,
    roblox_place_id: int,
    roblox_game_id: str,
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxCatalogApiCatalogSearchDetailedResponseItem | None:
    """Lists bundles that contain the given asset (hydrated search-detail shape for marketplace).

    Args:
        asset_id (int):
        limit (GetV2AssetsAssetIdBundlesLimit | Unset):  Default:
            GetV2AssetsAssetIdBundlesLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV2AssetsAssetIdBundlesSortOrder | Unset):  Default:
            GetV2AssetsAssetIdBundlesSortOrder.ASC.
        roblox_place_id (int):
        roblox_game_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiPageResponseRobloxCatalogApiCatalogSearchDetailedResponseItem
    """

    return sync_detailed(
        asset_id=asset_id,
        client=client,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
        roblox_place_id=roblox_place_id,
        roblox_game_id=roblox_game_id,
    ).parsed


async def asyncio_detailed(
    asset_id: int,
    *,
    client: AuthenticatedClient,
    limit: GetV2AssetsAssetIdBundlesLimit | Unset = GetV2AssetsAssetIdBundlesLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV2AssetsAssetIdBundlesSortOrder | Unset = GetV2AssetsAssetIdBundlesSortOrder.ASC,
    roblox_place_id: int,
    roblox_game_id: str,
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxCatalogApiCatalogSearchDetailedResponseItem]:
    """Lists bundles that contain the given asset (hydrated search-detail shape for marketplace).

    Args:
        asset_id (int):
        limit (GetV2AssetsAssetIdBundlesLimit | Unset):  Default:
            GetV2AssetsAssetIdBundlesLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV2AssetsAssetIdBundlesSortOrder | Unset):  Default:
            GetV2AssetsAssetIdBundlesSortOrder.ASC.
        roblox_place_id (int):
        roblox_game_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxCatalogApiCatalogSearchDetailedResponseItem]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
        roblox_place_id=roblox_place_id,
        roblox_game_id=roblox_game_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: int,
    *,
    client: AuthenticatedClient,
    limit: GetV2AssetsAssetIdBundlesLimit | Unset = GetV2AssetsAssetIdBundlesLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV2AssetsAssetIdBundlesSortOrder | Unset = GetV2AssetsAssetIdBundlesSortOrder.ASC,
    roblox_place_id: int,
    roblox_game_id: str,
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxCatalogApiCatalogSearchDetailedResponseItem | None:
    """Lists bundles that contain the given asset (hydrated search-detail shape for marketplace).

    Args:
        asset_id (int):
        limit (GetV2AssetsAssetIdBundlesLimit | Unset):  Default:
            GetV2AssetsAssetIdBundlesLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV2AssetsAssetIdBundlesSortOrder | Unset):  Default:
            GetV2AssetsAssetIdBundlesSortOrder.ASC.
        roblox_place_id (int):
        roblox_game_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiPageResponseRobloxCatalogApiCatalogSearchDetailedResponseItem
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            client=client,
            limit=limit,
            cursor=cursor,
            sort_order=sort_order,
            roblox_place_id=roblox_place_id,
            roblox_game_id=roblox_game_id,
        )
    ).parsed
