from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.asset_permissions_error_response import AssetPermissionsErrorResponse
from ...models.batch_grant_permissions_request import BatchGrantPermissionsRequest
from ...models.batch_grant_permissions_response import BatchGrantPermissionsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: BatchGrantPermissionsRequest
    | BatchGrantPermissionsRequest
    | BatchGrantPermissionsRequest
    | BatchGrantPermissionsRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/asset-permissions-api/v1/assets/permissions",
        "extensions": {
            "openapi-extensions": {
                "x-roblox-stability": "BETA",
                "x-roblox-rate-limits": {"perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 100}},
                "x-roblox-scopes": [{"name": "asset-permissions:write", "targetResourceSpecifier": ""}],
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            },
            "openapi-id": "patch_asset-permissions-api_v1_assets_permissions",
        },
    }

    if isinstance(body, BatchGrantPermissionsRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, BatchGrantPermissionsRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, BatchGrantPermissionsRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"
    if isinstance(body, BatchGrantPermissionsRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> AssetPermissionsErrorResponse | BatchGrantPermissionsResponse | None:
    if response.status_code == 200:
        response_200 = BatchGrantPermissionsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = AssetPermissionsErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = AssetPermissionsErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 500:
        response_500 = AssetPermissionsErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[AssetPermissionsErrorResponse | BatchGrantPermissionsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: BatchGrantPermissionsRequest
    | BatchGrantPermissionsRequest
    | BatchGrantPermissionsRequest
    | BatchGrantPermissionsRequest
    | Unset = UNSET,
) -> Response[AssetPermissionsErrorResponse | BatchGrantPermissionsResponse]:
    """Grant a subject permission to multiple assets.

    Authorization is required to grant permissions to the subject and asset IDs in the request.

    Args:
        body (BatchGrantPermissionsRequest | Unset): Request object to grant one permission to
            multiple assets.
        body (BatchGrantPermissionsRequest | Unset): Request object to grant one permission to
            multiple assets.
        body (BatchGrantPermissionsRequest | Unset): Request object to grant one permission to
            multiple assets.
        body (BatchGrantPermissionsRequest | Unset): Request object to grant one permission to
            multiple assets.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssetPermissionsErrorResponse | BatchGrantPermissionsResponse]
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
    body: BatchGrantPermissionsRequest
    | BatchGrantPermissionsRequest
    | BatchGrantPermissionsRequest
    | BatchGrantPermissionsRequest
    | Unset = UNSET,
) -> AssetPermissionsErrorResponse | BatchGrantPermissionsResponse | None:
    """Grant a subject permission to multiple assets.

    Authorization is required to grant permissions to the subject and asset IDs in the request.

    Args:
        body (BatchGrantPermissionsRequest | Unset): Request object to grant one permission to
            multiple assets.
        body (BatchGrantPermissionsRequest | Unset): Request object to grant one permission to
            multiple assets.
        body (BatchGrantPermissionsRequest | Unset): Request object to grant one permission to
            multiple assets.
        body (BatchGrantPermissionsRequest | Unset): Request object to grant one permission to
            multiple assets.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssetPermissionsErrorResponse | BatchGrantPermissionsResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BatchGrantPermissionsRequest
    | BatchGrantPermissionsRequest
    | BatchGrantPermissionsRequest
    | BatchGrantPermissionsRequest
    | Unset = UNSET,
) -> Response[AssetPermissionsErrorResponse | BatchGrantPermissionsResponse]:
    """Grant a subject permission to multiple assets.

    Authorization is required to grant permissions to the subject and asset IDs in the request.

    Args:
        body (BatchGrantPermissionsRequest | Unset): Request object to grant one permission to
            multiple assets.
        body (BatchGrantPermissionsRequest | Unset): Request object to grant one permission to
            multiple assets.
        body (BatchGrantPermissionsRequest | Unset): Request object to grant one permission to
            multiple assets.
        body (BatchGrantPermissionsRequest | Unset): Request object to grant one permission to
            multiple assets.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssetPermissionsErrorResponse | BatchGrantPermissionsResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: BatchGrantPermissionsRequest
    | BatchGrantPermissionsRequest
    | BatchGrantPermissionsRequest
    | BatchGrantPermissionsRequest
    | Unset = UNSET,
) -> AssetPermissionsErrorResponse | BatchGrantPermissionsResponse | None:
    """Grant a subject permission to multiple assets.

    Authorization is required to grant permissions to the subject and asset IDs in the request.

    Args:
        body (BatchGrantPermissionsRequest | Unset): Request object to grant one permission to
            multiple assets.
        body (BatchGrantPermissionsRequest | Unset): Request object to grant one permission to
            multiple assets.
        body (BatchGrantPermissionsRequest | Unset): Request object to grant one permission to
            multiple assets.
        body (BatchGrantPermissionsRequest | Unset): Request object to grant one permission to
            multiple assets.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssetPermissionsErrorResponse | BatchGrantPermissionsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
