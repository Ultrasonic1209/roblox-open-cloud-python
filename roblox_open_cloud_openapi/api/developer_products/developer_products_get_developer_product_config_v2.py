from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.developer_product_config_v2 import DeveloperProductConfigV2
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    universe_id: int,
    product_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/developer-products/v2/universes/{universe_id}/developer-products/{product_id}/creator".format(
            universe_id=quote(str(universe_id), safe=""),
            product_id=quote(str(product_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> DeveloperProductConfigV2 | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = DeveloperProductConfigV2.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[DeveloperProductConfigV2 | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    universe_id: int,
    product_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[DeveloperProductConfigV2 | ErrorResponse]:
    """Get developer product with configuration details

    Args:
        universe_id (int):
        product_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeveloperProductConfigV2 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        product_id=product_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: int,
    product_id: int,
    *,
    client: AuthenticatedClient,
) -> DeveloperProductConfigV2 | ErrorResponse | None:
    """Get developer product with configuration details

    Args:
        universe_id (int):
        product_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeveloperProductConfigV2 | ErrorResponse
    """

    return sync_detailed(
        universe_id=universe_id,
        product_id=product_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    universe_id: int,
    product_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[DeveloperProductConfigV2 | ErrorResponse]:
    """Get developer product with configuration details

    Args:
        universe_id (int):
        product_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeveloperProductConfigV2 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        product_id=product_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: int,
    product_id: int,
    *,
    client: AuthenticatedClient,
) -> DeveloperProductConfigV2 | ErrorResponse | None:
    """Get developer product with configuration details

    Args:
        universe_id (int):
        product_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeveloperProductConfigV2 | ErrorResponse
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            product_id=product_id,
            client=client,
        )
    ).parsed
