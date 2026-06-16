from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.entries_increment_entry_async_response_200 import EntriesIncrementEntryAsyncResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    universe_id: int,
    *,
    datastore_name: None | str | Unset = UNSET,
    entry_key: None | str | Unset = UNSET,
    increment_by: int | Unset = 1,
    scope: None | str | Unset = "global",
    roblox_entry_attributes: None | str | Unset = UNSET,
    roblox_entry_userids: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(roblox_entry_attributes, Unset):
        headers["roblox-entry-attributes"] = roblox_entry_attributes

    if not isinstance(roblox_entry_userids, Unset):
        headers["roblox-entry-userids"] = roblox_entry_userids

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

    params["incrementBy"] = increment_by

    json_scope: None | str | Unset
    if isinstance(scope, Unset):
        json_scope = UNSET
    else:
        json_scope = scope
    params["scope"] = json_scope

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/datastores/v1/universes/{universe_id}/standard-datastores/datastore/entries/entry/increment".format(
            universe_id=quote(str(universe_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | EntriesIncrementEntryAsyncResponse200 | None:
    if response.status_code == 200:
        response_200 = EntriesIncrementEntryAsyncResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | EntriesIncrementEntryAsyncResponse200]:
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
    entry_key: None | str | Unset = UNSET,
    increment_by: int | Unset = 1,
    scope: None | str | Unset = "global",
    roblox_entry_attributes: None | str | Unset = UNSET,
    roblox_entry_userids: None | str | Unset = UNSET,
) -> Response[Any | EntriesIncrementEntryAsyncResponse200]:
    r"""Increment entry

     Increments the value for an entry by a given amount, or create a new entry with that amount. Returns
    the entry and metadata.

    Metadata can be found in the response headers like the following:
    ```text
    content-md5: zuYxEhwuySMv0i8CitXImw==
    roblox-entry-version: 08D9E6A3F2188CFF.0000000001.08D9E6A3F2188CFF.01
    roblox-entry-created-time: 2022-02-02T23:30:06.5388799+00:00
    roblox-entry-version-created-time: 2022-02-02T23:30:06.5388799+00:00
    roblox-entry-attributes: { \"myAttribute\": \"myValue\" }
    roblox-entry-userids: [1, 2, 3]
    ```

    | Header | Description |
    |---|---|
    | `content-md5` | The base64-encoded MD5 checksum of the content. See [Content-
    MD5](/cloud/guides/data-stores/request-handling.md#content-md5). |
    | `roblox-entry-version` | The version of the returned entry. |
    | `roblox-entry-created-time` | The time at which the entry was created. |
    | `roblox-entry-version-created-time` | The time at which this particular version was created. |
    | `roblox-entry-attributes` | Attributes tagged with the entry. Serialized JSON map object. |
    | `roblox-entry-userids` | Comma-separated list of Roblox user IDs tagged with the entry. |

    Args:
        universe_id (int):
        datastore_name (None | str | Unset):
        entry_key (None | str | Unset):
        increment_by (int | Unset):  Default: 1.
        scope (None | str | Unset):  Default: 'global'.
        roblox_entry_attributes (None | str | Unset):
        roblox_entry_userids (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EntriesIncrementEntryAsyncResponse200]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        datastore_name=datastore_name,
        entry_key=entry_key,
        increment_by=increment_by,
        scope=scope,
        roblox_entry_attributes=roblox_entry_attributes,
        roblox_entry_userids=roblox_entry_userids,
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
    entry_key: None | str | Unset = UNSET,
    increment_by: int | Unset = 1,
    scope: None | str | Unset = "global",
    roblox_entry_attributes: None | str | Unset = UNSET,
    roblox_entry_userids: None | str | Unset = UNSET,
) -> Any | EntriesIncrementEntryAsyncResponse200 | None:
    r"""Increment entry

     Increments the value for an entry by a given amount, or create a new entry with that amount. Returns
    the entry and metadata.

    Metadata can be found in the response headers like the following:
    ```text
    content-md5: zuYxEhwuySMv0i8CitXImw==
    roblox-entry-version: 08D9E6A3F2188CFF.0000000001.08D9E6A3F2188CFF.01
    roblox-entry-created-time: 2022-02-02T23:30:06.5388799+00:00
    roblox-entry-version-created-time: 2022-02-02T23:30:06.5388799+00:00
    roblox-entry-attributes: { \"myAttribute\": \"myValue\" }
    roblox-entry-userids: [1, 2, 3]
    ```

    | Header | Description |
    |---|---|
    | `content-md5` | The base64-encoded MD5 checksum of the content. See [Content-
    MD5](/cloud/guides/data-stores/request-handling.md#content-md5). |
    | `roblox-entry-version` | The version of the returned entry. |
    | `roblox-entry-created-time` | The time at which the entry was created. |
    | `roblox-entry-version-created-time` | The time at which this particular version was created. |
    | `roblox-entry-attributes` | Attributes tagged with the entry. Serialized JSON map object. |
    | `roblox-entry-userids` | Comma-separated list of Roblox user IDs tagged with the entry. |

    Args:
        universe_id (int):
        datastore_name (None | str | Unset):
        entry_key (None | str | Unset):
        increment_by (int | Unset):  Default: 1.
        scope (None | str | Unset):  Default: 'global'.
        roblox_entry_attributes (None | str | Unset):
        roblox_entry_userids (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EntriesIncrementEntryAsyncResponse200
    """

    return sync_detailed(
        universe_id=universe_id,
        client=client,
        datastore_name=datastore_name,
        entry_key=entry_key,
        increment_by=increment_by,
        scope=scope,
        roblox_entry_attributes=roblox_entry_attributes,
        roblox_entry_userids=roblox_entry_userids,
    ).parsed


async def asyncio_detailed(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    datastore_name: None | str | Unset = UNSET,
    entry_key: None | str | Unset = UNSET,
    increment_by: int | Unset = 1,
    scope: None | str | Unset = "global",
    roblox_entry_attributes: None | str | Unset = UNSET,
    roblox_entry_userids: None | str | Unset = UNSET,
) -> Response[Any | EntriesIncrementEntryAsyncResponse200]:
    r"""Increment entry

     Increments the value for an entry by a given amount, or create a new entry with that amount. Returns
    the entry and metadata.

    Metadata can be found in the response headers like the following:
    ```text
    content-md5: zuYxEhwuySMv0i8CitXImw==
    roblox-entry-version: 08D9E6A3F2188CFF.0000000001.08D9E6A3F2188CFF.01
    roblox-entry-created-time: 2022-02-02T23:30:06.5388799+00:00
    roblox-entry-version-created-time: 2022-02-02T23:30:06.5388799+00:00
    roblox-entry-attributes: { \"myAttribute\": \"myValue\" }
    roblox-entry-userids: [1, 2, 3]
    ```

    | Header | Description |
    |---|---|
    | `content-md5` | The base64-encoded MD5 checksum of the content. See [Content-
    MD5](/cloud/guides/data-stores/request-handling.md#content-md5). |
    | `roblox-entry-version` | The version of the returned entry. |
    | `roblox-entry-created-time` | The time at which the entry was created. |
    | `roblox-entry-version-created-time` | The time at which this particular version was created. |
    | `roblox-entry-attributes` | Attributes tagged with the entry. Serialized JSON map object. |
    | `roblox-entry-userids` | Comma-separated list of Roblox user IDs tagged with the entry. |

    Args:
        universe_id (int):
        datastore_name (None | str | Unset):
        entry_key (None | str | Unset):
        increment_by (int | Unset):  Default: 1.
        scope (None | str | Unset):  Default: 'global'.
        roblox_entry_attributes (None | str | Unset):
        roblox_entry_userids (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EntriesIncrementEntryAsyncResponse200]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        datastore_name=datastore_name,
        entry_key=entry_key,
        increment_by=increment_by,
        scope=scope,
        roblox_entry_attributes=roblox_entry_attributes,
        roblox_entry_userids=roblox_entry_userids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    datastore_name: None | str | Unset = UNSET,
    entry_key: None | str | Unset = UNSET,
    increment_by: int | Unset = 1,
    scope: None | str | Unset = "global",
    roblox_entry_attributes: None | str | Unset = UNSET,
    roblox_entry_userids: None | str | Unset = UNSET,
) -> Any | EntriesIncrementEntryAsyncResponse200 | None:
    r"""Increment entry

     Increments the value for an entry by a given amount, or create a new entry with that amount. Returns
    the entry and metadata.

    Metadata can be found in the response headers like the following:
    ```text
    content-md5: zuYxEhwuySMv0i8CitXImw==
    roblox-entry-version: 08D9E6A3F2188CFF.0000000001.08D9E6A3F2188CFF.01
    roblox-entry-created-time: 2022-02-02T23:30:06.5388799+00:00
    roblox-entry-version-created-time: 2022-02-02T23:30:06.5388799+00:00
    roblox-entry-attributes: { \"myAttribute\": \"myValue\" }
    roblox-entry-userids: [1, 2, 3]
    ```

    | Header | Description |
    |---|---|
    | `content-md5` | The base64-encoded MD5 checksum of the content. See [Content-
    MD5](/cloud/guides/data-stores/request-handling.md#content-md5). |
    | `roblox-entry-version` | The version of the returned entry. |
    | `roblox-entry-created-time` | The time at which the entry was created. |
    | `roblox-entry-version-created-time` | The time at which this particular version was created. |
    | `roblox-entry-attributes` | Attributes tagged with the entry. Serialized JSON map object. |
    | `roblox-entry-userids` | Comma-separated list of Roblox user IDs tagged with the entry. |

    Args:
        universe_id (int):
        datastore_name (None | str | Unset):
        entry_key (None | str | Unset):
        increment_by (int | Unset):  Default: 1.
        scope (None | str | Unset):  Default: 'global'.
        roblox_entry_attributes (None | str | Unset):
        roblox_entry_userids (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EntriesIncrementEntryAsyncResponse200
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            client=client,
            datastore_name=datastore_name,
            entry_key=entry_key,
            increment_by=increment_by,
            scope=scope,
            roblox_entry_attributes=roblox_entry_attributes,
            roblox_entry_userids=roblox_entry_userids,
        )
    ).parsed
