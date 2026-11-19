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
{'x-roblox-scopes': [{'name': 'asset:write', 'description': "Required for the asset's creator (user or group)."}], 'x-roblox-cloud-api-operation': True, 'x-roblox-cloud-api-operation-name': 'Restore Asset', 'x-roblox-cloud-api-operation-code-samples': [{'language': 'Restore Asset', 'script': "curl --location 'https://apis.roblox.com/assets/v1/assets/{assetid}:restore' \\\n--header 'x-api-key: {apiKey}' \\\n--header 'Content-Type: application/json'"}], 'x-roblox-stability': 'BETA', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'MINUTE', 'maxInPeriod': 100}, 'perOauth2Authorization': {'period': 'MINUTE', 'maxInPeriod': 100}}, 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.assets_upload_api_asset import AssetsUploadApiAsset
from ...models.assets_upload_api_status import AssetsUploadApiStatus


def _get_kwargs(
    asset_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/assets/v1/assets/{asset_id}:restore".format(
            asset_id=quote(str(asset_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AssetsUploadApiAsset | AssetsUploadApiStatus | None:
    if response.status_code == 200:
        response_200 = AssetsUploadApiAsset.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = AssetsUploadApiStatus.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = AssetsUploadApiStatus.from_dict(response.json())

        return response_401

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
) -> Response[AssetsUploadApiAsset | AssetsUploadApiStatus]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    asset_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[AssetsUploadApiAsset | AssetsUploadApiStatus]:
    """Restores an archived asset.

     Restores an archived asset.

    Args:
        asset_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssetsUploadApiAsset | AssetsUploadApiStatus]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: int,
    *,
    client: AuthenticatedClient,
) -> AssetsUploadApiAsset | AssetsUploadApiStatus | None:
    """Restores an archived asset.

     Restores an archived asset.

    Args:
        asset_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssetsUploadApiAsset | AssetsUploadApiStatus
    """

    return sync_detailed(
        asset_id=asset_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    asset_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[AssetsUploadApiAsset | AssetsUploadApiStatus]:
    """Restores an archived asset.

     Restores an archived asset.

    Args:
        asset_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssetsUploadApiAsset | AssetsUploadApiStatus]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: int,
    *,
    client: AuthenticatedClient,
) -> AssetsUploadApiAsset | AssetsUploadApiStatus | None:
    """Restores an archived asset.

     Restores an archived asset.

    Args:
        asset_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssetsUploadApiAsset | AssetsUploadApiStatus
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            client=client,
        )
    ).parsed
