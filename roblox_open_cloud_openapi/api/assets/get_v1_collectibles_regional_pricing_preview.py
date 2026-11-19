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


from ...models.get_v1_collectibles_regional_pricing_preview_publishing_type import (
    GetV1CollectiblesRegionalPricingPreviewPublishingType,
)
from ...models.get_v1_collectibles_regional_pricing_preview_target_type import (
    GetV1CollectiblesRegionalPricingPreviewTargetType,
)
from ...models.roblox_item_configuration_api_get_regionalpricing_preview_response import (
    RobloxItemConfigurationApiGetRegionalpricingPreviewResponse,
)


def _get_kwargs(
    *,
    target_type: GetV1CollectiblesRegionalPricingPreviewTargetType,
    target_id: int,
    publishing_type: GetV1CollectiblesRegionalPricingPreviewPublishingType,
    minimum_price: int,
    price_offset: int,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_target_type = target_type.value
    params["TargetType"] = json_target_type

    params["TargetId"] = target_id

    json_publishing_type = publishing_type.value
    params["PublishingType"] = json_publishing_type

    params["MinimumPrice"] = minimum_price

    params["PriceOffset"] = price_offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://itemconfiguration.roblox.com/v1/collectibles/regional-pricing/preview",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxItemConfigurationApiGetRegionalpricingPreviewResponse | None:
    if response.status_code == 200:
        response_200 = RobloxItemConfigurationApiGetRegionalpricingPreviewResponse.from_dict(response.json())

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
) -> Response[Any | RobloxItemConfigurationApiGetRegionalpricingPreviewResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    target_type: GetV1CollectiblesRegionalPricingPreviewTargetType,
    target_id: int,
    publishing_type: GetV1CollectiblesRegionalPricingPreviewPublishingType,
    minimum_price: int,
    price_offset: int,
) -> Response[Any | RobloxItemConfigurationApiGetRegionalpricingPreviewResponse]:
    """Get the preview for regional prices.

    Args:
        target_type (GetV1CollectiblesRegionalPricingPreviewTargetType):
        target_id (int):
        publishing_type (GetV1CollectiblesRegionalPricingPreviewPublishingType):
        minimum_price (int):
        price_offset (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxItemConfigurationApiGetRegionalpricingPreviewResponse]
    """

    kwargs = _get_kwargs(
        target_type=target_type,
        target_id=target_id,
        publishing_type=publishing_type,
        minimum_price=minimum_price,
        price_offset=price_offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    target_type: GetV1CollectiblesRegionalPricingPreviewTargetType,
    target_id: int,
    publishing_type: GetV1CollectiblesRegionalPricingPreviewPublishingType,
    minimum_price: int,
    price_offset: int,
) -> Any | RobloxItemConfigurationApiGetRegionalpricingPreviewResponse | None:
    """Get the preview for regional prices.

    Args:
        target_type (GetV1CollectiblesRegionalPricingPreviewTargetType):
        target_id (int):
        publishing_type (GetV1CollectiblesRegionalPricingPreviewPublishingType):
        minimum_price (int):
        price_offset (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxItemConfigurationApiGetRegionalpricingPreviewResponse
    """

    return sync_detailed(
        client=client,
        target_type=target_type,
        target_id=target_id,
        publishing_type=publishing_type,
        minimum_price=minimum_price,
        price_offset=price_offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    target_type: GetV1CollectiblesRegionalPricingPreviewTargetType,
    target_id: int,
    publishing_type: GetV1CollectiblesRegionalPricingPreviewPublishingType,
    minimum_price: int,
    price_offset: int,
) -> Response[Any | RobloxItemConfigurationApiGetRegionalpricingPreviewResponse]:
    """Get the preview for regional prices.

    Args:
        target_type (GetV1CollectiblesRegionalPricingPreviewTargetType):
        target_id (int):
        publishing_type (GetV1CollectiblesRegionalPricingPreviewPublishingType):
        minimum_price (int):
        price_offset (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxItemConfigurationApiGetRegionalpricingPreviewResponse]
    """

    kwargs = _get_kwargs(
        target_type=target_type,
        target_id=target_id,
        publishing_type=publishing_type,
        minimum_price=minimum_price,
        price_offset=price_offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    target_type: GetV1CollectiblesRegionalPricingPreviewTargetType,
    target_id: int,
    publishing_type: GetV1CollectiblesRegionalPricingPreviewPublishingType,
    minimum_price: int,
    price_offset: int,
) -> Any | RobloxItemConfigurationApiGetRegionalpricingPreviewResponse | None:
    """Get the preview for regional prices.

    Args:
        target_type (GetV1CollectiblesRegionalPricingPreviewTargetType):
        target_id (int):
        publishing_type (GetV1CollectiblesRegionalPricingPreviewPublishingType):
        minimum_price (int):
        price_offset (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxItemConfigurationApiGetRegionalpricingPreviewResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            target_type=target_type,
            target_id=target_id,
            publishing_type=publishing_type,
            minimum_price=minimum_price,
            price_offset=price_offset,
        )
    ).parsed
