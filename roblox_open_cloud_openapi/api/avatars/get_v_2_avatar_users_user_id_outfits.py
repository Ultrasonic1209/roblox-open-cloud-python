from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_api_avatar_models_avatar_page_response_roblox_api_avatar_models_outfit_model import (
    RobloxApiAvatarModelsAvatarPageResponseRobloxApiAvatarModelsOutfitModel,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: int,
    *,
    pagination_token: str | Unset = "",
    outfit_type: str | Unset = UNSET,
    page: int | Unset = 1,
    items_per_page: int | Unset = 25,
    is_editable: bool | Unset = UNSET,
    roblox_place_id: int | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(roblox_place_id, Unset):
        headers["Roblox-Place-Id"] = str(roblox_place_id)

    params: dict[str, Any] = {}

    params["paginationToken"] = pagination_token

    params["outfitType"] = outfit_type

    params["page"] = page

    params["itemsPerPage"] = items_per_page

    params["isEditable"] = is_editable

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://avatar.roblox.com/v2/avatar/users/{user_id}/outfits".format(
            user_id=quote(str(user_id), safe=""),
        ),
        "params": params,
        "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
        "openapi-id": "get_v2_avatar_users_userId_outfits",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxApiAvatarModelsAvatarPageResponseRobloxApiAvatarModelsOutfitModel | None:
    if response.status_code == 200:
        response_200 = RobloxApiAvatarModelsAvatarPageResponseRobloxApiAvatarModelsOutfitModel.from_dict(
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
) -> Response[Any | RobloxApiAvatarModelsAvatarPageResponseRobloxApiAvatarModelsOutfitModel]:
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
    pagination_token: str | Unset = "",
    outfit_type: str | Unset = UNSET,
    page: int | Unset = 1,
    items_per_page: int | Unset = 25,
    is_editable: bool | Unset = UNSET,
    roblox_place_id: int | Unset = UNSET,
) -> Response[Any | RobloxApiAvatarModelsAvatarPageResponseRobloxApiAvatarModelsOutfitModel]:
    """Gets a list of outfits for the specified user.

    Args:
        user_id (int):
        pagination_token (str | Unset):  Default: ''.
        outfit_type (str | Unset):
        page (int | Unset):  Default: 1.
        items_per_page (int | Unset):  Default: 25.
        is_editable (bool | Unset):
        roblox_place_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxApiAvatarModelsAvatarPageResponseRobloxApiAvatarModelsOutfitModel]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        pagination_token=pagination_token,
        outfit_type=outfit_type,
        page=page,
        items_per_page=items_per_page,
        is_editable=is_editable,
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
    pagination_token: str | Unset = "",
    outfit_type: str | Unset = UNSET,
    page: int | Unset = 1,
    items_per_page: int | Unset = 25,
    is_editable: bool | Unset = UNSET,
    roblox_place_id: int | Unset = UNSET,
) -> Any | RobloxApiAvatarModelsAvatarPageResponseRobloxApiAvatarModelsOutfitModel | None:
    """Gets a list of outfits for the specified user.

    Args:
        user_id (int):
        pagination_token (str | Unset):  Default: ''.
        outfit_type (str | Unset):
        page (int | Unset):  Default: 1.
        items_per_page (int | Unset):  Default: 25.
        is_editable (bool | Unset):
        roblox_place_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxApiAvatarModelsAvatarPageResponseRobloxApiAvatarModelsOutfitModel
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        pagination_token=pagination_token,
        outfit_type=outfit_type,
        page=page,
        items_per_page=items_per_page,
        is_editable=is_editable,
        roblox_place_id=roblox_place_id,
    ).parsed


async def asyncio_detailed(
    user_id: int,
    *,
    client: AuthenticatedClient,
    pagination_token: str | Unset = "",
    outfit_type: str | Unset = UNSET,
    page: int | Unset = 1,
    items_per_page: int | Unset = 25,
    is_editable: bool | Unset = UNSET,
    roblox_place_id: int | Unset = UNSET,
) -> Response[Any | RobloxApiAvatarModelsAvatarPageResponseRobloxApiAvatarModelsOutfitModel]:
    """Gets a list of outfits for the specified user.

    Args:
        user_id (int):
        pagination_token (str | Unset):  Default: ''.
        outfit_type (str | Unset):
        page (int | Unset):  Default: 1.
        items_per_page (int | Unset):  Default: 25.
        is_editable (bool | Unset):
        roblox_place_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxApiAvatarModelsAvatarPageResponseRobloxApiAvatarModelsOutfitModel]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        pagination_token=pagination_token,
        outfit_type=outfit_type,
        page=page,
        items_per_page=items_per_page,
        is_editable=is_editable,
        roblox_place_id=roblox_place_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: int,
    *,
    client: AuthenticatedClient,
    pagination_token: str | Unset = "",
    outfit_type: str | Unset = UNSET,
    page: int | Unset = 1,
    items_per_page: int | Unset = 25,
    is_editable: bool | Unset = UNSET,
    roblox_place_id: int | Unset = UNSET,
) -> Any | RobloxApiAvatarModelsAvatarPageResponseRobloxApiAvatarModelsOutfitModel | None:
    """Gets a list of outfits for the specified user.

    Args:
        user_id (int):
        pagination_token (str | Unset):  Default: ''.
        outfit_type (str | Unset):
        page (int | Unset):  Default: 1.
        items_per_page (int | Unset):  Default: 25.
        is_editable (bool | Unset):
        roblox_place_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxApiAvatarModelsAvatarPageResponseRobloxApiAvatarModelsOutfitModel
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            pagination_token=pagination_token,
            outfit_type=outfit_type,
            page=page,
            items_per_page=items_per_page,
            is_editable=is_editable,
            roblox_place_id=roblox_place_id,
        )
    ).parsed
