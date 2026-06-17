from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_trades_api_models_v2_trade_details_response import RobloxTradesApiModelsV2TradeDetailsResponse
from ...types import Response


def _get_kwargs(
    trade_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://trades.roblox.com/v2/trades/{trade_id}".format(
            trade_id=quote(str(trade_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxTradesApiModelsV2TradeDetailsResponse | None:
    if response.status_code == 200:
        response_200 = RobloxTradesApiModelsV2TradeDetailsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxTradesApiModelsV2TradeDetailsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    trade_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxTradesApiModelsV2TradeDetailsResponse]:
    """Gets the details of a trade.

    Args:
        trade_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxTradesApiModelsV2TradeDetailsResponse]
    """

    kwargs = _get_kwargs(
        trade_id=trade_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    trade_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxTradesApiModelsV2TradeDetailsResponse | None:
    """Gets the details of a trade.

    Args:
        trade_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxTradesApiModelsV2TradeDetailsResponse
    """

    return sync_detailed(
        trade_id=trade_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    trade_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxTradesApiModelsV2TradeDetailsResponse]:
    """Gets the details of a trade.

    Args:
        trade_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxTradesApiModelsV2TradeDetailsResponse]
    """

    kwargs = _get_kwargs(
        trade_id=trade_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    trade_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxTradesApiModelsV2TradeDetailsResponse | None:
    """Gets the details of a trade.

    Args:
        trade_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxTradesApiModelsV2TradeDetailsResponse
    """

    return (
        await asyncio_detailed(
            trade_id=trade_id,
            client=client,
        )
    ).parsed
