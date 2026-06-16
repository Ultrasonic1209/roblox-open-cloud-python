from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_ordered_data_store_entries_response import ListOrderedDataStoreEntriesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    universe_id: str,
    ordered_data_store_id: str,
    scope_id: str,
    *,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    order_by: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["maxPageSize"] = max_page_size

    params["pageToken"] = page_token

    params["orderBy"] = order_by

    params["filter"] = filter_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/cloud/v2/universes/{universe_id}/ordered-data-stores/{ordered_data_store_id}/scopes/{scope_id}/entries".format(
            universe_id=quote(str(universe_id), safe=""),
            ordered_data_store_id=quote(str(ordered_data_store_id), safe=""),
            scope_id=quote(str(scope_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListOrderedDataStoreEntriesResponse | None:
    if response.status_code == 200:
        response_200 = ListOrderedDataStoreEntriesResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ListOrderedDataStoreEntriesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    universe_id: str,
    ordered_data_store_id: str,
    scope_id: str,
    *,
    client: AuthenticatedClient,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    order_by: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
) -> Response[ListOrderedDataStoreEntriesResponse]:
    """List Ordered Data Store Entries

     Returns a list of entries from an ordered data store.

    Args:
        universe_id (str):
        ordered_data_store_id (str):
        scope_id (str):
        max_page_size (int | Unset):
        page_token (str | Unset):
        order_by (str | Unset):
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListOrderedDataStoreEntriesResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        ordered_data_store_id=ordered_data_store_id,
        scope_id=scope_id,
        max_page_size=max_page_size,
        page_token=page_token,
        order_by=order_by,
        filter_=filter_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: str,
    ordered_data_store_id: str,
    scope_id: str,
    *,
    client: AuthenticatedClient,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    order_by: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
) -> ListOrderedDataStoreEntriesResponse | None:
    """List Ordered Data Store Entries

     Returns a list of entries from an ordered data store.

    Args:
        universe_id (str):
        ordered_data_store_id (str):
        scope_id (str):
        max_page_size (int | Unset):
        page_token (str | Unset):
        order_by (str | Unset):
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListOrderedDataStoreEntriesResponse
    """

    return sync_detailed(
        universe_id=universe_id,
        ordered_data_store_id=ordered_data_store_id,
        scope_id=scope_id,
        client=client,
        max_page_size=max_page_size,
        page_token=page_token,
        order_by=order_by,
        filter_=filter_,
    ).parsed


async def asyncio_detailed(
    universe_id: str,
    ordered_data_store_id: str,
    scope_id: str,
    *,
    client: AuthenticatedClient,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    order_by: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
) -> Response[ListOrderedDataStoreEntriesResponse]:
    """List Ordered Data Store Entries

     Returns a list of entries from an ordered data store.

    Args:
        universe_id (str):
        ordered_data_store_id (str):
        scope_id (str):
        max_page_size (int | Unset):
        page_token (str | Unset):
        order_by (str | Unset):
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListOrderedDataStoreEntriesResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        ordered_data_store_id=ordered_data_store_id,
        scope_id=scope_id,
        max_page_size=max_page_size,
        page_token=page_token,
        order_by=order_by,
        filter_=filter_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: str,
    ordered_data_store_id: str,
    scope_id: str,
    *,
    client: AuthenticatedClient,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    order_by: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
) -> ListOrderedDataStoreEntriesResponse | None:
    """List Ordered Data Store Entries

     Returns a list of entries from an ordered data store.

    Args:
        universe_id (str):
        ordered_data_store_id (str):
        scope_id (str):
        max_page_size (int | Unset):
        page_token (str | Unset):
        order_by (str | Unset):
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListOrderedDataStoreEntriesResponse
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            ordered_data_store_id=ordered_data_store_id,
            scope_id=scope_id,
            client=client,
            max_page_size=max_page_size,
            page_token=page_token,
            order_by=order_by,
            filter_=filter_,
        )
    ).parsed
