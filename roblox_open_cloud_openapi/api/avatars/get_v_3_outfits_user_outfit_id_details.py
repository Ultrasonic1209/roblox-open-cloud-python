from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_api_avatar_models_outfit_details_model_v2 import RobloxApiAvatarModelsOutfitDetailsModelV2
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_outfit_id: int,
    *,
    check_asset_availability: bool | Unset = False,
    roblox_place_id: int | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(roblox_place_id, Unset):
        headers["Roblox-Place-Id"] = str(roblox_place_id)

    params: dict[str, Any] = {}

    params["checkAssetAvailability"] = check_asset_availability

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://avatar.roblox.com/v3/outfits/{user_outfit_id}/details".format(
            user_outfit_id=quote(str(user_outfit_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxApiAvatarModelsOutfitDetailsModelV2 | None:
    if response.status_code == 200:
        response_200 = RobloxApiAvatarModelsOutfitDetailsModelV2.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxApiAvatarModelsOutfitDetailsModelV2]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_outfit_id: int,
    *,
    client: AuthenticatedClient,
    check_asset_availability: bool | Unset = False,
    roblox_place_id: int | Unset = UNSET,
) -> Response[Any | RobloxApiAvatarModelsOutfitDetailsModelV2]:
    """Gets details about the contents of an outfit.

    Args:
        user_outfit_id (int):
        check_asset_availability (bool | Unset):  Default: False.
        roblox_place_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxApiAvatarModelsOutfitDetailsModelV2]
    """

    kwargs = _get_kwargs(
        user_outfit_id=user_outfit_id,
        check_asset_availability=check_asset_availability,
        roblox_place_id=roblox_place_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_outfit_id: int,
    *,
    client: AuthenticatedClient,
    check_asset_availability: bool | Unset = False,
    roblox_place_id: int | Unset = UNSET,
) -> Any | RobloxApiAvatarModelsOutfitDetailsModelV2 | None:
    """Gets details about the contents of an outfit.

    Args:
        user_outfit_id (int):
        check_asset_availability (bool | Unset):  Default: False.
        roblox_place_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxApiAvatarModelsOutfitDetailsModelV2
    """

    return sync_detailed(
        user_outfit_id=user_outfit_id,
        client=client,
        check_asset_availability=check_asset_availability,
        roblox_place_id=roblox_place_id,
    ).parsed


async def asyncio_detailed(
    user_outfit_id: int,
    *,
    client: AuthenticatedClient,
    check_asset_availability: bool | Unset = False,
    roblox_place_id: int | Unset = UNSET,
) -> Response[Any | RobloxApiAvatarModelsOutfitDetailsModelV2]:
    """Gets details about the contents of an outfit.

    Args:
        user_outfit_id (int):
        check_asset_availability (bool | Unset):  Default: False.
        roblox_place_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxApiAvatarModelsOutfitDetailsModelV2]
    """

    kwargs = _get_kwargs(
        user_outfit_id=user_outfit_id,
        check_asset_availability=check_asset_availability,
        roblox_place_id=roblox_place_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_outfit_id: int,
    *,
    client: AuthenticatedClient,
    check_asset_availability: bool | Unset = False,
    roblox_place_id: int | Unset = UNSET,
) -> Any | RobloxApiAvatarModelsOutfitDetailsModelV2 | None:
    """Gets details about the contents of an outfit.

    Args:
        user_outfit_id (int):
        check_asset_availability (bool | Unset):  Default: False.
        roblox_place_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxApiAvatarModelsOutfitDetailsModelV2
    """

    return (
        await asyncio_detailed(
            user_outfit_id=user_outfit_id,
            client=client,
            check_asset_availability=check_asset_availability,
            roblox_place_id=roblox_place_id,
        )
    ).parsed
