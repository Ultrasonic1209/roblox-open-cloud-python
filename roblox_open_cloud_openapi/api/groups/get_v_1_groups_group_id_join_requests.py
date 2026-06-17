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

from ...models.get_v1_groups_group_id_join_requests_limit import GetV1GroupsGroupIdJoinRequestsLimit
from ...models.get_v1_groups_group_id_join_requests_sort_order import GetV1GroupsGroupIdJoinRequestsSortOrder
from ...models.roblox_web_web_api_models_api_page_response_roblox_groups_api_group_join_request_response import (
    RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiGroupJoinRequestResponse,
)


def _get_kwargs(
    group_id: int,
    *,
    limit: GetV1GroupsGroupIdJoinRequestsLimit | Unset = GetV1GroupsGroupIdJoinRequestsLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1GroupsGroupIdJoinRequestsSortOrder | Unset = GetV1GroupsGroupIdJoinRequestsSortOrder.ASC,
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
        "url": "https://groups.roblox.com/v1/groups/{group_id}/join-requests".format(
            group_id=quote(str(group_id), safe=""),
        ),
        "params": params,
        "openapi-extensions": {
            "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            "x-roblox-recommended-alternatives": [
                {
                    "url": "https://apis.roblox.com/cloud/v2/groups/{group_id}/join-requests",
                    "httpMethod": "GET",
                    "documentationUrl": "https://create.roblox.com/docs/cloud/reference/features/groups#Cloud_ListGroupJoinRequests",
                }
            ],
        },
        "openapi-id": "get_v1_groups_groupId_join-requests",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiGroupJoinRequestResponse | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiGroupJoinRequestResponse.from_dict(
            response.json()
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
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiGroupJoinRequestResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/groups#groups_get_v1_groups__groupId__join_requests"
)
def sync_detailed(
    group_id: int,
    *,
    client: AuthenticatedClient,
    limit: GetV1GroupsGroupIdJoinRequestsLimit | Unset = GetV1GroupsGroupIdJoinRequestsLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1GroupsGroupIdJoinRequestsSortOrder | Unset = GetV1GroupsGroupIdJoinRequestsSortOrder.ASC,
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiGroupJoinRequestResponse]:
    """Gets a page of Group Join Requests for a group.

    Args:
        group_id (int):
        limit (GetV1GroupsGroupIdJoinRequestsLimit | Unset):  Default:
            GetV1GroupsGroupIdJoinRequestsLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV1GroupsGroupIdJoinRequestsSortOrder | Unset):  Default:
            GetV1GroupsGroupIdJoinRequestsSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiGroupJoinRequestResponse]
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


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/groups#groups_get_v1_groups__groupId__join_requests"
)
def sync(
    group_id: int,
    *,
    client: AuthenticatedClient,
    limit: GetV1GroupsGroupIdJoinRequestsLimit | Unset = GetV1GroupsGroupIdJoinRequestsLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1GroupsGroupIdJoinRequestsSortOrder | Unset = GetV1GroupsGroupIdJoinRequestsSortOrder.ASC,
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiGroupJoinRequestResponse | None:
    """Gets a page of Group Join Requests for a group.

    Args:
        group_id (int):
        limit (GetV1GroupsGroupIdJoinRequestsLimit | Unset):  Default:
            GetV1GroupsGroupIdJoinRequestsLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV1GroupsGroupIdJoinRequestsSortOrder | Unset):  Default:
            GetV1GroupsGroupIdJoinRequestsSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiGroupJoinRequestResponse
    """

    return sync_detailed(
        group_id=group_id,
        client=client,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
    ).parsed


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/groups#groups_get_v1_groups__groupId__join_requests"
)
async def asyncio_detailed(
    group_id: int,
    *,
    client: AuthenticatedClient,
    limit: GetV1GroupsGroupIdJoinRequestsLimit | Unset = GetV1GroupsGroupIdJoinRequestsLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1GroupsGroupIdJoinRequestsSortOrder | Unset = GetV1GroupsGroupIdJoinRequestsSortOrder.ASC,
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiGroupJoinRequestResponse]:
    """Gets a page of Group Join Requests for a group.

    Args:
        group_id (int):
        limit (GetV1GroupsGroupIdJoinRequestsLimit | Unset):  Default:
            GetV1GroupsGroupIdJoinRequestsLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV1GroupsGroupIdJoinRequestsSortOrder | Unset):  Default:
            GetV1GroupsGroupIdJoinRequestsSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiGroupJoinRequestResponse]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/groups#groups_get_v1_groups__groupId__join_requests"
)
async def asyncio(
    group_id: int,
    *,
    client: AuthenticatedClient,
    limit: GetV1GroupsGroupIdJoinRequestsLimit | Unset = GetV1GroupsGroupIdJoinRequestsLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1GroupsGroupIdJoinRequestsSortOrder | Unset = GetV1GroupsGroupIdJoinRequestsSortOrder.ASC,
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiGroupJoinRequestResponse | None:
    """Gets a page of Group Join Requests for a group.

    Args:
        group_id (int):
        limit (GetV1GroupsGroupIdJoinRequestsLimit | Unset):  Default:
            GetV1GroupsGroupIdJoinRequestsLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV1GroupsGroupIdJoinRequestsSortOrder | Unset):  Default:
            GetV1GroupsGroupIdJoinRequestsSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiGroupJoinRequestResponse
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
