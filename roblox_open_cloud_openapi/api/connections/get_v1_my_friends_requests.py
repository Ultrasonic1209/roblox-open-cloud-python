from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v1_my_friends_requests_friend_request_sort import GetV1MyFriendsRequestsFriendRequestSort
from ...models.roblox_web_web_api_models_api_page_response_roblox_friends_api_friend_request_response import (
    RobloxWebWebAPIModelsApiPageResponseRobloxFriendsApiFriendRequestResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 10,
    cursor: str | Unset = UNSET,
    session_id: str | Unset = UNSET,
    friend_request_sort: GetV1MyFriendsRequestsFriendRequestSort
    | Unset = GetV1MyFriendsRequestsFriendRequestSort.VALUE_1,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    params["sessionId"] = session_id

    json_friend_request_sort: int | Unset = UNSET
    if not isinstance(friend_request_sort, Unset):
        json_friend_request_sort = friend_request_sort.value

    params["friendRequestSort"] = json_friend_request_sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://friends.roblox.com/v1/my/friends/requests",
        "params": params,
        "extensions": {
            "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
            "openapi-id": "get_v1_my_friends_requests",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxFriendsApiFriendRequestResponse | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIModelsApiPageResponseRobloxFriendsApiFriendRequestResponse.from_dict(
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

    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxFriendsApiFriendRequestResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 10,
    cursor: str | Unset = UNSET,
    session_id: str | Unset = UNSET,
    friend_request_sort: GetV1MyFriendsRequestsFriendRequestSort
    | Unset = GetV1MyFriendsRequestsFriendRequestSort.VALUE_1,
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxFriendsApiFriendRequestResponse]:
    """Get all users that friend requests with targetUserId using exclusive start paging

    Args:
        limit (int | Unset):  Default: 10.
        cursor (str | Unset):
        session_id (str | Unset):
        friend_request_sort (GetV1MyFriendsRequestsFriendRequestSort | Unset):  Default:
            GetV1MyFriendsRequestsFriendRequestSort.VALUE_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxFriendsApiFriendRequestResponse]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        session_id=session_id,
        friend_request_sort=friend_request_sort,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 10,
    cursor: str | Unset = UNSET,
    session_id: str | Unset = UNSET,
    friend_request_sort: GetV1MyFriendsRequestsFriendRequestSort
    | Unset = GetV1MyFriendsRequestsFriendRequestSort.VALUE_1,
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxFriendsApiFriendRequestResponse | None:
    """Get all users that friend requests with targetUserId using exclusive start paging

    Args:
        limit (int | Unset):  Default: 10.
        cursor (str | Unset):
        session_id (str | Unset):
        friend_request_sort (GetV1MyFriendsRequestsFriendRequestSort | Unset):  Default:
            GetV1MyFriendsRequestsFriendRequestSort.VALUE_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiPageResponseRobloxFriendsApiFriendRequestResponse
    """

    return sync_detailed(
        client=client,
        limit=limit,
        cursor=cursor,
        session_id=session_id,
        friend_request_sort=friend_request_sort,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 10,
    cursor: str | Unset = UNSET,
    session_id: str | Unset = UNSET,
    friend_request_sort: GetV1MyFriendsRequestsFriendRequestSort
    | Unset = GetV1MyFriendsRequestsFriendRequestSort.VALUE_1,
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxFriendsApiFriendRequestResponse]:
    """Get all users that friend requests with targetUserId using exclusive start paging

    Args:
        limit (int | Unset):  Default: 10.
        cursor (str | Unset):
        session_id (str | Unset):
        friend_request_sort (GetV1MyFriendsRequestsFriendRequestSort | Unset):  Default:
            GetV1MyFriendsRequestsFriendRequestSort.VALUE_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxFriendsApiFriendRequestResponse]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        session_id=session_id,
        friend_request_sort=friend_request_sort,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 10,
    cursor: str | Unset = UNSET,
    session_id: str | Unset = UNSET,
    friend_request_sort: GetV1MyFriendsRequestsFriendRequestSort
    | Unset = GetV1MyFriendsRequestsFriendRequestSort.VALUE_1,
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxFriendsApiFriendRequestResponse | None:
    """Get all users that friend requests with targetUserId using exclusive start paging

    Args:
        limit (int | Unset):  Default: 10.
        cursor (str | Unset):
        session_id (str | Unset):
        friend_request_sort (GetV1MyFriendsRequestsFriendRequestSort | Unset):  Default:
            GetV1MyFriendsRequestsFriendRequestSort.VALUE_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiPageResponseRobloxFriendsApiFriendRequestResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            cursor=cursor,
            session_id=session_id,
            friend_request_sort=friend_request_sort,
        )
    ).parsed
