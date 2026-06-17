from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_friends_api_models_response_new_friend_requests_count_response import (
    RobloxFriendsApiModelsResponseNewFriendRequestsCountResponse,
)
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://friends.roblox.com/v1/my/new-friend-requests/count",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxFriendsApiModelsResponseNewFriendRequestsCountResponse | None:
    if response.status_code == 200:
        response_200 = RobloxFriendsApiModelsResponseNewFriendRequestsCountResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxFriendsApiModelsResponseNewFriendRequestsCountResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxFriendsApiModelsResponseNewFriendRequestsCountResponse]:
    """
    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxFriendsApiModelsResponseNewFriendRequestsCountResponse]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Any | RobloxFriendsApiModelsResponseNewFriendRequestsCountResponse | None:
    """
    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxFriendsApiModelsResponseNewFriendRequestsCountResponse
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxFriendsApiModelsResponseNewFriendRequestsCountResponse]:
    """
    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxFriendsApiModelsResponseNewFriendRequestsCountResponse]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Any | RobloxFriendsApiModelsResponseNewFriendRequestsCountResponse | None:
    """
    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxFriendsApiModelsResponseNewFriendRequestsCountResponse
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
