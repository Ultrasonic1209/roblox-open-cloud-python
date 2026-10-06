from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_group_invitation_request_model import CreateGroupInvitationRequestModel
from ...models.group_invitation import GroupInvitation
from ...models.organizations_service_api_error_response import OrganizationsServiceApiErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    group_id: int,
    *,
    body: CreateGroupInvitationRequestModel
    | CreateGroupInvitationRequestModel
    | CreateGroupInvitationRequestModel
    | CreateGroupInvitationRequestModel
    | Unset = UNSET,
    is_secure: bool | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["isSecure"] = is_secure

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "https://groups.roblox.com/v2/groups/{group_id}/invitations".format(
            group_id=quote(str(group_id), safe=""),
        ),
        "params": params,
        "extensions": {
            "openapi-extensions": {
                "x-roblox-stability": "BETA",
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            },
            "openapi-id": "post_v2_groups_groupId_invitations",
        },
    }

    if isinstance(body, CreateGroupInvitationRequestModel):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, CreateGroupInvitationRequestModel):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CreateGroupInvitationRequestModel):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"
    if isinstance(body, CreateGroupInvitationRequestModel):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> GroupInvitation | OrganizationsServiceApiErrorResponse | None:
    if response.status_code == 200:
        response_200 = GroupInvitation.from_dict(response.json())

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

    if response.status_code == 429:
        response_429 = OrganizationsServiceApiErrorResponse.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = OrganizationsServiceApiErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[GroupInvitation | OrganizationsServiceApiErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    group_id: int,
    *,
    client: AuthenticatedClient,
    body: CreateGroupInvitationRequestModel
    | CreateGroupInvitationRequestModel
    | CreateGroupInvitationRequestModel
    | CreateGroupInvitationRequestModel
    | Unset = UNSET,
    is_secure: bool | Unset = UNSET,
) -> Response[GroupInvitation | OrganizationsServiceApiErrorResponse]:
    """Invite a user to a group

    Args:
        group_id (int):
        is_secure (bool | Unset):
        body (CreateGroupInvitationRequestModel): Request for inviting a user to a group.
        body (CreateGroupInvitationRequestModel): Request for inviting a user to a group.
        body (CreateGroupInvitationRequestModel): Request for inviting a user to a group.
        body (CreateGroupInvitationRequestModel): Request for inviting a user to a group.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GroupInvitation | OrganizationsServiceApiErrorResponse]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        body=body,
        is_secure=is_secure,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: int,
    *,
    client: AuthenticatedClient,
    body: CreateGroupInvitationRequestModel
    | CreateGroupInvitationRequestModel
    | CreateGroupInvitationRequestModel
    | CreateGroupInvitationRequestModel
    | Unset = UNSET,
    is_secure: bool | Unset = UNSET,
) -> GroupInvitation | OrganizationsServiceApiErrorResponse | None:
    """Invite a user to a group

    Args:
        group_id (int):
        is_secure (bool | Unset):
        body (CreateGroupInvitationRequestModel): Request for inviting a user to a group.
        body (CreateGroupInvitationRequestModel): Request for inviting a user to a group.
        body (CreateGroupInvitationRequestModel): Request for inviting a user to a group.
        body (CreateGroupInvitationRequestModel): Request for inviting a user to a group.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GroupInvitation | OrganizationsServiceApiErrorResponse
    """

    return sync_detailed(
        group_id=group_id,
        client=client,
        body=body,
        is_secure=is_secure,
    ).parsed


async def asyncio_detailed(
    group_id: int,
    *,
    client: AuthenticatedClient,
    body: CreateGroupInvitationRequestModel
    | CreateGroupInvitationRequestModel
    | CreateGroupInvitationRequestModel
    | CreateGroupInvitationRequestModel
    | Unset = UNSET,
    is_secure: bool | Unset = UNSET,
) -> Response[GroupInvitation | OrganizationsServiceApiErrorResponse]:
    """Invite a user to a group

    Args:
        group_id (int):
        is_secure (bool | Unset):
        body (CreateGroupInvitationRequestModel): Request for inviting a user to a group.
        body (CreateGroupInvitationRequestModel): Request for inviting a user to a group.
        body (CreateGroupInvitationRequestModel): Request for inviting a user to a group.
        body (CreateGroupInvitationRequestModel): Request for inviting a user to a group.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GroupInvitation | OrganizationsServiceApiErrorResponse]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        body=body,
        is_secure=is_secure,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: int,
    *,
    client: AuthenticatedClient,
    body: CreateGroupInvitationRequestModel
    | CreateGroupInvitationRequestModel
    | CreateGroupInvitationRequestModel
    | CreateGroupInvitationRequestModel
    | Unset = UNSET,
    is_secure: bool | Unset = UNSET,
) -> GroupInvitation | OrganizationsServiceApiErrorResponse | None:
    """Invite a user to a group

    Args:
        group_id (int):
        is_secure (bool | Unset):
        body (CreateGroupInvitationRequestModel): Request for inviting a user to a group.
        body (CreateGroupInvitationRequestModel): Request for inviting a user to a group.
        body (CreateGroupInvitationRequestModel): Request for inviting a user to a group.
        body (CreateGroupInvitationRequestModel): Request for inviting a user to a group.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GroupInvitation | OrganizationsServiceApiErrorResponse
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
            body=body,
            is_secure=is_secure,
        )
    ).parsed
