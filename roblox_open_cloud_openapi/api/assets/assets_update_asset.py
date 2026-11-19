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
{'x-roblox-scopes': [{'name': 'asset:write', 'description': "Required for the asset's creator (user or group)."}], 'x-roblox-cloud-api-operation': True, 'x-roblox-cloud-api-operation-name': 'Update Asset', 'x-roblox-cloud-api-operation-code-samples': [{'language': 'Update Content Only and Create a New Version', 'script': 'curl --location --request PATCH \'https://apis.roblox.com/assets/v1/assets/{assetId}\' \\\n--header \'x-api-key: {apiKey}\' \\\n--form \'request="{\\"assetId\\": {assetId} }"\' \\\n--form \'fileContent="@\\"{file-path}\\""\''}, {'language': 'Update Content and Metadata', 'script': 'curl --location --request PATCH \'https://apis.roblox.com/assets/v1/assets/{assetId}?updateMask=description%2CdisplayName\' \\\n--header \'x-api-key: {apiKey}\' \\\n--form \'request="{\n    \\"assetType\\": \\"{assetType}\\",\n    \\"assetId\\": {assetId},\n    \\"displayName\\": \\"{new display name}\\",\n    \\"description\\": \\"{new description}\\",    \n    \\"creationContext\\": { \n        \\"creator\\": {\n            \\"userId\\": {userId}\n        },\n        \\"expectedPrice\\":{expectedPrice}\n    },\n}"\' \\\n--form \'fileContent=@\\"{file-path}\\"\''}, {'language': 'Update a List of Previews', 'script': 'curl --location --request PATCH \'https://apis.roblox.com/assets/v1/assets/{assetId}?updateMask=previews\' \\\n--header \'x-api-key: {apiKey}\' \\\n--form \'request="{\\"assetId\\": \\"{assetId}\\", \\"previews\\": [{\\"asset\\": \\"assets/123\\", \\"altText\\": \\"Your alt text.\\"}]}"\''}, {'language': 'Update Social Links', 'script': 'curl --location --request PATCH \'https://apis.roblox.com/assets/v1/assets/{assetId}?updateMask=twitchSocialLink%2CgithubSocialLink\' \\\n--header \'x-api-key: {apiKey}\' \\\n--form \'request="{\\"assetId\\": \\"{assetId}\\", \\"twitchSocialLink\\": {\\"title\\": \\"Optional title\\", \\"uri\\": \\"https://twitch.tv/your-channel\\"}, \\"githubSocialLink\\": {\\"title\\": \\"Optional title\\", \\"uri\\": \\"https://github.com/your-repo\\"}}"\''}], 'x-roblox-stability': 'BETA', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'MINUTE', 'maxInPeriod': 120}, 'perOauth2Authorization': {'period': 'MINUTE', 'maxInPeriod': 120}}, 'x-roblox-engine-usability': {'apiKeyWithHttpService': True}}
"""


from ...models.assets_update_asset_body import AssetsUpdateAssetBody
from ...models.assets_upload_api_operation import AssetsUploadApiOperation
from ...models.assets_upload_api_status import AssetsUploadApiStatus
from ...types import Unset


def _get_kwargs(
    asset_id: int,
    *,
    body: AssetsUpdateAssetBody | Unset = UNSET,
    update_mask: list[str] | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_update_mask: list[str] | Unset = UNSET
    if not isinstance(update_mask, Unset):
        json_update_mask = update_mask

    params["updateMask"] = json_update_mask

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/assets/v1/assets/{asset_id}".format(
            asset_id=quote(str(asset_id), safe=""),
        ),
        "params": params,
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
    asset_id: int,
    *,
    client: AuthenticatedClient,
    body: AssetsUpdateAssetBody | Unset = UNSET,
    update_mask: list[str] | Unset = UNSET,
) -> Response[AssetsUploadApiOperation | AssetsUploadApiStatus]:
    """Updates an asset with provided content and metadata.

     Updates an asset's content, metadata, or both. Metadata includes the description, display name,
    icon, social links, and previews. Updating content creates a new asset version and is supported for
    **Models** and **Places**. For Places, set `published` to `true` to publish the new version. Icons
    and previews must be **Image** assets, and icons must have square dimensions.

    Provide the `Asset`, binary asset file path, and [content type](/cloud/guides/usage-
    assets.md#supported-asset-types-and-limits) in the form data.

    Args:
        asset_id (int):
        update_mask (list[str] | Unset):
        body (AssetsUpdateAssetBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssetsUploadApiOperation | AssetsUploadApiStatus]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        body=body,
        update_mask=update_mask,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: int,
    *,
    client: AuthenticatedClient,
    body: AssetsUpdateAssetBody | Unset = UNSET,
    update_mask: list[str] | Unset = UNSET,
) -> AssetsUploadApiOperation | AssetsUploadApiStatus | None:
    """Updates an asset with provided content and metadata.

     Updates an asset's content, metadata, or both. Metadata includes the description, display name,
    icon, social links, and previews. Updating content creates a new asset version and is supported for
    **Models** and **Places**. For Places, set `published` to `true` to publish the new version. Icons
    and previews must be **Image** assets, and icons must have square dimensions.

    Provide the `Asset`, binary asset file path, and [content type](/cloud/guides/usage-
    assets.md#supported-asset-types-and-limits) in the form data.

    Args:
        asset_id (int):
        update_mask (list[str] | Unset):
        body (AssetsUpdateAssetBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssetsUploadApiOperation | AssetsUploadApiStatus
    """

    return sync_detailed(
        asset_id=asset_id,
        client=client,
        body=body,
        update_mask=update_mask,
    ).parsed


async def asyncio_detailed(
    asset_id: int,
    *,
    client: AuthenticatedClient,
    body: AssetsUpdateAssetBody | Unset = UNSET,
    update_mask: list[str] | Unset = UNSET,
) -> Response[AssetsUploadApiOperation | AssetsUploadApiStatus]:
    """Updates an asset with provided content and metadata.

     Updates an asset's content, metadata, or both. Metadata includes the description, display name,
    icon, social links, and previews. Updating content creates a new asset version and is supported for
    **Models** and **Places**. For Places, set `published` to `true` to publish the new version. Icons
    and previews must be **Image** assets, and icons must have square dimensions.

    Provide the `Asset`, binary asset file path, and [content type](/cloud/guides/usage-
    assets.md#supported-asset-types-and-limits) in the form data.

    Args:
        asset_id (int):
        update_mask (list[str] | Unset):
        body (AssetsUpdateAssetBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssetsUploadApiOperation | AssetsUploadApiStatus]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        body=body,
        update_mask=update_mask,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: int,
    *,
    client: AuthenticatedClient,
    body: AssetsUpdateAssetBody | Unset = UNSET,
    update_mask: list[str] | Unset = UNSET,
) -> AssetsUploadApiOperation | AssetsUploadApiStatus | None:
    """Updates an asset with provided content and metadata.

     Updates an asset's content, metadata, or both. Metadata includes the description, display name,
    icon, social links, and previews. Updating content creates a new asset version and is supported for
    **Models** and **Places**. For Places, set `published` to `true` to publish the new version. Icons
    and previews must be **Image** assets, and icons must have square dimensions.

    Provide the `Asset`, binary asset file path, and [content type](/cloud/guides/usage-
    assets.md#supported-asset-types-and-limits) in the form data.

    Args:
        asset_id (int):
        update_mask (list[str] | Unset):
        body (AssetsUpdateAssetBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssetsUploadApiOperation | AssetsUploadApiStatus
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            client=client,
            body=body,
            update_mask=update_mask,
        )
    ).parsed
