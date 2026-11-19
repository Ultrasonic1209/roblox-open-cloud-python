from http import HTTPStatus
from typing import TYPE_CHECKING, Any
from urllib.parse import quote

if TYPE_CHECKING:
    import httpx2 as httpx
else:
    try:
        import httpx2 as httpx
    except ModuleNotFoundError:
        try:
            import httpx
        except ModuleNotFoundError:
            raise RuntimeError(
                "This module requires the httpx2 package to be installed.\n"
                "You can install it with:\n"
                "    $ pip install httpx2\n"
            ) from None


from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response

"""
{'x-roblox-stability': 'BETA', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'MINUTE', 'maxInPeriod': 1000000}}, 'x-roblox-scopes': [{'name': 'memory-store:get', 'targetResourceSpecifier': 'universes', 'firstPartyOAuthOnly': True}], 'x-roblox-engine-usability': {'apiKeyWithHttpService': True}}
"""


from ...models.cloud_get_memory_store_flush_operation_scope import CloudGetMemoryStoreFlushOperationScope
from ...models.memory_store_flush_operation import MemoryStoreFlushOperation
from ...types import Unset


def _get_kwargs(
    universe_id: int,
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
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MemoryStoreFlushOperation | None:
    if response.status_code == 200:
        response_200 = MemoryStoreFlushOperation.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[MemoryStoreFlushOperation]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    universe_id: int,
    operation_id: str,
    *,
    client: AuthenticatedClient,
    scope: CloudGetMemoryStoreFlushOperationScope | Unset = UNSET,
) -> Response[MemoryStoreFlushOperation]:
    """Get Memory Store Flush Operation

     Retrieves the status of the operation to [flush the memory stores of a
    universe](https://create.roblox.com/docs/cloud/reference/features/storage#Cloud_FlushMemoryStore).

    Args:
        universe_id (int):
        operation_id (str):
        scope (CloudGetMemoryStoreFlushOperationScope | Unset):  Example: LIVE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MemoryStoreFlushOperation]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        operation_id=operation_id,
        scope=scope,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: int,
    operation_id: str,
    *,
    client: AuthenticatedClient,
    scope: CloudGetMemoryStoreFlushOperationScope | Unset = UNSET,
) -> MemoryStoreFlushOperation | None:
    """Get Memory Store Flush Operation

     Retrieves the status of the operation to [flush the memory stores of a
    universe](https://create.roblox.com/docs/cloud/reference/features/storage#Cloud_FlushMemoryStore).

    Args:
        universe_id (int):
        operation_id (str):
        scope (CloudGetMemoryStoreFlushOperationScope | Unset):  Example: LIVE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MemoryStoreFlushOperation
    """

    return sync_detailed(
        universe_id=universe_id,
        operation_id=operation_id,
        client=client,
        scope=scope,
    ).parsed


async def asyncio_detailed(
    universe_id: int,
    operation_id: str,
    *,
    client: AuthenticatedClient,
    scope: CloudGetMemoryStoreFlushOperationScope | Unset = UNSET,
) -> Response[MemoryStoreFlushOperation]:
    """Get Memory Store Flush Operation

     Retrieves the status of the operation to [flush the memory stores of a
    universe](https://create.roblox.com/docs/cloud/reference/features/storage#Cloud_FlushMemoryStore).

    Args:
        universe_id (int):
        operation_id (str):
        scope (CloudGetMemoryStoreFlushOperationScope | Unset):  Example: LIVE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MemoryStoreFlushOperation]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        operation_id=operation_id,
        scope=scope,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: int,
    operation_id: str,
    *,
    client: AuthenticatedClient,
    scope: CloudGetMemoryStoreFlushOperationScope | Unset = UNSET,
) -> MemoryStoreFlushOperation | None:
    """Get Memory Store Flush Operation

     Retrieves the status of the operation to [flush the memory stores of a
    universe](https://create.roblox.com/docs/cloud/reference/features/storage#Cloud_FlushMemoryStore).

    Args:
        universe_id (int):
        operation_id (str):
        scope (CloudGetMemoryStoreFlushOperationScope | Unset):  Example: LIVE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MemoryStoreFlushOperation
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            operation_id=operation_id,
            client=client,
            scope=scope,
        )
    ).parsed
