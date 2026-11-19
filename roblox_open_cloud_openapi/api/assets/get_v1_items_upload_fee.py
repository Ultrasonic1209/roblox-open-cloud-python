from http import HTTPStatus
from typing import TYPE_CHECKING, Any, cast

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
{'x-roblox-stability': 'EXPERIMENTAL', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'SECOND', 'maxInPeriod': 10}}, 'x-roblox-scopes': [{'name': 'marketplace.item-upload-fee:read', 'firstPartyOAuthOnly': True}], 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.get_v1_items_upload_fee_asset_type import GetV1ItemsUploadFeeAssetType
from ...models.get_v1_items_upload_fee_bundle_type import GetV1ItemsUploadFeeBundleType
from ...models.roblox_item_configuration_api_get_item_upload_fee_response import (
    RobloxItemConfigurationApiGetItemUploadFeeResponse,
)
from ...types import Unset


def _get_kwargs(
    *,
    bundle_type: GetV1ItemsUploadFeeBundleType | Unset = UNSET,
    asset_type: GetV1ItemsUploadFeeAssetType | Unset = UNSET,
    is_emissive: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_bundle_type: int | Unset = UNSET
    if not isinstance(bundle_type, Unset):
        json_bundle_type = bundle_type.value

    params["bundleType"] = json_bundle_type

    json_asset_type: int | Unset = UNSET
    if not isinstance(asset_type, Unset):
        json_asset_type = asset_type.value

    params["assetType"] = json_asset_type

    params["IsEmissive"] = is_emissive

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://itemconfiguration.roblox.com/v1/items/upload-fee",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxItemConfigurationApiGetItemUploadFeeResponse | None:
    if response.status_code == 200:
        response_200 = RobloxItemConfigurationApiGetItemUploadFeeResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RobloxItemConfigurationApiGetItemUploadFeeResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    bundle_type: GetV1ItemsUploadFeeBundleType | Unset = UNSET,
    asset_type: GetV1ItemsUploadFeeAssetType | Unset = UNSET,
    is_emissive: bool | Unset = UNSET,
) -> Response[Any | RobloxItemConfigurationApiGetItemUploadFeeResponse]:
    """Get the upload fee for an item type.

    Args:
        bundle_type (GetV1ItemsUploadFeeBundleType | Unset):
        asset_type (GetV1ItemsUploadFeeAssetType | Unset):
        is_emissive (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxItemConfigurationApiGetItemUploadFeeResponse]
    """

    kwargs = _get_kwargs(
        bundle_type=bundle_type,
        asset_type=asset_type,
        is_emissive=is_emissive,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    bundle_type: GetV1ItemsUploadFeeBundleType | Unset = UNSET,
    asset_type: GetV1ItemsUploadFeeAssetType | Unset = UNSET,
    is_emissive: bool | Unset = UNSET,
) -> Any | RobloxItemConfigurationApiGetItemUploadFeeResponse | None:
    """Get the upload fee for an item type.

    Args:
        bundle_type (GetV1ItemsUploadFeeBundleType | Unset):
        asset_type (GetV1ItemsUploadFeeAssetType | Unset):
        is_emissive (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxItemConfigurationApiGetItemUploadFeeResponse
    """

    return sync_detailed(
        client=client,
        bundle_type=bundle_type,
        asset_type=asset_type,
        is_emissive=is_emissive,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    bundle_type: GetV1ItemsUploadFeeBundleType | Unset = UNSET,
    asset_type: GetV1ItemsUploadFeeAssetType | Unset = UNSET,
    is_emissive: bool | Unset = UNSET,
) -> Response[Any | RobloxItemConfigurationApiGetItemUploadFeeResponse]:
    """Get the upload fee for an item type.

    Args:
        bundle_type (GetV1ItemsUploadFeeBundleType | Unset):
        asset_type (GetV1ItemsUploadFeeAssetType | Unset):
        is_emissive (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxItemConfigurationApiGetItemUploadFeeResponse]
    """

    kwargs = _get_kwargs(
        bundle_type=bundle_type,
        asset_type=asset_type,
        is_emissive=is_emissive,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    bundle_type: GetV1ItemsUploadFeeBundleType | Unset = UNSET,
    asset_type: GetV1ItemsUploadFeeAssetType | Unset = UNSET,
    is_emissive: bool | Unset = UNSET,
) -> Any | RobloxItemConfigurationApiGetItemUploadFeeResponse | None:
    """Get the upload fee for an item type.

    Args:
        bundle_type (GetV1ItemsUploadFeeBundleType | Unset):
        asset_type (GetV1ItemsUploadFeeAssetType | Unset):
        is_emissive (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxItemConfigurationApiGetItemUploadFeeResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            bundle_type=bundle_type,
            asset_type=asset_type,
            is_emissive=is_emissive,
        )
    ).parsed
