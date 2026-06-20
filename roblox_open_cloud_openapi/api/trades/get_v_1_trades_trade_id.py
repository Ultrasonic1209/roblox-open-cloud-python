import sys
from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response

if sys.version_info >= (3, 13):
    from warnings import deprecated
else:
    from typing_extensions import deprecated

from ...models.roblox_trades_api_trade_detail_response import RobloxTradesApiTradeDetailResponse


def _get_kwargs(
    trade_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://trades.roblox.com/v1/trades/{trade_id}".format(
            trade_id=quote(str(trade_id), safe=""),
        ),
        "extensions": {
            "openapi-extensions": {
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
                "x-roblox-recommended-alternatives": [
                    {
                        "url": "https://trades.roblox.com/v2/trades/{tradeId}",
                        "httpMethod": "GET",
                        "documentationUrl": "https://create.roblox.com/docs/cloud/reference/features/trades#trades_get_v2_trades__tradeId_",
                    }
                ],
            },
            "openapi-id": "get_v1_trades_tradeId",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxTradesApiTradeDetailResponse | None:
    if response.status_code == 200:
        response_200 = RobloxTradesApiTradeDetailResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxTradesApiTradeDetailResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/trades#trades_get_v1_trades__tradeId_"
)
def sync_detailed(
    trade_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxTradesApiTradeDetailResponse]:
    """Gets detailed information about a trade.

    Args:
        trade_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxTradesApiTradeDetailResponse]
    """

    kwargs = _get_kwargs(
        trade_id=trade_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/trades#trades_get_v1_trades__tradeId_"
)
def sync(
    trade_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxTradesApiTradeDetailResponse | None:
    """Gets detailed information about a trade.

    Args:
        trade_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxTradesApiTradeDetailResponse
    """

    return sync_detailed(
        trade_id=trade_id,
        client=client,
    ).parsed


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/trades#trades_get_v1_trades__tradeId_"
)
async def asyncio_detailed(
    trade_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxTradesApiTradeDetailResponse]:
    """Gets detailed information about a trade.

    Args:
        trade_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxTradesApiTradeDetailResponse]
    """

    kwargs = _get_kwargs(
        trade_id=trade_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/trades#trades_get_v1_trades__tradeId_"
)
async def asyncio(
    trade_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxTradesApiTradeDetailResponse | None:
    """Gets detailed information about a trade.

    Args:
        trade_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxTradesApiTradeDetailResponse
    """

    return (
        await asyncio_detailed(
            trade_id=trade_id,
            client=client,
        )
    ).parsed
