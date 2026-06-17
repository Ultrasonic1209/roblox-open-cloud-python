from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v1_trades_trade_status_type_count_trade_status_type import (
    GetV1TradesTradeStatusTypeCountTradeStatusType,
)
from ...models.roblox_trades_api_trade_count_response import RobloxTradesApiTradeCountResponse
from ...types import Response


def _get_kwargs(
    trade_status_type: GetV1TradesTradeStatusTypeCountTradeStatusType,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://trades.roblox.com/v1/trades/{trade_status_type}/count".format(
            trade_status_type=quote(str(trade_status_type), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxTradesApiTradeCountResponse | None:
    if response.status_code == 200:
        response_200 = RobloxTradesApiTradeCountResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxTradesApiTradeCountResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    trade_status_type: GetV1TradesTradeStatusTypeCountTradeStatusType,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxTradesApiTradeCountResponse]:
    """Gets the total number of pending trades for the authenticated user.
    Inbound is the only accepted tradeStatusType.

    Args:
        trade_status_type (GetV1TradesTradeStatusTypeCountTradeStatusType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxTradesApiTradeCountResponse]
    """

    kwargs = _get_kwargs(
        trade_status_type=trade_status_type,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    trade_status_type: GetV1TradesTradeStatusTypeCountTradeStatusType,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxTradesApiTradeCountResponse | None:
    """Gets the total number of pending trades for the authenticated user.
    Inbound is the only accepted tradeStatusType.

    Args:
        trade_status_type (GetV1TradesTradeStatusTypeCountTradeStatusType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxTradesApiTradeCountResponse
    """

    return sync_detailed(
        trade_status_type=trade_status_type,
        client=client,
    ).parsed


async def asyncio_detailed(
    trade_status_type: GetV1TradesTradeStatusTypeCountTradeStatusType,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxTradesApiTradeCountResponse]:
    """Gets the total number of pending trades for the authenticated user.
    Inbound is the only accepted tradeStatusType.

    Args:
        trade_status_type (GetV1TradesTradeStatusTypeCountTradeStatusType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxTradesApiTradeCountResponse]
    """

    kwargs = _get_kwargs(
        trade_status_type=trade_status_type,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    trade_status_type: GetV1TradesTradeStatusTypeCountTradeStatusType,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxTradesApiTradeCountResponse | None:
    """Gets the total number of pending trades for the authenticated user.
    Inbound is the only accepted tradeStatusType.

    Args:
        trade_status_type (GetV1TradesTradeStatusTypeCountTradeStatusType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxTradesApiTradeCountResponse
    """

    return (
        await asyncio_detailed(
            trade_status_type=trade_status_type,
            client=client,
        )
    ).parsed
