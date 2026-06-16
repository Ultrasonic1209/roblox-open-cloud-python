from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_groups_api_group_permissions_response import RobloxGroupsApiGroupPermissionsResponse
from ...types import Response


def _get_kwargs(
    group_id: int,
    role_set_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/groups/{group_id}/roles/{role_set_id}/permissions".format(
            group_id=quote(str(group_id), safe=""),
            role_set_id=quote(str(role_set_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxGroupsApiGroupPermissionsResponse | None:
    if response.status_code == 200:
        response_200 = RobloxGroupsApiGroupPermissionsResponse.from_dict(response.json())

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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RobloxGroupsApiGroupPermissionsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    group_id: int,
    role_set_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxGroupsApiGroupPermissionsResponse]:
    """Gets the permissions for a group's roleset. The authorized user must either be the group owner or
    the roleset being requested, except for guest roles, which can be viewed by all (members and
    guests).

    Args:
        group_id (int):
        role_set_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxGroupsApiGroupPermissionsResponse]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        role_set_id=role_set_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: int,
    role_set_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxGroupsApiGroupPermissionsResponse | None:
    """Gets the permissions for a group's roleset. The authorized user must either be the group owner or
    the roleset being requested, except for guest roles, which can be viewed by all (members and
    guests).

    Args:
        group_id (int):
        role_set_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxGroupsApiGroupPermissionsResponse
    """

    return sync_detailed(
        group_id=group_id,
        role_set_id=role_set_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    group_id: int,
    role_set_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxGroupsApiGroupPermissionsResponse]:
    """Gets the permissions for a group's roleset. The authorized user must either be the group owner or
    the roleset being requested, except for guest roles, which can be viewed by all (members and
    guests).

    Args:
        group_id (int):
        role_set_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxGroupsApiGroupPermissionsResponse]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        role_set_id=role_set_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: int,
    role_set_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxGroupsApiGroupPermissionsResponse | None:
    """Gets the permissions for a group's roleset. The authorized user must either be the group owner or
    the roleset being requested, except for guest roles, which can be viewed by all (members and
    guests).

    Args:
        group_id (int):
        role_set_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxGroupsApiGroupPermissionsResponse
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            role_set_id=role_set_id,
            client=client,
        )
    ).parsed
