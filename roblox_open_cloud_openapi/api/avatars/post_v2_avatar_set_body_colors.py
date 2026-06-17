from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_api_avatar_models_avatar_api_success_response import RobloxApiAvatarModelsAvatarApiSuccessResponse
from ...models.roblox_platform_avatar_body_colors_model_v2 import RobloxPlatformAvatarBodyColorsModelV2
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: RobloxPlatformAvatarBodyColorsModelV2 | RobloxPlatformAvatarBodyColorsModelV2 | Unset = UNSET,
    roblox_place_id: int | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(roblox_place_id, Unset):
        headers["Roblox-Place-Id"] = str(roblox_place_id)

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "https://avatar.roblox.com/v2/avatar/set-body-colors",
    }

    if isinstance(body, RobloxPlatformAvatarBodyColorsModelV2):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxPlatformAvatarBodyColorsModelV2):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxApiAvatarModelsAvatarApiSuccessResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxPlatformAvatarBodyColorsModelV2 | RobloxPlatformAvatarBodyColorsModelV2 | Unset = UNSET,
    roblox_place_id: int | Unset = UNSET,
) -> Response[Any | RobloxApiAvatarModelsAvatarApiSuccessResponse]:
    """Sets the authenticated user's body colors.

    Args:
        roblox_place_id (int | Unset):
        body (RobloxPlatformAvatarBodyColorsModelV2):
        body (RobloxPlatformAvatarBodyColorsModelV2):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxApiAvatarModelsAvatarApiSuccessResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        roblox_place_id=roblox_place_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: RobloxPlatformAvatarBodyColorsModelV2 | RobloxPlatformAvatarBodyColorsModelV2 | Unset = UNSET,
    roblox_place_id: int | Unset = UNSET,
) -> Any | RobloxApiAvatarModelsAvatarApiSuccessResponse | None:
    """Sets the authenticated user's body colors.

    Args:
        roblox_place_id (int | Unset):
        body (RobloxPlatformAvatarBodyColorsModelV2):
        body (RobloxPlatformAvatarBodyColorsModelV2):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxApiAvatarModelsAvatarApiSuccessResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        roblox_place_id=roblox_place_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxPlatformAvatarBodyColorsModelV2 | RobloxPlatformAvatarBodyColorsModelV2 | Unset = UNSET,
    roblox_place_id: int | Unset = UNSET,
) -> Response[Any | RobloxApiAvatarModelsAvatarApiSuccessResponse]:
    """Sets the authenticated user's body colors.

    Args:
        roblox_place_id (int | Unset):
        body (RobloxPlatformAvatarBodyColorsModelV2):
        body (RobloxPlatformAvatarBodyColorsModelV2):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxApiAvatarModelsAvatarApiSuccessResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        roblox_place_id=roblox_place_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RobloxPlatformAvatarBodyColorsModelV2 | RobloxPlatformAvatarBodyColorsModelV2 | Unset = UNSET,
    roblox_place_id: int | Unset = UNSET,
) -> Any | RobloxApiAvatarModelsAvatarApiSuccessResponse | None:
    """Sets the authenticated user's body colors.

    Args:
        roblox_place_id (int | Unset):
        body (RobloxPlatformAvatarBodyColorsModelV2):
        body (RobloxPlatformAvatarBodyColorsModelV2):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxApiAvatarModelsAvatarApiSuccessResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            roblox_place_id=roblox_place_id,
        )
    ).parsed
