import sys
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset

if sys.version_info >= (3, 13):
    from warnings import deprecated
else:
    from typing_extensions import deprecated

from ...models.entries_list_keys_async_response_200 import EntriesListKeysAsyncResponse200


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
        "extensions": {
            "openapi-extensions": {
                "x-roblox-cloud-api-operation-name": "List Entries",
                "x-roblox-stability": "BETA",
                "x-roblox-scopes": [{"name": "universe-datastores.objects:list"}],
                "x-roblox-cloud-api-operation": True,
                "x-roblox-lua-equivalent": "DataStore:ListKeysAsync",
                "x-roblox-cloud-api-operation-code-samples": [
                    {
                        "language": "curl",
                        "script": 'curl --include --location --request GET "https://apis.roblox.com/datastores/v1/universes/3310576216/standard-datastores/datastore/entries" \\\n--header "x-api-key: ${API_KEY}" \\\n--get \\\n-d "datastoreName=Coins" \\\n-d "prefix=" \\\n-d "limit=5"',
                    }
                ],
                "x-roblox-rate-limits": {
                    "description": "See [Throttling](/cloud/guides/data-stores/throttling.md).",
                    "perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 5000},
                },
                "x-roblox-recommended-alternatives": [
                    {
                        "url": "https://apis.roblox.com/cloud/v2/universes/{universe_id}/data-stores/{data_store_id}/entries",
                        "httpMethod": "GET",
                        "documentationUrl": "https://create.roblox.com/docs/cloud/reference/features/storage#Cloud_ListDataStoreEntries__Using_Universes",
                    },
                    {
                        "url": "https://apis.roblox.com/cloud/v2/universes/{universe_id}/data-stores/{data_store_id}/scopes/{scope_id}/entries",
                        "httpMethod": "GET",
                        "documentationUrl": "https://create.roblox.com/docs/cloud/reference/features/storage#Cloud_ListDataStoreEntries__Using_Universes_DataStores",
                    },
                ],
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            },
            "openapi-id": "Entries_ListKeysAsync",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> EntriesListKeysAsyncResponse200 | None:
    if response.status_code == 200:
        response_200 = EntriesListKeysAsyncResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[EntriesListKeysAsyncResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/storage#Entries_ListKeysAsync"
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

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/storage#Entries_ListKeysAsync"
)
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


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/storage#Entries_ListKeysAsync"
)
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

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/storage#Entries_ListKeysAsync"
)
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
