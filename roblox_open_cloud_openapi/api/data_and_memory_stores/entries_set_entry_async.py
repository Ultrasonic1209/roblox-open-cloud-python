import sys
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response

if sys.version_info >= (3, 13):
    from warnings import deprecated
else:
    from typing_extensions import deprecated

from ...models.entry_version import EntryVersion
from ...types import Unset


def _get_kwargs(
    universe_id: int,
    *,
    body: str | Unset = UNSET,
    datastore_name: None | str | Unset = UNSET,
    entry_key: None | str | Unset = UNSET,
    match_version: None | str | Unset = UNSET,
    exclusive_create: bool | Unset = False,
    scope: None | str | Unset = "global",
    roblox_entry_attributes: None | str | Unset = UNSET,
    roblox_entry_userids: None | str | Unset = UNSET,
    content_md5: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(roblox_entry_attributes, Unset):
        headers["roblox-entry-attributes"] = roblox_entry_attributes

    if not isinstance(roblox_entry_userids, Unset):
        headers["roblox-entry-userids"] = roblox_entry_userids

    if not isinstance(content_md5, Unset):
        headers["content-md5"] = content_md5

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

    json_match_version: None | str | Unset
    if isinstance(match_version, Unset):
        json_match_version = UNSET
    else:
        json_match_version = match_version
    params["matchVersion"] = json_match_version

    params["exclusiveCreate"] = exclusive_create

    json_scope: None | str | Unset
    if isinstance(scope, Unset):
        json_scope = UNSET
    else:
        json_scope = scope
    params["scope"] = json_scope

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/datastores/v1/universes/{universe_id}/standard-datastores/datastore/entries/entry".format(
            universe_id=quote(str(universe_id), safe=""),
        ),
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> EntryVersion | None:
    if response.status_code == 200:
        response_200 = EntryVersion.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[EntryVersion]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/storage#Entries_SetEntryAsync"
)
def sync_detailed(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    body: str | Unset = UNSET,
    datastore_name: None | str | Unset = UNSET,
    entry_key: None | str | Unset = UNSET,
    match_version: None | str | Unset = UNSET,
    exclusive_create: bool | Unset = False,
    scope: None | str | Unset = "global",
    roblox_entry_attributes: None | str | Unset = UNSET,
    roblox_entry_userids: None | str | Unset = UNSET,
    content_md5: None | str | Unset = UNSET,
) -> Response[EntryVersion]:
    """Set entry.

     Sets the value, metadata and user IDs associated with an entry.

    Args:
        universe_id (int):
        datastore_name (None | str | Unset):
        entry_key (None | str | Unset):
        match_version (None | str | Unset):
        exclusive_create (bool | Unset):  Default: False.
        scope (None | str | Unset):  Default: 'global'.
        roblox_entry_attributes (None | str | Unset):
        roblox_entry_userids (None | str | Unset):
        content_md5 (None | str | Unset):
        body (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EntryVersion]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        body=body,
        datastore_name=datastore_name,
        entry_key=entry_key,
        match_version=match_version,
        exclusive_create=exclusive_create,
        scope=scope,
        roblox_entry_attributes=roblox_entry_attributes,
        roblox_entry_userids=roblox_entry_userids,
        content_md5=content_md5,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/storage#Entries_SetEntryAsync"
)
def sync(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    body: str | Unset = UNSET,
    datastore_name: None | str | Unset = UNSET,
    entry_key: None | str | Unset = UNSET,
    match_version: None | str | Unset = UNSET,
    exclusive_create: bool | Unset = False,
    scope: None | str | Unset = "global",
    roblox_entry_attributes: None | str | Unset = UNSET,
    roblox_entry_userids: None | str | Unset = UNSET,
    content_md5: None | str | Unset = UNSET,
) -> EntryVersion | None:
    """Set entry.

     Sets the value, metadata and user IDs associated with an entry.

    Args:
        universe_id (int):
        datastore_name (None | str | Unset):
        entry_key (None | str | Unset):
        match_version (None | str | Unset):
        exclusive_create (bool | Unset):  Default: False.
        scope (None | str | Unset):  Default: 'global'.
        roblox_entry_attributes (None | str | Unset):
        roblox_entry_userids (None | str | Unset):
        content_md5 (None | str | Unset):
        body (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EntryVersion
    """

    return sync_detailed(
        universe_id=universe_id,
        client=client,
        body=body,
        datastore_name=datastore_name,
        entry_key=entry_key,
        match_version=match_version,
        exclusive_create=exclusive_create,
        scope=scope,
        roblox_entry_attributes=roblox_entry_attributes,
        roblox_entry_userids=roblox_entry_userids,
        content_md5=content_md5,
    ).parsed


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/storage#Entries_SetEntryAsync"
)
async def asyncio_detailed(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    body: str | Unset = UNSET,
    datastore_name: None | str | Unset = UNSET,
    entry_key: None | str | Unset = UNSET,
    match_version: None | str | Unset = UNSET,
    exclusive_create: bool | Unset = False,
    scope: None | str | Unset = "global",
    roblox_entry_attributes: None | str | Unset = UNSET,
    roblox_entry_userids: None | str | Unset = UNSET,
    content_md5: None | str | Unset = UNSET,
) -> Response[EntryVersion]:
    """Set entry.

     Sets the value, metadata and user IDs associated with an entry.

    Args:
        universe_id (int):
        datastore_name (None | str | Unset):
        entry_key (None | str | Unset):
        match_version (None | str | Unset):
        exclusive_create (bool | Unset):  Default: False.
        scope (None | str | Unset):  Default: 'global'.
        roblox_entry_attributes (None | str | Unset):
        roblox_entry_userids (None | str | Unset):
        content_md5 (None | str | Unset):
        body (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EntryVersion]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        body=body,
        datastore_name=datastore_name,
        entry_key=entry_key,
        match_version=match_version,
        exclusive_create=exclusive_create,
        scope=scope,
        roblox_entry_attributes=roblox_entry_attributes,
        roblox_entry_userids=roblox_entry_userids,
        content_md5=content_md5,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/storage#Entries_SetEntryAsync"
)
async def asyncio(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    body: str | Unset = UNSET,
    datastore_name: None | str | Unset = UNSET,
    entry_key: None | str | Unset = UNSET,
    match_version: None | str | Unset = UNSET,
    exclusive_create: bool | Unset = False,
    scope: None | str | Unset = "global",
    roblox_entry_attributes: None | str | Unset = UNSET,
    roblox_entry_userids: None | str | Unset = UNSET,
    content_md5: None | str | Unset = UNSET,
) -> EntryVersion | None:
    """Set entry.

     Sets the value, metadata and user IDs associated with an entry.

    Args:
        universe_id (int):
        datastore_name (None | str | Unset):
        entry_key (None | str | Unset):
        match_version (None | str | Unset):
        exclusive_create (bool | Unset):  Default: False.
        scope (None | str | Unset):  Default: 'global'.
        roblox_entry_attributes (None | str | Unset):
        roblox_entry_userids (None | str | Unset):
        content_md5 (None | str | Unset):
        body (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EntryVersion
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            client=client,
            body=body,
            datastore_name=datastore_name,
            entry_key=entry_key,
            match_version=match_version,
            exclusive_create=exclusive_create,
            scope=scope,
            roblox_entry_attributes=roblox_entry_attributes,
            roblox_entry_userids=roblox_entry_userids,
            content_md5=content_md5,
        )
    ).parsed
