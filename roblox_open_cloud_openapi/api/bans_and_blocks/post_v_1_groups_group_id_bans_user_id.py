from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_groups_api_group_ban_member_response import RobloxGroupsApiGroupBanMemberResponse
from ...types import Response


def _get_kwargs(
    group_id: int,
    user_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/groups/{group_id}/bans/{user_id}".format(
            group_id=quote(str(group_id), safe=""),
            user_id=quote(str(user_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxGroupsApiGroupBanMemberResponse | None:
    if response.status_code == 200:
        response_200 = RobloxGroupsApiGroupBanMemberResponse.from_dict(response.json())

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
) -> Response[Any | RobloxGroupsApiGroupBanMemberResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    group_id: int,
    user_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxGroupsApiGroupBanMemberResponse]:
    """Bans a user from a group

    Args:
        group_id (int):
        user_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxGroupsApiGroupBanMemberResponse]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        user_id=user_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: int,
    user_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxGroupsApiGroupBanMemberResponse | None:
    """Bans a user from a group

    Args:
        group_id (int):
        user_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxGroupsApiGroupBanMemberResponse
    """

    return sync_detailed(
        group_id=group_id,
        user_id=user_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    group_id: int,
    user_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxGroupsApiGroupBanMemberResponse]:
    """Bans a user from a group

    Args:
        group_id (int):
        user_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxGroupsApiGroupBanMemberResponse]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        user_id=user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: int,
    user_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxGroupsApiGroupBanMemberResponse | None:
    """Bans a user from a group

    Args:
        group_id (int):
        user_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxGroupsApiGroupBanMemberResponse
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            user_id=user_id,
            client=client,
        )
    ).parsed
