from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_data_stores_response import ListDataStoresResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    universe_id: str,
    *,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
    show_deleted: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["maxPageSize"] = max_page_size

    params["pageToken"] = page_token

    params["filter"] = filter_

    params["showDeleted"] = show_deleted

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/cloud/v2/universes/{universe_id}/data-stores".format(
            universe_id=quote(str(universe_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ListDataStoresResponse | None:
    if response.status_code == 200:
        response_200 = ListDataStoresResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ListDataStoresResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    universe_id: str,
    *,
    client: AuthenticatedClient,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
    show_deleted: bool | Unset = UNSET,
) -> Response[ListDataStoresResponse]:
    """List Data Stores

     Returns a list of data stores.

    Data stores scheduled for permanent deletion are omitted from the results
    by default (or when `showDeleted` is set to `false`). When this is the
    case, the operation will check up to 512 data stores. If all checked data
    stores are deleted, it will return an empty list with a page token to
    continue iteration.

    Args:
        universe_id (str):
        max_page_size (int | Unset):
        page_token (str | Unset):
        filter_ (str | Unset):
        show_deleted (bool | Unset):  Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListDataStoresResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        max_page_size=max_page_size,
        page_token=page_token,
        filter_=filter_,
        show_deleted=show_deleted,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: str,
    *,
    client: AuthenticatedClient,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
    show_deleted: bool | Unset = UNSET,
) -> ListDataStoresResponse | None:
    """List Data Stores

     Returns a list of data stores.

    Data stores scheduled for permanent deletion are omitted from the results
    by default (or when `showDeleted` is set to `false`). When this is the
    case, the operation will check up to 512 data stores. If all checked data
    stores are deleted, it will return an empty list with a page token to
    continue iteration.

    Args:
        universe_id (str):
        max_page_size (int | Unset):
        page_token (str | Unset):
        filter_ (str | Unset):
        show_deleted (bool | Unset):  Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListDataStoresResponse
    """

    return sync_detailed(
        universe_id=universe_id,
        client=client,
        max_page_size=max_page_size,
        page_token=page_token,
        filter_=filter_,
        show_deleted=show_deleted,
    ).parsed


async def asyncio_detailed(
    universe_id: str,
    *,
    client: AuthenticatedClient,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
    show_deleted: bool | Unset = UNSET,
) -> Response[ListDataStoresResponse]:
    """List Data Stores

     Returns a list of data stores.

    Data stores scheduled for permanent deletion are omitted from the results
    by default (or when `showDeleted` is set to `false`). When this is the
    case, the operation will check up to 512 data stores. If all checked data
    stores are deleted, it will return an empty list with a page token to
    continue iteration.

    Args:
        universe_id (str):
        max_page_size (int | Unset):
        page_token (str | Unset):
        filter_ (str | Unset):
        show_deleted (bool | Unset):  Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListDataStoresResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        max_page_size=max_page_size,
        page_token=page_token,
        filter_=filter_,
        show_deleted=show_deleted,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: str,
    *,
    client: AuthenticatedClient,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
    show_deleted: bool | Unset = UNSET,
) -> ListDataStoresResponse | None:
    """List Data Stores

     Returns a list of data stores.

    Data stores scheduled for permanent deletion are omitted from the results
    by default (or when `showDeleted` is set to `false`). When this is the
    case, the operation will check up to 512 data stores. If all checked data
    stores are deleted, it will return an empty list with a page token to
    continue iteration.

    Args:
        universe_id (str):
        max_page_size (int | Unset):
        page_token (str | Unset):
        filter_ (str | Unset):
        show_deleted (bool | Unset):  Example: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListDataStoresResponse
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            client=client,
            max_page_size=max_page_size,
            page_token=page_token,
            filter_=filter_,
            show_deleted=show_deleted,
        )
    ).parsed
