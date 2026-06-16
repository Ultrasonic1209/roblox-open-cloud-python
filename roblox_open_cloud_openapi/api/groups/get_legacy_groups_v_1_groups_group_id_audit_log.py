from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_legacy_groups_v1_groups_group_id_audit_log_action_type import (
    GetLegacyGroupsV1GroupsGroupIdAuditLogActionType,
)
from ...models.get_legacy_groups_v1_groups_group_id_audit_log_limit import GetLegacyGroupsV1GroupsGroupIdAuditLogLimit
from ...models.get_legacy_groups_v1_groups_group_id_audit_log_sort_order import (
    GetLegacyGroupsV1GroupsGroupIdAuditLogSortOrder,
)
from ...models.roblox_groups_api_group_audit_log_page_response_roblox_groups_api_models_response_group_audit_log_response_item import (
    RobloxGroupsApiGroupAuditLogPageResponseRobloxGroupsApiModelsResponseGroupAuditLogResponseItem,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    group_id: int,
    *,
    action_type: GetLegacyGroupsV1GroupsGroupIdAuditLogActionType | Unset = UNSET,
    user_id: int | Unset = UNSET,
    limit: GetLegacyGroupsV1GroupsGroupIdAuditLogLimit | Unset = GetLegacyGroupsV1GroupsGroupIdAuditLogLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetLegacyGroupsV1GroupsGroupIdAuditLogSortOrder
    | Unset = GetLegacyGroupsV1GroupsGroupIdAuditLogSortOrder.ASC,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_action_type: str | Unset = UNSET
    if not isinstance(action_type, Unset):
        json_action_type = action_type.value

    params["actionType"] = json_action_type

    params["userId"] = user_id

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
        "url": "/legacy-groups/v1/groups/{group_id}/audit-log".format(
            group_id=quote(str(group_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxGroupsApiGroupAuditLogPageResponseRobloxGroupsApiModelsResponseGroupAuditLogResponseItem | None:
    if response.status_code == 200:
        response_200 = (
            RobloxGroupsApiGroupAuditLogPageResponseRobloxGroupsApiModelsResponseGroupAuditLogResponseItem.from_dict(
                response.json()
            )
        )

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RobloxGroupsApiGroupAuditLogPageResponseRobloxGroupsApiModelsResponseGroupAuditLogResponseItem]:
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
    action_type: GetLegacyGroupsV1GroupsGroupIdAuditLogActionType | Unset = UNSET,
    user_id: int | Unset = UNSET,
    limit: GetLegacyGroupsV1GroupsGroupIdAuditLogLimit | Unset = GetLegacyGroupsV1GroupsGroupIdAuditLogLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetLegacyGroupsV1GroupsGroupIdAuditLogSortOrder
    | Unset = GetLegacyGroupsV1GroupsGroupIdAuditLogSortOrder.ASC,
) -> Response[Any | RobloxGroupsApiGroupAuditLogPageResponseRobloxGroupsApiModelsResponseGroupAuditLogResponseItem]:
    """Gets the Group's audit log

    Args:
        group_id (int):
        action_type (GetLegacyGroupsV1GroupsGroupIdAuditLogActionType | Unset):
        user_id (int | Unset):
        limit (GetLegacyGroupsV1GroupsGroupIdAuditLogLimit | Unset):  Default:
            GetLegacyGroupsV1GroupsGroupIdAuditLogLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetLegacyGroupsV1GroupsGroupIdAuditLogSortOrder | Unset):  Default:
            GetLegacyGroupsV1GroupsGroupIdAuditLogSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxGroupsApiGroupAuditLogPageResponseRobloxGroupsApiModelsResponseGroupAuditLogResponseItem]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        action_type=action_type,
        user_id=user_id,
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
    action_type: GetLegacyGroupsV1GroupsGroupIdAuditLogActionType | Unset = UNSET,
    user_id: int | Unset = UNSET,
    limit: GetLegacyGroupsV1GroupsGroupIdAuditLogLimit | Unset = GetLegacyGroupsV1GroupsGroupIdAuditLogLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetLegacyGroupsV1GroupsGroupIdAuditLogSortOrder
    | Unset = GetLegacyGroupsV1GroupsGroupIdAuditLogSortOrder.ASC,
) -> Any | RobloxGroupsApiGroupAuditLogPageResponseRobloxGroupsApiModelsResponseGroupAuditLogResponseItem | None:
    """Gets the Group's audit log

    Args:
        group_id (int):
        action_type (GetLegacyGroupsV1GroupsGroupIdAuditLogActionType | Unset):
        user_id (int | Unset):
        limit (GetLegacyGroupsV1GroupsGroupIdAuditLogLimit | Unset):  Default:
            GetLegacyGroupsV1GroupsGroupIdAuditLogLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetLegacyGroupsV1GroupsGroupIdAuditLogSortOrder | Unset):  Default:
            GetLegacyGroupsV1GroupsGroupIdAuditLogSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxGroupsApiGroupAuditLogPageResponseRobloxGroupsApiModelsResponseGroupAuditLogResponseItem
    """

    return sync_detailed(
        group_id=group_id,
        client=client,
        action_type=action_type,
        user_id=user_id,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
    ).parsed


async def asyncio_detailed(
    group_id: int,
    *,
    client: AuthenticatedClient,
    action_type: GetLegacyGroupsV1GroupsGroupIdAuditLogActionType | Unset = UNSET,
    user_id: int | Unset = UNSET,
    limit: GetLegacyGroupsV1GroupsGroupIdAuditLogLimit | Unset = GetLegacyGroupsV1GroupsGroupIdAuditLogLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetLegacyGroupsV1GroupsGroupIdAuditLogSortOrder
    | Unset = GetLegacyGroupsV1GroupsGroupIdAuditLogSortOrder.ASC,
) -> Response[Any | RobloxGroupsApiGroupAuditLogPageResponseRobloxGroupsApiModelsResponseGroupAuditLogResponseItem]:
    """Gets the Group's audit log

    Args:
        group_id (int):
        action_type (GetLegacyGroupsV1GroupsGroupIdAuditLogActionType | Unset):
        user_id (int | Unset):
        limit (GetLegacyGroupsV1GroupsGroupIdAuditLogLimit | Unset):  Default:
            GetLegacyGroupsV1GroupsGroupIdAuditLogLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetLegacyGroupsV1GroupsGroupIdAuditLogSortOrder | Unset):  Default:
            GetLegacyGroupsV1GroupsGroupIdAuditLogSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxGroupsApiGroupAuditLogPageResponseRobloxGroupsApiModelsResponseGroupAuditLogResponseItem]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        action_type=action_type,
        user_id=user_id,
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
    action_type: GetLegacyGroupsV1GroupsGroupIdAuditLogActionType | Unset = UNSET,
    user_id: int | Unset = UNSET,
    limit: GetLegacyGroupsV1GroupsGroupIdAuditLogLimit | Unset = GetLegacyGroupsV1GroupsGroupIdAuditLogLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetLegacyGroupsV1GroupsGroupIdAuditLogSortOrder
    | Unset = GetLegacyGroupsV1GroupsGroupIdAuditLogSortOrder.ASC,
) -> Any | RobloxGroupsApiGroupAuditLogPageResponseRobloxGroupsApiModelsResponseGroupAuditLogResponseItem | None:
    """Gets the Group's audit log

    Args:
        group_id (int):
        action_type (GetLegacyGroupsV1GroupsGroupIdAuditLogActionType | Unset):
        user_id (int | Unset):
        limit (GetLegacyGroupsV1GroupsGroupIdAuditLogLimit | Unset):  Default:
            GetLegacyGroupsV1GroupsGroupIdAuditLogLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetLegacyGroupsV1GroupsGroupIdAuditLogSortOrder | Unset):  Default:
            GetLegacyGroupsV1GroupsGroupIdAuditLogSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxGroupsApiGroupAuditLogPageResponseRobloxGroupsApiModelsResponseGroupAuditLogResponseItem
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
            action_type=action_type,
            user_id=user_id,
            limit=limit,
            cursor=cursor,
            sort_order=sort_order,
        )
    ).parsed
