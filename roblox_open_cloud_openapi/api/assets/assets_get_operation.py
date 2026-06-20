from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ocv1_assets_operation import OCV1AssetsOperation
from ...models.ocv1_assets_status import OCV1AssetsStatus
from ...types import Response


def _get_kwargs(
    operation_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/assets/v1/operations/{operation_id}".format(
            operation_id=quote(str(operation_id), safe=""),
        ),
        "extensions": {
            "openapi-extensions": {
                "x-roblox-cloud-api-operation": True,
                "x-roblox-cloud-api-operation-name": "Get Operation",
                "x-roblox-stability": "BETA",
                "x-roblox-scopes": [{"name": "asset:read"}],
                "x-roblox-cloud-api-operation-code-samples": [
                    {
                        "language": "Get Operation",
                        "script": "curl --location 'https://apis.roblox.com/assets/v1/operations/{operationId}' \\\n--header 'x-api-key: {apiKey}'\n",
                    }
                ],
                "x-roblox-rate-limits": {
                    "perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 300},
                    "perOauth2Authorization": {"period": "MINUTE", "maxInPeriod": 300},
                },
                "x-roblox-throttling-limit": {"perApiKey": {"periodInSeconds": "60", "maxInPeriod": 100}},
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            },
            "openapi-id": "Assets_GetOperation",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | OCV1AssetsOperation | OCV1AssetsStatus | None:
    if response.status_code == 200:
        response_200 = OCV1AssetsOperation.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = OCV1AssetsStatus.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | OCV1AssetsOperation | OCV1AssetsStatus]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    operation_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | OCV1AssetsOperation | OCV1AssetsStatus]:
    """Get the result of an asset creation or update.

     Get the result of an asset creation or update using the returned Operation ID. Requires **Read** for
    the API key permission and **asset:read** for OAuth 2.0 apps.

    Args:
        operation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | OCV1AssetsOperation | OCV1AssetsStatus]
    """

    kwargs = _get_kwargs(
        operation_id=operation_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    operation_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | OCV1AssetsOperation | OCV1AssetsStatus | None:
    """Get the result of an asset creation or update.

     Get the result of an asset creation or update using the returned Operation ID. Requires **Read** for
    the API key permission and **asset:read** for OAuth 2.0 apps.

    Args:
        operation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | OCV1AssetsOperation | OCV1AssetsStatus
    """

    return sync_detailed(
        operation_id=operation_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    operation_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | OCV1AssetsOperation | OCV1AssetsStatus]:
    """Get the result of an asset creation or update.

     Get the result of an asset creation or update using the returned Operation ID. Requires **Read** for
    the API key permission and **asset:read** for OAuth 2.0 apps.

    Args:
        operation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | OCV1AssetsOperation | OCV1AssetsStatus]
    """

    kwargs = _get_kwargs(
        operation_id=operation_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    operation_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | OCV1AssetsOperation | OCV1AssetsStatus | None:
    """Get the result of an asset creation or update.

     Get the result of an asset creation or update using the returned Operation ID. Requires **Read** for
    the API key permission and **asset:read** for OAuth 2.0 apps.

    Args:
        operation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | OCV1AssetsOperation | OCV1AssetsStatus
    """

    return (
        await asyncio_detailed(
            operation_id=operation_id,
            client=client,
        )
    ).parsed
