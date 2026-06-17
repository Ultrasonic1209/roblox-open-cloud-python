from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_friends_api_follow_count_response import RobloxFriendsApiFollowCountResponse
from ...types import Response


def _get_kwargs(
    target_user_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://friends.roblox.com/v1/users/{target_user_id}/followers/count".format(
            target_user_id=quote(str(target_user_id), safe=""),
        ),
        "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
        "openapi-id": "get_v1_users_targetUserId_followers_count",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxFriendsApiFollowCountResponse | None:
    if response.status_code == 200:
        response_200 = RobloxFriendsApiFollowCountResponse.from_dict(response.json())

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
) -> Response[Any | RobloxFriendsApiFollowCountResponse]:
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
) -> Response[Any | RobloxFriendsApiFollowCountResponse]:
    """Get the number of following a user has

    Args:
        target_user_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxFriendsApiFollowCountResponse]
    """

    kwargs = _get_kwargs(
        target_user_id=target_user_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    target_user_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxFriendsApiFollowCountResponse | None:
    """Get the number of following a user has

    Args:
        target_user_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxFriendsApiFollowCountResponse
    """

    return sync_detailed(
        target_user_id=target_user_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    target_user_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxFriendsApiFollowCountResponse]:
    """Get the number of following a user has

    Args:
        target_user_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxFriendsApiFollowCountResponse]
    """

    kwargs = _get_kwargs(
        target_user_id=target_user_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    target_user_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxFriendsApiFollowCountResponse | None:
    """Get the number of following a user has

    Args:
        target_user_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxFriendsApiFollowCountResponse
    """

    return (
        await asyncio_detailed(
            target_user_id=target_user_id,
            client=client,
        )
    ).parsed
