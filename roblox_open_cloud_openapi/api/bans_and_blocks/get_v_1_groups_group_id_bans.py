from http import HTTPStatus
from typing import TYPE_CHECKING, Any, cast
from urllib.parse import quote

if TYPE_CHECKING:
    import httpx2 as httpx
else:
    try:
        import httpx2 as httpx
    except ModuleNotFoundError:
        try:
            import httpx
        except ModuleNotFoundError:
            raise RuntimeError(
                "This module requires the httpx2 package to be installed.\n"
                "You can install it with:\n"
                "    $ pip install httpx2\n"
            ) from None


from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response

"""
{'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.get_v1_groups_group_id_bans_limit import GetV1GroupsGroupIdBansLimit
from ...models.get_v1_groups_group_id_bans_sort_order import GetV1GroupsGroupIdBansSortOrder
from ...models.roblox_web_web_api_models_api_page_response_roblox_groups_api_group_ban_member_response import (
    RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiGroupBanMemberResponse,
)
from ...types import Unset


def _get_kwargs(
    group_id: int,
    *,
    limit: GetV1GroupsGroupIdBansLimit | Unset = GetV1GroupsGroupIdBansLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1GroupsGroupIdBansSortOrder | Unset = GetV1GroupsGroupIdBansSortOrder.ASC,
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
        "url": "https://groups.roblox.com/v1/groups/{group_id}/bans".format(
            group_id=quote(str(group_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiGroupBanMemberResponse | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiGroupBanMemberResponse.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 405:
        response_405 = cast(Any, None)
        return response_405

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiGroupBanMemberResponse]:
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
    limit: GetV1GroupsGroupIdBansLimit | Unset = GetV1GroupsGroupIdBansLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1GroupsGroupIdBansSortOrder | Unset = GetV1GroupsGroupIdBansSortOrder.ASC,
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiGroupBanMemberResponse]:
    """Gets the bans for the group

    Args:
        group_id (int):
        limit (GetV1GroupsGroupIdBansLimit | Unset):  Default:
            GetV1GroupsGroupIdBansLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV1GroupsGroupIdBansSortOrder | Unset):  Default:
            GetV1GroupsGroupIdBansSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiGroupBanMemberResponse]
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
    limit: GetV1GroupsGroupIdBansLimit | Unset = GetV1GroupsGroupIdBansLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1GroupsGroupIdBansSortOrder | Unset = GetV1GroupsGroupIdBansSortOrder.ASC,
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiGroupBanMemberResponse | None:
    """Gets the bans for the group

    Args:
        group_id (int):
        limit (GetV1GroupsGroupIdBansLimit | Unset):  Default:
            GetV1GroupsGroupIdBansLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV1GroupsGroupIdBansSortOrder | Unset):  Default:
            GetV1GroupsGroupIdBansSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiGroupBanMemberResponse
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
    limit: GetV1GroupsGroupIdBansLimit | Unset = GetV1GroupsGroupIdBansLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1GroupsGroupIdBansSortOrder | Unset = GetV1GroupsGroupIdBansSortOrder.ASC,
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiGroupBanMemberResponse]:
    """Gets the bans for the group

    Args:
        group_id (int):
        limit (GetV1GroupsGroupIdBansLimit | Unset):  Default:
            GetV1GroupsGroupIdBansLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV1GroupsGroupIdBansSortOrder | Unset):  Default:
            GetV1GroupsGroupIdBansSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiGroupBanMemberResponse]
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
    limit: GetV1GroupsGroupIdBansLimit | Unset = GetV1GroupsGroupIdBansLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1GroupsGroupIdBansSortOrder | Unset = GetV1GroupsGroupIdBansSortOrder.ASC,
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiGroupBanMemberResponse | None:
    """Gets the bans for the group

    Args:
        group_id (int):
        limit (GetV1GroupsGroupIdBansLimit | Unset):  Default:
            GetV1GroupsGroupIdBansLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV1GroupsGroupIdBansSortOrder | Unset):  Default:
            GetV1GroupsGroupIdBansSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiGroupBanMemberResponse
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
