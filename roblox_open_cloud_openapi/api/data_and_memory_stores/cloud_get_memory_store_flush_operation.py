from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cloud_get_memory_store_flush_operation_scope import CloudGetMemoryStoreFlushOperationScope
from ...models.ocv2_operations_operation import OCV2OperationsOperation
from ...types import UNSET, Response, Unset


def _get_kwargs(
    universe_id: str,
    operation_id: str,
    *,
    scope: CloudGetMemoryStoreFlushOperationScope | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_scope: str | Unset = UNSET
    if not isinstance(scope, Unset):
        json_scope = scope.value

    params["scope"] = json_scope

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/cloud/v2/universes/{universe_id}/memory-store/operations/{operation_id}".format(
            universe_id=quote(str(universe_id), safe=""),
            operation_id=quote(str(operation_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> OCV2OperationsOperation | None:
    if response.status_code == 200:
        response_200 = OCV2OperationsOperation.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[OCV2OperationsOperation]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    universe_id: str,
    operation_id: str,
    *,
    client: AuthenticatedClient,
    scope: CloudGetMemoryStoreFlushOperationScope | Unset = UNSET,
) -> Response[OCV2OperationsOperation]:
    """Get Memory Store Flush Operation

     Retrieves the status of the operation to [flush the memory stores of a
    universe](https://create.roblox.com/docs/cloud/reference/features/memory-
    stores#Cloud_FlushMemoryStore).

    Args:
        universe_id (str):
        operation_id (str):
        scope (CloudGetMemoryStoreFlushOperationScope | Unset):  Example: LIVE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OCV2OperationsOperation]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        operation_id=operation_id,
        scope=scope,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: str,
    operation_id: str,
    *,
    client: AuthenticatedClient,
    scope: CloudGetMemoryStoreFlushOperationScope | Unset = UNSET,
) -> OCV2OperationsOperation | None:
    """Get Memory Store Flush Operation

     Retrieves the status of the operation to [flush the memory stores of a
    universe](https://create.roblox.com/docs/cloud/reference/features/memory-
    stores#Cloud_FlushMemoryStore).

    Args:
        universe_id (str):
        operation_id (str):
        scope (CloudGetMemoryStoreFlushOperationScope | Unset):  Example: LIVE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OCV2OperationsOperation
    """

    return sync_detailed(
        universe_id=universe_id,
        operation_id=operation_id,
        client=client,
        scope=scope,
    ).parsed


async def asyncio_detailed(
    universe_id: str,
    operation_id: str,
    *,
    client: AuthenticatedClient,
    scope: CloudGetMemoryStoreFlushOperationScope | Unset = UNSET,
) -> Response[OCV2OperationsOperation]:
    """Get Memory Store Flush Operation

     Retrieves the status of the operation to [flush the memory stores of a
    universe](https://create.roblox.com/docs/cloud/reference/features/memory-
    stores#Cloud_FlushMemoryStore).

    Args:
        universe_id (str):
        operation_id (str):
        scope (CloudGetMemoryStoreFlushOperationScope | Unset):  Example: LIVE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OCV2OperationsOperation]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        operation_id=operation_id,
        scope=scope,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: str,
    operation_id: str,
    *,
    client: AuthenticatedClient,
    scope: CloudGetMemoryStoreFlushOperationScope | Unset = UNSET,
) -> OCV2OperationsOperation | None:
    """Get Memory Store Flush Operation

     Retrieves the status of the operation to [flush the memory stores of a
    universe](https://create.roblox.com/docs/cloud/reference/features/memory-
    stores#Cloud_FlushMemoryStore).

    Args:
        universe_id (str):
        operation_id (str):
        scope (CloudGetMemoryStoreFlushOperationScope | Unset):  Example: LIVE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OCV2OperationsOperation
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            operation_id=operation_id,
            client=client,
            scope=scope,
        )
    ).parsed
