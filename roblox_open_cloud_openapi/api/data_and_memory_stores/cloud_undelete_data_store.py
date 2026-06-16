from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.data_store import DataStore
from ...models.undelete_data_store_request import UndeleteDataStoreRequest
from ...types import Response


def _get_kwargs(
    universe_id: str,
    data_store_id: str,
    *,
    body: UndeleteDataStoreRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/cloud/v2/universes/{universe_id}/data-stores/{data_store_id}:undelete".format(
            universe_id=quote(str(universe_id), safe=""),
            data_store_id=quote(str(data_store_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DataStore | None:
    if response.status_code == 200:
        response_200 = DataStore.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DataStore]:
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
    body: UndeleteDataStoreRequest,
) -> Response[DataStore]:
    """Undelete Data Store

     Restore the data store

    Args:
        universe_id (str):
        data_store_id (str):
        body (UndeleteDataStoreRequest): Restore the data store

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataStore]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        data_store_id=data_store_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: str,
    data_store_id: str,
    *,
    client: AuthenticatedClient,
    body: UndeleteDataStoreRequest,
) -> DataStore | None:
    """Undelete Data Store

     Restore the data store

    Args:
        universe_id (str):
        data_store_id (str):
        body (UndeleteDataStoreRequest): Restore the data store

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
        body=body,
    ).parsed


async def asyncio_detailed(
    universe_id: str,
    data_store_id: str,
    *,
    client: AuthenticatedClient,
    body: UndeleteDataStoreRequest,
) -> Response[DataStore]:
    """Undelete Data Store

     Restore the data store

    Args:
        universe_id (str):
        data_store_id (str):
        body (UndeleteDataStoreRequest): Restore the data store

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DataStore]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        data_store_id=data_store_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: str,
    data_store_id: str,
    *,
    client: AuthenticatedClient,
    body: UndeleteDataStoreRequest,
) -> DataStore | None:
    """Undelete Data Store

     Restore the data store

    Args:
        universe_id (str):
        data_store_id (str):
        body (UndeleteDataStoreRequest): Restore the data store

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
            body=body,
        )
    ).parsed
