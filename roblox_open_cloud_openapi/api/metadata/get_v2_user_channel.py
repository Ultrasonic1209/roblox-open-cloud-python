from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_client_settings_api_models_response_user_channel_response import (
    RobloxClientSettingsApiModelsResponseUserChannelResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    binary_type: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["binaryType"] = binary_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://clientsettings.roblox.com/v2/user-channel",
        "params": params,
        "extensions": {
            "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
            "openapi-id": "get_v2_user-channel",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> RobloxClientSettingsApiModelsResponseUserChannelResponse | None:
    if response.status_code == 200:
        response_200 = RobloxClientSettingsApiModelsResponseUserChannelResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[RobloxClientSettingsApiModelsResponseUserChannelResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    binary_type: str | Unset = UNSET,
) -> Response[RobloxClientSettingsApiModelsResponseUserChannelResponse]:
    """Get channel name for currently logged in user

    Args:
        binary_type (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RobloxClientSettingsApiModelsResponseUserChannelResponse]
    """

    kwargs = _get_kwargs(
        binary_type=binary_type,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    binary_type: str | Unset = UNSET,
) -> RobloxClientSettingsApiModelsResponseUserChannelResponse | None:
    """Get channel name for currently logged in user

    Args:
        binary_type (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RobloxClientSettingsApiModelsResponseUserChannelResponse
    """

    return sync_detailed(
        client=client,
        binary_type=binary_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    binary_type: str | Unset = UNSET,
) -> Response[RobloxClientSettingsApiModelsResponseUserChannelResponse]:
    """Get channel name for currently logged in user

    Args:
        binary_type (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RobloxClientSettingsApiModelsResponseUserChannelResponse]
    """

    kwargs = _get_kwargs(
        binary_type=binary_type,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    binary_type: str | Unset = UNSET,
) -> RobloxClientSettingsApiModelsResponseUserChannelResponse | None:
    """Get channel name for currently logged in user

    Args:
        binary_type (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RobloxClientSettingsApiModelsResponseUserChannelResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            binary_type=binary_type,
        )
    ).parsed
