from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.group_invitation_cursor_page_response import GroupInvitationCursorPageResponse
from ...models.organizations_service_api_error_response import OrganizationsServiceApiErrorResponse
from ...models.organizations_service_api_sort_order import OrganizationsServiceApiSortOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    group_id: int,
    role_id: int,
    *,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    sort_order: OrganizationsServiceApiSortOrder | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["Cursor"] = cursor

    params["Limit"] = limit

    json_sort_order: str | Unset = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value

    params["SortOrder"] = json_sort_order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://groups.roblox.com/v2/groups/{group_id}/roles/{role_id}/invitations".format(
            group_id=quote(str(group_id), safe=""),
            role_id=quote(str(role_id), safe=""),
        ),
        "params": params,
        "extensions": {
            "openapi-extensions": {
                "x-roblox-stability": "BETA",
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            },
            "openapi-id": "get_v2_groups_groupId_roles_roleId_invitations",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> GroupInvitationCursorPageResponse | OrganizationsServiceApiErrorResponse | None:
    if response.status_code == 200:
        response_200 = GroupInvitationCursorPageResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = OrganizationsServiceApiErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = OrganizationsServiceApiErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = OrganizationsServiceApiErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = OrganizationsServiceApiErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = OrganizationsServiceApiErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[GroupInvitationCursorPageResponse | OrganizationsServiceApiErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    group_id: int,
    role_id: int,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    sort_order: OrganizationsServiceApiSortOrder | Unset = UNSET,
) -> Response[GroupInvitationCursorPageResponse | OrganizationsServiceApiErrorResponse]:
    """List open invitations to a group that grant a role

    Args:
        group_id (int):
        role_id (int):
        cursor (str | Unset):
        limit (int | Unset):
        sort_order (OrganizationsServiceApiSortOrder | Unset): Sort order for groups-api style
            paginated requests.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GroupInvitationCursorPageResponse | OrganizationsServiceApiErrorResponse]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        role_id=role_id,
        cursor=cursor,
        limit=limit,
        sort_order=sort_order,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: int,
    role_id: int,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    sort_order: OrganizationsServiceApiSortOrder | Unset = UNSET,
) -> GroupInvitationCursorPageResponse | OrganizationsServiceApiErrorResponse | None:
    """List open invitations to a group that grant a role

    Args:
        group_id (int):
        role_id (int):
        cursor (str | Unset):
        limit (int | Unset):
        sort_order (OrganizationsServiceApiSortOrder | Unset): Sort order for groups-api style
            paginated requests.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GroupInvitationCursorPageResponse | OrganizationsServiceApiErrorResponse
    """

    return sync_detailed(
        group_id=group_id,
        role_id=role_id,
        client=client,
        cursor=cursor,
        limit=limit,
        sort_order=sort_order,
    ).parsed


async def asyncio_detailed(
    group_id: int,
    role_id: int,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    sort_order: OrganizationsServiceApiSortOrder | Unset = UNSET,
) -> Response[GroupInvitationCursorPageResponse | OrganizationsServiceApiErrorResponse]:
    """List open invitations to a group that grant a role

    Args:
        group_id (int):
        role_id (int):
        cursor (str | Unset):
        limit (int | Unset):
        sort_order (OrganizationsServiceApiSortOrder | Unset): Sort order for groups-api style
            paginated requests.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GroupInvitationCursorPageResponse | OrganizationsServiceApiErrorResponse]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        role_id=role_id,
        cursor=cursor,
        limit=limit,
        sort_order=sort_order,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: int,
    role_id: int,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    sort_order: OrganizationsServiceApiSortOrder | Unset = UNSET,
) -> GroupInvitationCursorPageResponse | OrganizationsServiceApiErrorResponse | None:
    """List open invitations to a group that grant a role

    Args:
        group_id (int):
        role_id (int):
        cursor (str | Unset):
        limit (int | Unset):
        sort_order (OrganizationsServiceApiSortOrder | Unset): Sort order for groups-api style
            paginated requests.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GroupInvitationCursorPageResponse | OrganizationsServiceApiErrorResponse
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            role_id=role_id,
            client=client,
            cursor=cursor,
            limit=limit,
            sort_order=sort_order,
        )
    ).parsed
