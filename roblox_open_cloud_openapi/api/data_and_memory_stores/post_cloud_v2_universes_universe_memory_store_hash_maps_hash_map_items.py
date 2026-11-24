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
{'x-roblox-stability': 'EXPERIMENTAL', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'MINUTE', 'maxInPeriod': 1000000}}, 'x-roblox-scopes': [{'name': 'memory-store.hash-map:write', 'targetResourceSpecifier': 'universes', 'firstPartyOAuthOnly': True}], 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.ums_ums_service_models_open_cloud_open_cloud_hash_map_item import (
    UmsUmsServiceModelsOpenCloudOpenCloudHashMapItem,
)
from ...types import Unset


def _get_kwargs(
    universe: int,
    hash_map: str,
    *,
    body: UmsUmsServiceModelsOpenCloudOpenCloudHashMapItem | Unset = UNSET,
    id: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["id"] = id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/cloud/v2/universes/{universe}/memory-store/hash-maps/{hash_map}/items".format(
            universe=quote(str(universe), safe=""),
            hash_map=quote(str(hash_map), safe=""),
        ),
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> UmsUmsServiceModelsOpenCloudOpenCloudHashMapItem | None:
    if response.status_code == 200:
        response_200 = UmsUmsServiceModelsOpenCloudOpenCloudHashMapItem.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[UmsUmsServiceModelsOpenCloudOpenCloudHashMapItem]:
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
    body: UmsUmsServiceModelsOpenCloudOpenCloudHashMapItem | Unset = UNSET,
    id: str,
) -> Response[UmsUmsServiceModelsOpenCloudOpenCloudHashMapItem]:
    """Create Memory Store Hash Map Item

     Creates the specified map item if it doesn't exist.

    Args:
        universe (int):
        hash_map (str):
        id (str):
        body (UmsUmsServiceModelsOpenCloudOpenCloudHashMapItem | Unset): Represents a sorted map
            item name.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UmsUmsServiceModelsOpenCloudOpenCloudHashMapItem]
    """

    kwargs = _get_kwargs(
        universe=universe,
        hash_map=hash_map,
        body=body,
        id=id,
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
    body: UmsUmsServiceModelsOpenCloudOpenCloudHashMapItem | Unset = UNSET,
    id: str,
) -> UmsUmsServiceModelsOpenCloudOpenCloudHashMapItem | None:
    """Create Memory Store Hash Map Item

     Creates the specified map item if it doesn't exist.

    Args:
        universe (int):
        hash_map (str):
        id (str):
        body (UmsUmsServiceModelsOpenCloudOpenCloudHashMapItem | Unset): Represents a sorted map
            item name.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UmsUmsServiceModelsOpenCloudOpenCloudHashMapItem
    """

    return sync_detailed(
        universe=universe,
        hash_map=hash_map,
        client=client,
        body=body,
        id=id,
    ).parsed


async def asyncio_detailed(
    universe: int,
    hash_map: str,
    *,
    client: AuthenticatedClient,
    body: UmsUmsServiceModelsOpenCloudOpenCloudHashMapItem | Unset = UNSET,
    id: str,
) -> Response[UmsUmsServiceModelsOpenCloudOpenCloudHashMapItem]:
    """Create Memory Store Hash Map Item

     Creates the specified map item if it doesn't exist.

    Args:
        universe (int):
        hash_map (str):
        id (str):
        body (UmsUmsServiceModelsOpenCloudOpenCloudHashMapItem | Unset): Represents a sorted map
            item name.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UmsUmsServiceModelsOpenCloudOpenCloudHashMapItem]
    """

    kwargs = _get_kwargs(
        universe=universe,
        hash_map=hash_map,
        body=body,
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe: int,
    hash_map: str,
    *,
    client: AuthenticatedClient,
    body: UmsUmsServiceModelsOpenCloudOpenCloudHashMapItem | Unset = UNSET,
    id: str,
) -> UmsUmsServiceModelsOpenCloudOpenCloudHashMapItem | None:
    """Create Memory Store Hash Map Item

     Creates the specified map item if it doesn't exist.

    Args:
        universe (int):
        hash_map (str):
        id (str):
        body (UmsUmsServiceModelsOpenCloudOpenCloudHashMapItem | Unset): Represents a sorted map
            item name.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UmsUmsServiceModelsOpenCloudOpenCloudHashMapItem
    """

    return (
        await asyncio_detailed(
            universe=universe,
            hash_map=hash_map,
            client=client,
            body=body,
            id=id,
        )
    ).parsed
