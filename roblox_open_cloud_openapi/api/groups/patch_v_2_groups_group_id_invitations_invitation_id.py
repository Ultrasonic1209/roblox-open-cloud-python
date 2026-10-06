from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.organizations_service_api_error_response import OrganizationsServiceApiErrorResponse
from ...models.success_response import SuccessResponse
from ...models.update_group_invitation_request_model import UpdateGroupInvitationRequestModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    group_id: int,
    invitation_id: int,
    *,
    body: UpdateGroupInvitationRequestModel
    | UpdateGroupInvitationRequestModel
    | UpdateGroupInvitationRequestModel
    | UpdateGroupInvitationRequestModel
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "https://groups.roblox.com/v2/groups/{group_id}/invitations/{invitation_id}".format(
            group_id=quote(str(group_id), safe=""),
            invitation_id=quote(str(invitation_id), safe=""),
        ),
        "extensions": {
            "openapi-extensions": {
                "x-roblox-stability": "BETA",
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            },
            "openapi-id": "patch_v2_groups_groupId_invitations_invitationId",
        },
    }

    if isinstance(body, UpdateGroupInvitationRequestModel):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, UpdateGroupInvitationRequestModel):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, UpdateGroupInvitationRequestModel):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"
    if isinstance(body, UpdateGroupInvitationRequestModel):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> OrganizationsServiceApiErrorResponse | SuccessResponse | None:
    if response.status_code == 200:
        response_200 = SuccessResponse.from_dict(response.json())

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
) -> Response[OrganizationsServiceApiErrorResponse | SuccessResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    group_id: int,
    invitation_id: int,
    *,
    client: AuthenticatedClient,
    body: UpdateGroupInvitationRequestModel
    | UpdateGroupInvitationRequestModel
    | UpdateGroupInvitationRequestModel
    | UpdateGroupInvitationRequestModel
    | Unset = UNSET,
) -> Response[OrganizationsServiceApiErrorResponse | SuccessResponse]:
    """Accept or decline an invitation to a group (recipient)

    Args:
        group_id (int):
        invitation_id (int):
        body (UpdateGroupInvitationRequestModel): Request for accepting or declining a group
            invitation.
        body (UpdateGroupInvitationRequestModel): Request for accepting or declining a group
            invitation.
        body (UpdateGroupInvitationRequestModel): Request for accepting or declining a group
            invitation.
        body (UpdateGroupInvitationRequestModel): Request for accepting or declining a group
            invitation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrganizationsServiceApiErrorResponse | SuccessResponse]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        invitation_id=invitation_id,
        body=body,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: int,
    invitation_id: int,
    *,
    client: AuthenticatedClient,
    body: UpdateGroupInvitationRequestModel
    | UpdateGroupInvitationRequestModel
    | UpdateGroupInvitationRequestModel
    | UpdateGroupInvitationRequestModel
    | Unset = UNSET,
) -> OrganizationsServiceApiErrorResponse | SuccessResponse | None:
    """Accept or decline an invitation to a group (recipient)

    Args:
        group_id (int):
        invitation_id (int):
        body (UpdateGroupInvitationRequestModel): Request for accepting or declining a group
            invitation.
        body (UpdateGroupInvitationRequestModel): Request for accepting or declining a group
            invitation.
        body (UpdateGroupInvitationRequestModel): Request for accepting or declining a group
            invitation.
        body (UpdateGroupInvitationRequestModel): Request for accepting or declining a group
            invitation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrganizationsServiceApiErrorResponse | SuccessResponse
    """

    return sync_detailed(
        group_id=group_id,
        invitation_id=invitation_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    group_id: int,
    invitation_id: int,
    *,
    client: AuthenticatedClient,
    body: UpdateGroupInvitationRequestModel
    | UpdateGroupInvitationRequestModel
    | UpdateGroupInvitationRequestModel
    | UpdateGroupInvitationRequestModel
    | Unset = UNSET,
) -> Response[OrganizationsServiceApiErrorResponse | SuccessResponse]:
    """Accept or decline an invitation to a group (recipient)

    Args:
        group_id (int):
        invitation_id (int):
        body (UpdateGroupInvitationRequestModel): Request for accepting or declining a group
            invitation.
        body (UpdateGroupInvitationRequestModel): Request for accepting or declining a group
            invitation.
        body (UpdateGroupInvitationRequestModel): Request for accepting or declining a group
            invitation.
        body (UpdateGroupInvitationRequestModel): Request for accepting or declining a group
            invitation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrganizationsServiceApiErrorResponse | SuccessResponse]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        invitation_id=invitation_id,
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: int,
    invitation_id: int,
    *,
    client: AuthenticatedClient,
    body: UpdateGroupInvitationRequestModel
    | UpdateGroupInvitationRequestModel
    | UpdateGroupInvitationRequestModel
    | UpdateGroupInvitationRequestModel
    | Unset = UNSET,
) -> OrganizationsServiceApiErrorResponse | SuccessResponse | None:
    """Accept or decline an invitation to a group (recipient)

    Args:
        group_id (int):
        invitation_id (int):
        body (UpdateGroupInvitationRequestModel): Request for accepting or declining a group
            invitation.
        body (UpdateGroupInvitationRequestModel): Request for accepting or declining a group
            invitation.
        body (UpdateGroupInvitationRequestModel): Request for accepting or declining a group
            invitation.
        body (UpdateGroupInvitationRequestModel): Request for accepting or declining a group
            invitation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrganizationsServiceApiErrorResponse | SuccessResponse
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            invitation_id=invitation_id,
            client=client,
            body=body,
        )
    ).parsed
