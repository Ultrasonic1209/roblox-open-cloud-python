from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_api_notifications_models_notification_stream_entries_model import (
    RobloxApiNotificationsModelsNotificationStreamEntriesModel,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    start_index: int | Unset = 0,
    max_rows: int | Unset = 10,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["startIndex"] = start_index

    params["maxRows"] = max_rows

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://notifications.roblox.com/v2/stream-notifications/get-recent",
        "params": params,
        "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
        "openapi-id": "get_v2_stream-notifications_get-recent",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | list[RobloxApiNotificationsModelsNotificationStreamEntriesModel] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = RobloxApiNotificationsModelsNotificationStreamEntriesModel.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

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
) -> Response[Any | list[RobloxApiNotificationsModelsNotificationStreamEntriesModel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    start_index: int | Unset = 0,
    max_rows: int | Unset = 10,
) -> Response[Any | list[RobloxApiNotificationsModelsNotificationStreamEntriesModel]]:
    """Gets the recent entries from the notification stream

    Args:
        start_index (int | Unset):  Default: 0.
        max_rows (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[RobloxApiNotificationsModelsNotificationStreamEntriesModel]]
    """

    kwargs = _get_kwargs(
        start_index=start_index,
        max_rows=max_rows,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    start_index: int | Unset = 0,
    max_rows: int | Unset = 10,
) -> Any | list[RobloxApiNotificationsModelsNotificationStreamEntriesModel] | None:
    """Gets the recent entries from the notification stream

    Args:
        start_index (int | Unset):  Default: 0.
        max_rows (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[RobloxApiNotificationsModelsNotificationStreamEntriesModel]
    """

    return sync_detailed(
        client=client,
        start_index=start_index,
        max_rows=max_rows,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start_index: int | Unset = 0,
    max_rows: int | Unset = 10,
) -> Response[Any | list[RobloxApiNotificationsModelsNotificationStreamEntriesModel]]:
    """Gets the recent entries from the notification stream

    Args:
        start_index (int | Unset):  Default: 0.
        max_rows (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[RobloxApiNotificationsModelsNotificationStreamEntriesModel]]
    """

    kwargs = _get_kwargs(
        start_index=start_index,
        max_rows=max_rows,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    start_index: int | Unset = 0,
    max_rows: int | Unset = 10,
) -> Any | list[RobloxApiNotificationsModelsNotificationStreamEntriesModel] | None:
    """Gets the recent entries from the notification stream

    Args:
        start_index (int | Unset):  Default: 0.
        max_rows (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[RobloxApiNotificationsModelsNotificationStreamEntriesModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            start_index=start_index,
            max_rows=max_rows,
        )
    ).parsed
