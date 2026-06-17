from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_api_avatar_models_outfit_model import RobloxApiAvatarModelsOutfitModel
from ...models.roblox_api_avatar_models_outfit_update_model_v3 import RobloxApiAvatarModelsOutfitUpdateModelV3
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_outfit_id: int,
    *,
    body: RobloxApiAvatarModelsOutfitUpdateModelV3 | RobloxApiAvatarModelsOutfitUpdateModelV3 | Unset = UNSET,
    roblox_place_id: int | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(roblox_place_id, Unset):
        headers["Roblox-Place-Id"] = str(roblox_place_id)

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "https://avatar.roblox.com/v3/outfits/{user_outfit_id}".format(
            user_outfit_id=quote(str(user_outfit_id), safe=""),
        ),
    }

    if isinstance(body, RobloxApiAvatarModelsOutfitUpdateModelV3):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxApiAvatarModelsOutfitUpdateModelV3):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxApiAvatarModelsOutfitModel | None:
    if response.status_code == 200:
        response_200 = RobloxApiAvatarModelsOutfitModel.from_dict(response.json())

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

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxApiAvatarModelsOutfitModel]:
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
    body: RobloxApiAvatarModelsOutfitUpdateModelV3 | RobloxApiAvatarModelsOutfitUpdateModelV3 | Unset = UNSET,
    roblox_place_id: int | Unset = UNSET,
) -> Response[Any | RobloxApiAvatarModelsOutfitModel]:
    """Updates the contents of an outfit.

     Fails if the user does not own any of the assetIds or if they are not wearable asset types.
    Accepts partial updates.

    Args:
        user_outfit_id (int):
        roblox_place_id (int | Unset):
        body (RobloxApiAvatarModelsOutfitUpdateModelV3): A model containing details needed to
            update or create an outfit.
        body (RobloxApiAvatarModelsOutfitUpdateModelV3): A model containing details needed to
            update or create an outfit.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxApiAvatarModelsOutfitModel]
    """

    kwargs = _get_kwargs(
        user_outfit_id=user_outfit_id,
        body=body,
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
    body: RobloxApiAvatarModelsOutfitUpdateModelV3 | RobloxApiAvatarModelsOutfitUpdateModelV3 | Unset = UNSET,
    roblox_place_id: int | Unset = UNSET,
) -> Any | RobloxApiAvatarModelsOutfitModel | None:
    """Updates the contents of an outfit.

     Fails if the user does not own any of the assetIds or if they are not wearable asset types.
    Accepts partial updates.

    Args:
        user_outfit_id (int):
        roblox_place_id (int | Unset):
        body (RobloxApiAvatarModelsOutfitUpdateModelV3): A model containing details needed to
            update or create an outfit.
        body (RobloxApiAvatarModelsOutfitUpdateModelV3): A model containing details needed to
            update or create an outfit.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxApiAvatarModelsOutfitModel
    """

    return sync_detailed(
        user_outfit_id=user_outfit_id,
        client=client,
        body=body,
        roblox_place_id=roblox_place_id,
    ).parsed


async def asyncio_detailed(
    user_outfit_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxApiAvatarModelsOutfitUpdateModelV3 | RobloxApiAvatarModelsOutfitUpdateModelV3 | Unset = UNSET,
    roblox_place_id: int | Unset = UNSET,
) -> Response[Any | RobloxApiAvatarModelsOutfitModel]:
    """Updates the contents of an outfit.

     Fails if the user does not own any of the assetIds or if they are not wearable asset types.
    Accepts partial updates.

    Args:
        user_outfit_id (int):
        roblox_place_id (int | Unset):
        body (RobloxApiAvatarModelsOutfitUpdateModelV3): A model containing details needed to
            update or create an outfit.
        body (RobloxApiAvatarModelsOutfitUpdateModelV3): A model containing details needed to
            update or create an outfit.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxApiAvatarModelsOutfitModel]
    """

    kwargs = _get_kwargs(
        user_outfit_id=user_outfit_id,
        body=body,
        roblox_place_id=roblox_place_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_outfit_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxApiAvatarModelsOutfitUpdateModelV3 | RobloxApiAvatarModelsOutfitUpdateModelV3 | Unset = UNSET,
    roblox_place_id: int | Unset = UNSET,
) -> Any | RobloxApiAvatarModelsOutfitModel | None:
    """Updates the contents of an outfit.

     Fails if the user does not own any of the assetIds or if they are not wearable asset types.
    Accepts partial updates.

    Args:
        user_outfit_id (int):
        roblox_place_id (int | Unset):
        body (RobloxApiAvatarModelsOutfitUpdateModelV3): A model containing details needed to
            update or create an outfit.
        body (RobloxApiAvatarModelsOutfitUpdateModelV3): A model containing details needed to
            update or create an outfit.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxApiAvatarModelsOutfitModel
    """

    return (
        await asyncio_detailed(
            user_outfit_id=user_outfit_id,
            client=client,
            body=body,
            roblox_place_id=roblox_place_id,
        )
    ).parsed
