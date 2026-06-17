from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_trades_api_models_v2_new_trade_response import RobloxTradesApiModelsV2NewTradeResponse
from ...models.roblox_trades_api_models_v2_trade_request import RobloxTradesApiModelsV2TradeRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: RobloxTradesApiModelsV2TradeRequest | RobloxTradesApiModelsV2TradeRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "https://trades.roblox.com/v2/trades/send",
        "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
        "openapi-id": "post_v2_trades_send",
    }

    if isinstance(body, RobloxTradesApiModelsV2TradeRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxTradesApiModelsV2TradeRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxTradesApiModelsV2NewTradeResponse | None:
    if response.status_code == 200:
        response_200 = RobloxTradesApiModelsV2NewTradeResponse.from_dict(response.json())

        return response_200

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
) -> Response[Any | RobloxTradesApiModelsV2NewTradeResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxTradesApiModelsV2TradeRequest | RobloxTradesApiModelsV2TradeRequest | Unset = UNSET,
) -> Response[Any | RobloxTradesApiModelsV2NewTradeResponse]:
    """Sends a new trade.

    Args:
        body (RobloxTradesApiModelsV2TradeRequest): Represents a trade request. The calling user
            must be either participant A or B in the trade.
        body (RobloxTradesApiModelsV2TradeRequest): Represents a trade request. The calling user
            must be either participant A or B in the trade.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxTradesApiModelsV2NewTradeResponse]
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
    body: RobloxTradesApiModelsV2TradeRequest | RobloxTradesApiModelsV2TradeRequest | Unset = UNSET,
) -> Any | RobloxTradesApiModelsV2NewTradeResponse | None:
    """Sends a new trade.

    Args:
        body (RobloxTradesApiModelsV2TradeRequest): Represents a trade request. The calling user
            must be either participant A or B in the trade.
        body (RobloxTradesApiModelsV2TradeRequest): Represents a trade request. The calling user
            must be either participant A or B in the trade.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxTradesApiModelsV2NewTradeResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxTradesApiModelsV2TradeRequest | RobloxTradesApiModelsV2TradeRequest | Unset = UNSET,
) -> Response[Any | RobloxTradesApiModelsV2NewTradeResponse]:
    """Sends a new trade.

    Args:
        body (RobloxTradesApiModelsV2TradeRequest): Represents a trade request. The calling user
            must be either participant A or B in the trade.
        body (RobloxTradesApiModelsV2TradeRequest): Represents a trade request. The calling user
            must be either participant A or B in the trade.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxTradesApiModelsV2NewTradeResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RobloxTradesApiModelsV2TradeRequest | RobloxTradesApiModelsV2TradeRequest | Unset = UNSET,
) -> Any | RobloxTradesApiModelsV2NewTradeResponse | None:
    """Sends a new trade.

    Args:
        body (RobloxTradesApiModelsV2TradeRequest): Represents a trade request. The calling user
            must be either participant A or B in the trade.
        body (RobloxTradesApiModelsV2TradeRequest): Represents a trade request. The calling user
            must be either participant A or B in the trade.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxTradesApiModelsV2NewTradeResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
