from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.creator_store_product import CreatorStoreProduct
from ...types import Response


def _get_kwargs(
    *,
    body: CreatorStoreProduct,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/cloud/v2/creator-store-products",
        "openapi-extensions": {
            "x-roblox-engine-usability": {"apiKeyWithHttpService": True},
            "x-roblox-scopes": [{"name": "creator-store-product:write"}],
            "x-roblox-docs": {
                "category": "Monetization",
                "methodProperties": {"scopes": ["creator-store-product:write"]},
                "resource": {"$ref": "#/components/schemas/CreatorStoreProduct", "name": "CreatorStoreProduct"},
            },
            "x-roblox-stability": "BETA",
            "x-roblox-rate-limits": {
                "perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 30},
                "perOauth2Authorization": {"period": "MINUTE", "maxInPeriod": 30},
            },
        },
        "openapi-id": "Cloud_CreateCreatorStoreProduct",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    *,
    client: AuthenticatedClient,
    body: CreatorStoreProduct,
) -> Response[CreatorStoreProduct]:
    """Create Creator Store Product

     Add a Creator Store product. Only use this method if your product has never
    been distributed on the Creator Store; otherwise, use the `PATCH` method to
    update the product.

    Args:
        body (CreatorStoreProduct): Represents a product in the Creator Store. This resource is
            used to manage
            distribution and pricing of assets on the Creator Store.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreatorStoreProduct]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: CreatorStoreProduct,
) -> CreatorStoreProduct | None:
    """Create Creator Store Product

     Add a Creator Store product. Only use this method if your product has never
    been distributed on the Creator Store; otherwise, use the `PATCH` method to
    update the product.

    Args:
        body (CreatorStoreProduct): Represents a product in the Creator Store. This resource is
            used to manage
            distribution and pricing of assets on the Creator Store.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreatorStoreProduct
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreatorStoreProduct,
) -> Response[CreatorStoreProduct]:
    """Create Creator Store Product

     Add a Creator Store product. Only use this method if your product has never
    been distributed on the Creator Store; otherwise, use the `PATCH` method to
    update the product.

    Args:
        body (CreatorStoreProduct): Represents a product in the Creator Store. This resource is
            used to manage
            distribution and pricing of assets on the Creator Store.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreatorStoreProduct]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreatorStoreProduct,
) -> CreatorStoreProduct | None:
    """Create Creator Store Product

     Add a Creator Store product. Only use this method if your product has never
    been distributed on the Creator Store; otherwise, use the `PATCH` method to
    update the product.

    Args:
        body (CreatorStoreProduct): Represents a product in the Creator Store. This resource is
            used to manage
            distribution and pricing of assets on the Creator Store.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreatorStoreProduct
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
