import sys
from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response

if sys.version_info >= (3, 13):
    from warnings import deprecated
else:
    from typing_extensions import deprecated

from ...models.get_v1_groups_group_id_roles_role_set_id_users_limit import GetV1GroupsGroupIdRolesRoleSetIdUsersLimit
from ...models.get_v1_groups_group_id_roles_role_set_id_users_sort_order import (
    GetV1GroupsGroupIdRolesRoleSetIdUsersSortOrder,
)
from ...models.roblox_web_web_api_models_api_page_response_roblox_groups_api_models_response_user_model import (
    RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiModelsResponseUserModel,
)
from ...types import Unset


def _get_kwargs(
    group_id: int,
    role_set_id: int,
    *,
    limit: GetV1GroupsGroupIdRolesRoleSetIdUsersLimit | Unset = GetV1GroupsGroupIdRolesRoleSetIdUsersLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1GroupsGroupIdRolesRoleSetIdUsersSortOrder
    | Unset = GetV1GroupsGroupIdRolesRoleSetIdUsersSortOrder.ASC,
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
        "url": "/v1/groups/{group_id}/roles/{role_set_id}/users".format(
            group_id=quote(str(group_id), safe=""),
            role_set_id=quote(str(role_set_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiModelsResponseUserModel | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiModelsResponseUserModel.from_dict(
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
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiModelsResponseUserModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/groups#groups_get_v1_groups__groupId__roles__roleSetId__users"
)
def sync_detailed(
    group_id: int,
    role_set_id: int,
    *,
    client: AuthenticatedClient,
    limit: GetV1GroupsGroupIdRolesRoleSetIdUsersLimit | Unset = GetV1GroupsGroupIdRolesRoleSetIdUsersLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1GroupsGroupIdRolesRoleSetIdUsersSortOrder
    | Unset = GetV1GroupsGroupIdRolesRoleSetIdUsersSortOrder.ASC,
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiModelsResponseUserModel]:
    """Gets a list of users in a group for a specific roleset.

    Args:
        group_id (int):
        role_set_id (int):
        limit (GetV1GroupsGroupIdRolesRoleSetIdUsersLimit | Unset):  Default:
            GetV1GroupsGroupIdRolesRoleSetIdUsersLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV1GroupsGroupIdRolesRoleSetIdUsersSortOrder | Unset):  Default:
            GetV1GroupsGroupIdRolesRoleSetIdUsersSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiModelsResponseUserModel]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        role_set_id=role_set_id,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/groups#groups_get_v1_groups__groupId__roles__roleSetId__users"
)
def sync(
    group_id: int,
    role_set_id: int,
    *,
    client: AuthenticatedClient,
    limit: GetV1GroupsGroupIdRolesRoleSetIdUsersLimit | Unset = GetV1GroupsGroupIdRolesRoleSetIdUsersLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1GroupsGroupIdRolesRoleSetIdUsersSortOrder
    | Unset = GetV1GroupsGroupIdRolesRoleSetIdUsersSortOrder.ASC,
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiModelsResponseUserModel | None:
    """Gets a list of users in a group for a specific roleset.

    Args:
        group_id (int):
        role_set_id (int):
        limit (GetV1GroupsGroupIdRolesRoleSetIdUsersLimit | Unset):  Default:
            GetV1GroupsGroupIdRolesRoleSetIdUsersLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV1GroupsGroupIdRolesRoleSetIdUsersSortOrder | Unset):  Default:
            GetV1GroupsGroupIdRolesRoleSetIdUsersSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiModelsResponseUserModel
    """

    return sync_detailed(
        group_id=group_id,
        role_set_id=role_set_id,
        client=client,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
    ).parsed


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/groups#groups_get_v1_groups__groupId__roles__roleSetId__users"
)
async def asyncio_detailed(
    group_id: int,
    role_set_id: int,
    *,
    client: AuthenticatedClient,
    limit: GetV1GroupsGroupIdRolesRoleSetIdUsersLimit | Unset = GetV1GroupsGroupIdRolesRoleSetIdUsersLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1GroupsGroupIdRolesRoleSetIdUsersSortOrder
    | Unset = GetV1GroupsGroupIdRolesRoleSetIdUsersSortOrder.ASC,
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiModelsResponseUserModel]:
    """Gets a list of users in a group for a specific roleset.

    Args:
        group_id (int):
        role_set_id (int):
        limit (GetV1GroupsGroupIdRolesRoleSetIdUsersLimit | Unset):  Default:
            GetV1GroupsGroupIdRolesRoleSetIdUsersLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV1GroupsGroupIdRolesRoleSetIdUsersSortOrder | Unset):  Default:
            GetV1GroupsGroupIdRolesRoleSetIdUsersSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiModelsResponseUserModel]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        role_set_id=role_set_id,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/groups#groups_get_v1_groups__groupId__roles__roleSetId__users"
)
async def asyncio(
    group_id: int,
    role_set_id: int,
    *,
    client: AuthenticatedClient,
    limit: GetV1GroupsGroupIdRolesRoleSetIdUsersLimit | Unset = GetV1GroupsGroupIdRolesRoleSetIdUsersLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1GroupsGroupIdRolesRoleSetIdUsersSortOrder
    | Unset = GetV1GroupsGroupIdRolesRoleSetIdUsersSortOrder.ASC,
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiModelsResponseUserModel | None:
    """Gets a list of users in a group for a specific roleset.

    Args:
        group_id (int):
        role_set_id (int):
        limit (GetV1GroupsGroupIdRolesRoleSetIdUsersLimit | Unset):  Default:
            GetV1GroupsGroupIdRolesRoleSetIdUsersLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV1GroupsGroupIdRolesRoleSetIdUsersSortOrder | Unset):  Default:
            GetV1GroupsGroupIdRolesRoleSetIdUsersSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiModelsResponseUserModel
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            role_set_id=role_set_id,
            client=client,
            limit=limit,
            cursor=cursor,
            sort_order=sort_order,
        )
    ).parsed
