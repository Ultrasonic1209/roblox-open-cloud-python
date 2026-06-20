from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    universe_id: str,
    ordered_data_store_id: str,
    scope_id: str,
    entry_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/cloud/v2/universes/{universe_id}/ordered-data-stores/{ordered_data_store_id}/scopes/{scope_id}/entries/{entry_id}".format(
            universe_id=quote(str(universe_id), safe=""),
            ordered_data_store_id=quote(str(ordered_data_store_id), safe=""),
            scope_id=quote(str(scope_id), safe=""),
            entry_id=quote(str(entry_id), safe=""),
        ),
        "extensions": {
            "openapi-extensions": {
                "x-roblox-engine-usability": {"apiKeyWithHttpService": True},
                "x-roblox-rate-limits": {
                    "description": "Ordered data stores requests are subject to additional throttling limits described in the [Open Cloud guide for data stores](https://create.roblox.com/docs/cloud/guides/data-stores/throttling).",
                    "perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 100000},
                },
                "x-roblox-scopes": [{"name": "universe.ordered-data-store.scope.entry:write"}],
                "x-roblox-docs": {
                    "category": "Data and memory stores",
                    "methodProperties": {"scopes": ["universe.ordered-data-store.scope.entry:write"]},
                    "resource": {"$ref": "#/components/schemas/OrderedDataStoreEntry", "name": "OrderedDataStoreEntry"},
                },
                "x-roblox-stability": "STABLE",
            },
            "openapi-id": "Cloud_DeleteOrderedDataStoreEntry",
        },
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
    ordered_data_store_id: str,
    scope_id: str,
    entry_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """Delete Ordered Data Store Entry

     Deletes the specified entry.

    On success, returns 200 OK. If the entry doesn't exist, returns
    404 Not Found.

    Args:
        universe_id (str):
        ordered_data_store_id (str):
        scope_id (str):
        entry_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        ordered_data_store_id=ordered_data_store_id,
        scope_id=scope_id,
        entry_id=entry_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    universe_id: str,
    ordered_data_store_id: str,
    scope_id: str,
    entry_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """Delete Ordered Data Store Entry

     Deletes the specified entry.

    On success, returns 200 OK. If the entry doesn't exist, returns
    404 Not Found.

    Args:
        universe_id (str):
        ordered_data_store_id (str):
        scope_id (str):
        entry_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        ordered_data_store_id=ordered_data_store_id,
        scope_id=scope_id,
        entry_id=entry_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)
