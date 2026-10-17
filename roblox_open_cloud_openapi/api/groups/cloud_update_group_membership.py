from http import HTTPStatus
from typing import TYPE_CHECKING, Any
from urllib.parse import quote

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
from ...types import Response

"""
{'x-roblox-engine-usability': {'apiKeyWithHttpService': True}, 'x-roblox-scopes': [{'name': 'group:write', 'targetResourceSpecifier': ''}, {'name': 'group:write'}], 'x-roblox-docs': {'category': 'Users and groups', 'methodProperties': {'scopes': ['group:write']}, 'resource': {'$ref': '#/components/schemas/GroupMembership', 'name': 'GroupMembership'}}, 'x-roblox-stability': 'BETA', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'MINUTE', 'maxInPeriod': 300}, 'perOauth2Authorization': {'period': 'MINUTE', 'maxInPeriod': 90}}}
"""


from ...models.group_membership import GroupMembership


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


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GroupMembership | None:
    if response.status_code == 200:
        response_200 = GroupMembership.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GroupMembership]:
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
    requires the requester to be able to assign or remove roles below their
    highest role. The requester cannot change their own roles.

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

    response = client.get_httpx_client().request(
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
    requires the requester to be able to assign or remove roles below their
    highest role. The requester cannot change their own roles.

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
    requires the requester to be able to assign or remove roles below their
    highest role. The requester cannot change their own roles.

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

    response = await client.get_async_httpx_client().request(**kwargs)

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
    requires the requester to be able to assign or remove roles below their
    highest role. The requester cannot change their own roles.

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
