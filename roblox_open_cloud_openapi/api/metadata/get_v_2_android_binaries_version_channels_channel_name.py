from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_client_settings_api_models_response_android_binary_response import (
    RobloxClientSettingsApiModelsResponseAndroidBinaryResponse,
)
from ...types import Response


def _get_kwargs(
    version: str,
    channel_name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://clientsettings.roblox.com/v2/android-binaries/{version}/channels/{channel_name}".format(
            version=quote(str(version), safe=""),
            channel_name=quote(str(channel_name), safe=""),
        ),
        "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
        "openapi-id": "get_v2_android-binaries_version_channels_channelName",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> RobloxClientSettingsApiModelsResponseAndroidBinaryResponse | None:
    if response.status_code == 200:
        response_200 = RobloxClientSettingsApiModelsResponseAndroidBinaryResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[RobloxClientSettingsApiModelsResponseAndroidBinaryResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    version: str,
    channel_name: str,
    *,
    client: AuthenticatedClient,
) -> Response[RobloxClientSettingsApiModelsResponseAndroidBinaryResponse]:
    """Retrieve the Android binary information for a given version and channel name.

    Args:
        version (str):
        channel_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RobloxClientSettingsApiModelsResponseAndroidBinaryResponse]
    """

    kwargs = _get_kwargs(
        version=version,
        channel_name=channel_name,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    version: str,
    channel_name: str,
    *,
    client: AuthenticatedClient,
) -> RobloxClientSettingsApiModelsResponseAndroidBinaryResponse | None:
    """Retrieve the Android binary information for a given version and channel name.

    Args:
        version (str):
        channel_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RobloxClientSettingsApiModelsResponseAndroidBinaryResponse
    """

    return sync_detailed(
        version=version,
        channel_name=channel_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    version: str,
    channel_name: str,
    *,
    client: AuthenticatedClient,
) -> Response[RobloxClientSettingsApiModelsResponseAndroidBinaryResponse]:
    """Retrieve the Android binary information for a given version and channel name.

    Args:
        version (str):
        channel_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RobloxClientSettingsApiModelsResponseAndroidBinaryResponse]
    """

    kwargs = _get_kwargs(
        version=version,
        channel_name=channel_name,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    version: str,
    channel_name: str,
    *,
    client: AuthenticatedClient,
) -> RobloxClientSettingsApiModelsResponseAndroidBinaryResponse | None:
    """Retrieve the Android binary information for a given version and channel name.

    Args:
        version (str):
        channel_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RobloxClientSettingsApiModelsResponseAndroidBinaryResponse
    """

    return (
        await asyncio_detailed(
            version=version,
            channel_name=channel_name,
            client=client,
        )
    ).parsed
