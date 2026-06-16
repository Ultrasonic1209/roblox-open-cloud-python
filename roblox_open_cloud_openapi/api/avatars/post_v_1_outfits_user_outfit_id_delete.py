from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_api_avatar_models_avatar_api_success_response import RobloxApiAvatarModelsAvatarApiSuccessResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_outfit_id: int,
    *,
    roblox_place_id: int | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(roblox_place_id, Unset):
        headers["Roblox-Place-Id"] = str(roblox_place_id)

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/outfits/{user_outfit_id}/delete".format(
            user_outfit_id=quote(str(user_outfit_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxApiAvatarModelsAvatarApiSuccessResponse | None:
    if response.status_code == 200:
        response_200 = RobloxApiAvatarModelsAvatarApiSuccessResponse.from_dict(response.json())

        return response_200

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
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RobloxApiAvatarModelsAvatarApiSuccessResponse]:
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
    roblox_place_id: int | Unset = UNSET,
) -> Response[Any | RobloxApiAvatarModelsAvatarApiSuccessResponse]:
    """Deletes the outfit.

     You are only allowed to delete outfits you created.

    Args:
        user_outfit_id (int):
        roblox_place_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxApiAvatarModelsAvatarApiSuccessResponse]
    """

    kwargs = _get_kwargs(
        user_outfit_id=user_outfit_id,
        roblox_place_id=roblox_place_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_outfit_id: int,
    *,
    client: AuthenticatedClient,
    roblox_place_id: int | Unset = UNSET,
) -> Any | RobloxApiAvatarModelsAvatarApiSuccessResponse | None:
    """Deletes the outfit.

     You are only allowed to delete outfits you created.

    Args:
        user_outfit_id (int):
        roblox_place_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxApiAvatarModelsAvatarApiSuccessResponse
    """

    return sync_detailed(
        user_outfit_id=user_outfit_id,
        client=client,
        roblox_place_id=roblox_place_id,
    ).parsed


async def asyncio_detailed(
    user_outfit_id: int,
    *,
    client: AuthenticatedClient,
    roblox_place_id: int | Unset = UNSET,
) -> Response[Any | RobloxApiAvatarModelsAvatarApiSuccessResponse]:
    """Deletes the outfit.

     You are only allowed to delete outfits you created.

    Args:
        user_outfit_id (int):
        roblox_place_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxApiAvatarModelsAvatarApiSuccessResponse]
    """

    kwargs = _get_kwargs(
        user_outfit_id=user_outfit_id,
        roblox_place_id=roblox_place_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_outfit_id: int,
    *,
    client: AuthenticatedClient,
    roblox_place_id: int | Unset = UNSET,
) -> Any | RobloxApiAvatarModelsAvatarApiSuccessResponse | None:
    """Deletes the outfit.

     You are only allowed to delete outfits you created.

    Args:
        user_outfit_id (int):
        roblox_place_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxApiAvatarModelsAvatarApiSuccessResponse
    """

    return (
        await asyncio_detailed(
            user_outfit_id=user_outfit_id,
            client=client,
            roblox_place_id=roblox_place_id,
        )
    ).parsed
