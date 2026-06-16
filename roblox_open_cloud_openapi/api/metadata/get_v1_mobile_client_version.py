from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_client_settings_api_models_response_mobile_client_version_response import (
    RobloxClientSettingsApiModelsResponseMobileClientVersionResponse,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    app_version: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["appVersion"] = app_version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/mobile-client-version",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxClientSettingsApiModelsResponseMobileClientVersionResponse | None:
    if response.status_code == 200:
        response_200 = RobloxClientSettingsApiModelsResponseMobileClientVersionResponse.from_dict(response.json())

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
) -> Response[Any | RobloxClientSettingsApiModelsResponseMobileClientVersionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    app_version: str,
) -> Response[Any | RobloxClientSettingsApiModelsResponseMobileClientVersionResponse]:
    """Get mobile client version information based on app version parameter

    Args:
        app_version (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxClientSettingsApiModelsResponseMobileClientVersionResponse]
    """

    kwargs = _get_kwargs(
        app_version=app_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    app_version: str,
) -> Any | RobloxClientSettingsApiModelsResponseMobileClientVersionResponse | None:
    """Get mobile client version information based on app version parameter

    Args:
        app_version (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxClientSettingsApiModelsResponseMobileClientVersionResponse
    """

    return sync_detailed(
        client=client,
        app_version=app_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    app_version: str,
) -> Response[Any | RobloxClientSettingsApiModelsResponseMobileClientVersionResponse]:
    """Get mobile client version information based on app version parameter

    Args:
        app_version (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxClientSettingsApiModelsResponseMobileClientVersionResponse]
    """

    kwargs = _get_kwargs(
        app_version=app_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    app_version: str,
) -> Any | RobloxClientSettingsApiModelsResponseMobileClientVersionResponse | None:
    """Get mobile client version information based on app version parameter

    Args:
        app_version (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxClientSettingsApiModelsResponseMobileClientVersionResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            app_version=app_version,
        )
    ).parsed
