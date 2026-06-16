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

from ...types import Unset


def _get_kwargs(
    universe_id: int,
    *,
    datastore_name: None | str | Unset = UNSET,
    entry_key: None | str | Unset = UNSET,
    scope: None | str | Unset = "global",
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

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/datastores/v1/universes/{universe_id}/standard-datastores/datastore/entries/entry".format(
            universe_id=quote(str(universe_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 204:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/storage#Entries_DeleteEntryAsync"
)
def sync_detailed(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    datastore_name: None | str | Unset = UNSET,
    entry_key: None | str | Unset = UNSET,
    scope: None | str | Unset = "global",
) -> Response[Any]:
    """Delete entry.

     Marks the entry as deleted by creating a tombstone version. Entries are deleted permanently after 30
    days.

    Args:
        universe_id (int):
        datastore_name (None | str | Unset):
        entry_key (None | str | Unset):
        scope (None | str | Unset):  Default: 'global'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        datastore_name=datastore_name,
        entry_key=entry_key,
        scope=scope,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/storage#Entries_DeleteEntryAsync"
)
async def asyncio_detailed(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    datastore_name: None | str | Unset = UNSET,
    entry_key: None | str | Unset = UNSET,
    scope: None | str | Unset = "global",
) -> Response[Any]:
    """Delete entry.

     Marks the entry as deleted by creating a tombstone version. Entries are deleted permanently after 30
    days.

    Args:
        universe_id (int):
        datastore_name (None | str | Unset):
        entry_key (None | str | Unset):
        scope (None | str | Unset):  Default: 'global'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        datastore_name=datastore_name,
        entry_key=entry_key,
        scope=scope,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
