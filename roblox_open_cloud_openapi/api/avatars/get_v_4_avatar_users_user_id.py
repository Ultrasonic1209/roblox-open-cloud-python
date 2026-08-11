from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v4_avatar_users_user_id_selection_types_item import GetV4AvatarUsersUserIdSelectionTypesItem
from ...models.roblox_api_avatar_models_v4_avatar_definition import RobloxApiAvatarModelsV4AvatarDefinition
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: int,
    *,
    selection_types: list[GetV4AvatarUsersUserIdSelectionTypesItem],
    roblox_place_id: int | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(roblox_place_id, Unset):
        headers["Roblox-Place-Id"] = str(roblox_place_id)

    params: dict[str, Any] = {}

    json_selection_types = []
    for selection_types_item_data in selection_types:
        selection_types_item = selection_types_item_data.value
        json_selection_types.append(selection_types_item)

    params["selectionTypes"] = json_selection_types

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://avatar.roblox.com/v4/avatar/users/{user_id}".format(
            user_id=quote(str(user_id), safe=""),
        ),
        "params": params,
        "extensions": {
            "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
            "openapi-id": "get_v4_avatar_users_userId",
        },
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxApiAvatarModelsV4AvatarDefinition | None:
    if response.status_code == 200:
        response_200 = RobloxApiAvatarModelsV4AvatarDefinition.from_dict(response.json())

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
) -> Response[Any | RobloxApiAvatarModelsV4AvatarDefinition]:
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
    selection_types: list[GetV4AvatarUsersUserIdSelectionTypesItem],
    roblox_place_id: int | Unset = UNSET,
) -> Response[Any | RobloxApiAvatarModelsV4AvatarDefinition]:
    """Gets the currently wearing avatar definition for the specified user.

     Returns an Roblox.Api.Avatar.Models.V4.AvatarDefinition containing an
    Roblox.Api.Avatar.Models.V4.AvatarModelV4 and Roblox.Api.Avatar.Models.V4.AvatarConfigurations.
    Behavior is aligned with the V2 `GET v2/avatar/users/{userId}/avatar` endpoint.

    Args:
        user_id (int):
        selection_types (list[GetV4AvatarUsersUserIdSelectionTypesItem]):
        roblox_place_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxApiAvatarModelsV4AvatarDefinition]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        selection_types=selection_types,
        roblox_place_id=roblox_place_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: int,
    *,
    client: AuthenticatedClient,
    selection_types: list[GetV4AvatarUsersUserIdSelectionTypesItem],
    roblox_place_id: int | Unset = UNSET,
) -> Any | RobloxApiAvatarModelsV4AvatarDefinition | None:
    """Gets the currently wearing avatar definition for the specified user.

     Returns an Roblox.Api.Avatar.Models.V4.AvatarDefinition containing an
    Roblox.Api.Avatar.Models.V4.AvatarModelV4 and Roblox.Api.Avatar.Models.V4.AvatarConfigurations.
    Behavior is aligned with the V2 `GET v2/avatar/users/{userId}/avatar` endpoint.

    Args:
        user_id (int):
        selection_types (list[GetV4AvatarUsersUserIdSelectionTypesItem]):
        roblox_place_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxApiAvatarModelsV4AvatarDefinition
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        selection_types=selection_types,
        roblox_place_id=roblox_place_id,
    ).parsed


async def asyncio_detailed(
    user_id: int,
    *,
    client: AuthenticatedClient,
    selection_types: list[GetV4AvatarUsersUserIdSelectionTypesItem],
    roblox_place_id: int | Unset = UNSET,
) -> Response[Any | RobloxApiAvatarModelsV4AvatarDefinition]:
    """Gets the currently wearing avatar definition for the specified user.

     Returns an Roblox.Api.Avatar.Models.V4.AvatarDefinition containing an
    Roblox.Api.Avatar.Models.V4.AvatarModelV4 and Roblox.Api.Avatar.Models.V4.AvatarConfigurations.
    Behavior is aligned with the V2 `GET v2/avatar/users/{userId}/avatar` endpoint.

    Args:
        user_id (int):
        selection_types (list[GetV4AvatarUsersUserIdSelectionTypesItem]):
        roblox_place_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxApiAvatarModelsV4AvatarDefinition]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        selection_types=selection_types,
        roblox_place_id=roblox_place_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: int,
    *,
    client: AuthenticatedClient,
    selection_types: list[GetV4AvatarUsersUserIdSelectionTypesItem],
    roblox_place_id: int | Unset = UNSET,
) -> Any | RobloxApiAvatarModelsV4AvatarDefinition | None:
    """Gets the currently wearing avatar definition for the specified user.

     Returns an Roblox.Api.Avatar.Models.V4.AvatarDefinition containing an
    Roblox.Api.Avatar.Models.V4.AvatarModelV4 and Roblox.Api.Avatar.Models.V4.AvatarConfigurations.
    Behavior is aligned with the V2 `GET v2/avatar/users/{userId}/avatar` endpoint.

    Args:
        user_id (int):
        selection_types (list[GetV4AvatarUsersUserIdSelectionTypesItem]):
        roblox_place_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxApiAvatarModelsV4AvatarDefinition
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            selection_types=selection_types,
            roblox_place_id=roblox_place_id,
        )
    ).parsed
