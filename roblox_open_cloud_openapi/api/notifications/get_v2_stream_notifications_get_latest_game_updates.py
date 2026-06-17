import datetime
from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_api_notifications_models_game_update_notification_model import (
    RobloxApiNotificationsModelsGameUpdateNotificationModel,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    universe_ids: list[int],
    since_date_time: datetime.datetime | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_universe_ids = universe_ids

    params["universeIds"] = json_universe_ids

    json_since_date_time: str | Unset = UNSET
    if not isinstance(since_date_time, Unset):
        json_since_date_time = since_date_time.isoformat()
    params["sinceDateTime"] = json_since_date_time

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://notifications.roblox.com/v2/stream-notifications/get-latest-game-updates",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | list[RobloxApiNotificationsModelsGameUpdateNotificationModel] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = RobloxApiNotificationsModelsGameUpdateNotificationModel.from_dict(
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
) -> Response[Any | list[RobloxApiNotificationsModelsGameUpdateNotificationModel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    universe_ids: list[int],
    since_date_time: datetime.datetime | Unset = UNSET,
) -> Response[Any | list[RobloxApiNotificationsModelsGameUpdateNotificationModel]]:
    """Get the latest non aggregated Game Updates sent to the logged in user

    Args:
        universe_ids (list[int]):
        since_date_time (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[RobloxApiNotificationsModelsGameUpdateNotificationModel]]
    """

    kwargs = _get_kwargs(
        universe_ids=universe_ids,
        since_date_time=since_date_time,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    universe_ids: list[int],
    since_date_time: datetime.datetime | Unset = UNSET,
) -> Any | list[RobloxApiNotificationsModelsGameUpdateNotificationModel] | None:
    """Get the latest non aggregated Game Updates sent to the logged in user

    Args:
        universe_ids (list[int]):
        since_date_time (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[RobloxApiNotificationsModelsGameUpdateNotificationModel]
    """

    return sync_detailed(
        client=client,
        universe_ids=universe_ids,
        since_date_time=since_date_time,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    universe_ids: list[int],
    since_date_time: datetime.datetime | Unset = UNSET,
) -> Response[Any | list[RobloxApiNotificationsModelsGameUpdateNotificationModel]]:
    """Get the latest non aggregated Game Updates sent to the logged in user

    Args:
        universe_ids (list[int]):
        since_date_time (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[RobloxApiNotificationsModelsGameUpdateNotificationModel]]
    """

    kwargs = _get_kwargs(
        universe_ids=universe_ids,
        since_date_time=since_date_time,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    universe_ids: list[int],
    since_date_time: datetime.datetime | Unset = UNSET,
) -> Any | list[RobloxApiNotificationsModelsGameUpdateNotificationModel] | None:
    """Get the latest non aggregated Game Updates sent to the logged in user

    Args:
        universe_ids (list[int]):
        since_date_time (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[RobloxApiNotificationsModelsGameUpdateNotificationModel]
    """

    return (
        await asyncio_detailed(
            client=client,
            universe_ids=universe_ids,
            since_date_time=since_date_time,
        )
    ).parsed
