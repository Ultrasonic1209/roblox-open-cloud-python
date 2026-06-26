from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.data_store_entry import DataStoreEntry
from ...types import Response


def _get_kwargs(
    universe_id: str,
    data_store_id: str,
    scope_id: str,
    entry_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/cloud/v2/universes/{universe_id}/data-stores/{data_store_id}/scopes/{scope_id}/entries/{entry_id}".format(
            universe_id=quote(str(universe_id), safe=""),
            data_store_id=quote(str(data_store_id), safe=""),
            scope_id=quote(str(scope_id), safe=""),
            entry_id=quote(str(entry_id), safe=""),
        ),
        "extensions": {
            "openapi-extensions": {
                "x-roblox-engine-usability": {"apiKeyWithHttpService": True},
                "x-roblox-rate-limits": {
                    "description": "Data stores requests are subject to additional throttling limits described in the [Open Cloud guide for data stores](https://create.roblox.com/docs/cloud/guides/data-stores/throttling).",
                    "perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 1000000},
                },
                "x-roblox-scopes": [{"name": "universe-datastores.objects:read"}],
                "x-roblox-docs": {
                    "category": "Data and memory stores",
                    "methodProperties": {"scopes": ["universe-datastores.objects:read"]},
                    "resource": {"$ref": "#/components/schemas/DataStoreEntry", "name": "DataStoreEntry"},
                },
                "x-roblox-stability": "STABLE",
            },
            "openapi-id": "Cloud_GetDataStoreEntry__Using_Universes_DataStores_Scopes",
        },
    }

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
) -> Response[DataStoreEntry]:
    """Get Data Store Entry

     Gets the specified entry.

    To get the entry at a specific revision, add `@<revisionId>` to the end of
    the path.

    For example, to get `my-entry` at the revision ID
    `08DC3D3F43F9FCC1.0000000001.08DC3D3F43F9FCC1.01`, use the path
    `/cloud/v2/universes/1234/data-stores/5678/entries/my-
    entry@08DC3D3F43F9FCC1.0000000001.08DC3D3F43F9FCC1.01`.

    If your entry ID contains one or more `@` characters, and you want to get
    the latest version rather than at any specific revision, append the special
    revision ID `@latest` to the end of the path. Otherwise, the segment of the
    entry ID after the last `@` will be interpreted as a revision ID.

    For example, to get the latest revision of `my-entry`, use the path
    `/cloud/v2/universes/1234/data-stores/5678/entries/my@entry@latest`.

    To get the entry that was current at a specific time, add
    `@latest:<timestamp>` to the end of the path, where `<timestamp>` is
    RFC-3339 formatted. The given timestamp must be after
    the Unix epoch (1/1/1970) and not more than ten minutes in the future.

    For example, to get the revision of `my-entry` that was current on
    12/2/2024 at 06:00 UTC, use the path
    `/cloud/v2/universes/1234/data-stores/5678/entries/my-entry@latest:2024-12-02T06:00:00Z`.

    Args:
        universe_id (str):
        data_store_id (str):
        scope_id (str):
        entry_id (str):

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
) -> DataStoreEntry | None:
    """Get Data Store Entry

     Gets the specified entry.

    To get the entry at a specific revision, add `@<revisionId>` to the end of
    the path.

    For example, to get `my-entry` at the revision ID
    `08DC3D3F43F9FCC1.0000000001.08DC3D3F43F9FCC1.01`, use the path
    `/cloud/v2/universes/1234/data-stores/5678/entries/my-
    entry@08DC3D3F43F9FCC1.0000000001.08DC3D3F43F9FCC1.01`.

    If your entry ID contains one or more `@` characters, and you want to get
    the latest version rather than at any specific revision, append the special
    revision ID `@latest` to the end of the path. Otherwise, the segment of the
    entry ID after the last `@` will be interpreted as a revision ID.

    For example, to get the latest revision of `my-entry`, use the path
    `/cloud/v2/universes/1234/data-stores/5678/entries/my@entry@latest`.

    To get the entry that was current at a specific time, add
    `@latest:<timestamp>` to the end of the path, where `<timestamp>` is
    RFC-3339 formatted. The given timestamp must be after
    the Unix epoch (1/1/1970) and not more than ten minutes in the future.

    For example, to get the revision of `my-entry` that was current on
    12/2/2024 at 06:00 UTC, use the path
    `/cloud/v2/universes/1234/data-stores/5678/entries/my-entry@latest:2024-12-02T06:00:00Z`.

    Args:
        universe_id (str):
        data_store_id (str):
        scope_id (str):
        entry_id (str):

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
    ).parsed


