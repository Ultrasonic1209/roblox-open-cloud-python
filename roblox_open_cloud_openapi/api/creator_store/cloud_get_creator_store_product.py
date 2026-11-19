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


from ...client import AuthenticatedClient, Client
from ...types import Response

"""
{'x-roblox-stability': 'BETA', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'MINUTE', 'maxInPeriod': 30}, 'perOauth2Authorization': {'period': 'MINUTE', 'maxInPeriod': 30}}, 'x-roblox-scopes': [{'name': 'creator-store-product:read', 'targetResourceSpecifier': ''}], 'x-roblox-engine-usability': {'apiKeyWithHttpService': True}}
"""


from ...models.google_rpc_status import GoogleRpcStatus
from ...models.marketplace_fiat_service_creator_store_product import MarketplaceFiatServiceCreatorStoreProduct


def _get_kwargs(
    creator_store_product_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/cloud/v2/creator-store-products/{creator_store_product_id}".format(
            creator_store_product_id=quote(str(creator_store_product_id), safe=""),
        ),
    }

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
    creator_store_product_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[GoogleRpcStatus | MarketplaceFiatServiceCreatorStoreProduct]:
    """Get Creator Store Product

     Get a Creator Store product.

    Args:
        creator_store_product_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GoogleRpcStatus | MarketplaceFiatServiceCreatorStoreProduct]
    """

    kwargs = _get_kwargs(
        creator_store_product_id=creator_store_product_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    creator_store_product_id: str,
    *,
    client: AuthenticatedClient,
) -> GoogleRpcStatus | MarketplaceFiatServiceCreatorStoreProduct | None:
    """Get Creator Store Product

     Get a Creator Store product.

    Args:
        creator_store_product_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GoogleRpcStatus | MarketplaceFiatServiceCreatorStoreProduct
    """

    return sync_detailed(
        creator_store_product_id=creator_store_product_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    creator_store_product_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[GoogleRpcStatus | MarketplaceFiatServiceCreatorStoreProduct]:
    """Get Creator Store Product

     Get a Creator Store product.

    Args:
        creator_store_product_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GoogleRpcStatus | MarketplaceFiatServiceCreatorStoreProduct]
    """

    kwargs = _get_kwargs(
        creator_store_product_id=creator_store_product_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    creator_store_product_id: str,
    *,
    client: AuthenticatedClient,
) -> GoogleRpcStatus | MarketplaceFiatServiceCreatorStoreProduct | None:
    """Get Creator Store Product

     Get a Creator Store product.

    Args:
        creator_store_product_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GoogleRpcStatus | MarketplaceFiatServiceCreatorStoreProduct
    """

    return (
        await asyncio_detailed(
            creator_store_product_id=creator_store_product_id,
            client=client,
        )
    ).parsed
