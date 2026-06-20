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

from ...models.entry import Entry
from ...models.update_entry_request import UpdateEntryRequest


def _get_kwargs(
    universe_id: str,
    ordered_data_store: str,
    scope: str,
    entry: str,
    *,
    body: UpdateEntryRequest,
    allow_missing: bool | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["allow_missing"] = allow_missing

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/ordered-data-stores/v1/universes/{universe_id}/orderedDataStores/{ordered_data_store}/scopes/{scope}/entries/{entry}".format(
            universe_id=quote(str(universe_id), safe=""),
            ordered_data_store=quote(str(ordered_data_store), safe=""),
            scope=quote(str(scope), safe=""),
            entry=quote(str(entry), safe=""),
        ),
        "params": params,
        "extensions": {
            "openapi-extensions": {
                "x-roblox-cloud-api-operation-name": "Update",
                "x-roblox-stability": "BETA",
                "x-roblox-scopes": [{"name": "universe.ordered-data-store.scope.entry:write"}],
                "x-roblox-cloud-api-operation-code-samples": [
                    {
                        "language": "curl",
                        "script": "curl --location --request PATCH 'https://apis.roblox.com/ordered-data-stores/v1/universes/<universeId>/orderedDataStores/<orderedDataStore>/scopes/<scope>/entries/<entry>' \\\n--header 'x-api-key: <insert-api-key>' \\\n--header 'Content-Type: application/json' \\\n--data '{ \n    \"value\": <long> \n}'\n",
                    }
                ],
                "x-roblox-rate-limits": {
                    "description": "See [Throttling](/cloud/guides/data-stores/throttling.md).",
                    "perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 500},
                },
                "x-roblox-recommended-alternatives": [
                    {
                        "url": "https://apis.roblox.com/cloud/v2/universes/{universe_id}/ordered-data-stores/{ordered_data_store_id}/scopes/{scope_id}/entries/{entry_id}",
                        "httpMethod": "PATCH",
                        "documentationUrl": "https://create.roblox.com/docs/cloud/reference/features/storage#Cloud_UpdateOrderedDataStoreEntry",
                    }
                ],
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            },
            "openapi-id": "OrderedDataStores_UpdateEntry",
        },
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Any | Entry | None:
    if response.status_code == 200:
        response_200 = Entry.from_dict(response.json())

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

    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409

    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[Any | Entry]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/storage#OrderedDataStores_UpdateEntry"
)
def sync_detailed(
    universe_id: str,
    ordered_data_store: str,
    scope: str,
    entry: str,
    *,
    client: AuthenticatedClient,
    body: UpdateEntryRequest,
    allow_missing: bool | Unset = UNSET,
) -> Response[Any | Entry]:
    """Updates an entry value and returns the updated entry.

    Args:
        universe_id (str):
        ordered_data_store (str):
        scope (str):
        entry (str):
        allow_missing (bool | Unset):
        body (UpdateEntryRequest): Updates the entry provided with a new value.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Entry]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        ordered_data_store=ordered_data_store,
        scope=scope,
        entry=entry,
        body=body,
        allow_missing=allow_missing,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/storage#OrderedDataStores_UpdateEntry"
)
def sync(
    universe_id: str,
    ordered_data_store: str,
    scope: str,
    entry: str,
    *,
    client: AuthenticatedClient,
    body: UpdateEntryRequest,
    allow_missing: bool | Unset = UNSET,
) -> Any | Entry | None:
    """Updates an entry value and returns the updated entry.

    Args:
        universe_id (str):
        ordered_data_store (str):
        scope (str):
        entry (str):
        allow_missing (bool | Unset):
        body (UpdateEntryRequest): Updates the entry provided with a new value.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Entry
    """

    return sync_detailed(
        universe_id=universe_id,
        ordered_data_store=ordered_data_store,
        scope=scope,
        entry=entry,
        client=client,
        body=body,
        allow_missing=allow_missing,
    ).parsed


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/storage#OrderedDataStores_UpdateEntry"
)
async def asyncio_detailed(
    universe_id: str,
    ordered_data_store: str,
    scope: str,
    entry: str,
    *,
    client: AuthenticatedClient,
    body: UpdateEntryRequest,
    allow_missing: bool | Unset = UNSET,
) -> Response[Any | Entry]:
    """Updates an entry value and returns the updated entry.

    Args:
        universe_id (str):
        ordered_data_store (str):
        scope (str):
        entry (str):
        allow_missing (bool | Unset):
        body (UpdateEntryRequest): Updates the entry provided with a new value.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Entry]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        ordered_data_store=ordered_data_store,
        scope=scope,
        entry=entry,
        body=body,
        allow_missing=allow_missing,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/storage#OrderedDataStores_UpdateEntry"
)
async def asyncio(
    universe_id: str,
    ordered_data_store: str,
    scope: str,
    entry: str,
    *,
    client: AuthenticatedClient,
    body: UpdateEntryRequest,
    allow_missing: bool | Unset = UNSET,
) -> Any | Entry | None:
    """Updates an entry value and returns the updated entry.

    Args:
        universe_id (str):
        ordered_data_store (str):
        scope (str):
        entry (str):
        allow_missing (bool | Unset):
        body (UpdateEntryRequest): Updates the entry provided with a new value.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Entry
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            ordered_data_store=ordered_data_store,
            scope=scope,
            entry=entry,
            client=client,
            body=body,
            allow_missing=allow_missing,
        )
    ).parsed
