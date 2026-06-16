from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v1_groups_group_id_users_limit import GetV1GroupsGroupIdUsersLimit
from ...models.get_v1_groups_group_id_users_sort_order import GetV1GroupsGroupIdUsersSortOrder
from ...models.roblox_web_web_api_models_api_page_response_roblox_groups_api_user_group_role_response import (
    RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiUserGroupRoleResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    group_id: int,
    *,
    limit: GetV1GroupsGroupIdUsersLimit | Unset = GetV1GroupsGroupIdUsersLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1GroupsGroupIdUsersSortOrder | Unset = GetV1GroupsGroupIdUsersSortOrder.ASC,
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
        "url": "/v1/groups/{group_id}/users".format(
            group_id=quote(str(group_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiUserGroupRoleResponse | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiUserGroupRoleResponse.from_dict(
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
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiUserGroupRoleResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    group_id: int,
    *,
    client: AuthenticatedClient,
    limit: GetV1GroupsGroupIdUsersLimit | Unset = GetV1GroupsGroupIdUsersLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1GroupsGroupIdUsersSortOrder | Unset = GetV1GroupsGroupIdUsersSortOrder.ASC,
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiUserGroupRoleResponse]:
    """Gets a list of users in a group.

    Args:
        group_id (int):
        limit (GetV1GroupsGroupIdUsersLimit | Unset):  Default:
            GetV1GroupsGroupIdUsersLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV1GroupsGroupIdUsersSortOrder | Unset):  Default:
            GetV1GroupsGroupIdUsersSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiUserGroupRoleResponse]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: int,
    *,
    client: AuthenticatedClient,
    limit: GetV1GroupsGroupIdUsersLimit | Unset = GetV1GroupsGroupIdUsersLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1GroupsGroupIdUsersSortOrder | Unset = GetV1GroupsGroupIdUsersSortOrder.ASC,
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiUserGroupRoleResponse | None:
    """Gets a list of users in a group.

    Args:
        group_id (int):
        limit (GetV1GroupsGroupIdUsersLimit | Unset):  Default:
            GetV1GroupsGroupIdUsersLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV1GroupsGroupIdUsersSortOrder | Unset):  Default:
            GetV1GroupsGroupIdUsersSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiUserGroupRoleResponse
    """

    return sync_detailed(
        group_id=group_id,
        client=client,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
    ).parsed


async def asyncio_detailed(
    group_id: int,
    *,
    client: AuthenticatedClient,
    limit: GetV1GroupsGroupIdUsersLimit | Unset = GetV1GroupsGroupIdUsersLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1GroupsGroupIdUsersSortOrder | Unset = GetV1GroupsGroupIdUsersSortOrder.ASC,
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiUserGroupRoleResponse]:
    """Gets a list of users in a group.

    Args:
        group_id (int):
        limit (GetV1GroupsGroupIdUsersLimit | Unset):  Default:
            GetV1GroupsGroupIdUsersLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV1GroupsGroupIdUsersSortOrder | Unset):  Default:
            GetV1GroupsGroupIdUsersSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiUserGroupRoleResponse]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: int,
    *,
    client: AuthenticatedClient,
    limit: GetV1GroupsGroupIdUsersLimit | Unset = GetV1GroupsGroupIdUsersLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1GroupsGroupIdUsersSortOrder | Unset = GetV1GroupsGroupIdUsersSortOrder.ASC,
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiUserGroupRoleResponse | None:
    """Gets a list of users in a group.

    Args:
        group_id (int):
        limit (GetV1GroupsGroupIdUsersLimit | Unset):  Default:
            GetV1GroupsGroupIdUsersLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV1GroupsGroupIdUsersSortOrder | Unset):  Default:
            GetV1GroupsGroupIdUsersSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiUserGroupRoleResponse
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
            limit=limit,
            cursor=cursor,
            sort_order=sort_order,
        )
    ).parsed
