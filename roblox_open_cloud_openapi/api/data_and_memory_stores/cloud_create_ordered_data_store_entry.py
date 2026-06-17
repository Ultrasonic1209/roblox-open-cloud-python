from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ordered_data_store_entry import OrderedDataStoreEntry
from ...types import UNSET, Response, Unset


def _get_kwargs(
    universe_id: str,
    ordered_data_store_id: str,
    scope_id: str,
    *,
    body: OrderedDataStoreEntry,
    id: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["id"] = id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/cloud/v2/universes/{universe_id}/ordered-data-stores/{ordered_data_store_id}/scopes/{scope_id}/entries".format(
            universe_id=quote(str(universe_id), safe=""),
            ordered_data_store_id=quote(str(ordered_data_store_id), safe=""),
            scope_id=quote(str(scope_id), safe=""),
        ),
        "params": params,
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
        "openapi-id": "Cloud_CreateOrderedDataStoreEntry",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> OrderedDataStoreEntry | None:
    if response.status_code == 200:
        response_200 = OrderedDataStoreEntry.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[OrderedDataStoreEntry]:
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
    *,
    client: AuthenticatedClient,
    body: OrderedDataStoreEntry,
    id: str | Unset = UNSET,
) -> Response[OrderedDataStoreEntry]:
    """Create Ordered Data Store Entry

     Creates an entry with the provided ID and value.

    Returns a 400 Bad Request if the entry exists.

    Args:
        universe_id (str):
        ordered_data_store_id (str):
        scope_id (str):
        id (str | Unset):
        body (OrderedDataStoreEntry): A key-value entry in an ordered data store.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrderedDataStoreEntry]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        ordered_data_store_id=ordered_data_store_id,
        scope_id=scope_id,
        body=body,
        id=id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: str,
    ordered_data_store_id: str,
    scope_id: str,
    *,
    client: AuthenticatedClient,
    body: OrderedDataStoreEntry,
    id: str | Unset = UNSET,
) -> OrderedDataStoreEntry | None:
    """Create Ordered Data Store Entry

     Creates an entry with the provided ID and value.

    Returns a 400 Bad Request if the entry exists.

    Args:
        universe_id (str):
        ordered_data_store_id (str):
        scope_id (str):
        id (str | Unset):
        body (OrderedDataStoreEntry): A key-value entry in an ordered data store.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrderedDataStoreEntry
    """

    return sync_detailed(
        universe_id=universe_id,
        ordered_data_store_id=ordered_data_store_id,
        scope_id=scope_id,
        client=client,
        body=body,
        id=id,
    ).parsed


async def asyncio_detailed(
    universe_id: str,
    ordered_data_store_id: str,
    scope_id: str,
    *,
    client: AuthenticatedClient,
    body: OrderedDataStoreEntry,
    id: str | Unset = UNSET,
) -> Response[OrderedDataStoreEntry]:
    """Create Ordered Data Store Entry

     Creates an entry with the provided ID and value.

    Returns a 400 Bad Request if the entry exists.

    Args:
        universe_id (str):
        ordered_data_store_id (str):
        scope_id (str):
        id (str | Unset):
        body (OrderedDataStoreEntry): A key-value entry in an ordered data store.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrderedDataStoreEntry]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        ordered_data_store_id=ordered_data_store_id,
        scope_id=scope_id,
        body=body,
        id=id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: str,
    ordered_data_store_id: str,
    scope_id: str,
    *,
    client: AuthenticatedClient,
    body: OrderedDataStoreEntry,
    id: str | Unset = UNSET,
) -> OrderedDataStoreEntry | None:
    """Create Ordered Data Store Entry

     Creates an entry with the provided ID and value.

    Returns a 400 Bad Request if the entry exists.

    Args:
        universe_id (str):
        ordered_data_store_id (str):
        scope_id (str):
        id (str | Unset):
        body (OrderedDataStoreEntry): A key-value entry in an ordered data store.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrderedDataStoreEntry
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            ordered_data_store_id=ordered_data_store_id,
            scope_id=scope_id,
            client=client,
            body=body,
            id=id,
        )
    ).parsed
