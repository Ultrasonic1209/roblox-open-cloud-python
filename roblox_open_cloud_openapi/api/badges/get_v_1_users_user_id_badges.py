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

from ...models.get_v1_users_user_id_badges_limit import GetV1UsersUserIdBadgesLimit
from ...models.get_v1_users_user_id_badges_sort_order import GetV1UsersUserIdBadgesSortOrder
from ...models.roblox_web_web_api_models_api_page_response_roblox_badges_api_get_badges_by_user_response import (
    RobloxWebWebAPIModelsApiPageResponseRobloxBadgesApiGetBadgesByUserResponse,
)


def _get_kwargs(
    user_id: int,
    *,
    limit: GetV1UsersUserIdBadgesLimit | Unset = GetV1UsersUserIdBadgesLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1UsersUserIdBadgesSortOrder | Unset = GetV1UsersUserIdBadgesSortOrder.ASC,
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
        "url": "https://badges.roblox.com/v1/users/{user_id}/badges".format(
            user_id=quote(str(user_id), safe=""),
        ),
        "params": params,
        "extensions": {
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
            "openapi-id": "get_v1_users_userId_badges",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxBadgesApiGetBadgesByUserResponse | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIModelsApiPageResponseRobloxBadgesApiGetBadgesByUserResponse.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxBadgesApiGetBadgesByUserResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/badges#badges_get_v1_users__userId__badges"
)
def sync_detailed(
    user_id: int,
    *,
    client: AuthenticatedClient,
    limit: GetV1UsersUserIdBadgesLimit | Unset = GetV1UsersUserIdBadgesLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1UsersUserIdBadgesSortOrder | Unset = GetV1UsersUserIdBadgesSortOrder.ASC,
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxBadgesApiGetBadgesByUserResponse]:
    """Gets a list of badges a user has been awarded.

    Args:
        user_id (int):
        limit (GetV1UsersUserIdBadgesLimit | Unset):  Default:
            GetV1UsersUserIdBadgesLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV1UsersUserIdBadgesSortOrder | Unset):  Default:
            GetV1UsersUserIdBadgesSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxBadgesApiGetBadgesByUserResponse]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/badges#badges_get_v1_users__userId__badges"
)
def sync(
    user_id: int,
    *,
    client: AuthenticatedClient,
    limit: GetV1UsersUserIdBadgesLimit | Unset = GetV1UsersUserIdBadgesLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1UsersUserIdBadgesSortOrder | Unset = GetV1UsersUserIdBadgesSortOrder.ASC,
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxBadgesApiGetBadgesByUserResponse | None:
    """Gets a list of badges a user has been awarded.

    Args:
        user_id (int):
        limit (GetV1UsersUserIdBadgesLimit | Unset):  Default:
            GetV1UsersUserIdBadgesLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV1UsersUserIdBadgesSortOrder | Unset):  Default:
            GetV1UsersUserIdBadgesSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiPageResponseRobloxBadgesApiGetBadgesByUserResponse
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
    ).parsed


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/badges#badges_get_v1_users__userId__badges"
)
async def asyncio_detailed(
    user_id: int,
    *,
    client: AuthenticatedClient,
    limit: GetV1UsersUserIdBadgesLimit | Unset = GetV1UsersUserIdBadgesLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1UsersUserIdBadgesSortOrder | Unset = GetV1UsersUserIdBadgesSortOrder.ASC,
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxBadgesApiGetBadgesByUserResponse]:
    """Gets a list of badges a user has been awarded.

    Args:
        user_id (int):
        limit (GetV1UsersUserIdBadgesLimit | Unset):  Default:
            GetV1UsersUserIdBadgesLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV1UsersUserIdBadgesSortOrder | Unset):  Default:
            GetV1UsersUserIdBadgesSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxBadgesApiGetBadgesByUserResponse]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/badges#badges_get_v1_users__userId__badges"
)
async def asyncio(
    user_id: int,
    *,
    client: AuthenticatedClient,
    limit: GetV1UsersUserIdBadgesLimit | Unset = GetV1UsersUserIdBadgesLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1UsersUserIdBadgesSortOrder | Unset = GetV1UsersUserIdBadgesSortOrder.ASC,
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxBadgesApiGetBadgesByUserResponse | None:
    """Gets a list of badges a user has been awarded.

    Args:
        user_id (int):
        limit (GetV1UsersUserIdBadgesLimit | Unset):  Default:
            GetV1UsersUserIdBadgesLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV1UsersUserIdBadgesSortOrder | Unset):  Default:
            GetV1UsersUserIdBadgesSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiPageResponseRobloxBadgesApiGetBadgesByUserResponse
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            limit=limit,
            cursor=cursor,
            sort_order=sort_order,
        )
    ).parsed
