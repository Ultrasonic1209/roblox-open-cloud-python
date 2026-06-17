from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.asset import Asset
from ...types import Response


def _get_kwargs(
    asset_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/assets/v1/assets/{asset_id}:archive".format(
            asset_id=quote(str(asset_id), safe=""),
        ),
        "openapi-extensions": {
            "x-roblox-cloud-api-operation": True,
            "x-roblox-cloud-api-operation-name": "Archive Asset",
            "x-roblox-stability": "BETA",
            "x-roblox-scopes": [{"name": "asset:read"}, {"name": "asset:write"}],
            "x-roblox-cloud-api-operation-code-samples": [
                {
                    "language": "Archive Asset",
                    "script": "curl --location 'https://apis.roblox.com/assets/v1/assets/{assetid}:archive' \\\n--header 'x-api-key: {apiKey}' \\\n--header 'Content-Type: application/json'",
                }
            ],
            "x-roblox-rate-limits": {
                "perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 100},
                "perOauth2Authorization": {"period": "MINUTE", "maxInPeriod": 100},
            },
            "x-roblox-throttling-limit": {"perApiKey": {"periodInSeconds": "60", "maxInPeriod": 100}},
            "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
        },
        "openapi-id": "Assets_ArchiveAsset",
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Any | Asset | None:
    if response.status_code == 200:
        response_200 = Asset.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[Any | Asset]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    asset_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | Asset]:
    """Archives the asset.

     Archives the asset. Archived assets disappear from the website and are no longer usable or visible
    in Roblox experiences, but you can [restore](#POST-v1-assets-{assetId}:restore) them.

    Args:
        asset_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Asset]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | Asset | None:
    """Archives the asset.

     Archives the asset. Archived assets disappear from the website and are no longer usable or visible
    in Roblox experiences, but you can [restore](#POST-v1-assets-{assetId}:restore) them.

    Args:
        asset_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Asset
    """

    return sync_detailed(
        asset_id=asset_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | Asset]:
    """Archives the asset.

     Archives the asset. Archived assets disappear from the website and are no longer usable or visible
    in Roblox experiences, but you can [restore](#POST-v1-assets-{assetId}:restore) them.

    Args:
        asset_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Asset]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | Asset | None:
    """Archives the asset.

     Archives the asset. Archived assets disappear from the website and are no longer usable or visible
    in Roblox experiences, but you can [restore](#POST-v1-assets-{assetId}:restore) them.

    Args:
        asset_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Asset
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            client=client,
        )
    ).parsed
