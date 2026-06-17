from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_api_notifications_models_get_metadata_response_model import (
    RobloxApiNotificationsModelsGetMetadataResponseModel,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    notification_token: str,
    notification_id: UUID,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["notificationToken"] = notification_token

    json_notification_id = str(notification_id)
    params["notificationId"] = json_notification_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://notifications.roblox.com/v2/push-notifications/metadata",
        "params": params,
        "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
        "openapi-id": "get_v2_push-notifications_metadata",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxApiNotificationsModelsGetMetadataResponseModel | None:
    if response.status_code == 200:
        response_200 = RobloxApiNotificationsModelsGetMetadataResponseModel.from_dict(response.json())

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
) -> Response[Any | RobloxApiNotificationsModelsGetMetadataResponseModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    notification_token: str,
    notification_id: UUID,
) -> Response[Any | RobloxApiNotificationsModelsGetMetadataResponseModel]:
    """Gets the corresponding metadata for the specified notification

    Args:
        notification_token (str):
        notification_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxApiNotificationsModelsGetMetadataResponseModel]
    """

    kwargs = _get_kwargs(
        notification_token=notification_token,
        notification_id=notification_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    notification_token: str,
    notification_id: UUID,
) -> Any | RobloxApiNotificationsModelsGetMetadataResponseModel | None:
    """Gets the corresponding metadata for the specified notification

    Args:
        notification_token (str):
        notification_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxApiNotificationsModelsGetMetadataResponseModel
    """

    return sync_detailed(
        client=client,
        notification_token=notification_token,
        notification_id=notification_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    notification_token: str,
    notification_id: UUID,
) -> Response[Any | RobloxApiNotificationsModelsGetMetadataResponseModel]:
    """Gets the corresponding metadata for the specified notification

    Args:
        notification_token (str):
        notification_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxApiNotificationsModelsGetMetadataResponseModel]
    """

    kwargs = _get_kwargs(
        notification_token=notification_token,
        notification_id=notification_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    notification_token: str,
    notification_id: UUID,
) -> Any | RobloxApiNotificationsModelsGetMetadataResponseModel | None:
    """Gets the corresponding metadata for the specified notification

    Args:
        notification_token (str):
        notification_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxApiNotificationsModelsGetMetadataResponseModel
    """

    return (
        await asyncio_detailed(
            client=client,
            notification_token=notification_token,
            notification_id=notification_id,
        )
    ).parsed
