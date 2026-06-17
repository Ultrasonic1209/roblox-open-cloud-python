from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v1_assets_asset_id_bundles_limit import GetV1AssetsAssetIdBundlesLimit
from ...models.get_v1_assets_asset_id_bundles_sort_order import GetV1AssetsAssetIdBundlesSortOrder
from ...models.roblox_web_web_api_models_api_page_response_roblox_catalog_api_bundle_details_model import (
    RobloxWebWebAPIModelsApiPageResponseRobloxCatalogApiBundleDetailsModel,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    asset_id: int,
    *,
    limit: GetV1AssetsAssetIdBundlesLimit | Unset = GetV1AssetsAssetIdBundlesLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1AssetsAssetIdBundlesSortOrder | Unset = GetV1AssetsAssetIdBundlesSortOrder.ASC,
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
        "url": "https://catalog.roblox.com/v1/assets/{asset_id}/bundles".format(
            asset_id=quote(str(asset_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxCatalogApiBundleDetailsModel | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIModelsApiPageResponseRobloxCatalogApiBundleDetailsModel.from_dict(response.json())

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
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxCatalogApiBundleDetailsModel]:
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
    limit: GetV1AssetsAssetIdBundlesLimit | Unset = GetV1AssetsAssetIdBundlesLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1AssetsAssetIdBundlesSortOrder | Unset = GetV1AssetsAssetIdBundlesSortOrder.ASC,
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxCatalogApiBundleDetailsModel]:
    """Lists the bundles a particular asset belongs to. Use the Id of the last bundle in the response to
    get the next page.

    Args:
        asset_id (int):
        limit (GetV1AssetsAssetIdBundlesLimit | Unset):  Default:
            GetV1AssetsAssetIdBundlesLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV1AssetsAssetIdBundlesSortOrder | Unset):  Default:
            GetV1AssetsAssetIdBundlesSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxCatalogApiBundleDetailsModel]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: int,
    *,
    client: AuthenticatedClient,
    limit: GetV1AssetsAssetIdBundlesLimit | Unset = GetV1AssetsAssetIdBundlesLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1AssetsAssetIdBundlesSortOrder | Unset = GetV1AssetsAssetIdBundlesSortOrder.ASC,
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxCatalogApiBundleDetailsModel | None:
    """Lists the bundles a particular asset belongs to. Use the Id of the last bundle in the response to
    get the next page.

    Args:
        asset_id (int):
        limit (GetV1AssetsAssetIdBundlesLimit | Unset):  Default:
            GetV1AssetsAssetIdBundlesLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV1AssetsAssetIdBundlesSortOrder | Unset):  Default:
            GetV1AssetsAssetIdBundlesSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiPageResponseRobloxCatalogApiBundleDetailsModel
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
    limit: GetV1AssetsAssetIdBundlesLimit | Unset = GetV1AssetsAssetIdBundlesLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1AssetsAssetIdBundlesSortOrder | Unset = GetV1AssetsAssetIdBundlesSortOrder.ASC,
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxCatalogApiBundleDetailsModel]:
    """Lists the bundles a particular asset belongs to. Use the Id of the last bundle in the response to
    get the next page.

    Args:
        asset_id (int):
        limit (GetV1AssetsAssetIdBundlesLimit | Unset):  Default:
            GetV1AssetsAssetIdBundlesLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV1AssetsAssetIdBundlesSortOrder | Unset):  Default:
            GetV1AssetsAssetIdBundlesSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxCatalogApiBundleDetailsModel]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: int,
    *,
    client: AuthenticatedClient,
    limit: GetV1AssetsAssetIdBundlesLimit | Unset = GetV1AssetsAssetIdBundlesLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1AssetsAssetIdBundlesSortOrder | Unset = GetV1AssetsAssetIdBundlesSortOrder.ASC,
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxCatalogApiBundleDetailsModel | None:
    """Lists the bundles a particular asset belongs to. Use the Id of the last bundle in the response to
    get the next page.

    Args:
        asset_id (int):
        limit (GetV1AssetsAssetIdBundlesLimit | Unset):  Default:
            GetV1AssetsAssetIdBundlesLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV1AssetsAssetIdBundlesSortOrder | Unset):  Default:
            GetV1AssetsAssetIdBundlesSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiPageResponseRobloxCatalogApiBundleDetailsModel
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
