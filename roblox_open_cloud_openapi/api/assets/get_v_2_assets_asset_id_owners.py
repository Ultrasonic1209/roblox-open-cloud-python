from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v2_assets_asset_id_owners_limit import GetV2AssetsAssetIdOwnersLimit
from ...models.get_v2_assets_asset_id_owners_sort_order import GetV2AssetsAssetIdOwnersSortOrder
from ...models.roblox_web_web_api_models_api_page_response_roblox_inventory_api_v2_asset_owner_response import (
    RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiV2AssetOwnerResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    asset_id: int,
    *,
    limit: GetV2AssetsAssetIdOwnersLimit | Unset = GetV2AssetsAssetIdOwnersLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV2AssetsAssetIdOwnersSortOrder | Unset = GetV2AssetsAssetIdOwnersSortOrder.ASC,
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
        "url": "/v2/assets/{asset_id}/owners".format(
            asset_id=quote(str(asset_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiV2AssetOwnerResponse | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiV2AssetOwnerResponse.from_dict(
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
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiV2AssetOwnerResponse]:
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
    limit: GetV2AssetsAssetIdOwnersLimit | Unset = GetV2AssetsAssetIdOwnersLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV2AssetsAssetIdOwnersSortOrder | Unset = GetV2AssetsAssetIdOwnersSortOrder.ASC,
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiV2AssetOwnerResponse]:
    """Gets a list of owners of an asset.

    Args:
        asset_id (int):
        limit (GetV2AssetsAssetIdOwnersLimit | Unset):  Default:
            GetV2AssetsAssetIdOwnersLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV2AssetsAssetIdOwnersSortOrder | Unset):  Default:
            GetV2AssetsAssetIdOwnersSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiV2AssetOwnerResponse]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: int,
    *,
    client: AuthenticatedClient,
    limit: GetV2AssetsAssetIdOwnersLimit | Unset = GetV2AssetsAssetIdOwnersLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV2AssetsAssetIdOwnersSortOrder | Unset = GetV2AssetsAssetIdOwnersSortOrder.ASC,
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiV2AssetOwnerResponse | None:
    """Gets a list of owners of an asset.

    Args:
        asset_id (int):
        limit (GetV2AssetsAssetIdOwnersLimit | Unset):  Default:
            GetV2AssetsAssetIdOwnersLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV2AssetsAssetIdOwnersSortOrder | Unset):  Default:
            GetV2AssetsAssetIdOwnersSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiV2AssetOwnerResponse
    """

    return sync_detailed(
        asset_id=asset_id,
        client=client,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
    ).parsed


async def asyncio_detailed(
    asset_id: int,
    *,
    client: AuthenticatedClient,
    limit: GetV2AssetsAssetIdOwnersLimit | Unset = GetV2AssetsAssetIdOwnersLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV2AssetsAssetIdOwnersSortOrder | Unset = GetV2AssetsAssetIdOwnersSortOrder.ASC,
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiV2AssetOwnerResponse]:
    """Gets a list of owners of an asset.

    Args:
        asset_id (int):
        limit (GetV2AssetsAssetIdOwnersLimit | Unset):  Default:
            GetV2AssetsAssetIdOwnersLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV2AssetsAssetIdOwnersSortOrder | Unset):  Default:
            GetV2AssetsAssetIdOwnersSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiV2AssetOwnerResponse]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: int,
    *,
    client: AuthenticatedClient,
    limit: GetV2AssetsAssetIdOwnersLimit | Unset = GetV2AssetsAssetIdOwnersLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV2AssetsAssetIdOwnersSortOrder | Unset = GetV2AssetsAssetIdOwnersSortOrder.ASC,
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiV2AssetOwnerResponse | None:
    """Gets a list of owners of an asset.

    Args:
        asset_id (int):
        limit (GetV2AssetsAssetIdOwnersLimit | Unset):  Default:
            GetV2AssetsAssetIdOwnersLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV2AssetsAssetIdOwnersSortOrder | Unset):  Default:
            GetV2AssetsAssetIdOwnersSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiV2AssetOwnerResponse
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            client=client,
            limit=limit,
            cursor=cursor,
            sort_order=sort_order,
        )
    ).parsed
