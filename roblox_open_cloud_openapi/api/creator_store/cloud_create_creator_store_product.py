from http import HTTPStatus
from typing import TYPE_CHECKING, Any

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


from ...client import AuthenticatedClient, Client
from ...types import Response

"""
{'x-roblox-stability': 'BETA', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'MINUTE', 'maxInPeriod': 30}, 'perOauth2Authorization': {'period': 'MINUTE', 'maxInPeriod': 30}}, 'x-roblox-scopes': [{'name': 'creator-store-product:write'}], 'x-roblox-engine-usability': {'apiKeyWithHttpService': True}}
"""


from ...models.google_rpc_status import GoogleRpcStatus
from ...models.marketplace_fiat_service_creator_store_product import MarketplaceFiatServiceCreatorStoreProduct


def _get_kwargs(
    *,
    body: MarketplaceFiatServiceCreatorStoreProduct,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/cloud/v2/creator-store-products",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GoogleRpcStatus | MarketplaceFiatServiceCreatorStoreProduct:
    if response.status_code == 200:
        response_200 = MarketplaceFiatServiceCreatorStoreProduct.from_dict(response.json())

        return response_200

    response_default = GoogleRpcStatus.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GoogleRpcStatus | MarketplaceFiatServiceCreatorStoreProduct]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: MarketplaceFiatServiceCreatorStoreProduct,
) -> Response[GoogleRpcStatus | MarketplaceFiatServiceCreatorStoreProduct]:
    """Create Creator Store Product

     Add a Creator Store product. Only use this method if your product has never been distributed on the
    Creator Store; otherwise, use the `PATCH` method to update the product.

    Args:
        body (MarketplaceFiatServiceCreatorStoreProduct): Represents a product in the Creator
            Store. This resource is used to manage
            distribution and pricing of assets on the Creator Store.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GoogleRpcStatus | MarketplaceFiatServiceCreatorStoreProduct]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: MarketplaceFiatServiceCreatorStoreProduct,
) -> GoogleRpcStatus | MarketplaceFiatServiceCreatorStoreProduct | None:
    """Create Creator Store Product

     Add a Creator Store product. Only use this method if your product has never been distributed on the
    Creator Store; otherwise, use the `PATCH` method to update the product.

    Args:
        body (MarketplaceFiatServiceCreatorStoreProduct): Represents a product in the Creator
            Store. This resource is used to manage
            distribution and pricing of assets on the Creator Store.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GoogleRpcStatus | MarketplaceFiatServiceCreatorStoreProduct
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: MarketplaceFiatServiceCreatorStoreProduct,
) -> Response[GoogleRpcStatus | MarketplaceFiatServiceCreatorStoreProduct]:
    """Create Creator Store Product

     Add a Creator Store product. Only use this method if your product has never been distributed on the
    Creator Store; otherwise, use the `PATCH` method to update the product.

    Args:
        body (MarketplaceFiatServiceCreatorStoreProduct): Represents a product in the Creator
            Store. This resource is used to manage
            distribution and pricing of assets on the Creator Store.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GoogleRpcStatus | MarketplaceFiatServiceCreatorStoreProduct]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: MarketplaceFiatServiceCreatorStoreProduct,
) -> GoogleRpcStatus | MarketplaceFiatServiceCreatorStoreProduct | None:
    """Create Creator Store Product

     Add a Creator Store product. Only use this method if your product has never been distributed on the
    Creator Store; otherwise, use the `PATCH` method to update the product.

    Args:
        body (MarketplaceFiatServiceCreatorStoreProduct): Represents a product in the Creator
            Store. This resource is used to manage
            distribution and pricing of assets on the Creator Store.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GoogleRpcStatus | MarketplaceFiatServiceCreatorStoreProduct
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
