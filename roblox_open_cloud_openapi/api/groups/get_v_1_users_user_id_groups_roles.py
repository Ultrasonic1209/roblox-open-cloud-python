from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v1_users_user_id_groups_roles_discovery_type import GetV1UsersUserIdGroupsRolesDiscoveryType
from ...models.roblox_web_web_api_models_api_array_response_roblox_groups_api_group_membership_detail_response import (
    RobloxWebWebAPIModelsApiArrayResponseRobloxGroupsApiGroupMembershipDetailResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: int,
    *,
    include_locked: bool | Unset = UNSET,
    include_notification_preferences: bool | Unset = UNSET,
    discovery_type: GetV1UsersUserIdGroupsRolesDiscoveryType | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["includeLocked"] = include_locked

    params["includeNotificationPreferences"] = include_notification_preferences

    json_discovery_type: int | Unset = UNSET
    if not isinstance(discovery_type, Unset):
        json_discovery_type = discovery_type.value

    params["discoveryType"] = json_discovery_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://groups.roblox.com/v1/users/{user_id}/groups/roles".format(
            user_id=quote(str(user_id), safe=""),
        ),
        "params": params,
        "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
        "openapi-id": "get_v1_users_userId_groups_roles",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGroupsApiGroupMembershipDetailResponse | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIModelsApiArrayResponseRobloxGroupsApiGroupMembershipDetailResponse.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGroupsApiGroupMembershipDetailResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: int,
    *,
    client: AuthenticatedClient,
    include_locked: bool | Unset = UNSET,
    include_notification_preferences: bool | Unset = UNSET,
    discovery_type: GetV1UsersUserIdGroupsRolesDiscoveryType | Unset = UNSET,
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGroupsApiGroupMembershipDetailResponse]:
    """Gets a list of all group roles for groups the specified user is in.

    Args:
        user_id (int):
        include_locked (bool | Unset):
        include_notification_preferences (bool | Unset):
        discovery_type (GetV1UsersUserIdGroupsRolesDiscoveryType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGroupsApiGroupMembershipDetailResponse]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        include_locked=include_locked,
        include_notification_preferences=include_notification_preferences,
        discovery_type=discovery_type,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: int,
    *,
    client: AuthenticatedClient,
    include_locked: bool | Unset = UNSET,
    include_notification_preferences: bool | Unset = UNSET,
    discovery_type: GetV1UsersUserIdGroupsRolesDiscoveryType | Unset = UNSET,
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGroupsApiGroupMembershipDetailResponse | None:
    """Gets a list of all group roles for groups the specified user is in.

    Args:
        user_id (int):
        include_locked (bool | Unset):
        include_notification_preferences (bool | Unset):
        discovery_type (GetV1UsersUserIdGroupsRolesDiscoveryType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGroupsApiGroupMembershipDetailResponse
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        include_locked=include_locked,
        include_notification_preferences=include_notification_preferences,
        discovery_type=discovery_type,
    ).parsed


async def asyncio_detailed(
    user_id: int,
    *,
    client: AuthenticatedClient,
    include_locked: bool | Unset = UNSET,
    include_notification_preferences: bool | Unset = UNSET,
    discovery_type: GetV1UsersUserIdGroupsRolesDiscoveryType | Unset = UNSET,
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGroupsApiGroupMembershipDetailResponse]:
    """Gets a list of all group roles for groups the specified user is in.

    Args:
        user_id (int):
        include_locked (bool | Unset):
        include_notification_preferences (bool | Unset):
        discovery_type (GetV1UsersUserIdGroupsRolesDiscoveryType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGroupsApiGroupMembershipDetailResponse]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        include_locked=include_locked,
        include_notification_preferences=include_notification_preferences,
        discovery_type=discovery_type,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: int,
    *,
    client: AuthenticatedClient,
    include_locked: bool | Unset = UNSET,
    include_notification_preferences: bool | Unset = UNSET,
    discovery_type: GetV1UsersUserIdGroupsRolesDiscoveryType | Unset = UNSET,
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGroupsApiGroupMembershipDetailResponse | None:
    """Gets a list of all group roles for groups the specified user is in.

    Args:
        user_id (int):
        include_locked (bool | Unset):
        include_notification_preferences (bool | Unset):
        discovery_type (GetV1UsersUserIdGroupsRolesDiscoveryType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiArrayResponseRobloxGroupsApiGroupMembershipDetailResponse
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            include_locked=include_locked,
            include_notification_preferences=include_notification_preferences,
            discovery_type=discovery_type,
        )
    ).parsed
