from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v1_users_user_id_friends_find_find_friends_type import GetV1UsersUserIdFriendsFindFindFriendsType
from ...models.get_v1_users_user_id_friends_find_user_sort import GetV1UsersUserIdFriendsFindUserSort
from ...models.roblox_paging_cursored_paged_result_roblox_friends_api_models_response_friend_response import (
    RobloxPagingCursoredPagedResultRobloxFriendsApiModelsResponseFriendResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: int,
    *,
    user_sort: GetV1UsersUserIdFriendsFindUserSort | Unset = GetV1UsersUserIdFriendsFindUserSort.VALUE_2,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 50,
    find_friends_type: GetV1UsersUserIdFriendsFindFindFriendsType
    | Unset = GetV1UsersUserIdFriendsFindFindFriendsType.VALUE_0,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_user_sort: int | Unset = UNSET
    if not isinstance(user_sort, Unset):
        json_user_sort = user_sort.value

    params["userSort"] = json_user_sort

    params["cursor"] = cursor

    params["limit"] = limit

    json_find_friends_type: int | Unset = UNSET
    if not isinstance(find_friends_type, Unset):
        json_find_friends_type = find_friends_type.value

    params["findFriendsType"] = json_find_friends_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://friends.roblox.com/v1/users/{user_id}/friends/find".format(
            user_id=quote(str(user_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxPagingCursoredPagedResultRobloxFriendsApiModelsResponseFriendResponse | None:
    if response.status_code == 200:
        response_200 = RobloxPagingCursoredPagedResultRobloxFriendsApiModelsResponseFriendResponse.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxPagingCursoredPagedResultRobloxFriendsApiModelsResponseFriendResponse]:
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
    user_sort: GetV1UsersUserIdFriendsFindUserSort | Unset = GetV1UsersUserIdFriendsFindUserSort.VALUE_2,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 50,
    find_friends_type: GetV1UsersUserIdFriendsFindFindFriendsType
    | Unset = GetV1UsersUserIdFriendsFindFindFriendsType.VALUE_0,
) -> Response[Any | RobloxPagingCursoredPagedResultRobloxFriendsApiModelsResponseFriendResponse]:
    """Get a paginated list of all friends for the specified user.

    Args:
        user_id (int):
        user_sort (GetV1UsersUserIdFriendsFindUserSort | Unset):  Default:
            GetV1UsersUserIdFriendsFindUserSort.VALUE_2.
        cursor (str | Unset):
        limit (int | Unset):  Default: 50.
        find_friends_type (GetV1UsersUserIdFriendsFindFindFriendsType | Unset):  Default:
            GetV1UsersUserIdFriendsFindFindFriendsType.VALUE_0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxPagingCursoredPagedResultRobloxFriendsApiModelsResponseFriendResponse]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        user_sort=user_sort,
        cursor=cursor,
        limit=limit,
        find_friends_type=find_friends_type,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: int,
    *,
    client: AuthenticatedClient,
    user_sort: GetV1UsersUserIdFriendsFindUserSort | Unset = GetV1UsersUserIdFriendsFindUserSort.VALUE_2,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 50,
    find_friends_type: GetV1UsersUserIdFriendsFindFindFriendsType
    | Unset = GetV1UsersUserIdFriendsFindFindFriendsType.VALUE_0,
) -> Any | RobloxPagingCursoredPagedResultRobloxFriendsApiModelsResponseFriendResponse | None:
    """Get a paginated list of all friends for the specified user.

    Args:
        user_id (int):
        user_sort (GetV1UsersUserIdFriendsFindUserSort | Unset):  Default:
            GetV1UsersUserIdFriendsFindUserSort.VALUE_2.
        cursor (str | Unset):
        limit (int | Unset):  Default: 50.
        find_friends_type (GetV1UsersUserIdFriendsFindFindFriendsType | Unset):  Default:
            GetV1UsersUserIdFriendsFindFindFriendsType.VALUE_0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxPagingCursoredPagedResultRobloxFriendsApiModelsResponseFriendResponse
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        user_sort=user_sort,
        cursor=cursor,
        limit=limit,
        find_friends_type=find_friends_type,
    ).parsed


async def asyncio_detailed(
    user_id: int,
    *,
    client: AuthenticatedClient,
    user_sort: GetV1UsersUserIdFriendsFindUserSort | Unset = GetV1UsersUserIdFriendsFindUserSort.VALUE_2,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 50,
    find_friends_type: GetV1UsersUserIdFriendsFindFindFriendsType
    | Unset = GetV1UsersUserIdFriendsFindFindFriendsType.VALUE_0,
) -> Response[Any | RobloxPagingCursoredPagedResultRobloxFriendsApiModelsResponseFriendResponse]:
    """Get a paginated list of all friends for the specified user.

    Args:
        user_id (int):
        user_sort (GetV1UsersUserIdFriendsFindUserSort | Unset):  Default:
            GetV1UsersUserIdFriendsFindUserSort.VALUE_2.
        cursor (str | Unset):
        limit (int | Unset):  Default: 50.
        find_friends_type (GetV1UsersUserIdFriendsFindFindFriendsType | Unset):  Default:
            GetV1UsersUserIdFriendsFindFindFriendsType.VALUE_0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxPagingCursoredPagedResultRobloxFriendsApiModelsResponseFriendResponse]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        user_sort=user_sort,
        cursor=cursor,
        limit=limit,
        find_friends_type=find_friends_type,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: int,
    *,
    client: AuthenticatedClient,
    user_sort: GetV1UsersUserIdFriendsFindUserSort | Unset = GetV1UsersUserIdFriendsFindUserSort.VALUE_2,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 50,
    find_friends_type: GetV1UsersUserIdFriendsFindFindFriendsType
    | Unset = GetV1UsersUserIdFriendsFindFindFriendsType.VALUE_0,
) -> Any | RobloxPagingCursoredPagedResultRobloxFriendsApiModelsResponseFriendResponse | None:
    """Get a paginated list of all friends for the specified user.

    Args:
        user_id (int):
        user_sort (GetV1UsersUserIdFriendsFindUserSort | Unset):  Default:
            GetV1UsersUserIdFriendsFindUserSort.VALUE_2.
        cursor (str | Unset):
        limit (int | Unset):  Default: 50.
        find_friends_type (GetV1UsersUserIdFriendsFindFindFriendsType | Unset):  Default:
            GetV1UsersUserIdFriendsFindFindFriendsType.VALUE_0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxPagingCursoredPagedResultRobloxFriendsApiModelsResponseFriendResponse
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            user_sort=user_sort,
            cursor=cursor,
            limit=limit,
            find_friends_type=find_friends_type,
        )
    ).parsed
