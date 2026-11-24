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
{'x-roblox-stability': 'EXPERIMENTAL', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'MINUTE', 'maxInPeriod': 1000000}}, 'x-roblox-scopes': [{'name': 'memory-store.hash-map:read', 'targetResourceSpecifier': 'universes', 'firstPartyOAuthOnly': True}], 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.ums_ums_service_models_open_cloud_open_cloud_batch_get_hash_map_items_request import (
    UmsUmsServiceModelsOpenCloudOpenCloudBatchGetHashMapItemsRequest,
)
from ...models.ums_ums_service_models_open_cloud_open_cloud_batch_get_hash_map_items_response import (
    UmsUmsServiceModelsOpenCloudOpenCloudBatchGetHashMapItemsResponse,
)
from ...types import Unset


def _get_kwargs(
    universe: int,
    hash_map: str,
    *,
    body: UmsUmsServiceModelsOpenCloudOpenCloudBatchGetHashMapItemsRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/cloud/v2/universes/{universe}/memory-store/hash-maps/{hash_map}/items:batchGet".format(
            universe=quote(str(universe), safe=""),
            hash_map=quote(str(hash_map), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> UmsUmsServiceModelsOpenCloudOpenCloudBatchGetHashMapItemsResponse | None:
    if response.status_code == 200:
        response_200 = UmsUmsServiceModelsOpenCloudOpenCloudBatchGetHashMapItemsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[UmsUmsServiceModelsOpenCloudOpenCloudBatchGetHashMapItemsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    universe: int,
    hash_map: str,
    *,
    client: AuthenticatedClient,
    body: UmsUmsServiceModelsOpenCloudOpenCloudBatchGetHashMapItemsRequest | Unset = UNSET,
) -> Response[UmsUmsServiceModelsOpenCloudOpenCloudBatchGetHashMapItemsResponse]:
    """Batch Get Memory Store Hash Map Items

     Retrieves the items for the provided keys. Keys that are not found are omitted from the response.

    Args:
        universe (int):
        hash_map (str):
        body (UmsUmsServiceModelsOpenCloudOpenCloudBatchGetHashMapItemsRequest | Unset): Request
            to retrieve multiple hash map items by key.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UmsUmsServiceModelsOpenCloudOpenCloudBatchGetHashMapItemsResponse]
    """

    kwargs = _get_kwargs(
        universe=universe,
        hash_map=hash_map,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe: int,
    hash_map: str,
    *,
    client: AuthenticatedClient,
    body: UmsUmsServiceModelsOpenCloudOpenCloudBatchGetHashMapItemsRequest | Unset = UNSET,
) -> UmsUmsServiceModelsOpenCloudOpenCloudBatchGetHashMapItemsResponse | None:
    """Batch Get Memory Store Hash Map Items

     Retrieves the items for the provided keys. Keys that are not found are omitted from the response.

    Args:
        universe (int):
        hash_map (str):
        body (UmsUmsServiceModelsOpenCloudOpenCloudBatchGetHashMapItemsRequest | Unset): Request
            to retrieve multiple hash map items by key.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UmsUmsServiceModelsOpenCloudOpenCloudBatchGetHashMapItemsResponse
    """

    return sync_detailed(
        universe=universe,
        hash_map=hash_map,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    universe: int,
    hash_map: str,
    *,
    client: AuthenticatedClient,
    body: UmsUmsServiceModelsOpenCloudOpenCloudBatchGetHashMapItemsRequest | Unset = UNSET,
) -> Response[UmsUmsServiceModelsOpenCloudOpenCloudBatchGetHashMapItemsResponse]:
    """Batch Get Memory Store Hash Map Items

     Retrieves the items for the provided keys. Keys that are not found are omitted from the response.

    Args:
        universe (int):
        hash_map (str):
        body (UmsUmsServiceModelsOpenCloudOpenCloudBatchGetHashMapItemsRequest | Unset): Request
            to retrieve multiple hash map items by key.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UmsUmsServiceModelsOpenCloudOpenCloudBatchGetHashMapItemsResponse]
    """

    kwargs = _get_kwargs(
        universe=universe,
        hash_map=hash_map,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe: int,
    hash_map: str,
    *,
    client: AuthenticatedClient,
    body: UmsUmsServiceModelsOpenCloudOpenCloudBatchGetHashMapItemsRequest | Unset = UNSET,
) -> UmsUmsServiceModelsOpenCloudOpenCloudBatchGetHashMapItemsResponse | None:
    """Batch Get Memory Store Hash Map Items

     Retrieves the items for the provided keys. Keys that are not found are omitted from the response.

    Args:
        universe (int):
        hash_map (str):
        body (UmsUmsServiceModelsOpenCloudOpenCloudBatchGetHashMapItemsRequest | Unset): Request
            to retrieve multiple hash map items by key.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UmsUmsServiceModelsOpenCloudOpenCloudBatchGetHashMapItemsResponse
    """

    return (
        await asyncio_detailed(
            universe=universe,
            hash_map=hash_map,
            client=client,
            body=body,
        )
    ).parsed
