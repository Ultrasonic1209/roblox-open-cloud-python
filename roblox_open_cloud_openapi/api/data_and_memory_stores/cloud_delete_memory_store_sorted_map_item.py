from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    universe_id: str,
    sorted_map_id: str,
    item_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/cloud/v2/universes/{universe_id}/memory-store/sorted-maps/{sorted_map_id}/items/{item_id}".format(
            universe_id=quote(str(universe_id), safe=""),
            sorted_map_id=quote(str(sorted_map_id), safe=""),
            item_id=quote(str(item_id), safe=""),
        ),
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
        "openapi-id": "Cloud_DeleteMemoryStoreSortedMapItem",
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Any | None:
    if response.status_code == 200:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[Any]:
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
) -> Response[Any]:
    """Delete Memory Store Sorted Map Item

     Deletes the specified item from the map.

    Args:
        universe_id (str):
        sorted_map_id (str):
        item_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        sorted_map_id=sorted_map_id,
        item_id=item_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    universe_id: str,
    sorted_map_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """Delete Memory Store Sorted Map Item

     Deletes the specified item from the map.

    Args:
        universe_id (str):
        sorted_map_id (str):
        item_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        sorted_map_id=sorted_map_id,
        item_id=item_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)
