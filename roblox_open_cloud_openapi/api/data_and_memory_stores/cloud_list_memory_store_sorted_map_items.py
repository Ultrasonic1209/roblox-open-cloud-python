from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_memory_store_sorted_map_items_response import ListMemoryStoreSortedMapItemsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    universe_id: str,
    sorted_map_id: str,
    *,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    order_by: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["maxPageSize"] = max_page_size

    params["pageToken"] = page_token

    params["orderBy"] = order_by

    params["filter"] = filter_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/cloud/v2/universes/{universe_id}/memory-store/sorted-maps/{sorted_map_id}/items".format(
            universe_id=quote(str(universe_id), safe=""),
            sorted_map_id=quote(str(sorted_map_id), safe=""),
        ),
        "params": params,
        "extensions": {
            "openapi-extensions": {
                "x-roblox-engine-usability": {"apiKeyWithHttpService": True},
                "x-roblox-scopes": [{"name": "memory-store.sorted-map:read"}],
                "x-roblox-docs": {
                    "category": "Data and memory stores",
                    "methodProperties": {"scopes": ["memory-store.sorted-map:read"]},
                    "resource": {
                        "$ref": "#/components/schemas/MemoryStoreSortedMapItem",
                        "name": "MemoryStoreSortedMapItem",
                    },
                },
                "x-roblox-stability": "STABLE",
                "x-roblox-rate-limits": {"perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 1000000}},
            },
            "openapi-id": "Cloud_ListMemoryStoreSortedMapItems",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ListMemoryStoreSortedMapItemsResponse | None:
    if response.status_code == 200:
        response_200 = ListMemoryStoreSortedMapItemsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ListMemoryStoreSortedMapItemsResponse]:
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
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    order_by: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
) -> Response[ListMemoryStoreSortedMapItemsResponse]:
    """List Memory Store Sorted Map Items

     Gets and returns items in the map with a given order and filter.

    Args:
        universe_id (str):
        sorted_map_id (str):
        max_page_size (int | Unset):
        page_token (str | Unset):
        order_by (str | Unset):
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListMemoryStoreSortedMapItemsResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        sorted_map_id=sorted_map_id,
        max_page_size=max_page_size,
        page_token=page_token,
        order_by=order_by,
        filter_=filter_,
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
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    order_by: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
) -> ListMemoryStoreSortedMapItemsResponse | None:
    """List Memory Store Sorted Map Items

     Gets and returns items in the map with a given order and filter.

    Args:
        universe_id (str):
        sorted_map_id (str):
        max_page_size (int | Unset):
        page_token (str | Unset):
        order_by (str | Unset):
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListMemoryStoreSortedMapItemsResponse
    """

    return sync_detailed(
        universe_id=universe_id,
        sorted_map_id=sorted_map_id,
        client=client,
        max_page_size=max_page_size,
        page_token=page_token,
        order_by=order_by,
        filter_=filter_,
    ).parsed


async def asyncio_detailed(
    universe_id: str,
    sorted_map_id: str,
    *,
    client: AuthenticatedClient,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    order_by: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
) -> Response[ListMemoryStoreSortedMapItemsResponse]:
    """List Memory Store Sorted Map Items

     Gets and returns items in the map with a given order and filter.

    Args:
        universe_id (str):
        sorted_map_id (str):
        max_page_size (int | Unset):
        page_token (str | Unset):
        order_by (str | Unset):
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListMemoryStoreSortedMapItemsResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        sorted_map_id=sorted_map_id,
        max_page_size=max_page_size,
        page_token=page_token,
        order_by=order_by,
        filter_=filter_,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: str,
    sorted_map_id: str,
    *,
    client: AuthenticatedClient,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    order_by: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
) -> ListMemoryStoreSortedMapItemsResponse | None:
    """List Memory Store Sorted Map Items

     Gets and returns items in the map with a given order and filter.

    Args:
        universe_id (str):
        sorted_map_id (str):
        max_page_size (int | Unset):
        page_token (str | Unset):
        order_by (str | Unset):
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListMemoryStoreSortedMapItemsResponse
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            sorted_map_id=sorted_map_id,
            client=client,
            max_page_size=max_page_size,
            page_token=page_token,
            order_by=order_by,
            filter_=filter_,
        )
    ).parsed
