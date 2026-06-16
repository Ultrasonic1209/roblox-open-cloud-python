from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v1_users_user_id_friends_online_user_sort import GetV1UsersUserIdFriendsOnlineUserSort
from ...models.roblox_web_web_api_models_api_array_response_roblox_friends_api_models_response_user_presence_response import (
    RobloxWebWebAPIModelsApiArrayResponseRobloxFriendsApiModelsResponseUserPresenceResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: int,
    *,
    user_sort: GetV1UsersUserIdFriendsOnlineUserSort | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_user_sort: int | Unset = UNSET
    if not isinstance(user_sort, Unset):
        json_user_sort = user_sort.value

    params["userSort"] = json_user_sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/users/{user_id}/friends/online".format(
            user_id=quote(str(user_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxFriendsApiModelsResponseUserPresenceResponse | None:
    if response.status_code == 200:
        response_200 = (
            RobloxWebWebAPIModelsApiArrayResponseRobloxFriendsApiModelsResponseUserPresenceResponse.from_dict(
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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxFriendsApiModelsResponseUserPresenceResponse]:
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
    user_sort: GetV1UsersUserIdFriendsOnlineUserSort | Unset = UNSET,
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxFriendsApiModelsResponseUserPresenceResponse]:
    """Get list of all online friends for the specified user.

    Args:
        user_id (int):
        user_sort (GetV1UsersUserIdFriendsOnlineUserSort | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxFriendsApiModelsResponseUserPresenceResponse]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        user_sort=user_sort,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: int,
    *,
    client: AuthenticatedClient,
    user_sort: GetV1UsersUserIdFriendsOnlineUserSort | Unset = UNSET,
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxFriendsApiModelsResponseUserPresenceResponse | None:
    """Get list of all online friends for the specified user.

    Args:
        user_id (int):
        user_sort (GetV1UsersUserIdFriendsOnlineUserSort | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiArrayResponseRobloxFriendsApiModelsResponseUserPresenceResponse
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        user_sort=user_sort,
    ).parsed


async def asyncio_detailed(
    user_id: int,
    *,
    client: AuthenticatedClient,
    user_sort: GetV1UsersUserIdFriendsOnlineUserSort | Unset = UNSET,
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxFriendsApiModelsResponseUserPresenceResponse]:
    """Get list of all online friends for the specified user.

    Args:
        user_id (int):
        user_sort (GetV1UsersUserIdFriendsOnlineUserSort | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxFriendsApiModelsResponseUserPresenceResponse]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        user_sort=user_sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: int,
    *,
    client: AuthenticatedClient,
    user_sort: GetV1UsersUserIdFriendsOnlineUserSort | Unset = UNSET,
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxFriendsApiModelsResponseUserPresenceResponse | None:
    """Get list of all online friends for the specified user.

    Args:
        user_id (int):
        user_sort (GetV1UsersUserIdFriendsOnlineUserSort | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiArrayResponseRobloxFriendsApiModelsResponseUserPresenceResponse
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            user_sort=user_sort,
        )
    ).parsed
