from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v1_trades_trade_status_type_limit import GetV1TradesTradeStatusTypeLimit
from ...models.get_v1_trades_trade_status_type_sort_order import GetV1TradesTradeStatusTypeSortOrder
from ...models.get_v1_trades_trade_status_type_trade_status_type import GetV1TradesTradeStatusTypeTradeStatusType
from ...models.roblox_web_web_api_models_api_page_response_roblox_trades_api_trade_response import (
    RobloxWebWebAPIModelsApiPageResponseRobloxTradesApiTradeResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    trade_status_type: GetV1TradesTradeStatusTypeTradeStatusType,
    *,
    limit: GetV1TradesTradeStatusTypeLimit | Unset = GetV1TradesTradeStatusTypeLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1TradesTradeStatusTypeSortOrder | Unset = GetV1TradesTradeStatusTypeSortOrder.ASC,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_limit: int | Unset = UNSET
    if not isinstance(limit, Unset):
        json_limit = limit.value

    params["limit"] = json_limit

    params["cursor"] = cursor

    json_sort_order: str | Unset = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value

    params["sortOrder"] = json_sort_order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://trades.roblox.com/v1/trades/{trade_status_type}".format(
            trade_status_type=quote(str(trade_status_type), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxTradesApiTradeResponse | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIModelsApiPageResponseRobloxTradesApiTradeResponse.from_dict(response.json())

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
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxTradesApiTradeResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    trade_status_type: GetV1TradesTradeStatusTypeTradeStatusType,
    *,
    client: AuthenticatedClient,
    limit: GetV1TradesTradeStatusTypeLimit | Unset = GetV1TradesTradeStatusTypeLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1TradesTradeStatusTypeSortOrder | Unset = GetV1TradesTradeStatusTypeSortOrder.ASC,
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxTradesApiTradeResponse]:
    """Fetches a list of the authenticated user's trades.

    Args:
        trade_status_type (GetV1TradesTradeStatusTypeTradeStatusType):
        limit (GetV1TradesTradeStatusTypeLimit | Unset):  Default:
            GetV1TradesTradeStatusTypeLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV1TradesTradeStatusTypeSortOrder | Unset):  Default:
            GetV1TradesTradeStatusTypeSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxTradesApiTradeResponse]
    """

    kwargs = _get_kwargs(
        trade_status_type=trade_status_type,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    trade_status_type: GetV1TradesTradeStatusTypeTradeStatusType,
    *,
    client: AuthenticatedClient,
    limit: GetV1TradesTradeStatusTypeLimit | Unset = GetV1TradesTradeStatusTypeLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1TradesTradeStatusTypeSortOrder | Unset = GetV1TradesTradeStatusTypeSortOrder.ASC,
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxTradesApiTradeResponse | None:
    """Fetches a list of the authenticated user's trades.

    Args:
        trade_status_type (GetV1TradesTradeStatusTypeTradeStatusType):
        limit (GetV1TradesTradeStatusTypeLimit | Unset):  Default:
            GetV1TradesTradeStatusTypeLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV1TradesTradeStatusTypeSortOrder | Unset):  Default:
            GetV1TradesTradeStatusTypeSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiPageResponseRobloxTradesApiTradeResponse
    """

    return sync_detailed(
        trade_status_type=trade_status_type,
        client=client,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
    ).parsed


async def asyncio_detailed(
    trade_status_type: GetV1TradesTradeStatusTypeTradeStatusType,
    *,
    client: AuthenticatedClient,
    limit: GetV1TradesTradeStatusTypeLimit | Unset = GetV1TradesTradeStatusTypeLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1TradesTradeStatusTypeSortOrder | Unset = GetV1TradesTradeStatusTypeSortOrder.ASC,
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxTradesApiTradeResponse]:
    """Fetches a list of the authenticated user's trades.

    Args:
        trade_status_type (GetV1TradesTradeStatusTypeTradeStatusType):
        limit (GetV1TradesTradeStatusTypeLimit | Unset):  Default:
            GetV1TradesTradeStatusTypeLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV1TradesTradeStatusTypeSortOrder | Unset):  Default:
            GetV1TradesTradeStatusTypeSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxTradesApiTradeResponse]
    """

    kwargs = _get_kwargs(
        trade_status_type=trade_status_type,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    trade_status_type: GetV1TradesTradeStatusTypeTradeStatusType,
    *,
    client: AuthenticatedClient,
    limit: GetV1TradesTradeStatusTypeLimit | Unset = GetV1TradesTradeStatusTypeLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1TradesTradeStatusTypeSortOrder | Unset = GetV1TradesTradeStatusTypeSortOrder.ASC,
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxTradesApiTradeResponse | None:
    """Fetches a list of the authenticated user's trades.

    Args:
        trade_status_type (GetV1TradesTradeStatusTypeTradeStatusType):
        limit (GetV1TradesTradeStatusTypeLimit | Unset):  Default:
            GetV1TradesTradeStatusTypeLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV1TradesTradeStatusTypeSortOrder | Unset):  Default:
            GetV1TradesTradeStatusTypeSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiPageResponseRobloxTradesApiTradeResponse
    """

    return (
        await asyncio_detailed(
            trade_status_type=trade_status_type,
            client=client,
            limit=limit,
            cursor=cursor,
            sort_order=sort_order,
        )
    ).parsed
