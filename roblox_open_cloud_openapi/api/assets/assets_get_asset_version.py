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


from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response

"""
{'x-roblox-scopes': [{'name': 'asset:read', 'description': 'Required.'}], 'x-roblox-cloud-api-operation': True, 'x-roblox-cloud-api-operation-name': 'Get Asset Version', 'x-roblox-cloud-api-operation-code-samples': [{'language': 'Get Asset Version', 'script': "curl --location 'https://apis.roblox.com/assets/v1/assets/{assetId}/versions/{versionNumber}' \\\n--header 'x-api-key: {apiKey}'"}], 'x-roblox-stability': 'BETA', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'MINUTE', 'maxInPeriod': 600}, 'perOauth2Authorization': {'period': 'MINUTE', 'maxInPeriod': 600}}, 'x-roblox-engine-usability': {'apiKeyWithHttpService': True}}
"""


from ...models.asset_version import AssetVersion
from ...models.assets_upload_api_status import AssetsUploadApiStatus


def _get_kwargs(
    asset_id: int,
    version_number: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/assets/v1/assets/{asset_id}/versions/{version_number}".format(
            asset_id=quote(str(asset_id), safe=""),
            version_number=quote(str(version_number), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AssetVersion | AssetsUploadApiStatus | None:
    if response.status_code == 200:
        response_200 = AssetVersion.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = AssetsUploadApiStatus.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = AssetsUploadApiStatus.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AssetVersion | AssetsUploadApiStatus]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    asset_id: int,
    version_number: int,
    *,
    client: AuthenticatedClient,
) -> Response[AssetVersion | AssetsUploadApiStatus]:
    """Get Asset Version

     Retrieve a specific asset version by the asset ID and the version number.

    Args:
        asset_id (int):
        version_number (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssetVersion | AssetsUploadApiStatus]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        version_number=version_number,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: int,
    version_number: int,
    *,
    client: AuthenticatedClient,
) -> AssetVersion | AssetsUploadApiStatus | None:
    """Get Asset Version

     Retrieve a specific asset version by the asset ID and the version number.

    Args:
        asset_id (int):
        version_number (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssetVersion | AssetsUploadApiStatus
    """

    return sync_detailed(
        asset_id=asset_id,
        version_number=version_number,
        client=client,
    ).parsed


async def asyncio_detailed(
    asset_id: int,
    version_number: int,
    *,
    client: AuthenticatedClient,
) -> Response[AssetVersion | AssetsUploadApiStatus]:
    """Get Asset Version

     Retrieve a specific asset version by the asset ID and the version number.

    Args:
        asset_id (int):
        version_number (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssetVersion | AssetsUploadApiStatus]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        version_number=version_number,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: int,
    version_number: int,
    *,
    client: AuthenticatedClient,
) -> AssetVersion | AssetsUploadApiStatus | None:
    """Get Asset Version

     Retrieve a specific asset version by the asset ID and the version number.

    Args:
        asset_id (int):
        version_number (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssetVersion | AssetsUploadApiStatus
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            version_number=version_number,
            client=client,
        )
    ).parsed
