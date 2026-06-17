from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.creator_store_product import CreatorStoreProduct
from ...types import UNSET, Response, Unset


def _get_kwargs(
    creator_store_product_id: str,
    *,
    body: CreatorStoreProduct,
    update_mask: str | Unset = UNSET,
    allow_missing: bool | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["updateMask"] = update_mask

    params["allowMissing"] = allow_missing

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/cloud/v2/creator-store-products/{creator_store_product_id}".format(
            creator_store_product_id=quote(str(creator_store_product_id), safe=""),
        ),
        "params": params,
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
    creator_store_product_id: str,
    *,
    client: AuthenticatedClient,
    body: CreatorStoreProduct,
    update_mask: str | Unset = UNSET,
    allow_missing: bool | Unset = UNSET,
) -> Response[CreatorStoreProduct]:
    """Update Creator Store Product

     Update a Creator Store product.

    Args:
        creator_store_product_id (str):
        update_mask (str | Unset):
        allow_missing (bool | Unset):  Example: True.
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
        creator_store_product_id=creator_store_product_id,
        body=body,
        update_mask=update_mask,
        allow_missing=allow_missing,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    creator_store_product_id: str,
    *,
    client: AuthenticatedClient,
    body: CreatorStoreProduct,
    update_mask: str | Unset = UNSET,
    allow_missing: bool | Unset = UNSET,
) -> CreatorStoreProduct | None:
    """Update Creator Store Product

     Update a Creator Store product.

    Args:
        creator_store_product_id (str):
        update_mask (str | Unset):
        allow_missing (bool | Unset):  Example: True.
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
        creator_store_product_id=creator_store_product_id,
        client=client,
        body=body,
        update_mask=update_mask,
        allow_missing=allow_missing,
    ).parsed


async def asyncio_detailed(
    creator_store_product_id: str,
    *,
    client: AuthenticatedClient,
    body: CreatorStoreProduct,
    update_mask: str | Unset = UNSET,
    allow_missing: bool | Unset = UNSET,
) -> Response[CreatorStoreProduct]:
    """Update Creator Store Product

     Update a Creator Store product.

    Args:
        creator_store_product_id (str):
        update_mask (str | Unset):
        allow_missing (bool | Unset):  Example: True.
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
        creator_store_product_id=creator_store_product_id,
        body=body,
        update_mask=update_mask,
        allow_missing=allow_missing,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    creator_store_product_id: str,
    *,
    client: AuthenticatedClient,
    body: CreatorStoreProduct,
    update_mask: str | Unset = UNSET,
    allow_missing: bool | Unset = UNSET,
) -> CreatorStoreProduct | None:
    """Update Creator Store Product

     Update a Creator Store product.

    Args:
        creator_store_product_id (str):
        update_mask (str | Unset):
        allow_missing (bool | Unset):  Example: True.
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
            creator_store_product_id=creator_store_product_id,
            client=client,
            body=body,
            update_mask=update_mask,
            allow_missing=allow_missing,
        )
    ).parsed
