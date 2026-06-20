from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.int_64_exclusive_start_key_cursor import Int64ExclusiveStartKeyCursor
from ...models.item_pricing_type import ItemPricingType
from ...models.transaction_record_response_api_page_response import TransactionRecordResponseApiPageResponse
from ...models.transaction_type import TransactionType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: int,
    *,
    exclusive_start_cursor: Int64ExclusiveStartKeyCursor | Unset = UNSET,
    transaction_type: TransactionType | Unset = UNSET,
    item_pricing_type: ItemPricingType | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_exclusive_start_cursor: dict[str, Any] | Unset = UNSET
    if not isinstance(exclusive_start_cursor, Unset):
        json_exclusive_start_cursor = exclusive_start_cursor.to_dict()
    if not isinstance(json_exclusive_start_cursor, Unset):
        params.update(json_exclusive_start_cursor)

    json_transaction_type: str | Unset = UNSET
    if not isinstance(transaction_type, Unset):
        json_transaction_type = transaction_type.value

    params["transactionType"] = json_transaction_type

    json_item_pricing_type: str | Unset = UNSET
    if not isinstance(item_pricing_type, Unset):
        json_item_pricing_type = item_pricing_type.value

    params["itemPricingType"] = json_item_pricing_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://economy.roblox.com/v2/users/{user_id}/transactions".format(
            user_id=quote(str(user_id), safe=""),
        ),
        "params": params,
        "extensions": {
            "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
            "openapi-id": "TransactionRecords_GetUserTransactions",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> TransactionRecordResponseApiPageResponse | None:
    if response.status_code == 200:
        response_200 = TransactionRecordResponseApiPageResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[TransactionRecordResponseApiPageResponse]:
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
    exclusive_start_cursor: Int64ExclusiveStartKeyCursor | Unset = UNSET,
    transaction_type: TransactionType | Unset = UNSET,
    item_pricing_type: ItemPricingType | Unset = UNSET,
) -> Response[TransactionRecordResponseApiPageResponse]:
    """
    Args:
        user_id (int):
        exclusive_start_cursor (Int64ExclusiveStartKeyCursor | Unset):
        transaction_type (TransactionType | Unset):
        item_pricing_type (ItemPricingType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TransactionRecordResponseApiPageResponse]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        exclusive_start_cursor=exclusive_start_cursor,
        transaction_type=transaction_type,
        item_pricing_type=item_pricing_type,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: int,
    *,
    client: AuthenticatedClient,
    exclusive_start_cursor: Int64ExclusiveStartKeyCursor | Unset = UNSET,
    transaction_type: TransactionType | Unset = UNSET,
    item_pricing_type: ItemPricingType | Unset = UNSET,
) -> TransactionRecordResponseApiPageResponse | None:
    """
    Args:
        user_id (int):
        exclusive_start_cursor (Int64ExclusiveStartKeyCursor | Unset):
        transaction_type (TransactionType | Unset):
        item_pricing_type (ItemPricingType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TransactionRecordResponseApiPageResponse
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        exclusive_start_cursor=exclusive_start_cursor,
        transaction_type=transaction_type,
        item_pricing_type=item_pricing_type,
    ).parsed


async def asyncio_detailed(
    user_id: int,
    *,
    client: AuthenticatedClient,
    exclusive_start_cursor: Int64ExclusiveStartKeyCursor | Unset = UNSET,
    transaction_type: TransactionType | Unset = UNSET,
    item_pricing_type: ItemPricingType | Unset = UNSET,
) -> Response[TransactionRecordResponseApiPageResponse]:
    """
    Args:
        user_id (int):
        exclusive_start_cursor (Int64ExclusiveStartKeyCursor | Unset):
        transaction_type (TransactionType | Unset):
        item_pricing_type (ItemPricingType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TransactionRecordResponseApiPageResponse]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        exclusive_start_cursor=exclusive_start_cursor,
        transaction_type=transaction_type,
        item_pricing_type=item_pricing_type,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: int,
    *,
    client: AuthenticatedClient,
    exclusive_start_cursor: Int64ExclusiveStartKeyCursor | Unset = UNSET,
    transaction_type: TransactionType | Unset = UNSET,
    item_pricing_type: ItemPricingType | Unset = UNSET,
) -> TransactionRecordResponseApiPageResponse | None:
    """
    Args:
        user_id (int):
        exclusive_start_cursor (Int64ExclusiveStartKeyCursor | Unset):
        transaction_type (TransactionType | Unset):
        item_pricing_type (ItemPricingType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TransactionRecordResponseApiPageResponse
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            exclusive_start_cursor=exclusive_start_cursor,
            transaction_type=transaction_type,
            item_pricing_type=item_pricing_type,
        )
    ).parsed
