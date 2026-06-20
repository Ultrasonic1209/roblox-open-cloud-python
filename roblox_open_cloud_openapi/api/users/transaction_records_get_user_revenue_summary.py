from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.int_64_exclusive_start_key_cursor import Int64ExclusiveStartKeyCursor
from ...models.revenue_summary_time_frame import RevenueSummaryTimeFrame
from ...models.transaction_totals_response import TransactionTotalsResponse
from ...models.transaction_type import TransactionType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: int,
    *,
    used_types: int | Unset = UNSET,
    time_frame: RevenueSummaryTimeFrame | Unset = UNSET,
    transaction_type: TransactionType | Unset = UNSET,
    exclusive_start_cursor: Int64ExclusiveStartKeyCursor | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["usedTypes"] = used_types

    json_time_frame: str | Unset = UNSET
    if not isinstance(time_frame, Unset):
        json_time_frame = time_frame.value

    params["timeFrame"] = json_time_frame

    json_transaction_type: str | Unset = UNSET
    if not isinstance(transaction_type, Unset):
        json_transaction_type = transaction_type.value

    params["transactionType"] = json_transaction_type

    json_exclusive_start_cursor: dict[str, Any] | Unset = UNSET
    if not isinstance(exclusive_start_cursor, Unset):
        json_exclusive_start_cursor = exclusive_start_cursor.to_dict()
    if not isinstance(json_exclusive_start_cursor, Unset):
        params.update(json_exclusive_start_cursor)

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://economy.roblox.com/v2/users/{user_id}/transaction-totals".format(
            user_id=quote(str(user_id), safe=""),
        ),
        "params": params,
        "extensions": {
            "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
            "openapi-id": "TransactionRecords_GetUserRevenueSummary",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> TransactionTotalsResponse | None:
    if response.status_code == 200:
        response_200 = TransactionTotalsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[TransactionTotalsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: int,
    *,
    client: AuthenticatedClient,
    used_types: int | Unset = UNSET,
    time_frame: RevenueSummaryTimeFrame | Unset = UNSET,
    transaction_type: TransactionType | Unset = UNSET,
    exclusive_start_cursor: Int64ExclusiveStartKeyCursor | Unset = UNSET,
) -> Response[TransactionTotalsResponse]:
    """
    Args:
        user_id (int):
        used_types (int | Unset):
        time_frame (RevenueSummaryTimeFrame | Unset):
        transaction_type (TransactionType | Unset):
        exclusive_start_cursor (Int64ExclusiveStartKeyCursor | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TransactionTotalsResponse]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        used_types=used_types,
        time_frame=time_frame,
        transaction_type=transaction_type,
        exclusive_start_cursor=exclusive_start_cursor,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: int,
    *,
    client: AuthenticatedClient,
    used_types: int | Unset = UNSET,
    time_frame: RevenueSummaryTimeFrame | Unset = UNSET,
    transaction_type: TransactionType | Unset = UNSET,
    exclusive_start_cursor: Int64ExclusiveStartKeyCursor | Unset = UNSET,
) -> TransactionTotalsResponse | None:
    """
    Args:
        user_id (int):
        used_types (int | Unset):
        time_frame (RevenueSummaryTimeFrame | Unset):
        transaction_type (TransactionType | Unset):
        exclusive_start_cursor (Int64ExclusiveStartKeyCursor | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TransactionTotalsResponse
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        used_types=used_types,
        time_frame=time_frame,
        transaction_type=transaction_type,
        exclusive_start_cursor=exclusive_start_cursor,
    ).parsed


async def asyncio_detailed(
    user_id: int,
    *,
    client: AuthenticatedClient,
    used_types: int | Unset = UNSET,
    time_frame: RevenueSummaryTimeFrame | Unset = UNSET,
    transaction_type: TransactionType | Unset = UNSET,
    exclusive_start_cursor: Int64ExclusiveStartKeyCursor | Unset = UNSET,
) -> Response[TransactionTotalsResponse]:
    """
    Args:
        user_id (int):
        used_types (int | Unset):
        time_frame (RevenueSummaryTimeFrame | Unset):
        transaction_type (TransactionType | Unset):
        exclusive_start_cursor (Int64ExclusiveStartKeyCursor | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TransactionTotalsResponse]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        used_types=used_types,
        time_frame=time_frame,
        transaction_type=transaction_type,
        exclusive_start_cursor=exclusive_start_cursor,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: int,
    *,
    client: AuthenticatedClient,
    used_types: int | Unset = UNSET,
    time_frame: RevenueSummaryTimeFrame | Unset = UNSET,
    transaction_type: TransactionType | Unset = UNSET,
    exclusive_start_cursor: Int64ExclusiveStartKeyCursor | Unset = UNSET,
) -> TransactionTotalsResponse | None:
    """
    Args:
        user_id (int):
        used_types (int | Unset):
        time_frame (RevenueSummaryTimeFrame | Unset):
        transaction_type (TransactionType | Unset):
        exclusive_start_cursor (Int64ExclusiveStartKeyCursor | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TransactionTotalsResponse
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            used_types=used_types,
            time_frame=time_frame,
            transaction_type=transaction_type,
            exclusive_start_cursor=exclusive_start_cursor,
        )
    ).parsed
