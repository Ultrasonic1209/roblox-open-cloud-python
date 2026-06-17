from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.creator_store_product import CreatorStoreProduct
from ...types import Response


def _get_kwargs(
    creator_store_product_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/cloud/v2/creator-store-products/{creator_store_product_id}".format(
            creator_store_product_id=quote(str(creator_store_product_id), safe=""),
        ),
        "openapi-extensions": {
            "x-roblox-engine-usability": {"apiKeyWithHttpService": True},
            "x-roblox-scopes": [{"name": "creator-store-product:read"}],
            "x-roblox-docs": {
                "category": "Monetization",
                "methodProperties": {"scopes": ["creator-store-product:read"]},
                "resource": {"$ref": "#/components/schemas/CreatorStoreProduct", "name": "CreatorStoreProduct"},
            },
            "x-roblox-stability": "BETA",
            "x-roblox-rate-limits": {
                "perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 30},
                "perOauth2Authorization": {"period": "MINUTE", "maxInPeriod": 30},
            },
        },
        "openapi-id": "Cloud_GetCreatorStoreProduct",
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> CreatorStoreProduct | None:
    if response.status_code == 200:
        response_200 = CreatorStoreProduct.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[CreatorStoreProduct]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    creator_store_product_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[CreatorStoreProduct]:
    """Get Creator Store Product

     Get a Creator Store product.

    Args:
        creator_store_product_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreatorStoreProduct]
    """

    kwargs = _get_kwargs(
        creator_store_product_id=creator_store_product_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    creator_store_product_id: str,
    *,
    client: AuthenticatedClient,
) -> CreatorStoreProduct | None:
    """Get Creator Store Product

     Get a Creator Store product.

    Args:
        creator_store_product_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreatorStoreProduct
    """

    return sync_detailed(
        creator_store_product_id=creator_store_product_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    creator_store_product_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[CreatorStoreProduct]:
    """Get Creator Store Product

     Get a Creator Store product.

    Args:
        creator_store_product_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreatorStoreProduct]
    """

    kwargs = _get_kwargs(
        creator_store_product_id=creator_store_product_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    creator_store_product_id: str,
    *,
    client: AuthenticatedClient,
) -> CreatorStoreProduct | None:
    """Get Creator Store Product

     Get a Creator Store product.

    Args:
        creator_store_product_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreatorStoreProduct
    """

    return (
        await asyncio_detailed(
            creator_store_product_id=creator_store_product_id,
            client=client,
        )
    ).parsed
