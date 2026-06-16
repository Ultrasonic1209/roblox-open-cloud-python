from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v1_game_localization_roles_games_game_id_roles_role_assignees_role import (
    GetV1GameLocalizationRolesGamesGameIdRolesRoleAssigneesRole,
)
from ...models.roblox_web_web_api_models_api_array_response_roblox_translation_roles_api_assignee import (
    RobloxWebWebAPIModelsApiArrayResponseRobloxTranslationRolesApiAssignee,
)
from ...types import Response


def _get_kwargs(
    game_id: int,
    role: GetV1GameLocalizationRolesGamesGameIdRolesRoleAssigneesRole,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/game-localization-roles/games/{game_id}/roles/{role}/assignees".format(
            game_id=quote(str(game_id), safe=""),
            role=quote(str(role), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxTranslationRolesApiAssignee | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIModelsApiArrayResponseRobloxTranslationRolesApiAssignee.from_dict(response.json())

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

    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxTranslationRolesApiAssignee]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    game_id: int,
    role: GetV1GameLocalizationRolesGamesGameIdRolesRoleAssigneesRole,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxTranslationRolesApiAssignee]:
    """Gets list of users assigned a specific role in a game.

    Args:
        game_id (int):
        role (GetV1GameLocalizationRolesGamesGameIdRolesRoleAssigneesRole):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxTranslationRolesApiAssignee]
    """

    kwargs = _get_kwargs(
        game_id=game_id,
        role=role,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    game_id: int,
    role: GetV1GameLocalizationRolesGamesGameIdRolesRoleAssigneesRole,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxTranslationRolesApiAssignee | None:
    """Gets list of users assigned a specific role in a game.

    Args:
        game_id (int):
        role (GetV1GameLocalizationRolesGamesGameIdRolesRoleAssigneesRole):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiArrayResponseRobloxTranslationRolesApiAssignee
    """

    return sync_detailed(
        game_id=game_id,
        role=role,
        client=client,
    ).parsed


async def asyncio_detailed(
    game_id: int,
    role: GetV1GameLocalizationRolesGamesGameIdRolesRoleAssigneesRole,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxTranslationRolesApiAssignee]:
    """Gets list of users assigned a specific role in a game.

    Args:
        game_id (int):
        role (GetV1GameLocalizationRolesGamesGameIdRolesRoleAssigneesRole):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxTranslationRolesApiAssignee]
    """

    kwargs = _get_kwargs(
        game_id=game_id,
        role=role,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    game_id: int,
    role: GetV1GameLocalizationRolesGamesGameIdRolesRoleAssigneesRole,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxTranslationRolesApiAssignee | None:
    """Gets list of users assigned a specific role in a game.

    Args:
        game_id (int):
        role (GetV1GameLocalizationRolesGamesGameIdRolesRoleAssigneesRole):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiArrayResponseRobloxTranslationRolesApiAssignee
    """

    return (
        await asyncio_detailed(
            game_id=game_id,
            role=role,
            client=client,
        )
    ).parsed
