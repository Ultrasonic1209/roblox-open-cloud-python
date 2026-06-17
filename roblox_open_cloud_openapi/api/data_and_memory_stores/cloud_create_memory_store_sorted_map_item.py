from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.memory_store_sorted_map_item import MemoryStoreSortedMapItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    universe_id: str,
    sorted_map_id: str,
    *,
    body: MemoryStoreSortedMapItem,
    id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["id"] = id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/cloud/v2/universes/{universe_id}/memory-store/sorted-maps/{sorted_map_id}/items".format(
            universe_id=quote(str(universe_id), safe=""),
            sorted_map_id=quote(str(sorted_map_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> MemoryStoreSortedMapItem | None:
    if response.status_code == 200:
        response_200 = MemoryStoreSortedMapItem.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[MemoryStoreSortedMapItem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    universe_id: str,
    sorted_map_id: str,
    *,
    client: AuthenticatedClient,
    body: MemoryStoreSortedMapItem,
    id: str | Unset = UNSET,
) -> Response[MemoryStoreSortedMapItem]:
    """Create Memory Store Sorted Map Item

     Creates the specified map item if it doesn't exist.

    Args:
        universe_id (str):
        sorted_map_id (str):
        id (str | Unset):
        body (MemoryStoreSortedMapItem): Represents an item within a sorted map structure.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MemoryStoreSortedMapItem]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        sorted_map_id=sorted_map_id,
        body=body,
        id=id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: str,
    sorted_map_id: str,
    *,
    client: AuthenticatedClient,
    body: MemoryStoreSortedMapItem,
    id: str | Unset = UNSET,
) -> MemoryStoreSortedMapItem | None:
    """Create Memory Store Sorted Map Item

     Creates the specified map item if it doesn't exist.

    Args:
        universe_id (str):
        sorted_map_id (str):
        id (str | Unset):
        body (MemoryStoreSortedMapItem): Represents an item within a sorted map structure.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MemoryStoreSortedMapItem
    """

    return sync_detailed(
        universe_id=universe_id,
        sorted_map_id=sorted_map_id,
        client=client,
        body=body,
        id=id,
    ).parsed


async def asyncio_detailed(
    universe_id: str,
    sorted_map_id: str,
    *,
    client: AuthenticatedClient,
    body: MemoryStoreSortedMapItem,
    id: str | Unset = UNSET,
) -> Response[MemoryStoreSortedMapItem]:
    """Create Memory Store Sorted Map Item

     Creates the specified map item if it doesn't exist.

    Args:
        universe_id (str):
        sorted_map_id (str):
        id (str | Unset):
        body (MemoryStoreSortedMapItem): Represents an item within a sorted map structure.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MemoryStoreSortedMapItem]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        sorted_map_id=sorted_map_id,
        body=body,
        id=id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: str,
    sorted_map_id: str,
    *,
    client: AuthenticatedClient,
    body: MemoryStoreSortedMapItem,
    id: str | Unset = UNSET,
) -> MemoryStoreSortedMapItem | None:
    """Create Memory Store Sorted Map Item

     Creates the specified map item if it doesn't exist.

    Args:
        universe_id (str):
        sorted_map_id (str):
        id (str | Unset):
        body (MemoryStoreSortedMapItem): Represents an item within a sorted map structure.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MemoryStoreSortedMapItem
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            sorted_map_id=sorted_map_id,
            client=client,
            body=body,
            id=id,
        )
    ).parsed
