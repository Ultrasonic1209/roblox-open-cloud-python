from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_api_avatar_models_avatar_model_v2 import RobloxApiAvatarModelsAvatarModelV2
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: int,
    *,
    roblox_place_id: int | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(roblox_place_id, Unset):
        headers["Roblox-Place-Id"] = str(roblox_place_id)

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/users/{user_id}/avatar".format(
            user_id=quote(str(user_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxApiAvatarModelsAvatarModelV2 | None:
    if response.status_code == 200:
        response_200 = RobloxApiAvatarModelsAvatarModelV2.from_dict(response.json())

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
) -> Response[Any | RobloxApiAvatarModelsAvatarModelV2]:
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
    roblox_place_id: int | Unset = UNSET,
) -> Response[Any | RobloxApiAvatarModelsAvatarModelV2]:
    """Returns details about a specified user's avatar.

     Includes assets, bodycolors, and playerAvatarType.

    Args:
        user_id (int):
        roblox_place_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxApiAvatarModelsAvatarModelV2]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        roblox_place_id=roblox_place_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: int,
    *,
    client: AuthenticatedClient,
    roblox_place_id: int | Unset = UNSET,
) -> Any | RobloxApiAvatarModelsAvatarModelV2 | None:
    """Returns details about a specified user's avatar.

     Includes assets, bodycolors, and playerAvatarType.

    Args:
        user_id (int):
        roblox_place_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxApiAvatarModelsAvatarModelV2
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        roblox_place_id=roblox_place_id,
    ).parsed


async def asyncio_detailed(
    user_id: int,
    *,
    client: AuthenticatedClient,
    roblox_place_id: int | Unset = UNSET,
) -> Response[Any | RobloxApiAvatarModelsAvatarModelV2]:
    """Returns details about a specified user's avatar.

     Includes assets, bodycolors, and playerAvatarType.

    Args:
        user_id (int):
        roblox_place_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxApiAvatarModelsAvatarModelV2]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        roblox_place_id=roblox_place_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: int,
    *,
    client: AuthenticatedClient,
    roblox_place_id: int | Unset = UNSET,
) -> Any | RobloxApiAvatarModelsAvatarModelV2 | None:
    """Returns details about a specified user's avatar.

     Includes assets, bodycolors, and playerAvatarType.

    Args:
        user_id (int):
        roblox_place_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxApiAvatarModelsAvatarModelV2
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            roblox_place_id=roblox_place_id,
        )
    ).parsed
