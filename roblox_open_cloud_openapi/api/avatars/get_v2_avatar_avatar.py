from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_api_avatar_models_avatar_model_v3 import RobloxApiAvatarModelsAvatarModelV3
from ...types import UNSET, Response, Unset


def _get_kwargs(
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
        "url": "https://avatar.roblox.com/v2/avatar/avatar",
        "params": params,
        "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
        "openapi-id": "get_v2_avatar_avatar",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxApiAvatarModelsAvatarModelV3 | None:
    if response.status_code == 200:
        response_200 = RobloxApiAvatarModelsAvatarModelV3.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxApiAvatarModelsAvatarModelV3]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    check_asset_availability: bool | Unset = False,
    roblox_place_id: int | Unset = UNSET,
) -> Response[Any | RobloxApiAvatarModelsAvatarModelV3]:
    """Returns details about the authenticated user's avatar.

    Args:
        check_asset_availability (bool | Unset):  Default: False.
        roblox_place_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxApiAvatarModelsAvatarModelV3]
    """

    kwargs = _get_kwargs(
        check_asset_availability=check_asset_availability,
        roblox_place_id=roblox_place_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    check_asset_availability: bool | Unset = False,
    roblox_place_id: int | Unset = UNSET,
) -> Any | RobloxApiAvatarModelsAvatarModelV3 | None:
    """Returns details about the authenticated user's avatar.

    Args:
        check_asset_availability (bool | Unset):  Default: False.
        roblox_place_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxApiAvatarModelsAvatarModelV3
    """

    return sync_detailed(
        client=client,
        check_asset_availability=check_asset_availability,
        roblox_place_id=roblox_place_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    check_asset_availability: bool | Unset = False,
    roblox_place_id: int | Unset = UNSET,
) -> Response[Any | RobloxApiAvatarModelsAvatarModelV3]:
    """Returns details about the authenticated user's avatar.

    Args:
        check_asset_availability (bool | Unset):  Default: False.
        roblox_place_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxApiAvatarModelsAvatarModelV3]
    """

    kwargs = _get_kwargs(
        check_asset_availability=check_asset_availability,
        roblox_place_id=roblox_place_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    check_asset_availability: bool | Unset = False,
    roblox_place_id: int | Unset = UNSET,
) -> Any | RobloxApiAvatarModelsAvatarModelV3 | None:
    """Returns details about the authenticated user's avatar.

    Args:
        check_asset_availability (bool | Unset):  Default: False.
        roblox_place_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxApiAvatarModelsAvatarModelV3
    """

    return (
        await asyncio_detailed(
            client=client,
            check_asset_availability=check_asset_availability,
            roblox_place_id=roblox_place_id,
        )
    ).parsed
