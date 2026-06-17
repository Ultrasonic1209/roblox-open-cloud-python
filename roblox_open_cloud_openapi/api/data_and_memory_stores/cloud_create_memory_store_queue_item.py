from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.memory_store_queue_item import MemoryStoreQueueItem
from ...types import Response


def _get_kwargs(
    universe_id: str,
    queue_id: str,
    *,
    body: MemoryStoreQueueItem,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/cloud/v2/universes/{universe_id}/memory-store/queues/{queue_id}/items".format(
            universe_id=quote(str(universe_id), safe=""),
            queue_id=quote(str(queue_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> MemoryStoreQueueItem | None:
    if response.status_code == 200:
        response_200 = MemoryStoreQueueItem.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[MemoryStoreQueueItem]:
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
    body: MemoryStoreQueueItem,
) -> Response[MemoryStoreQueueItem]:
    """Create Memory Store Queue Item

     Creates a new queue item.

    If `ttl` is set, the item will automatically be removed from the queue
    after the time interval specified.

    If a numerical `priority` is set, the item will be inserted into the queue
    based on the priority value. The higher the value, the closer to the front
    of the queue the item will be. If priority values are the same then the
    item will be inserted after existing values with the same priority.

    Args:
        universe_id (str):
        queue_id (str):
        body (MemoryStoreQueueItem): Represents an item within a queue structure.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MemoryStoreQueueItem]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        queue_id=queue_id,
        body=body,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: str,
    queue_id: str,
    *,
    client: AuthenticatedClient,
    body: MemoryStoreQueueItem,
) -> MemoryStoreQueueItem | None:
    """Create Memory Store Queue Item

     Creates a new queue item.

    If `ttl` is set, the item will automatically be removed from the queue
    after the time interval specified.

    If a numerical `priority` is set, the item will be inserted into the queue
    based on the priority value. The higher the value, the closer to the front
    of the queue the item will be. If priority values are the same then the
    item will be inserted after existing values with the same priority.

    Args:
        universe_id (str):
        queue_id (str):
        body (MemoryStoreQueueItem): Represents an item within a queue structure.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MemoryStoreQueueItem
    """

    return sync_detailed(
        universe_id=universe_id,
        queue_id=queue_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    universe_id: str,
    queue_id: str,
    *,
    client: AuthenticatedClient,
    body: MemoryStoreQueueItem,
) -> Response[MemoryStoreQueueItem]:
    """Create Memory Store Queue Item

     Creates a new queue item.

    If `ttl` is set, the item will automatically be removed from the queue
    after the time interval specified.

    If a numerical `priority` is set, the item will be inserted into the queue
    based on the priority value. The higher the value, the closer to the front
    of the queue the item will be. If priority values are the same then the
    item will be inserted after existing values with the same priority.

    Args:
        universe_id (str):
        queue_id (str):
        body (MemoryStoreQueueItem): Represents an item within a queue structure.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MemoryStoreQueueItem]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        queue_id=queue_id,
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: str,
    queue_id: str,
    *,
    client: AuthenticatedClient,
    body: MemoryStoreQueueItem,
) -> MemoryStoreQueueItem | None:
    """Create Memory Store Queue Item

     Creates a new queue item.

    If `ttl` is set, the item will automatically be removed from the queue
    after the time interval specified.

    If a numerical `priority` is set, the item will be inserted into the queue
    based on the priority value. The higher the value, the closer to the front
    of the queue the item will be. If priority values are the same then the
    item will be inserted after existing values with the same priority.

    Args:
        universe_id (str):
        queue_id (str):
        body (MemoryStoreQueueItem): Represents an item within a queue structure.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MemoryStoreQueueItem
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            queue_id=queue_id,
            client=client,
            body=body,
        )
    ).parsed
