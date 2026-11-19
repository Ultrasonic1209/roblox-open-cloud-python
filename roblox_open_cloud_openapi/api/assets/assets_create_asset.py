from http import HTTPStatus
from typing import TYPE_CHECKING, Any

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
{'x-roblox-scopes': [{'name': 'asset:write', 'description': "Required for the asset's creator (user or group)."}], 'x-roblox-cloud-api-operation': True, 'x-roblox-cloud-api-operation-name': 'Create Asset', 'x-roblox-cloud-api-operation-code-samples': [{'language': 'Create Asset', 'script': 'curl --location --request POST \'https://apis.roblox.com/assets/v1/assets\' \\\n--header \'x-api-key: {apiKey}\' \\\n--form \'request="{ \n  \\"assetType\\": \\"Model\\",  \n  \\"displayName\\": \\"Name\\", \n  \\"description\\": \\"This is a description\\", \n  \\"creationContext\\": { \n    \\"creator\\": { \n      \\"userId\\": \\"${userId}\\" \n    } \n  } \n}"\' \\\n--form \'fileContent=@"/filepath/model.fbx";type=model/fbx\' \n'}], 'x-roblox-stability': 'BETA', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'MINUTE', 'maxInPeriod': 120}, 'perOauth2Authorization': {'period': 'MINUTE', 'maxInPeriod': 120}}, 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.assets_create_asset_body import AssetsCreateAssetBody
from ...models.assets_upload_api_operation import AssetsUploadApiOperation
from ...models.assets_upload_api_status import AssetsUploadApiStatus
from ...types import Unset


def _get_kwargs(
    *,
    body: AssetsCreateAssetBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/assets/v1/assets",
    }

    if not isinstance(body, Unset):
        _kwargs["files"] = body.to_multipart()

    headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AssetsUploadApiOperation | AssetsUploadApiStatus | None:
    if response.status_code == 200:
        response_200 = AssetsUploadApiOperation.from_dict(response.json())

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

    if response.status_code == 500:
        response_500 = AssetsUploadApiStatus.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AssetsUploadApiOperation | AssetsUploadApiStatus]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: AssetsCreateAssetBody | Unset = UNSET,
) -> Response[AssetsUploadApiOperation | AssetsUploadApiStatus]:
    """Creates an asset with provided content and metadata.

     Creates an asset with provided content and metadata.

    You can't add `SocialLink` objects when you create an asset. Instead, use [Update
    Asset](#Assets_UpdateAsset).

    Provide the `Asset`, binary asset file path, and [content type](/cloud/guides/usage-
    assets.md#supported-asset-types-and-limits) in the form data.

    Args:
        body (AssetsCreateAssetBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssetsUploadApiOperation | AssetsUploadApiStatus]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: AssetsCreateAssetBody | Unset = UNSET,
) -> AssetsUploadApiOperation | AssetsUploadApiStatus | None:
    """Creates an asset with provided content and metadata.

     Creates an asset with provided content and metadata.

    You can't add `SocialLink` objects when you create an asset. Instead, use [Update
    Asset](#Assets_UpdateAsset).

    Provide the `Asset`, binary asset file path, and [content type](/cloud/guides/usage-
    assets.md#supported-asset-types-and-limits) in the form data.

    Args:
        body (AssetsCreateAssetBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssetsUploadApiOperation | AssetsUploadApiStatus
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: AssetsCreateAssetBody | Unset = UNSET,
) -> Response[AssetsUploadApiOperation | AssetsUploadApiStatus]:
    """Creates an asset with provided content and metadata.

     Creates an asset with provided content and metadata.

    You can't add `SocialLink` objects when you create an asset. Instead, use [Update
    Asset](#Assets_UpdateAsset).

    Provide the `Asset`, binary asset file path, and [content type](/cloud/guides/usage-
    assets.md#supported-asset-types-and-limits) in the form data.

    Args:
        body (AssetsCreateAssetBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssetsUploadApiOperation | AssetsUploadApiStatus]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: AssetsCreateAssetBody | Unset = UNSET,
) -> AssetsUploadApiOperation | AssetsUploadApiStatus | None:
    """Creates an asset with provided content and metadata.

     Creates an asset with provided content and metadata.

    You can't add `SocialLink` objects when you create an asset. Instead, use [Update
    Asset](#Assets_UpdateAsset).

    Provide the `Asset`, binary asset file path, and [content type](/cloud/guides/usage-
    assets.md#supported-asset-types-and-limits) in the form data.

    Args:
        body (AssetsCreateAssetBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssetsUploadApiOperation | AssetsUploadApiStatus
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
