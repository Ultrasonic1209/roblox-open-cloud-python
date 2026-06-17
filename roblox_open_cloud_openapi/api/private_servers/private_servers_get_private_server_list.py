from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_private_server_list_response import GetPrivateServerListResponse
from ...models.string_exclusive_start_key_cursor import StringExclusiveStartKeyCursor
from ...types import UNSET, Response, Unset


def _get_kwargs(
    place_id: int,
    *,
    exclusive_start_key_cursor: StringExclusiveStartKeyCursor | Unset = UNSET,
    exclude_friend_servers: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_exclusive_start_key_cursor: dict[str, Any] | Unset = UNSET
    if not isinstance(exclusive_start_key_cursor, Unset):
        json_exclusive_start_key_cursor = exclusive_start_key_cursor.to_dict()
    if not isinstance(json_exclusive_start_key_cursor, Unset):
        params.update(json_exclusive_start_key_cursor)

    params["excludeFriendServers"] = exclude_friend_servers

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://games.roblox.com/v1/games/{place_id}/private-servers".format(
            place_id=quote(str(place_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> GetPrivateServerListResponse | None:
    if response.status_code == 200:
        response_200 = GetPrivateServerListResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[GetPrivateServerListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    place_id: int,
    *,
    client: AuthenticatedClient,
    exclusive_start_key_cursor: StringExclusiveStartKeyCursor | Unset = UNSET,
    exclude_friend_servers: bool | Unset = False,
) -> Response[GetPrivateServerListResponse]:
    """
    Args:
        place_id (int):
        exclusive_start_key_cursor (StringExclusiveStartKeyCursor | Unset):
        exclude_friend_servers (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPrivateServerListResponse]
    """

    kwargs = _get_kwargs(
        place_id=place_id,
        exclusive_start_key_cursor=exclusive_start_key_cursor,
        exclude_friend_servers=exclude_friend_servers,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    place_id: int,
    *,
    client: AuthenticatedClient,
    exclusive_start_key_cursor: StringExclusiveStartKeyCursor | Unset = UNSET,
    exclude_friend_servers: bool | Unset = False,
) -> GetPrivateServerListResponse | None:
    """
    Args:
        place_id (int):
        exclusive_start_key_cursor (StringExclusiveStartKeyCursor | Unset):
        exclude_friend_servers (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPrivateServerListResponse
    """

    return sync_detailed(
        place_id=place_id,
        client=client,
        exclusive_start_key_cursor=exclusive_start_key_cursor,
        exclude_friend_servers=exclude_friend_servers,
    ).parsed


async def asyncio_detailed(
    place_id: int,
    *,
    client: AuthenticatedClient,
    exclusive_start_key_cursor: StringExclusiveStartKeyCursor | Unset = UNSET,
    exclude_friend_servers: bool | Unset = False,
) -> Response[GetPrivateServerListResponse]:
    """
    Args:
        place_id (int):
        exclusive_start_key_cursor (StringExclusiveStartKeyCursor | Unset):
        exclude_friend_servers (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPrivateServerListResponse]
    """

    kwargs = _get_kwargs(
        place_id=place_id,
        exclusive_start_key_cursor=exclusive_start_key_cursor,
        exclude_friend_servers=exclude_friend_servers,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    place_id: int,
    *,
    client: AuthenticatedClient,
    exclusive_start_key_cursor: StringExclusiveStartKeyCursor | Unset = UNSET,
    exclude_friend_servers: bool | Unset = False,
) -> GetPrivateServerListResponse | None:
    """
    Args:
        place_id (int):
        exclusive_start_key_cursor (StringExclusiveStartKeyCursor | Unset):
        exclude_friend_servers (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPrivateServerListResponse
    """

    return (
        await asyncio_detailed(
            place_id=place_id,
            client=client,
            exclusive_start_key_cursor=exclusive_start_key_cursor,
            exclude_friend_servers=exclude_friend_servers,
        )
    ).parsed
