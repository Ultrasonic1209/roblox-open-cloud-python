from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.developer_product_config_v2 import DeveloperProductConfigV2
from ...models.developer_products_create_developer_product_v2_body import DeveloperProductsCreateDeveloperProductV2Body
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    universe_id: int,
    *,
    body: DeveloperProductsCreateDeveloperProductV2Body | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/developer-products/v2/universes/{universe_id}/developer-products".format(
            universe_id=quote(str(universe_id), safe=""),
        ),
        "extensions": {
            "openapi-extensions": {
                "x-roblox-stability": "BETA",
                "x-roblox-rate-limits": {
                    "perApiKeyOwner": {"period": "SECOND", "maxInPeriod": 3},
                    "perOauth2Authorization": {"period": "SECOND", "maxInPeriod": 3},
                },
                "x-roblox-scopes": [{"name": "developer-product:write", "targetResourceSpecifier": "universes"}],
                "x-roblox-engine-usability": {"apiKeyWithHttpService": True},
            },
            "openapi-id": "DeveloperProducts_CreateDeveloperProductV2",
        },
    }

    if not isinstance(body, Unset):
        _kwargs["files"] = body.to_multipart()

    headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> DeveloperProductConfigV2 | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = DeveloperProductConfigV2.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

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
    *,
    client: AuthenticatedClient,
    body: DeveloperProductsCreateDeveloperProductV2Body | Unset = UNSET,
) -> Response[DeveloperProductConfigV2 | ErrorResponse]:
    """Create developer product

     Creates a new developer product with the provided configuration details.

    Args:
        universe_id (int):
        body (DeveloperProductsCreateDeveloperProductV2Body | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeveloperProductConfigV2 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        body=body,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    body: DeveloperProductsCreateDeveloperProductV2Body | Unset = UNSET,
) -> DeveloperProductConfigV2 | ErrorResponse | None:
    """Create developer product

     Creates a new developer product with the provided configuration details.

    Args:
        universe_id (int):
        body (DeveloperProductsCreateDeveloperProductV2Body | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeveloperProductConfigV2 | ErrorResponse
    """

    return sync_detailed(
        universe_id=universe_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    body: DeveloperProductsCreateDeveloperProductV2Body | Unset = UNSET,
) -> Response[DeveloperProductConfigV2 | ErrorResponse]:
    """Create developer product

     Creates a new developer product with the provided configuration details.

    Args:
        universe_id (int):
        body (DeveloperProductsCreateDeveloperProductV2Body | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeveloperProductConfigV2 | ErrorResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    body: DeveloperProductsCreateDeveloperProductV2Body | Unset = UNSET,
) -> DeveloperProductConfigV2 | ErrorResponse | None:
    """Create developer product

     Creates a new developer product with the provided configuration details.

    Args:
        universe_id (int):
        body (DeveloperProductsCreateDeveloperProductV2Body | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeveloperProductConfigV2 | ErrorResponse
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            client=client,
            body=body,
        )
    ).parsed
