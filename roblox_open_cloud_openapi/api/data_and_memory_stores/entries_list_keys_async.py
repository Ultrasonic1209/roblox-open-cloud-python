from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.entries_list_keys_async_response_200 import EntriesListKeysAsyncResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    universe_id: int,
    *,
    datastore_name: None | str | Unset = UNSET,
    scope: None | str | Unset = UNSET,
    all_scopes: bool | Unset = False,
    prefix: None | str | Unset = UNSET,
    cursor: None | str | Unset = UNSET,
    limit: int | Unset = 16,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_datastore_name: None | str | Unset
    if isinstance(datastore_name, Unset):
        json_datastore_name = UNSET
    else:
        json_datastore_name = datastore_name
    params["datastoreName"] = json_datastore_name

    json_scope: None | str | Unset
    if isinstance(scope, Unset):
        json_scope = UNSET
    else:
        json_scope = scope
    params["scope"] = json_scope

    params["allScopes"] = all_scopes

    json_prefix: None | str | Unset
    if isinstance(prefix, Unset):
        json_prefix = UNSET
    else:
        json_prefix = prefix
    params["prefix"] = json_prefix

    json_cursor: None | str | Unset
    if isinstance(cursor, Unset):
        json_cursor = UNSET
    else:
        json_cursor = cursor
    params["cursor"] = json_cursor

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/datastores/v1/universes/{universe_id}/standard-datastores/datastore/entries".format(
            universe_id=quote(str(universe_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EntriesListKeysAsyncResponse200 | None:
    if response.status_code == 200:
        response_200 = EntriesListKeysAsyncResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[EntriesListKeysAsyncResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    datastore_name: None | str | Unset = UNSET,
    scope: None | str | Unset = UNSET,
    all_scopes: bool | Unset = False,
    prefix: None | str | Unset = UNSET,
    cursor: None | str | Unset = UNSET,
    limit: int | Unset = 16,
) -> Response[EntriesListKeysAsyncResponse200]:
    """List entries

     Returns a list of entry keys within a data store.

     Entries marked deleted with a tombstone version are still included in the response if they have yet
    to be permanently deleted.

    Args:
        universe_id (int):
        datastore_name (None | str | Unset):
        scope (None | str | Unset):
        all_scopes (bool | Unset):  Default: False.
        prefix (None | str | Unset):
        cursor (None | str | Unset):
        limit (int | Unset):  Default: 16.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EntriesListKeysAsyncResponse200]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        datastore_name=datastore_name,
        scope=scope,
        all_scopes=all_scopes,
        prefix=prefix,
        cursor=cursor,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    datastore_name: None | str | Unset = UNSET,
    scope: None | str | Unset = UNSET,
    all_scopes: bool | Unset = False,
    prefix: None | str | Unset = UNSET,
    cursor: None | str | Unset = UNSET,
    limit: int | Unset = 16,
) -> EntriesListKeysAsyncResponse200 | None:
    """List entries

     Returns a list of entry keys within a data store.

     Entries marked deleted with a tombstone version are still included in the response if they have yet
    to be permanently deleted.

    Args:
        universe_id (int):
        datastore_name (None | str | Unset):
        scope (None | str | Unset):
        all_scopes (bool | Unset):  Default: False.
        prefix (None | str | Unset):
        cursor (None | str | Unset):
        limit (int | Unset):  Default: 16.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EntriesListKeysAsyncResponse200
    """

    return sync_detailed(
        universe_id=universe_id,
        client=client,
        datastore_name=datastore_name,
        scope=scope,
        all_scopes=all_scopes,
        prefix=prefix,
        cursor=cursor,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    datastore_name: None | str | Unset = UNSET,
    scope: None | str | Unset = UNSET,
    all_scopes: bool | Unset = False,
    prefix: None | str | Unset = UNSET,
    cursor: None | str | Unset = UNSET,
    limit: int | Unset = 16,
) -> Response[EntriesListKeysAsyncResponse200]:
    """List entries

     Returns a list of entry keys within a data store.

     Entries marked deleted with a tombstone version are still included in the response if they have yet
    to be permanently deleted.

    Args:
        universe_id (int):
        datastore_name (None | str | Unset):
        scope (None | str | Unset):
        all_scopes (bool | Unset):  Default: False.
        prefix (None | str | Unset):
        cursor (None | str | Unset):
        limit (int | Unset):  Default: 16.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EntriesListKeysAsyncResponse200]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        datastore_name=datastore_name,
        scope=scope,
        all_scopes=all_scopes,
        prefix=prefix,
        cursor=cursor,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    datastore_name: None | str | Unset = UNSET,
    scope: None | str | Unset = UNSET,
    all_scopes: bool | Unset = False,
    prefix: None | str | Unset = UNSET,
    cursor: None | str | Unset = UNSET,
    limit: int | Unset = 16,
) -> EntriesListKeysAsyncResponse200 | None:
    """List entries

     Returns a list of entry keys within a data store.

     Entries marked deleted with a tombstone version are still included in the response if they have yet
    to be permanently deleted.

    Args:
        universe_id (int):
        datastore_name (None | str | Unset):
        scope (None | str | Unset):
        all_scopes (bool | Unset):  Default: False.
        prefix (None | str | Unset):
        cursor (None | str | Unset):
        limit (int | Unset):  Default: 16.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EntriesListKeysAsyncResponse200
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            client=client,
            datastore_name=datastore_name,
            scope=scope,
            all_scopes=all_scopes,
            prefix=prefix,
            cursor=cursor,
            limit=limit,
        )
    ).parsed
