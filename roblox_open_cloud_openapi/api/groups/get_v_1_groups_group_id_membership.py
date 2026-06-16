import sys
from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response

if sys.version_info >= (3, 13):
    from warnings import deprecated
else:
    from typing_extensions import deprecated

from ...models.roblox_groups_api_group_membership_metadata_response import (
    RobloxGroupsApiGroupMembershipMetadataResponse,
)


def _get_kwargs(
    group_id: int,
    *,
    include_notification_preferences: bool,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["includeNotificationPreferences"] = include_notification_preferences

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/groups/{group_id}/membership".format(
            group_id=quote(str(group_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxGroupsApiGroupMembershipMetadataResponse | None:
    if response.status_code == 200:
        response_200 = RobloxGroupsApiGroupMembershipMetadataResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RobloxGroupsApiGroupMembershipMetadataResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/groups#groups_get_v1_groups__groupId__membership"
)
def sync_detailed(
    group_id: int,
    *,
    client: AuthenticatedClient,
    include_notification_preferences: bool,
) -> Response[Any | RobloxGroupsApiGroupMembershipMetadataResponse]:
    """Gets group membership information in the context of the authenticated user

    Args:
        group_id (int):
        include_notification_preferences (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxGroupsApiGroupMembershipMetadataResponse]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        include_notification_preferences=include_notification_preferences,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/groups#groups_get_v1_groups__groupId__membership"
)
def sync(
    group_id: int,
    *,
    client: AuthenticatedClient,
    include_notification_preferences: bool,
) -> Any | RobloxGroupsApiGroupMembershipMetadataResponse | None:
    """Gets group membership information in the context of the authenticated user

    Args:
        group_id (int):
        include_notification_preferences (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxGroupsApiGroupMembershipMetadataResponse
    """

    return sync_detailed(
        group_id=group_id,
        client=client,
        include_notification_preferences=include_notification_preferences,
    ).parsed


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/groups#groups_get_v1_groups__groupId__membership"
)
async def asyncio_detailed(
    group_id: int,
    *,
    client: AuthenticatedClient,
    include_notification_preferences: bool,
) -> Response[Any | RobloxGroupsApiGroupMembershipMetadataResponse]:
    """Gets group membership information in the context of the authenticated user

    Args:
        group_id (int):
        include_notification_preferences (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxGroupsApiGroupMembershipMetadataResponse]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        include_notification_preferences=include_notification_preferences,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/groups#groups_get_v1_groups__groupId__membership"
)
async def asyncio(
    group_id: int,
    *,
    client: AuthenticatedClient,
    include_notification_preferences: bool,
) -> Any | RobloxGroupsApiGroupMembershipMetadataResponse | None:
    """Gets group membership information in the context of the authenticated user

    Args:
        group_id (int):
        include_notification_preferences (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxGroupsApiGroupMembershipMetadataResponse
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
            include_notification_preferences=include_notification_preferences,
        )
    ).parsed
