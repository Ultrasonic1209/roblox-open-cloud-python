from http import HTTPStatus
from typing import TYPE_CHECKING, Any
from urllib.parse import quote

if TYPE_CHECKING:
    import httpx2 as httpx
else:
    try:
        import httpx2 as httpx
    except ModuleNotFoundError:
        try:
            import httpx
        except ModuleNotFoundError:
            raise RuntimeError(
                "This module requires the httpx2 package to be installed.\n"
                "You can install it with:\n"
                "    $ pip install httpx2\n"
            ) from None


from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response

"""
{'x-roblox-stability': 'STABLE', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'MINUTE', 'maxInPeriod': 1000000}}, 'x-roblox-scopes': [{'name': 'memory-store.queue:add', 'targetResourceSpecifier': 'universes', 'firstPartyOAuthOnly': True}], 'x-roblox-engine-usability': {'apiKeyWithHttpService': True}}
"""


from ...models.create_memory_store_queue_item_request import CreateMemoryStoreQueueItemRequest
from ...models.memory_store_queue_item import MemoryStoreQueueItem


def _get_kwargs(
    universe_id: int,
    queue_id: str,
    *,
    body: CreateMemoryStoreQueueItemRequest
    | CreateMemoryStoreQueueItemRequest
    | CreateMemoryStoreQueueItemRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/cloud/v2/universes/{universe_id}/memory-store/queues/{queue_id}/items".format(
            universe_id=quote(str(universe_id), safe=""),
            queue_id=quote(str(queue_id), safe=""),
        ),
    }

    if isinstance(body, CreateMemoryStoreQueueItemRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CreateMemoryStoreQueueItemRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"
    if isinstance(body, CreateMemoryStoreQueueItemRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MemoryStoreQueueItem | None:
    if response.status_code == 200:
        response_200 = MemoryStoreQueueItem.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[MemoryStoreQueueItem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    universe_id: int,
    queue_id: str,
    *,
    client: AuthenticatedClient,
    body: CreateMemoryStoreQueueItemRequest
    | CreateMemoryStoreQueueItemRequest
    | CreateMemoryStoreQueueItemRequest
    | Unset = UNSET,
) -> Response[MemoryStoreQueueItem]:
    """Create Memory Store Queue Item

     Creates a new queue item.

    `ttl` is optional. If omitted, the item expires after 45 days (3888000 seconds).
    If set, it must be a number ending in `s`, greater than 0 and at most `3888000s`.
    The response reports expiration as `expireTime`, not `ttl`.

    If a numerical `priority` is set, the item will be inserted into the queue
    based on the priority value. The higher the value, the closer to the front
    of the queue the item will be. If priority values are the same then the
    item will be inserted after existing values with the same priority.

    Args:
        universe_id (int):
        queue_id (str):
        body (CreateMemoryStoreQueueItemRequest): Represents an item within a queue structure.
        body (CreateMemoryStoreQueueItemRequest): Represents an item within a queue structure.
        body (CreateMemoryStoreQueueItemRequest): Represents an item within a queue structure.

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

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: int,
    queue_id: str,
    *,
    client: AuthenticatedClient,
    body: CreateMemoryStoreQueueItemRequest
    | CreateMemoryStoreQueueItemRequest
    | CreateMemoryStoreQueueItemRequest
    | Unset = UNSET,
) -> MemoryStoreQueueItem | None:
    """Create Memory Store Queue Item

     Creates a new queue item.

    `ttl` is optional. If omitted, the item expires after 45 days (3888000 seconds).
    If set, it must be a number ending in `s`, greater than 0 and at most `3888000s`.
    The response reports expiration as `expireTime`, not `ttl`.

    If a numerical `priority` is set, the item will be inserted into the queue
    based on the priority value. The higher the value, the closer to the front
    of the queue the item will be. If priority values are the same then the
    item will be inserted after existing values with the same priority.

    Args:
        universe_id (int):
        queue_id (str):
        body (CreateMemoryStoreQueueItemRequest): Represents an item within a queue structure.
        body (CreateMemoryStoreQueueItemRequest): Represents an item within a queue structure.
        body (CreateMemoryStoreQueueItemRequest): Represents an item within a queue structure.

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
    universe_id: int,
    queue_id: str,
    *,
    client: AuthenticatedClient,
    body: CreateMemoryStoreQueueItemRequest
    | CreateMemoryStoreQueueItemRequest
    | CreateMemoryStoreQueueItemRequest
    | Unset = UNSET,
) -> Response[MemoryStoreQueueItem]:
    """Create Memory Store Queue Item

     Creates a new queue item.

    `ttl` is optional. If omitted, the item expires after 45 days (3888000 seconds).
    If set, it must be a number ending in `s`, greater than 0 and at most `3888000s`.
    The response reports expiration as `expireTime`, not `ttl`.

    If a numerical `priority` is set, the item will be inserted into the queue
    based on the priority value. The higher the value, the closer to the front
    of the queue the item will be. If priority values are the same then the
    item will be inserted after existing values with the same priority.

    Args:
        universe_id (int):
        queue_id (str):
        body (CreateMemoryStoreQueueItemRequest): Represents an item within a queue structure.
        body (CreateMemoryStoreQueueItemRequest): Represents an item within a queue structure.
        body (CreateMemoryStoreQueueItemRequest): Represents an item within a queue structure.

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

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: int,
    queue_id: str,
    *,
    client: AuthenticatedClient,
    body: CreateMemoryStoreQueueItemRequest
    | CreateMemoryStoreQueueItemRequest
    | CreateMemoryStoreQueueItemRequest
    | Unset = UNSET,
) -> MemoryStoreQueueItem | None:
    """Create Memory Store Queue Item

     Creates a new queue item.

    `ttl` is optional. If omitted, the item expires after 45 days (3888000 seconds).
    If set, it must be a number ending in `s`, greater than 0 and at most `3888000s`.
    The response reports expiration as `expireTime`, not `ttl`.

    If a numerical `priority` is set, the item will be inserted into the queue
    based on the priority value. The higher the value, the closer to the front
    of the queue the item will be. If priority values are the same then the
    item will be inserted after existing values with the same priority.

    Args:
        universe_id (int):
        queue_id (str):
        body (CreateMemoryStoreQueueItemRequest): Represents an item within a queue structure.
        body (CreateMemoryStoreQueueItemRequest): Represents an item within a queue structure.
        body (CreateMemoryStoreQueueItemRequest): Represents an item within a queue structure.

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
