from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v1_users_target_user_id_followings_limit import GetV1UsersTargetUserIdFollowingsLimit
from ...models.get_v1_users_target_user_id_followings_sort_order import GetV1UsersTargetUserIdFollowingsSortOrder
from ...models.roblox_web_web_api_models_api_page_response_roblox_friends_api_models_response_user_response import (
    RobloxWebWebAPIModelsApiPageResponseRobloxFriendsApiModelsResponseUserResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    target_user_id: int,
    *,
    limit: GetV1UsersTargetUserIdFollowingsLimit | Unset = GetV1UsersTargetUserIdFollowingsLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1UsersTargetUserIdFollowingsSortOrder | Unset = GetV1UsersTargetUserIdFollowingsSortOrder.ASC,
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
        "url": "https://friends.roblox.com/v1/users/{target_user_id}/followings".format(
            target_user_id=quote(str(target_user_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxFriendsApiModelsResponseUserResponse | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIModelsApiPageResponseRobloxFriendsApiModelsResponseUserResponse.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

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
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxFriendsApiModelsResponseUserResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    target_user_id: int,
    *,
    client: AuthenticatedClient,
    limit: GetV1UsersTargetUserIdFollowingsLimit | Unset = GetV1UsersTargetUserIdFollowingsLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1UsersTargetUserIdFollowingsSortOrder | Unset = GetV1UsersTargetUserIdFollowingsSortOrder.ASC,
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxFriendsApiModelsResponseUserResponse]:
    """Get all users that user with targetUserId is following in page response format

    Args:
        target_user_id (int):
        limit (GetV1UsersTargetUserIdFollowingsLimit | Unset):  Default:
            GetV1UsersTargetUserIdFollowingsLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV1UsersTargetUserIdFollowingsSortOrder | Unset):  Default:
            GetV1UsersTargetUserIdFollowingsSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxFriendsApiModelsResponseUserResponse]
    """

    kwargs = _get_kwargs(
        target_user_id=target_user_id,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    target_user_id: int,
    *,
    client: AuthenticatedClient,
    limit: GetV1UsersTargetUserIdFollowingsLimit | Unset = GetV1UsersTargetUserIdFollowingsLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1UsersTargetUserIdFollowingsSortOrder | Unset = GetV1UsersTargetUserIdFollowingsSortOrder.ASC,
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxFriendsApiModelsResponseUserResponse | None:
    """Get all users that user with targetUserId is following in page response format

    Args:
        target_user_id (int):
        limit (GetV1UsersTargetUserIdFollowingsLimit | Unset):  Default:
            GetV1UsersTargetUserIdFollowingsLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV1UsersTargetUserIdFollowingsSortOrder | Unset):  Default:
            GetV1UsersTargetUserIdFollowingsSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiPageResponseRobloxFriendsApiModelsResponseUserResponse
    """

    return sync_detailed(
        target_user_id=target_user_id,
        client=client,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
    ).parsed


async def asyncio_detailed(
    target_user_id: int,
    *,
    client: AuthenticatedClient,
    limit: GetV1UsersTargetUserIdFollowingsLimit | Unset = GetV1UsersTargetUserIdFollowingsLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1UsersTargetUserIdFollowingsSortOrder | Unset = GetV1UsersTargetUserIdFollowingsSortOrder.ASC,
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxFriendsApiModelsResponseUserResponse]:
    """Get all users that user with targetUserId is following in page response format

    Args:
        target_user_id (int):
        limit (GetV1UsersTargetUserIdFollowingsLimit | Unset):  Default:
            GetV1UsersTargetUserIdFollowingsLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV1UsersTargetUserIdFollowingsSortOrder | Unset):  Default:
            GetV1UsersTargetUserIdFollowingsSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxFriendsApiModelsResponseUserResponse]
    """

    kwargs = _get_kwargs(
        target_user_id=target_user_id,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    target_user_id: int,
    *,
    client: AuthenticatedClient,
    limit: GetV1UsersTargetUserIdFollowingsLimit | Unset = GetV1UsersTargetUserIdFollowingsLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1UsersTargetUserIdFollowingsSortOrder | Unset = GetV1UsersTargetUserIdFollowingsSortOrder.ASC,
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxFriendsApiModelsResponseUserResponse | None:
    """Get all users that user with targetUserId is following in page response format

    Args:
        target_user_id (int):
        limit (GetV1UsersTargetUserIdFollowingsLimit | Unset):  Default:
            GetV1UsersTargetUserIdFollowingsLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV1UsersTargetUserIdFollowingsSortOrder | Unset):  Default:
            GetV1UsersTargetUserIdFollowingsSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiPageResponseRobloxFriendsApiModelsResponseUserResponse
    """

    return (
        await asyncio_detailed(
            target_user_id=target_user_id,
            client=client,
            limit=limit,
            cursor=cursor,
            sort_order=sort_order,
        )
    ).parsed
