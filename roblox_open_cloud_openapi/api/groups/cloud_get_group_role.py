from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.group_role import GroupRole
from ...types import Response


def _get_kwargs(
    group_id: str,
    role_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/cloud/v2/groups/{group_id}/roles/{role_id}".format(
            group_id=quote(str(group_id), safe=""),
            role_id=quote(str(role_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> GroupRole | None:
    if response.status_code == 200:
        response_200 = GroupRole.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[GroupRole]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    group_id: str,
    role_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[GroupRole]:
    """Get Group Role

     Get the group role

    Args:
        group_id (str):
        role_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GroupRole]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        role_id=role_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: str,
    role_id: str,
    *,
    client: AuthenticatedClient,
) -> GroupRole | None:
    """Get Group Role

     Get the group role

    Args:
        group_id (str):
        role_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GroupRole
    """

    return sync_detailed(
        group_id=group_id,
        role_id=role_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    group_id: str,
    role_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[GroupRole]:
    """Get Group Role

     Get the group role

    Args:
        group_id (str):
        role_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GroupRole]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        role_id=role_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: str,
    role_id: str,
    *,
    client: AuthenticatedClient,
) -> GroupRole | None:
    """Get Group Role

     Get the group role

    Args:
        group_id (str):
        role_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GroupRole
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            role_id=role_id,
            client=client,
        )
    ).parsed
