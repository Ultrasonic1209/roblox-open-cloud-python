from http import HTTPStatus
from typing import TYPE_CHECKING, Any, cast

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


from ...models.get_v1_my_trusted_friends_requests_sort_order import GetV1MyTrustedFriendsRequestsSortOrder
from ...models.roblox_web_web_api_models_api_page_response_roblox_friends_api_models_response_trusted_friend_request_response import (
    RobloxWebWebAPIModelsApiPageResponseRobloxFriendsApiModelsResponseTrustedFriendRequestResponse,
)
from ...types import Unset


def _get_kwargs(
    *,
    limit: int | Unset = 10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1MyTrustedFriendsRequestsSortOrder | Unset = GetV1MyTrustedFriendsRequestsSortOrder.VALUE_1,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    json_sort_order: int | Unset = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value

    params["sortOrder"] = json_sort_order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://friends.roblox.com/v1/my/trusted-friends/requests",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxFriendsApiModelsResponseTrustedFriendRequestResponse | None:
    if response.status_code == 200:
        response_200 = (
            RobloxWebWebAPIModelsApiPageResponseRobloxFriendsApiModelsResponseTrustedFriendRequestResponse.from_dict(
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

    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxFriendsApiModelsResponseTrustedFriendRequestResponse]:
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
    sort_order: GetV1MyTrustedFriendsRequestsSortOrder | Unset = GetV1MyTrustedFriendsRequestsSortOrder.VALUE_1,
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxFriendsApiModelsResponseTrustedFriendRequestResponse]:
    """Get all incoming trusted friend requests using exclusive start paging.

    Args:
        limit (int | Unset):  Default: 10.
        cursor (str | Unset):
        sort_order (GetV1MyTrustedFriendsRequestsSortOrder | Unset):  Default:
            GetV1MyTrustedFriendsRequestsSortOrder.VALUE_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxFriendsApiModelsResponseTrustedFriendRequestResponse]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1MyTrustedFriendsRequestsSortOrder | Unset = GetV1MyTrustedFriendsRequestsSortOrder.VALUE_1,
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxFriendsApiModelsResponseTrustedFriendRequestResponse | None:
    """Get all incoming trusted friend requests using exclusive start paging.

    Args:
        limit (int | Unset):  Default: 10.
        cursor (str | Unset):
        sort_order (GetV1MyTrustedFriendsRequestsSortOrder | Unset):  Default:
            GetV1MyTrustedFriendsRequestsSortOrder.VALUE_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiPageResponseRobloxFriendsApiModelsResponseTrustedFriendRequestResponse
    """

    return sync_detailed(
        client=client,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1MyTrustedFriendsRequestsSortOrder | Unset = GetV1MyTrustedFriendsRequestsSortOrder.VALUE_1,
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxFriendsApiModelsResponseTrustedFriendRequestResponse]:
    """Get all incoming trusted friend requests using exclusive start paging.

    Args:
        limit (int | Unset):  Default: 10.
        cursor (str | Unset):
        sort_order (GetV1MyTrustedFriendsRequestsSortOrder | Unset):  Default:
            GetV1MyTrustedFriendsRequestsSortOrder.VALUE_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxFriendsApiModelsResponseTrustedFriendRequestResponse]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1MyTrustedFriendsRequestsSortOrder | Unset = GetV1MyTrustedFriendsRequestsSortOrder.VALUE_1,
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxFriendsApiModelsResponseTrustedFriendRequestResponse | None:
    """Get all incoming trusted friend requests using exclusive start paging.

    Args:
        limit (int | Unset):  Default: 10.
        cursor (str | Unset):
        sort_order (GetV1MyTrustedFriendsRequestsSortOrder | Unset):  Default:
            GetV1MyTrustedFriendsRequestsSortOrder.VALUE_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiPageResponseRobloxFriendsApiModelsResponseTrustedFriendRequestResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            cursor=cursor,
            sort_order=sort_order,
        )
    ).parsed
