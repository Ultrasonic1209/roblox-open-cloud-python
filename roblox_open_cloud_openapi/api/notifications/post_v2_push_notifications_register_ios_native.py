from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_api_notifications_models_register_ios_native_request_model import (
    RobloxApiNotificationsModelsRegisterIOSNativeRequestModel,
)
from ...models.roblox_api_notifications_models_registration_response_model import (
    RobloxApiNotificationsModelsRegistrationResponseModel,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: RobloxApiNotificationsModelsRegisterIOSNativeRequestModel
    | RobloxApiNotificationsModelsRegisterIOSNativeRequestModel
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "https://notifications.roblox.com/v2/push-notifications/register-ios-native",
        "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
        "openapi-id": "post_v2_push-notifications_register-ios-native",
    }

    if isinstance(body, RobloxApiNotificationsModelsRegisterIOSNativeRequestModel):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxApiNotificationsModelsRegisterIOSNativeRequestModel):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxApiNotificationsModelsRegistrationResponseModel | None:
    if response.status_code == 200:
        response_200 = RobloxApiNotificationsModelsRegistrationResponseModel.from_dict(response.json())

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
) -> Response[Any | RobloxApiNotificationsModelsRegistrationResponseModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxApiNotificationsModelsRegisterIOSNativeRequestModel
    | RobloxApiNotificationsModelsRegisterIOSNativeRequestModel
    | Unset = UNSET,
) -> Response[Any | RobloxApiNotificationsModelsRegistrationResponseModel]:
    """Registers IOS device for push notifications

    Args:
        body (RobloxApiNotificationsModelsRegisterIOSNativeRequestModel):
        body (RobloxApiNotificationsModelsRegisterIOSNativeRequestModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxApiNotificationsModelsRegistrationResponseModel]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: RobloxApiNotificationsModelsRegisterIOSNativeRequestModel
    | RobloxApiNotificationsModelsRegisterIOSNativeRequestModel
    | Unset = UNSET,
) -> Any | RobloxApiNotificationsModelsRegistrationResponseModel | None:
    """Registers IOS device for push notifications

    Args:
        body (RobloxApiNotificationsModelsRegisterIOSNativeRequestModel):
        body (RobloxApiNotificationsModelsRegisterIOSNativeRequestModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxApiNotificationsModelsRegistrationResponseModel
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxApiNotificationsModelsRegisterIOSNativeRequestModel
    | RobloxApiNotificationsModelsRegisterIOSNativeRequestModel
    | Unset = UNSET,
) -> Response[Any | RobloxApiNotificationsModelsRegistrationResponseModel]:
    """Registers IOS device for push notifications

    Args:
        body (RobloxApiNotificationsModelsRegisterIOSNativeRequestModel):
        body (RobloxApiNotificationsModelsRegisterIOSNativeRequestModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxApiNotificationsModelsRegistrationResponseModel]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RobloxApiNotificationsModelsRegisterIOSNativeRequestModel
    | RobloxApiNotificationsModelsRegisterIOSNativeRequestModel
    | Unset = UNSET,
) -> Any | RobloxApiNotificationsModelsRegistrationResponseModel | None:
    """Registers IOS device for push notifications

    Args:
        body (RobloxApiNotificationsModelsRegisterIOSNativeRequestModel):
        body (RobloxApiNotificationsModelsRegisterIOSNativeRequestModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxApiNotificationsModelsRegistrationResponseModel
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
