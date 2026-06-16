from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.discard_memory_store_queue_items_request import DiscardMemoryStoreQueueItemsRequest
from ...types import Response


def _get_kwargs(
    universe_id: str,
    queue_id: str,
    *,
    body: DiscardMemoryStoreQueueItemsRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/cloud/v2/universes/{universe_id}/memory-store/queues/{queue_id}/items:discard".format(
            universe_id=quote(str(universe_id), safe=""),
            queue_id=quote(str(queue_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 200:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
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
    body: DiscardMemoryStoreQueueItemsRequest,
) -> Response[Any]:
    """Discard Memory Store Queue Items

     Discards read items from the front of the queue.

    Takes a `readId` from a previous `Read` operation.

    Args:
        universe_id (str):
        queue_id (str):
        body (DiscardMemoryStoreQueueItemsRequest): Discards read items from the front of the
            queue.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        queue_id=queue_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    universe_id: str,
    queue_id: str,
    *,
    client: AuthenticatedClient,
    body: DiscardMemoryStoreQueueItemsRequest,
) -> Response[Any]:
    """Discard Memory Store Queue Items

     Discards read items from the front of the queue.

    Takes a `readId` from a previous `Read` operation.

    Args:
        universe_id (str):
        queue_id (str):
        body (DiscardMemoryStoreQueueItemsRequest): Discards read items from the front of the
            queue.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        queue_id=queue_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
