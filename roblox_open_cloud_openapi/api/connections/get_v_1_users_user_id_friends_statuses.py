from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_web_web_api_models_api_array_response_roblox_friends_api_friend_status_response import (
    RobloxWebWebAPIModelsApiArrayResponseRobloxFriendsApiFriendStatusResponse,
)
from ...types import UNSET, Response


def _get_kwargs(
    user_id: int,
    *,
    user_ids: list[int],
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_user_ids = user_ids

    params["userIds"] = json_user_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://friends.roblox.com/v1/users/{user_id}/friends/statuses".format(
            user_id=quote(str(user_id), safe=""),
        ),
        "params": params,
        "extensions": {
            "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
            "openapi-id": "get_v1_users_userId_friends_statuses",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxFriendsApiFriendStatusResponse | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIModelsApiArrayResponseRobloxFriendsApiFriendStatusResponse.from_dict(
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
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxFriendsApiFriendStatusResponse]:
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
    user_ids: list[int],
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxFriendsApiFriendStatusResponse]:
    """Gets a list of friend statuses of specified users against the specified user.

    Args:
        user_id (int):
        user_ids (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxFriendsApiFriendStatusResponse]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        user_ids=user_ids,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: int,
    *,
    client: AuthenticatedClient,
    user_ids: list[int],
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxFriendsApiFriendStatusResponse | None:
    """Gets a list of friend statuses of specified users against the specified user.

    Args:
        user_id (int):
        user_ids (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiArrayResponseRobloxFriendsApiFriendStatusResponse
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        user_ids=user_ids,
    ).parsed


async def asyncio_detailed(
    user_id: int,
    *,
    client: AuthenticatedClient,
    user_ids: list[int],
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxFriendsApiFriendStatusResponse]:
    """Gets a list of friend statuses of specified users against the specified user.

    Args:
        user_id (int):
        user_ids (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxFriendsApiFriendStatusResponse]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        user_ids=user_ids,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: int,
    *,
    client: AuthenticatedClient,
    user_ids: list[int],
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxFriendsApiFriendStatusResponse | None:
    """Gets a list of friend statuses of specified users against the specified user.

    Args:
        user_id (int):
        user_ids (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiArrayResponseRobloxFriendsApiFriendStatusResponse
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            user_ids=user_ids,
        )
    ).parsed
