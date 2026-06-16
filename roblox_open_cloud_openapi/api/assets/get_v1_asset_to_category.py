from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v1_asset_to_category_response_200 import GetV1AssetToCategoryResponse200
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/asset-to-category",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetV1AssetToCategoryResponse200 | None:
    if response.status_code == 200:
        response_200 = GetV1AssetToCategoryResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetV1AssetToCategoryResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[GetV1AssetToCategoryResponse200]:
    """Lists a mapping for assets to category IDs to convert from inventory ID to catalog ID. Creates a
    mapping to link 'Get More' button in inventory page to the relevant catalog page.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetV1AssetToCategoryResponse200]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> GetV1AssetToCategoryResponse200 | None:
    """Lists a mapping for assets to category IDs to convert from inventory ID to catalog ID. Creates a
    mapping to link 'Get More' button in inventory page to the relevant catalog page.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetV1AssetToCategoryResponse200
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[GetV1AssetToCategoryResponse200]:
    """Lists a mapping for assets to category IDs to convert from inventory ID to catalog ID. Creates a
    mapping to link 'Get More' button in inventory page to the relevant catalog page.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetV1AssetToCategoryResponse200]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> GetV1AssetToCategoryResponse200 | None:
    """Lists a mapping for assets to category IDs to convert from inventory ID to catalog ID. Creates a
    mapping to link 'Get More' button in inventory page to the relevant catalog page.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetV1AssetToCategoryResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
