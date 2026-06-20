from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_translation_roles_api_update_role_request import RobloxTranslationRolesApiUpdateRoleRequest
from ...models.translation_roles_api_roblox_web_web_api_api_empty_response_model import (
    TranslationRolesApiRobloxWebWebAPIApiEmptyResponseModel,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    game_id: int,
    *,
    body: RobloxTranslationRolesApiUpdateRoleRequest | RobloxTranslationRolesApiUpdateRoleRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "https://translationroles.roblox.com/v1/game-localization-roles/games/{game_id}".format(
            game_id=quote(str(game_id), safe=""),
        ),
        "extensions": {
            "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
            "openapi-id": "patch_v1_game-localization-roles_games_gameId",
        },
    }

    if isinstance(body, RobloxTranslationRolesApiUpdateRoleRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxTranslationRolesApiUpdateRoleRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | TranslationRolesApiRobloxWebWebAPIApiEmptyResponseModel | None:
    if response.status_code == 200:
        response_200 = TranslationRolesApiRobloxWebWebAPIApiEmptyResponseModel.from_dict(response.json())

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

    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429

    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | TranslationRolesApiRobloxWebWebAPIApiEmptyResponseModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    game_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxTranslationRolesApiUpdateRoleRequest | RobloxTranslationRolesApiUpdateRoleRequest | Unset = UNSET,
) -> Response[Any | TranslationRolesApiRobloxWebWebAPIApiEmptyResponseModel]:
    """Assigns or revokes a role

    Args:
        game_id (int):
        body (RobloxTranslationRolesApiUpdateRoleRequest | Unset): The request body for update
            role endpoints
        body (RobloxTranslationRolesApiUpdateRoleRequest | Unset): The request body for update
            role endpoints

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TranslationRolesApiRobloxWebWebAPIApiEmptyResponseModel]
    """

    kwargs = _get_kwargs(
        game_id=game_id,
        body=body,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    game_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxTranslationRolesApiUpdateRoleRequest | RobloxTranslationRolesApiUpdateRoleRequest | Unset = UNSET,
) -> Any | TranslationRolesApiRobloxWebWebAPIApiEmptyResponseModel | None:
    """Assigns or revokes a role

    Args:
        game_id (int):
        body (RobloxTranslationRolesApiUpdateRoleRequest | Unset): The request body for update
            role endpoints
        body (RobloxTranslationRolesApiUpdateRoleRequest | Unset): The request body for update
            role endpoints

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | TranslationRolesApiRobloxWebWebAPIApiEmptyResponseModel
    """

    return sync_detailed(
        game_id=game_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    game_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxTranslationRolesApiUpdateRoleRequest | RobloxTranslationRolesApiUpdateRoleRequest | Unset = UNSET,
) -> Response[Any | TranslationRolesApiRobloxWebWebAPIApiEmptyResponseModel]:
    """Assigns or revokes a role

    Args:
        game_id (int):
        body (RobloxTranslationRolesApiUpdateRoleRequest | Unset): The request body for update
            role endpoints
        body (RobloxTranslationRolesApiUpdateRoleRequest | Unset): The request body for update
            role endpoints

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TranslationRolesApiRobloxWebWebAPIApiEmptyResponseModel]
    """

    kwargs = _get_kwargs(
        game_id=game_id,
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    game_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxTranslationRolesApiUpdateRoleRequest | RobloxTranslationRolesApiUpdateRoleRequest | Unset = UNSET,
) -> Any | TranslationRolesApiRobloxWebWebAPIApiEmptyResponseModel | None:
    """Assigns or revokes a role

    Args:
        game_id (int):
        body (RobloxTranslationRolesApiUpdateRoleRequest | Unset): The request body for update
            role endpoints
        body (RobloxTranslationRolesApiUpdateRoleRequest | Unset): The request body for update
            role endpoints

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | TranslationRolesApiRobloxWebWebAPIApiEmptyResponseModel
    """

    return (
        await asyncio_detailed(
            game_id=game_id,
            client=client,
            body=body,
        )
    ).parsed
