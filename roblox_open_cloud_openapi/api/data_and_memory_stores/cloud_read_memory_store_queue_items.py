from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.read_memory_store_queue_items_response import ReadMemoryStoreQueueItemsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    universe_id: str,
    queue_id: str,
    *,
    count: int | Unset = UNSET,
    all_or_nothing: bool | Unset = UNSET,
    invisibility_window: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["count"] = count

    params["allOrNothing"] = all_or_nothing

    params["invisibilityWindow"] = invisibility_window

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/cloud/v2/universes/{universe_id}/memory-store/queues/{queue_id}/items:read".format(
            universe_id=quote(str(universe_id), safe=""),
            queue_id=quote(str(queue_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ReadMemoryStoreQueueItemsResponse | None:
    if response.status_code == 200:
        response_200 = ReadMemoryStoreQueueItemsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ReadMemoryStoreQueueItemsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    universe_id: str,
    queue_id: str,
    *,
    client: AuthenticatedClient,
    count: int | Unset = UNSET,
    all_or_nothing: bool | Unset = UNSET,
    invisibility_window: str | Unset = UNSET,
) -> Response[ReadMemoryStoreQueueItemsResponse]:
    """Read Memory Store Queue Items

     Returns the specified number of items at the front of the queue.


    Args:
        universe_id (str):
        queue_id (str):
        count (int | Unset):
        all_or_nothing (bool | Unset):  Example: True.
        invisibility_window (str | Unset):  Example: 3s.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ReadMemoryStoreQueueItemsResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        queue_id=queue_id,
        count=count,
        all_or_nothing=all_or_nothing,
        invisibility_window=invisibility_window,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: str,
    queue_id: str,
    *,
    client: AuthenticatedClient,
    count: int | Unset = UNSET,
    all_or_nothing: bool | Unset = UNSET,
    invisibility_window: str | Unset = UNSET,
) -> ReadMemoryStoreQueueItemsResponse | None:
    """Read Memory Store Queue Items

     Returns the specified number of items at the front of the queue.


    Args:
        universe_id (str):
        queue_id (str):
        count (int | Unset):
        all_or_nothing (bool | Unset):  Example: True.
        invisibility_window (str | Unset):  Example: 3s.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ReadMemoryStoreQueueItemsResponse
    """

    return sync_detailed(
        universe_id=universe_id,
        queue_id=queue_id,
        client=client,
        count=count,
        all_or_nothing=all_or_nothing,
        invisibility_window=invisibility_window,
    ).parsed


async def asyncio_detailed(
    universe_id: str,
    queue_id: str,
    *,
    client: AuthenticatedClient,
    count: int | Unset = UNSET,
    all_or_nothing: bool | Unset = UNSET,
    invisibility_window: str | Unset = UNSET,
) -> Response[ReadMemoryStoreQueueItemsResponse]:
    """Read Memory Store Queue Items

     Returns the specified number of items at the front of the queue.


    Args:
        universe_id (str):
        queue_id (str):
        count (int | Unset):
        all_or_nothing (bool | Unset):  Example: True.
        invisibility_window (str | Unset):  Example: 3s.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ReadMemoryStoreQueueItemsResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        queue_id=queue_id,
        count=count,
        all_or_nothing=all_or_nothing,
        invisibility_window=invisibility_window,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: str,
    queue_id: str,
    *,
    client: AuthenticatedClient,
    count: int | Unset = UNSET,
    all_or_nothing: bool | Unset = UNSET,
    invisibility_window: str | Unset = UNSET,
) -> ReadMemoryStoreQueueItemsResponse | None:
    """Read Memory Store Queue Items

     Returns the specified number of items at the front of the queue.


    Args:
        universe_id (str):
        queue_id (str):
        count (int | Unset):
        all_or_nothing (bool | Unset):  Example: True.
        invisibility_window (str | Unset):  Example: 3s.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ReadMemoryStoreQueueItemsResponse
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            queue_id=queue_id,
            client=client,
            count=count,
            all_or_nothing=all_or_nothing,
            invisibility_window=invisibility_window,
        )
    ).parsed
