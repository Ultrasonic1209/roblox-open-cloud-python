from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v1_users_user_id_bundles_sort_order import GetV1UsersUserIdBundlesSortOrder
from ...models.roblox_web_web_api_models_api_page_response_roblox_catalog_api_owned_bundle_model import (
    RobloxWebWebAPIModelsApiPageResponseRobloxCatalogApiOwnedBundleModel,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: int,
    *,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 10,
    sort_order: GetV1UsersUserIdBundlesSortOrder | Unset = GetV1UsersUserIdBundlesSortOrder.VALUE_2,
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
        "url": "/v1/users/{user_id}/bundles".format(
            user_id=quote(str(user_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxCatalogApiOwnedBundleModel | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIModelsApiPageResponseRobloxCatalogApiOwnedBundleModel.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxCatalogApiOwnedBundleModel]:
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
    cursor: str | Unset = UNSET,
    limit: int | Unset = 10,
    sort_order: GetV1UsersUserIdBundlesSortOrder | Unset = GetV1UsersUserIdBundlesSortOrder.VALUE_2,
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxCatalogApiOwnedBundleModel]:
    """Lists the bundles owned by a given user.

    Args:
        user_id (int):
        cursor (str | Unset):
        limit (int | Unset):  Default: 10.
        sort_order (GetV1UsersUserIdBundlesSortOrder | Unset):  Default:
            GetV1UsersUserIdBundlesSortOrder.VALUE_2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxCatalogApiOwnedBundleModel]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        cursor=cursor,
        limit=limit,
        sort_order=sort_order,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: int,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 10,
    sort_order: GetV1UsersUserIdBundlesSortOrder | Unset = GetV1UsersUserIdBundlesSortOrder.VALUE_2,
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxCatalogApiOwnedBundleModel | None:
    """Lists the bundles owned by a given user.

    Args:
        user_id (int):
        cursor (str | Unset):
        limit (int | Unset):  Default: 10.
        sort_order (GetV1UsersUserIdBundlesSortOrder | Unset):  Default:
            GetV1UsersUserIdBundlesSortOrder.VALUE_2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiPageResponseRobloxCatalogApiOwnedBundleModel
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        cursor=cursor,
        limit=limit,
        sort_order=sort_order,
    ).parsed


async def asyncio_detailed(
    user_id: int,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 10,
    sort_order: GetV1UsersUserIdBundlesSortOrder | Unset = GetV1UsersUserIdBundlesSortOrder.VALUE_2,
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxCatalogApiOwnedBundleModel]:
    """Lists the bundles owned by a given user.

    Args:
        user_id (int):
        cursor (str | Unset):
        limit (int | Unset):  Default: 10.
        sort_order (GetV1UsersUserIdBundlesSortOrder | Unset):  Default:
            GetV1UsersUserIdBundlesSortOrder.VALUE_2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxCatalogApiOwnedBundleModel]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        cursor=cursor,
        limit=limit,
        sort_order=sort_order,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: int,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 10,
    sort_order: GetV1UsersUserIdBundlesSortOrder | Unset = GetV1UsersUserIdBundlesSortOrder.VALUE_2,
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxCatalogApiOwnedBundleModel | None:
    """Lists the bundles owned by a given user.

    Args:
        user_id (int):
        cursor (str | Unset):
        limit (int | Unset):  Default: 10.
        sort_order (GetV1UsersUserIdBundlesSortOrder | Unset):  Default:
            GetV1UsersUserIdBundlesSortOrder.VALUE_2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiPageResponseRobloxCatalogApiOwnedBundleModel
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            cursor=cursor,
            limit=limit,
            sort_order=sort_order,
        )
    ).parsed
