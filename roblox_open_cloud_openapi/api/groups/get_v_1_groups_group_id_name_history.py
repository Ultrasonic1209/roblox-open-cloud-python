from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v1_groups_group_id_name_history_limit import GetV1GroupsGroupIdNameHistoryLimit
from ...models.get_v1_groups_group_id_name_history_sort_order import GetV1GroupsGroupIdNameHistorySortOrder
from ...models.roblox_web_web_api_models_api_page_response_roblox_groups_api_models_response_group_name_history_response_item import (
    RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiModelsResponseGroupNameHistoryResponseItem,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    group_id: int,
    *,
    limit: GetV1GroupsGroupIdNameHistoryLimit | Unset = GetV1GroupsGroupIdNameHistoryLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1GroupsGroupIdNameHistorySortOrder | Unset = GetV1GroupsGroupIdNameHistorySortOrder.ASC,
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
        "url": "https://groups.roblox.com/v1/groups/{group_id}/name-history".format(
            group_id=quote(str(group_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiModelsResponseGroupNameHistoryResponseItem | None:
    if response.status_code == 200:
        response_200 = (
            RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiModelsResponseGroupNameHistoryResponseItem.from_dict(
                response.json()
            )
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
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiModelsResponseGroupNameHistoryResponseItem]:
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
    limit: GetV1GroupsGroupIdNameHistoryLimit | Unset = GetV1GroupsGroupIdNameHistoryLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1GroupsGroupIdNameHistorySortOrder | Unset = GetV1GroupsGroupIdNameHistorySortOrder.ASC,
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiModelsResponseGroupNameHistoryResponseItem]:
    """Gets the Group's name change history.

    Args:
        group_id (int):
        limit (GetV1GroupsGroupIdNameHistoryLimit | Unset):  Default:
            GetV1GroupsGroupIdNameHistoryLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV1GroupsGroupIdNameHistorySortOrder | Unset):  Default:
            GetV1GroupsGroupIdNameHistorySortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiModelsResponseGroupNameHistoryResponseItem]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: int,
    *,
    client: AuthenticatedClient,
    limit: GetV1GroupsGroupIdNameHistoryLimit | Unset = GetV1GroupsGroupIdNameHistoryLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1GroupsGroupIdNameHistorySortOrder | Unset = GetV1GroupsGroupIdNameHistorySortOrder.ASC,
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiModelsResponseGroupNameHistoryResponseItem | None:
    """Gets the Group's name change history.

    Args:
        group_id (int):
        limit (GetV1GroupsGroupIdNameHistoryLimit | Unset):  Default:
            GetV1GroupsGroupIdNameHistoryLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV1GroupsGroupIdNameHistorySortOrder | Unset):  Default:
            GetV1GroupsGroupIdNameHistorySortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiModelsResponseGroupNameHistoryResponseItem
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
    limit: GetV1GroupsGroupIdNameHistoryLimit | Unset = GetV1GroupsGroupIdNameHistoryLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1GroupsGroupIdNameHistorySortOrder | Unset = GetV1GroupsGroupIdNameHistorySortOrder.ASC,
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiModelsResponseGroupNameHistoryResponseItem]:
    """Gets the Group's name change history.

    Args:
        group_id (int):
        limit (GetV1GroupsGroupIdNameHistoryLimit | Unset):  Default:
            GetV1GroupsGroupIdNameHistoryLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV1GroupsGroupIdNameHistorySortOrder | Unset):  Default:
            GetV1GroupsGroupIdNameHistorySortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiModelsResponseGroupNameHistoryResponseItem]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: int,
    *,
    client: AuthenticatedClient,
    limit: GetV1GroupsGroupIdNameHistoryLimit | Unset = GetV1GroupsGroupIdNameHistoryLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1GroupsGroupIdNameHistorySortOrder | Unset = GetV1GroupsGroupIdNameHistorySortOrder.ASC,
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiModelsResponseGroupNameHistoryResponseItem | None:
    """Gets the Group's name change history.

    Args:
        group_id (int):
        limit (GetV1GroupsGroupIdNameHistoryLimit | Unset):  Default:
            GetV1GroupsGroupIdNameHistoryLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV1GroupsGroupIdNameHistorySortOrder | Unset):  Default:
            GetV1GroupsGroupIdNameHistorySortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiModelsResponseGroupNameHistoryResponseItem
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
