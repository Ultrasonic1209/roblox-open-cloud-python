import sys
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset

if sys.version_info >= (3, 13):
    from warnings import deprecated
else:
    from typing_extensions import deprecated

from ...models.get_v2_assets_id_versions_limit import GetV2AssetsIdVersionsLimit
from ...models.get_v2_assets_id_versions_sort_order import GetV2AssetsIdVersionsSortOrder
from ...models.roblox_web_web_api_models_api_page_response_roblox_api_develop_asset_version import (
    RobloxWebWebAPIModelsApiPageResponseRobloxApiDevelopAssetVersion,
)


def _get_kwargs(
    id: int,
    *,
    limit: GetV2AssetsIdVersionsLimit | Unset = GetV2AssetsIdVersionsLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV2AssetsIdVersionsSortOrder | Unset = GetV2AssetsIdVersionsSortOrder.DESC,
    roblox_place_id: int,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Roblox-Place-Id"] = str(roblox_place_id)

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
        "url": "https://develop.roblox.com/v2/assets/{id}/versions".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
        "extensions": {
            "openapi-extensions": {
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
                "x-roblox-recommended-alternatives": [
                    {
                        "url": "https://apis.roblox.com/assets/v1/assets/{assetId}",
                        "httpMethod": "GET",
                        "documentationUrl": "https://create.roblox.com/docs/cloud/reference/features/assets#Assets_GetAsset",
                    }
                ],
            },
            "openapi-id": "get_v2_assets_id_versions",
        },
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> RobloxWebWebAPIModelsApiPageResponseRobloxApiDevelopAssetVersion | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIModelsApiPageResponseRobloxApiDevelopAssetVersion.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[RobloxWebWebAPIModelsApiPageResponseRobloxApiDevelopAssetVersion]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/assets#develop_get_v2_assets__id__versions"
)
def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    limit: GetV2AssetsIdVersionsLimit | Unset = GetV2AssetsIdVersionsLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV2AssetsIdVersionsSortOrder | Unset = GetV2AssetsIdVersionsSortOrder.DESC,
    roblox_place_id: int,
) -> Response[RobloxWebWebAPIModelsApiPageResponseRobloxApiDevelopAssetVersion]:
    """Retrieves asset information for the specified asset ID. The authenticated user must be able to
    manage the asset
    or granted by package permission.

     Use OpenCloud Assets API instead.

    Args:
        id (int):
        limit (GetV2AssetsIdVersionsLimit | Unset):  Default: GetV2AssetsIdVersionsLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV2AssetsIdVersionsSortOrder | Unset):  Default:
            GetV2AssetsIdVersionsSortOrder.DESC.
        roblox_place_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RobloxWebWebAPIModelsApiPageResponseRobloxApiDevelopAssetVersion]
    """

    kwargs = _get_kwargs(
        id=id,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
        roblox_place_id=roblox_place_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/assets#develop_get_v2_assets__id__versions"
)
def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    limit: GetV2AssetsIdVersionsLimit | Unset = GetV2AssetsIdVersionsLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV2AssetsIdVersionsSortOrder | Unset = GetV2AssetsIdVersionsSortOrder.DESC,
    roblox_place_id: int,
) -> RobloxWebWebAPIModelsApiPageResponseRobloxApiDevelopAssetVersion | None:
    """Retrieves asset information for the specified asset ID. The authenticated user must be able to
    manage the asset
    or granted by package permission.

     Use OpenCloud Assets API instead.

    Args:
        id (int):
        limit (GetV2AssetsIdVersionsLimit | Unset):  Default: GetV2AssetsIdVersionsLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV2AssetsIdVersionsSortOrder | Unset):  Default:
            GetV2AssetsIdVersionsSortOrder.DESC.
        roblox_place_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RobloxWebWebAPIModelsApiPageResponseRobloxApiDevelopAssetVersion
    """

    return sync_detailed(
        id=id,
        client=client,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
        roblox_place_id=roblox_place_id,
    ).parsed


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/assets#develop_get_v2_assets__id__versions"
)
async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    limit: GetV2AssetsIdVersionsLimit | Unset = GetV2AssetsIdVersionsLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV2AssetsIdVersionsSortOrder | Unset = GetV2AssetsIdVersionsSortOrder.DESC,
    roblox_place_id: int,
) -> Response[RobloxWebWebAPIModelsApiPageResponseRobloxApiDevelopAssetVersion]:
    """Retrieves asset information for the specified asset ID. The authenticated user must be able to
    manage the asset
    or granted by package permission.

     Use OpenCloud Assets API instead.

    Args:
        id (int):
        limit (GetV2AssetsIdVersionsLimit | Unset):  Default: GetV2AssetsIdVersionsLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV2AssetsIdVersionsSortOrder | Unset):  Default:
            GetV2AssetsIdVersionsSortOrder.DESC.
        roblox_place_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RobloxWebWebAPIModelsApiPageResponseRobloxApiDevelopAssetVersion]
    """

    kwargs = _get_kwargs(
        id=id,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
        roblox_place_id=roblox_place_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/assets#develop_get_v2_assets__id__versions"
)
async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    limit: GetV2AssetsIdVersionsLimit | Unset = GetV2AssetsIdVersionsLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV2AssetsIdVersionsSortOrder | Unset = GetV2AssetsIdVersionsSortOrder.DESC,
    roblox_place_id: int,
) -> RobloxWebWebAPIModelsApiPageResponseRobloxApiDevelopAssetVersion | None:
    """Retrieves asset information for the specified asset ID. The authenticated user must be able to
    manage the asset
    or granted by package permission.

     Use OpenCloud Assets API instead.

    Args:
        id (int):
        limit (GetV2AssetsIdVersionsLimit | Unset):  Default: GetV2AssetsIdVersionsLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV2AssetsIdVersionsSortOrder | Unset):  Default:
            GetV2AssetsIdVersionsSortOrder.DESC.
        roblox_place_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RobloxWebWebAPIModelsApiPageResponseRobloxApiDevelopAssetVersion
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            limit=limit,
            cursor=cursor,
            sort_order=sort_order,
            roblox_place_id=roblox_place_id,
        )
    ).parsed
