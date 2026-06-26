from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.data_store_entry import DataStoreEntry
from ...types import UNSET, Response, Unset


def _get_kwargs(
    universe_id: str,
    data_store_id: str,
    scope_id: str,
    entry_id: str,
    *,
    body: DataStoreEntry,
    allow_missing: bool | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["allowMissing"] = allow_missing

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/cloud/v2/universes/{universe_id}/data-stores/{data_store_id}/scopes/{scope_id}/entries/{entry_id}".format(
            universe_id=quote(str(universe_id), safe=""),
            data_store_id=quote(str(data_store_id), safe=""),
            scope_id=quote(str(scope_id), safe=""),
            entry_id=quote(str(entry_id), safe=""),
        ),
        "params": params,
        "extensions": {
            "openapi-extensions": {
                "x-roblox-engine-usability": {"apiKeyWithHttpService": True},
                "x-roblox-rate-limits": {
                    "description": "Data stores requests are subject to additional throttling limits described in the [Open Cloud guide for data stores](https://create.roblox.com/docs/cloud/guides/data-stores/throttling).",
                    "perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 1000000},
                },
                "x-roblox-scopes": [{"name": "universe-datastores.objects:update"}],
                "x-roblox-docs": {
                    "category": "Data and memory stores",
                    "methodProperties": {"scopes": ["universe-datastores.objects:update"]},
                    "resource": {"$ref": "#/components/schemas/DataStoreEntry", "name": "DataStoreEntry"},
                },
                "x-roblox-stability": "STABLE",
            },
            "openapi-id": "Cloud_UpdateDataStoreEntry__Using_Universes_DataStores_Scopes",
        },
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> DataStoreEntry | None:
    if response.status_code == 200:
        response_200 = DataStoreEntry.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[DataStoreEntry]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    universe_id: str,
    data_store_id: str,
    scope_id: str,
    entry_id: str,
    *,
    client: AuthenticatedClient,
    body: DataStoreEntry,
    allow_missing: bool | Unset = UNSET,
) -> Response[DataStoreEntry]:
    """Update Data Store Entry

     Updates the value, attributes, and users of an entry.

    Updating specific revisions of the entry is **unsupported**. If you specify
    a revision ID in the path and `allow_missing` is `true`, the update request
    will instead create a new entry with the `@<revisionId>` suffix as part of
    the key.

    Partial update is **unsupported**. If attributes or users are not
    provided when updating the value, they will be cleared. Value must always
    be provided when updating an entry.

    Args:
        universe_id (str):
        data_store_id (str):
        scope_id (str):
        entry_id (str):
        allow_missing (bool | Unset):  Example: True.
        body (DataStoreEntry): A key-value entry in a data store.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataStoreEntry]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        data_store_id=data_store_id,
        scope_id=scope_id,
        entry_id=entry_id,
        body=body,
        allow_missing=allow_missing,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: str,
    data_store_id: str,
    scope_id: str,
    entry_id: str,
    *,
    client: AuthenticatedClient,
    body: DataStoreEntry,
    allow_missing: bool | Unset = UNSET,
) -> DataStoreEntry | None:
    """Update Data Store Entry

     Updates the value, attributes, and users of an entry.

    Updating specific revisions of the entry is **unsupported**. If you specify
    a revision ID in the path and `allow_missing` is `true`, the update request
    will instead create a new entry with the `@<revisionId>` suffix as part of
    the key.

    Partial update is **unsupported**. If attributes or users are not
    provided when updating the value, they will be cleared. Value must always
    be provided when updating an entry.

    Args:
        universe_id (str):
        data_store_id (str):
        scope_id (str):
        entry_id (str):
        allow_missing (bool | Unset):  Example: True.
        body (DataStoreEntry): A key-value entry in a data store.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataStoreEntry
    """

    return sync_detailed(
        universe_id=universe_id,
        data_store_id=data_store_id,
        scope_id=scope_id,
        entry_id=entry_id,
        client=client,
        body=body,
        allow_missing=allow_missing,
    ).parsed


async def asyncio_detailed(
    universe_id: str,
    data_store_id: str,
    scope_id: str,
    entry_id: str,
    *,
    client: AuthenticatedClient,
    body: DataStoreEntry,
    allow_missing: bool | Unset = UNSET,
) -> Response[DataStoreEntry]:
    """Update Data Store Entry

     Updates the value, attributes, and users of an entry.

    Updating specific revisions of the entry is **unsupported**. If you specify
    a revision ID in the path and `allow_missing` is `true`, the update request
    will instead create a new entry with the `@<revisionId>` suffix as part of
    the key.

    Partial update is **unsupported**. If attributes or users are not
    provided when updating the value, they will be cleared. Value must always
    be provided when updating an entry.

    Args:
        universe_id (str):
        data_store_id (str):
        scope_id (str):
        entry_id (str):
        allow_missing (bool | Unset):  Example: True.
        body (DataStoreEntry): A key-value entry in a data store.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataStoreEntry]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        data_store_id=data_store_id,
        scope_id=scope_id,
        entry_id=entry_id,
        body=body,
        allow_missing=allow_missing,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: str,
    data_store_id: str,
    scope_id: str,
    entry_id: str,
    *,
    client: AuthenticatedClient,
    body: DataStoreEntry,
    allow_missing: bool | Unset = UNSET,
) -> DataStoreEntry | None:
    """Update Data Store Entry

     Updates the value, attributes, and users of an entry.

    Updating specific revisions of the entry is **unsupported**. If you specify
    a revision ID in the path and `allow_missing` is `true`, the update request
    will instead create a new entry with the `@<revisionId>` suffix as part of
    the key.

    Partial update is **unsupported**. If attributes or users are not
    provided when updating the value, they will be cleared. Value must always
    be provided when updating an entry.

    Args:
        universe_id (str):
        data_store_id (str):
        scope_id (str):
        entry_id (str):
        allow_missing (bool | Unset):  Example: True.
        body (DataStoreEntry): A key-value entry in a data store.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataStoreEntry
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            data_store_id=data_store_id,
            scope_id=scope_id,
            entry_id=entry_id,
            client=client,
            body=body,
            allow_missing=allow_missing,
        )
    ).parsed
