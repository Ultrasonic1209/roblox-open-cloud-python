from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.group_membership import GroupMembership
from ...types import Response


def _get_kwargs(
    group_id: str,
    membership_id: str,
    *,
    body: GroupMembership,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/cloud/v2/groups/{group_id}/memberships/{membership_id}".format(
            group_id=quote(str(group_id), safe=""),
            membership_id=quote(str(membership_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> GroupMembership | None:
    if response.status_code == 200:
        response_200 = GroupMembership.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[GroupMembership]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    group_id: str,
    membership_id: str,
    *,
    client: AuthenticatedClient,
    body: GroupMembership,
) -> Response[GroupMembership]:
    """Update Group Membership

     **Deprecated.** Use AssignGroupRole and UnassignGroupRole instead.
    Updates the group membership for a particular group member. This action
    requires the requester to be able to manage lower ranked members. Guest or
    Owner ranks cannot be assigned, and a requester cannot change their own
    rank.

    Args:
        group_id (str):
        membership_id (str):
        body (GroupMembership): A membership to a group. A user ID can be used in place of a
            membership ID.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GroupMembership]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        membership_id=membership_id,
        body=body,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: str,
    membership_id: str,
    *,
    client: AuthenticatedClient,
    body: GroupMembership,
) -> GroupMembership | None:
    """Update Group Membership

     **Deprecated.** Use AssignGroupRole and UnassignGroupRole instead.
    Updates the group membership for a particular group member. This action
    requires the requester to be able to manage lower ranked members. Guest or
    Owner ranks cannot be assigned, and a requester cannot change their own
    rank.

    Args:
        group_id (str):
        membership_id (str):
        body (GroupMembership): A membership to a group. A user ID can be used in place of a
            membership ID.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GroupMembership
    """

    return sync_detailed(
        group_id=group_id,
        membership_id=membership_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    group_id: str,
    membership_id: str,
    *,
    client: AuthenticatedClient,
    body: GroupMembership,
) -> Response[GroupMembership]:
    """Update Group Membership

     **Deprecated.** Use AssignGroupRole and UnassignGroupRole instead.
    Updates the group membership for a particular group member. This action
    requires the requester to be able to manage lower ranked members. Guest or
    Owner ranks cannot be assigned, and a requester cannot change their own
    rank.

    Args:
        group_id (str):
        membership_id (str):
        body (GroupMembership): A membership to a group. A user ID can be used in place of a
            membership ID.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GroupMembership]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        membership_id=membership_id,
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: str,
    membership_id: str,
    *,
    client: AuthenticatedClient,
    body: GroupMembership,
) -> GroupMembership | None:
    """Update Group Membership

     **Deprecated.** Use AssignGroupRole and UnassignGroupRole instead.
    Updates the group membership for a particular group member. This action
    requires the requester to be able to manage lower ranked members. Guest or
    Owner ranks cannot be assigned, and a requester cannot change their own
    rank.

    Args:
        group_id (str):
        membership_id (str):
        body (GroupMembership): A membership to a group. A user ID can be used in place of a
            membership ID.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GroupMembership
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            membership_id=membership_id,
            client=client,
            body=body,
        )
    ).parsed
