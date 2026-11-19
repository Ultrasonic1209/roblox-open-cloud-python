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
{'x-roblox-scopes': [{'name': 'asset:read', 'description': 'Required.'}], 'x-roblox-cloud-api-operation': True, 'x-roblox-cloud-api-operation-name': 'Get Asset', 'x-roblox-cloud-api-operation-code-samples': [{'language': 'Get Asset without readMask', 'script': "curl --location --request GET 'https://apis.roblox.com/assets/v1/assets/{assetId}' \\\n--header 'x-api-key: {apiKey}'"}, {'language': 'Get Asset with readMask', 'script': "curl --location --request GET 'https://apis.roblox.com/assets/v1/assets/{assetId}?readMask={read_mask}' \\\n--header 'x-api-key: {apiKey}'"}], 'x-roblox-stability': 'BETA', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'MINUTE', 'maxInPeriod': 600}, 'perOauth2Authorization': {'period': 'MINUTE', 'maxInPeriod': 600}}, 'x-roblox-engine-usability': {'apiKeyWithHttpService': True}}
"""


from ...models.assets_upload_api_asset import AssetsUploadApiAsset
from ...models.assets_upload_api_status import AssetsUploadApiStatus
from ...types import Unset


def _get_kwargs(
    asset_id: int,
    *,
    read_mask: list[str] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_read_mask: list[str] | Unset = UNSET
    if not isinstance(read_mask, Unset):
        json_read_mask = read_mask

    params["readMask"] = json_read_mask

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/assets/v1/assets/{asset_id}".format(
            asset_id=quote(str(asset_id), safe=""),
        ),
        "params": params,
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

    if response.status_code == 500:
        response_500 = AssetsUploadApiStatus.from_dict(response.json())

        return response_500

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
    read_mask: list[str] | Unset = UNSET,
) -> Response[AssetsUploadApiAsset | AssetsUploadApiStatus]:
    """Retrieve specific asset metadata. Include the `readMask` parameter for additional asset metadata.

     Retrieve specific asset metadata.

    Args:
        asset_id (int):
        read_mask (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssetsUploadApiAsset | AssetsUploadApiStatus]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        read_mask=read_mask,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: int,
    *,
    client: AuthenticatedClient,
    read_mask: list[str] | Unset = UNSET,
) -> AssetsUploadApiAsset | AssetsUploadApiStatus | None:
    """Retrieve specific asset metadata. Include the `readMask` parameter for additional asset metadata.

     Retrieve specific asset metadata.

    Args:
        asset_id (int):
        read_mask (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssetsUploadApiAsset | AssetsUploadApiStatus
    """

    return sync_detailed(
        asset_id=asset_id,
        client=client,
        read_mask=read_mask,
    ).parsed


async def asyncio_detailed(
    asset_id: int,
    *,
    client: AuthenticatedClient,
    read_mask: list[str] | Unset = UNSET,
) -> Response[AssetsUploadApiAsset | AssetsUploadApiStatus]:
    """Retrieve specific asset metadata. Include the `readMask` parameter for additional asset metadata.

     Retrieve specific asset metadata.

    Args:
        asset_id (int):
        read_mask (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssetsUploadApiAsset | AssetsUploadApiStatus]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        read_mask=read_mask,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: int,
    *,
    client: AuthenticatedClient,
    read_mask: list[str] | Unset = UNSET,
) -> AssetsUploadApiAsset | AssetsUploadApiStatus | None:
    """Retrieve specific asset metadata. Include the `readMask` parameter for additional asset metadata.

     Retrieve specific asset metadata.

    Args:
        asset_id (int):
        read_mask (list[str] | Unset):

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
            read_mask=read_mask,
        )
    ).parsed
