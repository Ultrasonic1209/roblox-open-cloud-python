from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v1_game_localization_roles_roles_role_current_user_role import (
    GetV1GameLocalizationRolesRolesRoleCurrentUserRole,
)
from ...models.roblox_translation_roles_api_get_game_localization_role_assignments_for_user_response import (
    RobloxTranslationRolesApiGetGameLocalizationRoleAssignmentsForUserResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    role: GetV1GameLocalizationRolesRolesRoleCurrentUserRole,
    *,
    exclusive_start_key: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
    group_id: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["exclusiveStartKey"] = exclusive_start_key

    params["pageSize"] = page_size

    params["groupId"] = group_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://translationroles.roblox.com/v1/game-localization-roles/roles/{role}/current-user".format(
            role=quote(str(role), safe=""),
        ),
        "params": params,
        "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
        "openapi-id": "get_v1_game-localization-roles_roles_role_current-user",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxTranslationRolesApiGetGameLocalizationRoleAssignmentsForUserResponse | None:
    if response.status_code == 200:
        response_200 = RobloxTranslationRolesApiGetGameLocalizationRoleAssignmentsForUserResponse.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxTranslationRolesApiGetGameLocalizationRoleAssignmentsForUserResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    role: GetV1GameLocalizationRolesRolesRoleCurrentUserRole,
    *,
    client: AuthenticatedClient,
    exclusive_start_key: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
    group_id: int | Unset = UNSET,
) -> Response[Any | RobloxTranslationRolesApiGetGameLocalizationRoleAssignmentsForUserResponse]:
    """Gets the list of games and associated role assignment info for the requested user and role.

    Args:
        role (GetV1GameLocalizationRolesRolesRoleCurrentUserRole):
        exclusive_start_key (str | Unset):
        page_size (int | Unset):
        group_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxTranslationRolesApiGetGameLocalizationRoleAssignmentsForUserResponse]
    """

    kwargs = _get_kwargs(
        role=role,
        exclusive_start_key=exclusive_start_key,
        page_size=page_size,
        group_id=group_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    role: GetV1GameLocalizationRolesRolesRoleCurrentUserRole,
    *,
    client: AuthenticatedClient,
    exclusive_start_key: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
    group_id: int | Unset = UNSET,
) -> Any | RobloxTranslationRolesApiGetGameLocalizationRoleAssignmentsForUserResponse | None:
    """Gets the list of games and associated role assignment info for the requested user and role.

    Args:
        role (GetV1GameLocalizationRolesRolesRoleCurrentUserRole):
        exclusive_start_key (str | Unset):
        page_size (int | Unset):
        group_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxTranslationRolesApiGetGameLocalizationRoleAssignmentsForUserResponse
    """

    return sync_detailed(
        role=role,
        client=client,
        exclusive_start_key=exclusive_start_key,
        page_size=page_size,
        group_id=group_id,
    ).parsed


async def asyncio_detailed(
    role: GetV1GameLocalizationRolesRolesRoleCurrentUserRole,
    *,
    client: AuthenticatedClient,
    exclusive_start_key: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
    group_id: int | Unset = UNSET,
) -> Response[Any | RobloxTranslationRolesApiGetGameLocalizationRoleAssignmentsForUserResponse]:
    """Gets the list of games and associated role assignment info for the requested user and role.

    Args:
        role (GetV1GameLocalizationRolesRolesRoleCurrentUserRole):
        exclusive_start_key (str | Unset):
        page_size (int | Unset):
        group_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxTranslationRolesApiGetGameLocalizationRoleAssignmentsForUserResponse]
    """

    kwargs = _get_kwargs(
        role=role,
        exclusive_start_key=exclusive_start_key,
        page_size=page_size,
        group_id=group_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    role: GetV1GameLocalizationRolesRolesRoleCurrentUserRole,
    *,
    client: AuthenticatedClient,
    exclusive_start_key: str | Unset = UNSET,
    page_size: int | Unset = UNSET,
    group_id: int | Unset = UNSET,
) -> Any | RobloxTranslationRolesApiGetGameLocalizationRoleAssignmentsForUserResponse | None:
    """Gets the list of games and associated role assignment info for the requested user and role.

    Args:
        role (GetV1GameLocalizationRolesRolesRoleCurrentUserRole):
        exclusive_start_key (str | Unset):
        page_size (int | Unset):
        group_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxTranslationRolesApiGetGameLocalizationRoleAssignmentsForUserResponse
    """

    return (
        await asyncio_detailed(
            role=role,
            client=client,
            exclusive_start_key=exclusive_start_key,
            page_size=page_size,
            group_id=group_id,
        )
    ).parsed
