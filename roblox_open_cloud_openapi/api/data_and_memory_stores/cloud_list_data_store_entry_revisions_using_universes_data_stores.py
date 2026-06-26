from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_data_store_entry_revisions_response import ListDataStoreEntryRevisionsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    universe_id: str,
    data_store_id: str,
    entry_id: str,
    *,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["maxPageSize"] = max_page_size

    params["pageToken"] = page_token

    params["filter"] = filter_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/cloud/v2/universes/{universe_id}/data-stores/{data_store_id}/entries/{entry_id}:listRevisions".format(
            universe_id=quote(str(universe_id), safe=""),
            data_store_id=quote(str(data_store_id), safe=""),
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
                "x-roblox-scopes": [{"name": "universe-datastores.versions:list"}],
                "x-roblox-docs": {
                    "category": "Data and memory stores",
                    "methodProperties": {"scopes": ["universe-datastores.versions:list"]},
                    "resource": {"$ref": "#/components/schemas/DataStoreEntry", "name": "DataStoreEntry"},
                },
                "x-roblox-stability": "STABLE",
            },
            "openapi-id": "Cloud_ListDataStoreEntryRevisions__Using_Universes_DataStores",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ListDataStoreEntryRevisionsResponse | None:
    if response.status_code == 200:
        response_200 = ListDataStoreEntryRevisionsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ListDataStoreEntryRevisionsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    universe_id: str,
    data_store_id: str,
    entry_id: str,
    *,
    client: AuthenticatedClient,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
) -> Response[ListDataStoreEntryRevisionsResponse]:
    """List Data Store Entry Revisions

     List revisions of the data store entry.

    This method returns partial data store entries.

    In particular, only the `path`, `id`, `createTime`, `revisionCreateTime`,
    `revisionId`, `etag`, and `state` fields are populated. Both the `path` and
    `id` fields will have an `@<version>` suffix.

    In order to get the full entry at a revision, you can use the provided
    `path` field with the `GetDataStoreEntry` method, i.e. `GET
    /cloud/v2/universes/1234/data-stores/5678/entries/my-entry@<version>`.

    Args:
        universe_id (str):
        data_store_id (str):
        entry_id (str):
        max_page_size (int | Unset):
        page_token (str | Unset):
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListDataStoreEntryRevisionsResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        data_store_id=data_store_id,
        entry_id=entry_id,
        max_page_size=max_page_size,
        page_token=page_token,
        filter_=filter_,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: str,
    data_store_id: str,
    entry_id: str,
    *,
    client: AuthenticatedClient,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
) -> ListDataStoreEntryRevisionsResponse | None:
    """List Data Store Entry Revisions

     List revisions of the data store entry.

    This method returns partial data store entries.

    In particular, only the `path`, `id`, `createTime`, `revisionCreateTime`,
    `revisionId`, `etag`, and `state` fields are populated. Both the `path` and
    `id` fields will have an `@<version>` suffix.

    In order to get the full entry at a revision, you can use the provided
    `path` field with the `GetDataStoreEntry` method, i.e. `GET
    /cloud/v2/universes/1234/data-stores/5678/entries/my-entry@<version>`.

    Args:
        universe_id (str):
        data_store_id (str):
        entry_id (str):
        max_page_size (int | Unset):
        page_token (str | Unset):
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListDataStoreEntryRevisionsResponse
    """

    return sync_detailed(
        universe_id=universe_id,
        data_store_id=data_store_id,
        entry_id=entry_id,
        client=client,
        max_page_size=max_page_size,
        page_token=page_token,
        filter_=filter_,
    ).parsed


async def asyncio_detailed(
    universe_id: str,
    data_store_id: str,
    entry_id: str,
    *,
    client: AuthenticatedClient,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
) -> Response[ListDataStoreEntryRevisionsResponse]:
    """List Data Store Entry Revisions

     List revisions of the data store entry.

    This method returns partial data store entries.

    In particular, only the `path`, `id`, `createTime`, `revisionCreateTime`,
    `revisionId`, `etag`, and `state` fields are populated. Both the `path` and
    `id` fields will have an `@<version>` suffix.

    In order to get the full entry at a revision, you can use the provided
    `path` field with the `GetDataStoreEntry` method, i.e. `GET
    /cloud/v2/universes/1234/data-stores/5678/entries/my-entry@<version>`.

    Args:
        universe_id (str):
        data_store_id (str):
        entry_id (str):
        max_page_size (int | Unset):
        page_token (str | Unset):
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListDataStoreEntryRevisionsResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        data_store_id=data_store_id,
        entry_id=entry_id,
        max_page_size=max_page_size,
        page_token=page_token,
        filter_=filter_,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: str,
    data_store_id: str,
    entry_id: str,
    *,
    client: AuthenticatedClient,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
) -> ListDataStoreEntryRevisionsResponse | None:
    """List Data Store Entry Revisions

     List revisions of the data store entry.

    This method returns partial data store entries.

    In particular, only the `path`, `id`, `createTime`, `revisionCreateTime`,
    `revisionId`, `etag`, and `state` fields are populated. Both the `path` and
    `id` fields will have an `@<version>` suffix.

    In order to get the full entry at a revision, you can use the provided
    `path` field with the `GetDataStoreEntry` method, i.e. `GET
    /cloud/v2/universes/1234/data-stores/5678/entries/my-entry@<version>`.

    Args:
        universe_id (str):
        data_store_id (str):
        entry_id (str):
        max_page_size (int | Unset):
        page_token (str | Unset):
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListDataStoreEntryRevisionsResponse
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            data_store_id=data_store_id,
            entry_id=entry_id,
            client=client,
            max_page_size=max_page_size,
            page_token=page_token,
            filter_=filter_,
        )
    ).parsed
