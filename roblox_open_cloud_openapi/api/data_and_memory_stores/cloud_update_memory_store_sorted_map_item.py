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
    item_id: str,
    *,
    body: MemoryStoreSortedMapItem,
    allow_missing: bool | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["allowMissing"] = allow_missing

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/cloud/v2/universes/{universe_id}/memory-store/sorted-maps/{sorted_map_id}/items/{item_id}".format(
            universe_id=quote(str(universe_id), safe=""),
            sorted_map_id=quote(str(sorted_map_id), safe=""),
            item_id=quote(str(item_id), safe=""),
        ),
        "params": params,
        "openapi-extensions": {
            "x-roblox-engine-usability": {"apiKeyWithHttpService": True},
            "x-roblox-scopes": [{"name": "memory-store.sorted-map:write"}],
            "x-roblox-docs": {
                "category": "Data and memory stores",
                "methodProperties": {"scopes": ["memory-store.sorted-map:write"]},
                "resource": {
                    "$ref": "#/components/schemas/MemoryStoreSortedMapItem",
                    "name": "MemoryStoreSortedMapItem",
                },
            },
            "x-roblox-stability": "STABLE",
            "x-roblox-rate-limits": {"perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 1000000}},
        },
        "openapi-id": "Cloud_UpdateMemoryStoreSortedMapItem",
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
    item_id: str,
    *,
    client: AuthenticatedClient,
    body: MemoryStoreSortedMapItem,
    allow_missing: bool | Unset = UNSET,
) -> Response[MemoryStoreSortedMapItem]:
    """Update Memory Store Sorted Map Item

     Updates the specified map item.

    Args:
        universe_id (str):
        sorted_map_id (str):
        item_id (str):
        allow_missing (bool | Unset):  Example: True.
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
        item_id=item_id,
        body=body,
        allow_missing=allow_missing,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: str,
    sorted_map_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient,
    body: MemoryStoreSortedMapItem,
    allow_missing: bool | Unset = UNSET,
) -> MemoryStoreSortedMapItem | None:
    """Update Memory Store Sorted Map Item

     Updates the specified map item.

    Args:
        universe_id (str):
        sorted_map_id (str):
        item_id (str):
        allow_missing (bool | Unset):  Example: True.
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
        item_id=item_id,
        client=client,
        body=body,
        allow_missing=allow_missing,
    ).parsed


async def asyncio_detailed(
    universe_id: str,
    sorted_map_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient,
    body: MemoryStoreSortedMapItem,
    allow_missing: bool | Unset = UNSET,
) -> Response[MemoryStoreSortedMapItem]:
    """Update Memory Store Sorted Map Item

     Updates the specified map item.

    Args:
        universe_id (str):
        sorted_map_id (str):
        item_id (str):
        allow_missing (bool | Unset):  Example: True.
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
        item_id=item_id,
        body=body,
        allow_missing=allow_missing,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: str,
    sorted_map_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient,
    body: MemoryStoreSortedMapItem,
    allow_missing: bool | Unset = UNSET,
) -> MemoryStoreSortedMapItem | None:
    """Update Memory Store Sorted Map Item

     Updates the specified map item.

    Args:
        universe_id (str):
        sorted_map_id (str):
        item_id (str):
        allow_missing (bool | Unset):  Example: True.
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
            item_id=item_id,
            client=client,
            body=body,
            allow_missing=allow_missing,
        )
    ).parsed
