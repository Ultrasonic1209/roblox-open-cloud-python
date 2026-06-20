from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.int_64_exclusive_start_key_cursor import Int64ExclusiveStartKeyCursor
from ...models.transaction_response_api_page_response import TransactionResponseApiPageResponse
from ...models.transaction_type import TransactionType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    group_id: int,
    *,
    exclusive_start_request: Int64ExclusiveStartKeyCursor | Unset = UNSET,
    transaction_type: TransactionType | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_exclusive_start_request: dict[str, Any] | Unset = UNSET
    if not isinstance(exclusive_start_request, Unset):
        json_exclusive_start_request = exclusive_start_request.to_dict()
    if not isinstance(json_exclusive_start_request, Unset):
        params.update(json_exclusive_start_request)

    json_transaction_type: str | Unset = UNSET
    if not isinstance(transaction_type, Unset):
        json_transaction_type = transaction_type.value

    params["transactionType"] = json_transaction_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://economy.roblox.com/v2/groups/{group_id}/transactions".format(
            group_id=quote(str(group_id), safe=""),
        ),
        "params": params,
        "extensions": {
            "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
            "openapi-id": "TransactionHistory_GetGroupTransactions",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> TransactionResponseApiPageResponse | None:
    if response.status_code == 200:
        response_200 = TransactionResponseApiPageResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[TransactionResponseApiPageResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    group_id: int,
    *,
    client: AuthenticatedClient,
    exclusive_start_request: Int64ExclusiveStartKeyCursor | Unset = UNSET,
    transaction_type: TransactionType | Unset = UNSET,
) -> Response[TransactionResponseApiPageResponse]:
    """
    Args:
        group_id (int):
        exclusive_start_request (Int64ExclusiveStartKeyCursor | Unset):
        transaction_type (TransactionType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TransactionResponseApiPageResponse]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        exclusive_start_request=exclusive_start_request,
        transaction_type=transaction_type,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: int,
    *,
    client: AuthenticatedClient,
    exclusive_start_request: Int64ExclusiveStartKeyCursor | Unset = UNSET,
    transaction_type: TransactionType | Unset = UNSET,
) -> TransactionResponseApiPageResponse | None:
    """
    Args:
        group_id (int):
        exclusive_start_request (Int64ExclusiveStartKeyCursor | Unset):
        transaction_type (TransactionType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TransactionResponseApiPageResponse
    """

    return sync_detailed(
        group_id=group_id,
        client=client,
        exclusive_start_request=exclusive_start_request,
        transaction_type=transaction_type,
    ).parsed


async def asyncio_detailed(
    group_id: int,
    *,
    client: AuthenticatedClient,
    exclusive_start_request: Int64ExclusiveStartKeyCursor | Unset = UNSET,
    transaction_type: TransactionType | Unset = UNSET,
) -> Response[TransactionResponseApiPageResponse]:
    """
    Args:
        group_id (int):
        exclusive_start_request (Int64ExclusiveStartKeyCursor | Unset):
        transaction_type (TransactionType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TransactionResponseApiPageResponse]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        exclusive_start_request=exclusive_start_request,
        transaction_type=transaction_type,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: int,
    *,
    client: AuthenticatedClient,
    exclusive_start_request: Int64ExclusiveStartKeyCursor | Unset = UNSET,
    transaction_type: TransactionType | Unset = UNSET,
) -> TransactionResponseApiPageResponse | None:
    """
    Args:
        group_id (int):
        exclusive_start_request (Int64ExclusiveStartKeyCursor | Unset):
        transaction_type (TransactionType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TransactionResponseApiPageResponse
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
            exclusive_start_request=exclusive_start_request,
            transaction_type=transaction_type,
        )
    ).parsed
