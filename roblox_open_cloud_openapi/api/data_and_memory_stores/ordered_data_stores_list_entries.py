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

from ...models.list_entries_response import ListEntriesResponse


def _get_kwargs(
    universe_id: str,
    ordered_data_store: str,
    scope: str,
    *,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    order_by: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["max_page_size"] = max_page_size

    params["page_token"] = page_token

    params["order_by"] = order_by

    params["filter"] = filter_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/ordered-data-stores/v1/universes/{universe_id}/orderedDataStores/{ordered_data_store}/scopes/{scope}/entries".format(
            universe_id=quote(str(universe_id), safe=""),
            ordered_data_store=quote(str(ordered_data_store), safe=""),
            scope=quote(str(scope), safe=""),
        ),
        "params": params,
        "extensions": {
            "openapi-extensions": {
                "x-roblox-cloud-api-operation-name": "List",
                "x-roblox-stability": "BETA",
                "x-roblox-scopes": [{"name": "universe.ordered-data-store.scope.entry:read"}],
                "x-roblox-cloud-api-operation-code-samples": [
                    {
                        "language": "curl",
                        "script": "curl --location 'https://apis.roblox.com/ordered-data-stores/v1/universes/<universeId>/orderedDataStores/<orderedDataStore>/scopes/<scope>/entries' \\\n --header 'x-api-key: <insert-api-key>' \n",
                    }
                ],
                "x-roblox-rate-limits": {
                    "description": "See [Throttling](/cloud/guides/data-stores/throttling.md).",
                    "perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 500},
                },
                "x-roblox-recommended-alternatives": [
                    {
                        "url": "https://apis.roblox.com/cloud/v2/universes/{universe_id}/ordered-data-stores/{ordered_data_store_id}/scopes/{scope_id}/entries",
                        "httpMethod": "GET",
                        "documentationUrl": "https://create.roblox.com/docs/cloud/reference/features/storage#Cloud_ListOrderedDataStoreEntries",
                    }
                ],
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            },
            "openapi-id": "OrderedDataStores_ListEntries",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | ListEntriesResponse | None:
    if response.status_code == 200:
        response_200 = ListEntriesResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | ListEntriesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/storage#OrderedDataStores_ListEntries"
)
def sync_detailed(
    universe_id: str,
    ordered_data_store: str,
    scope: str,
    *,
    client: AuthenticatedClient,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    order_by: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
) -> Response[Any | ListEntriesResponse]:
    """Returns a list of entries from an ordered data store.

    Args:
        universe_id (str):
        ordered_data_store (str):
        scope (str):
        max_page_size (int | Unset):
        page_token (str | Unset):
        order_by (str | Unset):
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ListEntriesResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        ordered_data_store=ordered_data_store,
        scope=scope,
        max_page_size=max_page_size,
        page_token=page_token,
        order_by=order_by,
        filter_=filter_,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/storage#OrderedDataStores_ListEntries"
)
def sync(
    universe_id: str,
    ordered_data_store: str,
    scope: str,
    *,
    client: AuthenticatedClient,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    order_by: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
) -> Any | ListEntriesResponse | None:
    """Returns a list of entries from an ordered data store.

    Args:
        universe_id (str):
        ordered_data_store (str):
        scope (str):
        max_page_size (int | Unset):
        page_token (str | Unset):
        order_by (str | Unset):
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ListEntriesResponse
    """

    return sync_detailed(
        universe_id=universe_id,
        ordered_data_store=ordered_data_store,
        scope=scope,
        client=client,
        max_page_size=max_page_size,
        page_token=page_token,
        order_by=order_by,
        filter_=filter_,
    ).parsed


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/storage#OrderedDataStores_ListEntries"
)
async def asyncio_detailed(
    universe_id: str,
    ordered_data_store: str,
    scope: str,
    *,
    client: AuthenticatedClient,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    order_by: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
) -> Response[Any | ListEntriesResponse]:
    """Returns a list of entries from an ordered data store.

    Args:
        universe_id (str):
        ordered_data_store (str):
        scope (str):
        max_page_size (int | Unset):
        page_token (str | Unset):
        order_by (str | Unset):
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ListEntriesResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        ordered_data_store=ordered_data_store,
        scope=scope,
        max_page_size=max_page_size,
        page_token=page_token,
        order_by=order_by,
        filter_=filter_,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/storage#OrderedDataStores_ListEntries"
)
async def asyncio(
    universe_id: str,
    ordered_data_store: str,
    scope: str,
    *,
    client: AuthenticatedClient,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    order_by: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
) -> Any | ListEntriesResponse | None:
    """Returns a list of entries from an ordered data store.

    Args:
        universe_id (str):
        ordered_data_store (str):
        scope (str):
        max_page_size (int | Unset):
        page_token (str | Unset):
        order_by (str | Unset):
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ListEntriesResponse
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            ordered_data_store=ordered_data_store,
            scope=scope,
            client=client,
            max_page_size=max_page_size,
            page_token=page_token,
            order_by=order_by,
            filter_=filter_,
        )
    ).parsed
