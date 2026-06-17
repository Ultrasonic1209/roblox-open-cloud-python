from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.data_store import DataStore
from ...types import Response


def _get_kwargs(
    universe_id: str,
    data_store_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/cloud/v2/universes/{universe_id}/data-stores/{data_store_id}".format(
            universe_id=quote(str(universe_id), safe=""),
            data_store_id=quote(str(data_store_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> DataStore | None:
    if response.status_code == 200:
        response_200 = DataStore.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[DataStore]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    universe_id: str,
    data_store_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[DataStore]:
    """Delete Data Store

     Schedules the specified data store for permanent deletion.

    This operation assigns the data store an expiry time 30 days in the future,
    at which point permanent deletion begins. To cancel, use the
    `UndeleteDataStore` operation before the data store's expiry time.

    Permanent deletion consists of deleting all of the entries in the data
    store and then the data store resource itself. The data store is no longer
    returned by the `ListDataStores` Open Cloud endpoint or
    `ListDataStoresAsync` Luau API, and you can reuse the data store's name.

    The duration of the permanent deletion process depends on the number of
    entries in the data store. However, you can expect a data store with 1
    million or fewer entries to be permanently deleted within 3 days.

    Data stores scheduled for permanent deletion are returned by the
    `ListDataStores` Open Cloud endpoint when the query parameter `showDeleted`
    is set to `true`. In the return value, each data store will have a
    `DELETED` state and an `expireTime` field.

    Data stores scheduled for permanent deletion are immediately made
    inaccessible, meaning attempts to read or write to their entries will fail.

    Note: Due to caching in the backend service, attempts to read from or write
    to entries in these data stores can continue to succeed for a limited time
    after the deletion:
    * `GetDataStoreEntry`: can succeed for up to 24 hours.
    * All other endpoints: can succeed for several minutes.

    If the data store is already in a `DELETED` state, this operation is a
    no-op, and the data store is returned as-is.

    Args:
        universe_id (str):
        data_store_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataStore]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        data_store_id=data_store_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: str,
    data_store_id: str,
    *,
    client: AuthenticatedClient,
) -> DataStore | None:
    """Delete Data Store

     Schedules the specified data store for permanent deletion.

    This operation assigns the data store an expiry time 30 days in the future,
    at which point permanent deletion begins. To cancel, use the
    `UndeleteDataStore` operation before the data store's expiry time.

    Permanent deletion consists of deleting all of the entries in the data
    store and then the data store resource itself. The data store is no longer
    returned by the `ListDataStores` Open Cloud endpoint or
    `ListDataStoresAsync` Luau API, and you can reuse the data store's name.

    The duration of the permanent deletion process depends on the number of
    entries in the data store. However, you can expect a data store with 1
    million or fewer entries to be permanently deleted within 3 days.

    Data stores scheduled for permanent deletion are returned by the
    `ListDataStores` Open Cloud endpoint when the query parameter `showDeleted`
    is set to `true`. In the return value, each data store will have a
    `DELETED` state and an `expireTime` field.

    Data stores scheduled for permanent deletion are immediately made
    inaccessible, meaning attempts to read or write to their entries will fail.

    Note: Due to caching in the backend service, attempts to read from or write
    to entries in these data stores can continue to succeed for a limited time
    after the deletion:
    * `GetDataStoreEntry`: can succeed for up to 24 hours.
    * All other endpoints: can succeed for several minutes.

    If the data store is already in a `DELETED` state, this operation is a
    no-op, and the data store is returned as-is.

    Args:
        universe_id (str):
        data_store_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataStore
    """

    return sync_detailed(
        universe_id=universe_id,
        data_store_id=data_store_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    universe_id: str,
    data_store_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[DataStore]:
    """Delete Data Store

     Schedules the specified data store for permanent deletion.

    This operation assigns the data store an expiry time 30 days in the future,
    at which point permanent deletion begins. To cancel, use the
    `UndeleteDataStore` operation before the data store's expiry time.

    Permanent deletion consists of deleting all of the entries in the data
    store and then the data store resource itself. The data store is no longer
    returned by the `ListDataStores` Open Cloud endpoint or
    `ListDataStoresAsync` Luau API, and you can reuse the data store's name.

    The duration of the permanent deletion process depends on the number of
    entries in the data store. However, you can expect a data store with 1
    million or fewer entries to be permanently deleted within 3 days.

    Data stores scheduled for permanent deletion are returned by the
    `ListDataStores` Open Cloud endpoint when the query parameter `showDeleted`
    is set to `true`. In the return value, each data store will have a
    `DELETED` state and an `expireTime` field.

    Data stores scheduled for permanent deletion are immediately made
    inaccessible, meaning attempts to read or write to their entries will fail.

    Note: Due to caching in the backend service, attempts to read from or write
    to entries in these data stores can continue to succeed for a limited time
    after the deletion:
    * `GetDataStoreEntry`: can succeed for up to 24 hours.
    * All other endpoints: can succeed for several minutes.

    If the data store is already in a `DELETED` state, this operation is a
    no-op, and the data store is returned as-is.

    Args:
        universe_id (str):
        data_store_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataStore]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        data_store_id=data_store_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: str,
    data_store_id: str,
    *,
    client: AuthenticatedClient,
) -> DataStore | None:
    """Delete Data Store

     Schedules the specified data store for permanent deletion.

    This operation assigns the data store an expiry time 30 days in the future,
    at which point permanent deletion begins. To cancel, use the
    `UndeleteDataStore` operation before the data store's expiry time.

    Permanent deletion consists of deleting all of the entries in the data
    store and then the data store resource itself. The data store is no longer
    returned by the `ListDataStores` Open Cloud endpoint or
    `ListDataStoresAsync` Luau API, and you can reuse the data store's name.

    The duration of the permanent deletion process depends on the number of
    entries in the data store. However, you can expect a data store with 1
    million or fewer entries to be permanently deleted within 3 days.

    Data stores scheduled for permanent deletion are returned by the
    `ListDataStores` Open Cloud endpoint when the query parameter `showDeleted`
    is set to `true`. In the return value, each data store will have a
    `DELETED` state and an `expireTime` field.

    Data stores scheduled for permanent deletion are immediately made
    inaccessible, meaning attempts to read or write to their entries will fail.

    Note: Due to caching in the backend service, attempts to read from or write
    to entries in these data stores can continue to succeed for a limited time
    after the deletion:
    * `GetDataStoreEntry`: can succeed for up to 24 hours.
    * All other endpoints: can succeed for several minutes.

    If the data store is already in a `DELETED` state, this operation is a
    no-op, and the data store is returned as-is.

    Args:
        universe_id (str):
        data_store_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DataStore
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            data_store_id=data_store_id,
            client=client,
        )
    ).parsed
