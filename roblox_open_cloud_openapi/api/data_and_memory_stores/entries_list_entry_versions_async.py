import sys
from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response

if sys.version_info >= (3, 13):
    from warnings import deprecated
else:
    from typing_extensions import deprecated

import datetime

from ...models.entry_version import EntryVersion
from ...types import Unset


def _get_kwargs(
    universe_id: int,
    *,
    datastore_name: None | str | Unset = UNSET,
    entry_key: None | str | Unset = UNSET,
    scope: None | str | Unset = "global",
    cursor: datetime.datetime | None | Unset = UNSET,
    start_time: datetime.datetime | None | Unset = UNSET,
    end_time: None | str | Unset = UNSET,
    sort_order: None | str | Unset = "Ascending",
    limit: int | Unset = 16,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_datastore_name: None | str | Unset
    if isinstance(datastore_name, Unset):
        json_datastore_name = UNSET
    else:
        json_datastore_name = datastore_name
    params["datastoreName"] = json_datastore_name

    json_entry_key: None | str | Unset
    if isinstance(entry_key, Unset):
        json_entry_key = UNSET
    else:
        json_entry_key = entry_key
    params["entryKey"] = json_entry_key

    json_scope: None | str | Unset
    if isinstance(scope, Unset):
        json_scope = UNSET
    else:
        json_scope = scope
    params["scope"] = json_scope

    json_cursor: None | str | Unset
    if isinstance(cursor, Unset):
        json_cursor = UNSET
    elif isinstance(cursor, datetime.datetime):
        json_cursor = cursor.isoformat()
    else:
        json_cursor = cursor
    params["cursor"] = json_cursor

    json_start_time: None | str | Unset
    if isinstance(start_time, Unset):
        json_start_time = UNSET
    elif isinstance(start_time, datetime.datetime):
        json_start_time = start_time.isoformat()
    else:
        json_start_time = start_time
    params["startTime"] = json_start_time

    json_end_time: None | str | Unset
    if isinstance(end_time, Unset):
        json_end_time = UNSET
    else:
        json_end_time = end_time
    params["endTime"] = json_end_time

    json_sort_order: None | str | Unset
    if isinstance(sort_order, Unset):
        json_sort_order = UNSET
    else:
        json_sort_order = sort_order
    params["sortOrder"] = json_sort_order

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/datastores/v1/universes/{universe_id}/standard-datastores/datastore/entries/entry/versions".format(
            universe_id=quote(str(universe_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | EntryVersion | None:
    if response.status_code == 200:
        response_200 = EntryVersion.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | EntryVersion]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/storage#Entries_ListEntryVersionsAsync"
)
def sync_detailed(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    datastore_name: None | str | Unset = UNSET,
    entry_key: None | str | Unset = UNSET,
    scope: None | str | Unset = "global",
    cursor: datetime.datetime | None | Unset = UNSET,
    start_time: datetime.datetime | None | Unset = UNSET,
    end_time: None | str | Unset = UNSET,
    sort_order: None | str | Unset = "Ascending",
    limit: int | Unset = 16,
) -> Response[Any | EntryVersion]:
    """List entry versions

     Returns a list of versions for an entry.

    Args:
        universe_id (int):
        datastore_name (None | str | Unset):
        entry_key (None | str | Unset):
        scope (None | str | Unset):  Default: 'global'.
        cursor (datetime.datetime | None | Unset):
        start_time (datetime.datetime | None | Unset):
        end_time (None | str | Unset):
        sort_order (None | str | Unset):  Default: 'Ascending'.
        limit (int | Unset):  Default: 16.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EntryVersion]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        datastore_name=datastore_name,
        entry_key=entry_key,
        scope=scope,
        cursor=cursor,
        start_time=start_time,
        end_time=end_time,
        sort_order=sort_order,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/storage#Entries_ListEntryVersionsAsync"
)
def sync(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    datastore_name: None | str | Unset = UNSET,
    entry_key: None | str | Unset = UNSET,
    scope: None | str | Unset = "global",
    cursor: datetime.datetime | None | Unset = UNSET,
    start_time: datetime.datetime | None | Unset = UNSET,
    end_time: None | str | Unset = UNSET,
    sort_order: None | str | Unset = "Ascending",
    limit: int | Unset = 16,
) -> Any | EntryVersion | None:
    """List entry versions

     Returns a list of versions for an entry.

    Args:
        universe_id (int):
        datastore_name (None | str | Unset):
        entry_key (None | str | Unset):
        scope (None | str | Unset):  Default: 'global'.
        cursor (datetime.datetime | None | Unset):
        start_time (datetime.datetime | None | Unset):
        end_time (None | str | Unset):
        sort_order (None | str | Unset):  Default: 'Ascending'.
        limit (int | Unset):  Default: 16.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EntryVersion
    """

    return sync_detailed(
        universe_id=universe_id,
        client=client,
        datastore_name=datastore_name,
        entry_key=entry_key,
        scope=scope,
        cursor=cursor,
        start_time=start_time,
        end_time=end_time,
        sort_order=sort_order,
        limit=limit,
    ).parsed


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/storage#Entries_ListEntryVersionsAsync"
)
async def asyncio_detailed(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    datastore_name: None | str | Unset = UNSET,
    entry_key: None | str | Unset = UNSET,
    scope: None | str | Unset = "global",
    cursor: datetime.datetime | None | Unset = UNSET,
    start_time: datetime.datetime | None | Unset = UNSET,
    end_time: None | str | Unset = UNSET,
    sort_order: None | str | Unset = "Ascending",
    limit: int | Unset = 16,
) -> Response[Any | EntryVersion]:
    """List entry versions

     Returns a list of versions for an entry.

    Args:
        universe_id (int):
        datastore_name (None | str | Unset):
        entry_key (None | str | Unset):
        scope (None | str | Unset):  Default: 'global'.
        cursor (datetime.datetime | None | Unset):
        start_time (datetime.datetime | None | Unset):
        end_time (None | str | Unset):
        sort_order (None | str | Unset):  Default: 'Ascending'.
        limit (int | Unset):  Default: 16.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EntryVersion]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        datastore_name=datastore_name,
        entry_key=entry_key,
        scope=scope,
        cursor=cursor,
        start_time=start_time,
        end_time=end_time,
        sort_order=sort_order,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/storage#Entries_ListEntryVersionsAsync"
)
async def asyncio(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    datastore_name: None | str | Unset = UNSET,
    entry_key: None | str | Unset = UNSET,
    scope: None | str | Unset = "global",
    cursor: datetime.datetime | None | Unset = UNSET,
    start_time: datetime.datetime | None | Unset = UNSET,
    end_time: None | str | Unset = UNSET,
    sort_order: None | str | Unset = "Ascending",
    limit: int | Unset = 16,
) -> Any | EntryVersion | None:
    """List entry versions

     Returns a list of versions for an entry.

    Args:
        universe_id (int):
        datastore_name (None | str | Unset):
        entry_key (None | str | Unset):
        scope (None | str | Unset):  Default: 'global'.
        cursor (datetime.datetime | None | Unset):
        start_time (datetime.datetime | None | Unset):
        end_time (None | str | Unset):
        sort_order (None | str | Unset):  Default: 'Ascending'.
        limit (int | Unset):  Default: 16.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EntryVersion
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            client=client,
            datastore_name=datastore_name,
            entry_key=entry_key,
            scope=scope,
            cursor=cursor,
            start_time=start_time,
            end_time=end_time,
            sort_order=sort_order,
            limit=limit,
        )
    ).parsed
