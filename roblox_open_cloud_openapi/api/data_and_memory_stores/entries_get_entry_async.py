import sys
from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset

if sys.version_info >= (3, 13):
    from warnings import deprecated
else:
    from typing_extensions import deprecated

from ...models.entries_get_entry_async_response_200 import EntriesGetEntryAsyncResponse200


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
        "method": "get",
        "url": "/datastores/v1/universes/{universe_id}/standard-datastores/datastore/entries/entry".format(
            universe_id=quote(str(universe_id), safe=""),
        ),
        "params": params,
        "extensions": {
            "openapi-extensions": {
                "x-roblox-cloud-api-operation-name": "Get Entry",
                "x-roblox-stability": "BETA",
                "x-roblox-scopes": [{"name": "universe-datastores.objects:read"}],
                "x-roblox-cloud-api-operation": True,
                "x-roblox-lua-equivalent": "GlobalDataStore:GetAsync",
                "x-roblox-cloud-api-operation-code-samples": [
                    {
                        "language": "curl",
                        "script": 'curl --include --location --request GET "https://apis.roblox.com/datastores/v1/universes/3310576216/standard-datastores/datastore/entries/entry" \\\n--header "x-api-key: ${API_KEY}" \\\n--get \\\n-d "datastoreName=Coins" \\\n-d "entryKey=269323"',
                    }
                ],
                "x-roblox-rate-limits": {
                    "description": "See [Throttling](/cloud/guides/data-stores/throttling.md).",
                    "perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 5000},
                },
                "x-roblox-recommended-alternatives": [
                    {
                        "url": "https://apis.roblox.com/cloud/v2/universes/{universe_id}/data-stores/{data_store_id}/entries/{entry_id}",
                        "httpMethod": "GET",
                        "documentationUrl": "https://create.roblox.com/docs/cloud/reference/features/storage#Cloud_GetDataStoreEntry__Using_Universes_DataStores",
                    },
                    {
                        "url": "https://apis.roblox.com/cloud/v2/universes/{universe_id}/data-stores/{data_store_id}/scopes/{scope_id}/entries/{entry_id}",
                        "httpMethod": "GET",
                        "documentationUrl": "https://create.roblox.com/docs/cloud/reference/features/storage#Cloud_GetDataStoreEntry__Using_Universes_DataStores_Scopes",
                    },
                ],
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            },
            "openapi-id": "Entries_GetEntryAsync",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | EntriesGetEntryAsyncResponse200 | None:
    if response.status_code == 200:
        response_200 = EntriesGetEntryAsyncResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | EntriesGetEntryAsyncResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/storage#Entries_GetEntryAsync"
)
def sync_detailed(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    datastore_name: None | str | Unset = UNSET,
    entry_key: None | str | Unset = UNSET,
    scope: None | str | Unset = "global",
) -> Response[Any | EntriesGetEntryAsyncResponse200]:
    r"""Get entry.

     Returns the value and metadata associated with an entry.

    Entries marked deleted with a tombstone version will return 404 Not Found.

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
        scope (None | str | Unset):  Default: 'global'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EntriesGetEntryAsyncResponse200]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        datastore_name=datastore_name,
        entry_key=entry_key,
        scope=scope,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/storage#Entries_GetEntryAsync"
)
def sync(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    datastore_name: None | str | Unset = UNSET,
    entry_key: None | str | Unset = UNSET,
    scope: None | str | Unset = "global",
) -> Any | EntriesGetEntryAsyncResponse200 | None:
    r"""Get entry.

     Returns the value and metadata associated with an entry.

    Entries marked deleted with a tombstone version will return 404 Not Found.

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
        scope (None | str | Unset):  Default: 'global'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EntriesGetEntryAsyncResponse200
    """

    return sync_detailed(
        universe_id=universe_id,
        client=client,
        datastore_name=datastore_name,
        entry_key=entry_key,
        scope=scope,
    ).parsed


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/storage#Entries_GetEntryAsync"
)
async def asyncio_detailed(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    datastore_name: None | str | Unset = UNSET,
    entry_key: None | str | Unset = UNSET,
    scope: None | str | Unset = "global",
) -> Response[Any | EntriesGetEntryAsyncResponse200]:
    r"""Get entry.

     Returns the value and metadata associated with an entry.

    Entries marked deleted with a tombstone version will return 404 Not Found.

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
        scope (None | str | Unset):  Default: 'global'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EntriesGetEntryAsyncResponse200]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        datastore_name=datastore_name,
        entry_key=entry_key,
        scope=scope,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/storage#Entries_GetEntryAsync"
)
async def asyncio(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    datastore_name: None | str | Unset = UNSET,
    entry_key: None | str | Unset = UNSET,
    scope: None | str | Unset = "global",
) -> Any | EntriesGetEntryAsyncResponse200 | None:
    r"""Get entry.

     Returns the value and metadata associated with an entry.

    Entries marked deleted with a tombstone version will return 404 Not Found.

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
        scope (None | str | Unset):  Default: 'global'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EntriesGetEntryAsyncResponse200
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            client=client,
            datastore_name=datastore_name,
            entry_key=entry_key,
            scope=scope,
        )
    ).parsed
