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
from ...types import UNSET, Response

"""
{'x-roblox-scopes': [{'name': 'asset:read', 'description': 'Required.'}], 'x-roblox-cloud-api-operation': True, 'x-roblox-cloud-api-operation-name': 'List Asset Versions', 'x-roblox-cloud-api-operation-code-samples': [{'language': 'List Asset Versions', 'script': "curl --location 'https://apis.roblox.com/assets/v1/assets/{assetid}/versions?pageToken=&maxPageSize=' \\\n--header 'x-api-key: {apiKey}'"}], 'x-roblox-stability': 'BETA', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'MINUTE', 'maxInPeriod': 100}, 'perOauth2Authorization': {'period': 'MINUTE', 'maxInPeriod': 100}}, 'x-roblox-engine-usability': {'apiKeyWithHttpService': True}}
"""


from ...models.assets_upload_api_status import AssetsUploadApiStatus
from ...models.list_asset_versions_response import ListAssetVersionsResponse
from ...types import Unset


def _get_kwargs(
    asset_id: int,
    *,
    max_page_size: int | Unset = 8,
    page_token: str | Unset = UNSET,
    filter_: str | Unset = "",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["maxPageSize"] = max_page_size

    params["pageToken"] = page_token

    params["filter"] = filter_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/assets/v1/assets/{asset_id}/versions".format(
            asset_id=quote(str(asset_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AssetsUploadApiStatus | ListAssetVersionsResponse | None:
    if response.status_code == 200:
        response_200 = ListAssetVersionsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = AssetsUploadApiStatus.from_dict(response.json())

        return response_400

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
) -> Response[AssetsUploadApiStatus | ListAssetVersionsResponse]:
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
    max_page_size: int | Unset = 8,
    page_token: str | Unset = UNSET,
    filter_: str | Unset = "",
) -> Response[AssetsUploadApiStatus | ListAssetVersionsResponse]:
    """List Asset Versions of an Asset

     List all versions of a specific asset, with optional pagination.

    Args:
        asset_id (int):
        max_page_size (int | Unset):  Default: 8.
        page_token (str | Unset):
        filter_ (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssetsUploadApiStatus | ListAssetVersionsResponse]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        max_page_size=max_page_size,
        page_token=page_token,
        filter_=filter_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: int,
    *,
    client: AuthenticatedClient,
    max_page_size: int | Unset = 8,
    page_token: str | Unset = UNSET,
    filter_: str | Unset = "",
) -> AssetsUploadApiStatus | ListAssetVersionsResponse | None:
    """List Asset Versions of an Asset

     List all versions of a specific asset, with optional pagination.

    Args:
        asset_id (int):
        max_page_size (int | Unset):  Default: 8.
        page_token (str | Unset):
        filter_ (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssetsUploadApiStatus | ListAssetVersionsResponse
    """

    return sync_detailed(
        asset_id=asset_id,
        client=client,
        max_page_size=max_page_size,
        page_token=page_token,
        filter_=filter_,
    ).parsed


async def asyncio_detailed(
    asset_id: int,
    *,
    client: AuthenticatedClient,
    max_page_size: int | Unset = 8,
    page_token: str | Unset = UNSET,
    filter_: str | Unset = "",
) -> Response[AssetsUploadApiStatus | ListAssetVersionsResponse]:
    """List Asset Versions of an Asset

     List all versions of a specific asset, with optional pagination.

    Args:
        asset_id (int):
        max_page_size (int | Unset):  Default: 8.
        page_token (str | Unset):
        filter_ (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssetsUploadApiStatus | ListAssetVersionsResponse]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        max_page_size=max_page_size,
        page_token=page_token,
        filter_=filter_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: int,
    *,
    client: AuthenticatedClient,
    max_page_size: int | Unset = 8,
    page_token: str | Unset = UNSET,
    filter_: str | Unset = "",
) -> AssetsUploadApiStatus | ListAssetVersionsResponse | None:
    """List Asset Versions of an Asset

     List all versions of a specific asset, with optional pagination.

    Args:
        asset_id (int):
        max_page_size (int | Unset):  Default: 8.
        page_token (str | Unset):
        filter_ (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssetsUploadApiStatus | ListAssetVersionsResponse
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            client=client,
            max_page_size=max_page_size,
            page_token=page_token,
            filter_=filter_,
        )
    ).parsed
