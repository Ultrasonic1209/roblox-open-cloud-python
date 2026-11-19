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
{'x-roblox-stability': 'EXPERIMENTAL', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'SECOND', 'maxInPeriod': 10}}, 'x-roblox-scopes': [{'name': 'marketplace.item:read', 'firstPartyOAuthOnly': True}], 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.get_v1_collectibles_publishing_fees_preview_asset_type import (
    GetV1CollectiblesPublishingFeesPreviewAssetType,
)
from ...models.get_v1_collectibles_publishing_fees_preview_bundle_type import (
    GetV1CollectiblesPublishingFeesPreviewBundleType,
)
from ...models.get_v1_collectibles_publishing_fees_preview_publishing_type import (
    GetV1CollectiblesPublishingFeesPreviewPublishingType,
)
from ...models.roblox_item_configuration_api_publishing_fee_preview_response import (
    RobloxItemConfigurationApiPublishingFeePreviewResponse,
)


def _get_kwargs(
    *,
    asset_type: GetV1CollectiblesPublishingFeesPreviewAssetType,
    bundle_type: GetV1CollectiblesPublishingFeesPreviewBundleType,
    quantity: int,
    publishing_type: GetV1CollectiblesPublishingFeesPreviewPublishingType,
    is_free: bool,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_asset_type = asset_type.value
    params["AssetType"] = json_asset_type

    json_bundle_type = bundle_type.value
    params["BundleType"] = json_bundle_type

    params["Quantity"] = quantity

    json_publishing_type = publishing_type.value
    params["PublishingType"] = json_publishing_type

    params["IsFree"] = is_free

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://itemconfiguration.roblox.com/v1/collectibles/publishing-fees/preview",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxItemConfigurationApiPublishingFeePreviewResponse | None:
    if response.status_code == 200:
        response_200 = RobloxItemConfigurationApiPublishingFeePreviewResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

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
) -> Response[Any | RobloxItemConfigurationApiPublishingFeePreviewResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    asset_type: GetV1CollectiblesPublishingFeesPreviewAssetType,
    bundle_type: GetV1CollectiblesPublishingFeesPreviewBundleType,
    quantity: int,
    publishing_type: GetV1CollectiblesPublishingFeesPreviewPublishingType,
    is_free: bool,
) -> Response[Any | RobloxItemConfigurationApiPublishingFeePreviewResponse]:
    """Previews the publishing fee for an item type before the item exists, so the fee can be shown at
    upload time. Takes the item's type directly instead of a target id.

    Args:
        asset_type (GetV1CollectiblesPublishingFeesPreviewAssetType):
        bundle_type (GetV1CollectiblesPublishingFeesPreviewBundleType):
        quantity (int):
        publishing_type (GetV1CollectiblesPublishingFeesPreviewPublishingType):
        is_free (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxItemConfigurationApiPublishingFeePreviewResponse]
    """

    kwargs = _get_kwargs(
        asset_type=asset_type,
        bundle_type=bundle_type,
        quantity=quantity,
        publishing_type=publishing_type,
        is_free=is_free,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    asset_type: GetV1CollectiblesPublishingFeesPreviewAssetType,
    bundle_type: GetV1CollectiblesPublishingFeesPreviewBundleType,
    quantity: int,
    publishing_type: GetV1CollectiblesPublishingFeesPreviewPublishingType,
    is_free: bool,
) -> Any | RobloxItemConfigurationApiPublishingFeePreviewResponse | None:
    """Previews the publishing fee for an item type before the item exists, so the fee can be shown at
    upload time. Takes the item's type directly instead of a target id.

    Args:
        asset_type (GetV1CollectiblesPublishingFeesPreviewAssetType):
        bundle_type (GetV1CollectiblesPublishingFeesPreviewBundleType):
        quantity (int):
        publishing_type (GetV1CollectiblesPublishingFeesPreviewPublishingType):
        is_free (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxItemConfigurationApiPublishingFeePreviewResponse
    """

    return sync_detailed(
        client=client,
        asset_type=asset_type,
        bundle_type=bundle_type,
        quantity=quantity,
        publishing_type=publishing_type,
        is_free=is_free,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    asset_type: GetV1CollectiblesPublishingFeesPreviewAssetType,
    bundle_type: GetV1CollectiblesPublishingFeesPreviewBundleType,
    quantity: int,
    publishing_type: GetV1CollectiblesPublishingFeesPreviewPublishingType,
    is_free: bool,
) -> Response[Any | RobloxItemConfigurationApiPublishingFeePreviewResponse]:
    """Previews the publishing fee for an item type before the item exists, so the fee can be shown at
    upload time. Takes the item's type directly instead of a target id.

    Args:
        asset_type (GetV1CollectiblesPublishingFeesPreviewAssetType):
        bundle_type (GetV1CollectiblesPublishingFeesPreviewBundleType):
        quantity (int):
        publishing_type (GetV1CollectiblesPublishingFeesPreviewPublishingType):
        is_free (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxItemConfigurationApiPublishingFeePreviewResponse]
    """

    kwargs = _get_kwargs(
        asset_type=asset_type,
        bundle_type=bundle_type,
        quantity=quantity,
        publishing_type=publishing_type,
        is_free=is_free,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    asset_type: GetV1CollectiblesPublishingFeesPreviewAssetType,
    bundle_type: GetV1CollectiblesPublishingFeesPreviewBundleType,
    quantity: int,
    publishing_type: GetV1CollectiblesPublishingFeesPreviewPublishingType,
    is_free: bool,
) -> Any | RobloxItemConfigurationApiPublishingFeePreviewResponse | None:
    """Previews the publishing fee for an item type before the item exists, so the fee can be shown at
    upload time. Takes the item's type directly instead of a target id.

    Args:
        asset_type (GetV1CollectiblesPublishingFeesPreviewAssetType):
        bundle_type (GetV1CollectiblesPublishingFeesPreviewBundleType):
        quantity (int):
        publishing_type (GetV1CollectiblesPublishingFeesPreviewPublishingType):
        is_free (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxItemConfigurationApiPublishingFeePreviewResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            asset_type=asset_type,
            bundle_type=bundle_type,
            quantity=quantity,
            publishing_type=publishing_type,
            is_free=is_free,
        )
    ).parsed