async def asyncio_detailed(
    universe_id: str,
    data_store_id: str,
    scope_id: str,
    entry_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[DataStoreEntry]:
    """Get Data Store Entry

     Gets the specified entry.

    To get the entry at a specific revision, add `@<revisionId>` to the end of
    the path.

    For example, to get `my-entry` at the revision ID
    `08DC3D3F43F9FCC1.0000000001.08DC3D3F43F9FCC1.01`, use the path
    `/cloud/v2/universes/1234/data-stores/5678/entries/my-
    entry@08DC3D3F43F9FCC1.0000000001.08DC3D3F43F9FCC1.01`.

    If your entry ID contains one or more `@` characters, and you want to get
    the latest version rather than at any specific revision, append the special
    revision ID `@latest` to the end of the path. Otherwise, the segment of the
    entry ID after the last `@` will be interpreted as a revision ID.

    For example, to get the latest revision of `my-entry`, use the path
    `/cloud/v2/universes/1234/data-stores/5678/entries/my@entry@latest`.

    To get the entry that was current at a specific time, add
    `@latest:<timestamp>` to the end of the path, where `<timestamp>` is
    RFC-3339 formatted. The given timestamp must be after
    the Unix epoch (1/1/1970) and not more than ten minutes in the future.

    For example, to get the revision of `my-entry` that was current on
    12/2/2024 at 06:00 UTC, use the path
    `/cloud/v2/universes/1234/data-stores/5678/entries/my-entry@latest:2024-12-02T06:00:00Z`.

    Args:
        universe_id (str):
        data_store_id (str):
        scope_id (str):
        entry_id (str):

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
) -> DataStoreEntry | None:
    """Get Data Store Entry

     Gets the specified entry.

    To get the entry at a specific revision, add `@<revisionId>` to the end of
    the path.

    For example, to get `my-entry` at the revision ID
    `08DC3D3F43F9FCC1.0000000001.08DC3D3F43F9FCC1.01`, use the path
    `/cloud/v2/universes/1234/data-stores/5678/entries/my-
    entry@08DC3D3F43F9FCC1.0000000001.08DC3D3F43F9FCC1.01`.

    If your entry ID contains one or more `@` characters, and you want to get
    the latest version rather than at any specific revision, append the special
    revision ID `@latest` to the end of the path. Otherwise, the segment of the
    entry ID after the last `@` will be interpreted as a revision ID.

    For example, to get the latest revision of `my-entry`, use the path
    `/cloud/v2/universes/1234/data-stores/5678/entries/my@entry@latest`.

    To get the entry that was current at a specific time, add
    `@latest:<timestamp>` to the end of the path, where `<timestamp>` is
    RFC-3339 formatted. The given timestamp must be after
    the Unix epoch (1/1/1970) and not more than ten minutes in the future.

    For example, to get the revision of `my-entry` that was current on
    12/2/2024 at 06:00 UTC, use the path
    `/cloud/v2/universes/1234/data-stores/5678/entries/my-entry@latest:2024-12-02T06:00:00Z`.

    Args:
        universe_id (str):
        data_store_id (str):
        scope_id (str):
        entry_id (str):

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
        )
    ).parsed
