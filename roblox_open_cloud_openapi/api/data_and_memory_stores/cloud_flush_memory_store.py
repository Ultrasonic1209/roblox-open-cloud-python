from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cloud_flush_memory_store_scope import CloudFlushMemoryStoreScope
from ...models.operation import Operation
from ...types import UNSET, Response, Unset


def _get_kwargs(
    universe_id: str,
    *,
    scope: CloudFlushMemoryStoreScope | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_scope: str | Unset = UNSET
    if not isinstance(scope, Unset):
        json_scope = scope.value

    params["scope"] = json_scope

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/cloud/v2/universes/{universe_id}/memory-store:flush".format(
            universe_id=quote(str(universe_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Operation | None:
    if response.status_code == 200:
        response_200 = Operation.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Operation]:
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
    scope: CloudFlushMemoryStoreScope | Unset = UNSET,
) -> Response[Operation]:
    """Flush Memory Store

     Asynchronously flush all data structures in the universe.

    Args:
        universe_id (str):
        scope (CloudFlushMemoryStoreScope | Unset):  Example: LIVE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Operation]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        scope=scope,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: str,
    *,
    client: AuthenticatedClient,
    scope: CloudFlushMemoryStoreScope | Unset = UNSET,
) -> Operation | None:
    """Flush Memory Store

     Asynchronously flush all data structures in the universe.

    Args:
        universe_id (str):
        scope (CloudFlushMemoryStoreScope | Unset):  Example: LIVE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Operation
    """

    return sync_detailed(
        universe_id=universe_id,
        client=client,
        scope=scope,
    ).parsed


async def asyncio_detailed(
    universe_id: str,
    *,
    client: AuthenticatedClient,
    scope: CloudFlushMemoryStoreScope | Unset = UNSET,
) -> Response[Operation]:
    """Flush Memory Store

     Asynchronously flush all data structures in the universe.

    Args:
        universe_id (str):
        scope (CloudFlushMemoryStoreScope | Unset):  Example: LIVE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Operation]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        scope=scope,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: str,
    *,
    client: AuthenticatedClient,
    scope: CloudFlushMemoryStoreScope | Unset = UNSET,
) -> Operation | None:
    """Flush Memory Store

     Asynchronously flush all data structures in the universe.

    Args:
        universe_id (str):
        scope (CloudFlushMemoryStoreScope | Unset):  Example: LIVE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Operation
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            client=client,
            scope=scope,
        )
    ).parsed
