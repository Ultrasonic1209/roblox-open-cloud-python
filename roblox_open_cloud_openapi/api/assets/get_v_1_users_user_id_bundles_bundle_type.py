from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v1_users_user_id_bundles_bundle_type_bundle_type import GetV1UsersUserIdBundlesBundleTypeBundleType
from ...models.get_v1_users_user_id_bundles_bundle_type_sort_order import GetV1UsersUserIdBundlesBundleTypeSortOrder
from ...models.roblox_web_web_api_models_api_page_response_roblox_catalog_api_owned_bundle_model import (
    RobloxWebWebAPIModelsApiPageResponseRobloxCatalogApiOwnedBundleModel,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: int,
    bundle_type: GetV1UsersUserIdBundlesBundleTypeBundleType,
    *,
    cursor: str,
    limit: int | Unset = 10,
    sort_order: GetV1UsersUserIdBundlesBundleTypeSortOrder | Unset = GetV1UsersUserIdBundlesBundleTypeSortOrder.VALUE_2,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["cursor"] = cursor

    params["limit"] = limit

    json_sort_order: int | Unset = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value

    params["sortOrder"] = json_sort_order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://catalog.roblox.com/v1/users/{user_id}/bundles/{bundle_type}".format(
            user_id=quote(str(user_id), safe=""),
            bundle_type=quote(str(bundle_type), safe=""),
        ),
        "params": params,
        "extensions": {
            "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
            "openapi-id": "get_v1_users_userId_bundles_bundleType",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> RobloxWebWebAPIModelsApiPageResponseRobloxCatalogApiOwnedBundleModel | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIModelsApiPageResponseRobloxCatalogApiOwnedBundleModel.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[RobloxWebWebAPIModelsApiPageResponseRobloxCatalogApiOwnedBundleModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: int,
    bundle_type: GetV1UsersUserIdBundlesBundleTypeBundleType,
    *,
    client: AuthenticatedClient,
    cursor: str,
    limit: int | Unset = 10,
    sort_order: GetV1UsersUserIdBundlesBundleTypeSortOrder | Unset = GetV1UsersUserIdBundlesBundleTypeSortOrder.VALUE_2,
) -> Response[RobloxWebWebAPIModelsApiPageResponseRobloxCatalogApiOwnedBundleModel]:
    """
    Args:
        user_id (int):
        bundle_type (GetV1UsersUserIdBundlesBundleTypeBundleType):
        cursor (str):
        limit (int | Unset):  Default: 10.
        sort_order (GetV1UsersUserIdBundlesBundleTypeSortOrder | Unset):  Default:
            GetV1UsersUserIdBundlesBundleTypeSortOrder.VALUE_2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RobloxWebWebAPIModelsApiPageResponseRobloxCatalogApiOwnedBundleModel]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        bundle_type=bundle_type,
        cursor=cursor,
        limit=limit,
        sort_order=sort_order,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: int,
    bundle_type: GetV1UsersUserIdBundlesBundleTypeBundleType,
    *,
    client: AuthenticatedClient,
    cursor: str,
    limit: int | Unset = 10,
    sort_order: GetV1UsersUserIdBundlesBundleTypeSortOrder | Unset = GetV1UsersUserIdBundlesBundleTypeSortOrder.VALUE_2,
) -> RobloxWebWebAPIModelsApiPageResponseRobloxCatalogApiOwnedBundleModel | None:
    """
    Args:
        user_id (int):
        bundle_type (GetV1UsersUserIdBundlesBundleTypeBundleType):
        cursor (str):
        limit (int | Unset):  Default: 10.
        sort_order (GetV1UsersUserIdBundlesBundleTypeSortOrder | Unset):  Default:
            GetV1UsersUserIdBundlesBundleTypeSortOrder.VALUE_2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RobloxWebWebAPIModelsApiPageResponseRobloxCatalogApiOwnedBundleModel
    """

    return sync_detailed(
        user_id=user_id,
        bundle_type=bundle_type,
        client=client,
        cursor=cursor,
        limit=limit,
        sort_order=sort_order,
    ).parsed


async def asyncio_detailed(
    user_id: int,
    bundle_type: GetV1UsersUserIdBundlesBundleTypeBundleType,
    *,
    client: AuthenticatedClient,
    cursor: str,
    limit: int | Unset = 10,
    sort_order: GetV1UsersUserIdBundlesBundleTypeSortOrder | Unset = GetV1UsersUserIdBundlesBundleTypeSortOrder.VALUE_2,
) -> Response[RobloxWebWebAPIModelsApiPageResponseRobloxCatalogApiOwnedBundleModel]:
    """
    Args:
        user_id (int):
        bundle_type (GetV1UsersUserIdBundlesBundleTypeBundleType):
        cursor (str):
        limit (int | Unset):  Default: 10.
        sort_order (GetV1UsersUserIdBundlesBundleTypeSortOrder | Unset):  Default:
            GetV1UsersUserIdBundlesBundleTypeSortOrder.VALUE_2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RobloxWebWebAPIModelsApiPageResponseRobloxCatalogApiOwnedBundleModel]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        bundle_type=bundle_type,
        cursor=cursor,
        limit=limit,
        sort_order=sort_order,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: int,
    bundle_type: GetV1UsersUserIdBundlesBundleTypeBundleType,
    *,
    client: AuthenticatedClient,
    cursor: str,
    limit: int | Unset = 10,
    sort_order: GetV1UsersUserIdBundlesBundleTypeSortOrder | Unset = GetV1UsersUserIdBundlesBundleTypeSortOrder.VALUE_2,
) -> RobloxWebWebAPIModelsApiPageResponseRobloxCatalogApiOwnedBundleModel | None:
    """
    Args:
        user_id (int):
        bundle_type (GetV1UsersUserIdBundlesBundleTypeBundleType):
        cursor (str):
        limit (int | Unset):  Default: 10.
        sort_order (GetV1UsersUserIdBundlesBundleTypeSortOrder | Unset):  Default:
            GetV1UsersUserIdBundlesBundleTypeSortOrder.VALUE_2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RobloxWebWebAPIModelsApiPageResponseRobloxCatalogApiOwnedBundleModel
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            bundle_type=bundle_type,
            client=client,
            cursor=cursor,
            limit=limit,
            sort_order=sort_order,
        )
    ).parsed
