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


from ...models.get_v1_collectibles_revenue_split_collectible_item_type import (
    GetV1CollectiblesRevenueSplitCollectibleItemType,
)
from ...models.get_v1_collectibles_revenue_split_purchase_platform import GetV1CollectiblesRevenueSplitPurchasePlatform
from ...models.get_v1_collectibles_revenue_split_target_type import GetV1CollectiblesRevenueSplitTargetType
from ...models.roblox_item_configuration_api_models_request_collectibles_revenue_split_response import (
    RobloxItemConfigurationApiModelsRequestCollectiblesRevenueSplitResponse,
)


def _get_kwargs(
    *,
    target_type: GetV1CollectiblesRevenueSplitTargetType,
    target_id: str,
    collectible_item_type: GetV1CollectiblesRevenueSplitCollectibleItemType,
    minimum_price: int,
    price_offset: int,
    purchase_platform: GetV1CollectiblesRevenueSplitPurchasePlatform,
    license_id: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_target_type = target_type.value
    params["TargetType"] = json_target_type

    params["TargetID"] = target_id

    json_collectible_item_type = collectible_item_type.value
    params["CollectibleItemType"] = json_collectible_item_type

    params["MinimumPrice"] = minimum_price

    params["PriceOffset"] = price_offset

    json_purchase_platform = purchase_platform.value
    params["PurchasePlatform"] = json_purchase_platform

    params["LicenseId"] = license_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://itemconfiguration.roblox.com/v1/collectibles/revenue-split",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxItemConfigurationApiModelsRequestCollectiblesRevenueSplitResponse | None:
    if response.status_code == 200:
        response_200 = RobloxItemConfigurationApiModelsRequestCollectiblesRevenueSplitResponse.from_dict(
            response.json()
        )

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
) -> Response[Any | RobloxItemConfigurationApiModelsRequestCollectiblesRevenueSplitResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    target_type: GetV1CollectiblesRevenueSplitTargetType,
    target_id: str,
    collectible_item_type: GetV1CollectiblesRevenueSplitCollectibleItemType,
    minimum_price: int,
    price_offset: int,
    purchase_platform: GetV1CollectiblesRevenueSplitPurchasePlatform,
    license_id: str,
) -> Response[Any | RobloxItemConfigurationApiModelsRequestCollectiblesRevenueSplitResponse]:
    """Get Revenue Split for collectibles.

    Args:
        target_type (GetV1CollectiblesRevenueSplitTargetType):
        target_id (str):
        collectible_item_type (GetV1CollectiblesRevenueSplitCollectibleItemType):
        minimum_price (int):
        price_offset (int):
        purchase_platform (GetV1CollectiblesRevenueSplitPurchasePlatform):
        license_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxItemConfigurationApiModelsRequestCollectiblesRevenueSplitResponse]
    """

    kwargs = _get_kwargs(
        target_type=target_type,
        target_id=target_id,
        collectible_item_type=collectible_item_type,
        minimum_price=minimum_price,
        price_offset=price_offset,
        purchase_platform=purchase_platform,
        license_id=license_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    target_type: GetV1CollectiblesRevenueSplitTargetType,
    target_id: str,
    collectible_item_type: GetV1CollectiblesRevenueSplitCollectibleItemType,
    minimum_price: int,
    price_offset: int,
    purchase_platform: GetV1CollectiblesRevenueSplitPurchasePlatform,
    license_id: str,
) -> Any | RobloxItemConfigurationApiModelsRequestCollectiblesRevenueSplitResponse | None:
    """Get Revenue Split for collectibles.

    Args:
        target_type (GetV1CollectiblesRevenueSplitTargetType):
        target_id (str):
        collectible_item_type (GetV1CollectiblesRevenueSplitCollectibleItemType):
        minimum_price (int):
        price_offset (int):
        purchase_platform (GetV1CollectiblesRevenueSplitPurchasePlatform):
        license_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxItemConfigurationApiModelsRequestCollectiblesRevenueSplitResponse
    """

    return sync_detailed(
        client=client,
        target_type=target_type,
        target_id=target_id,
        collectible_item_type=collectible_item_type,
        minimum_price=minimum_price,
        price_offset=price_offset,
        purchase_platform=purchase_platform,
        license_id=license_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    target_type: GetV1CollectiblesRevenueSplitTargetType,
    target_id: str,
    collectible_item_type: GetV1CollectiblesRevenueSplitCollectibleItemType,
    minimum_price: int,
    price_offset: int,
    purchase_platform: GetV1CollectiblesRevenueSplitPurchasePlatform,
    license_id: str,
) -> Response[Any | RobloxItemConfigurationApiModelsRequestCollectiblesRevenueSplitResponse]:
    """Get Revenue Split for collectibles.

    Args:
        target_type (GetV1CollectiblesRevenueSplitTargetType):
        target_id (str):
        collectible_item_type (GetV1CollectiblesRevenueSplitCollectibleItemType):
        minimum_price (int):
        price_offset (int):
        purchase_platform (GetV1CollectiblesRevenueSplitPurchasePlatform):
        license_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxItemConfigurationApiModelsRequestCollectiblesRevenueSplitResponse]
    """

    kwargs = _get_kwargs(
        target_type=target_type,
        target_id=target_id,
        collectible_item_type=collectible_item_type,
        minimum_price=minimum_price,
        price_offset=price_offset,
        purchase_platform=purchase_platform,
        license_id=license_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    target_type: GetV1CollectiblesRevenueSplitTargetType,
    target_id: str,
    collectible_item_type: GetV1CollectiblesRevenueSplitCollectibleItemType,
    minimum_price: int,
    price_offset: int,
    purchase_platform: GetV1CollectiblesRevenueSplitPurchasePlatform,
    license_id: str,
) -> Any | RobloxItemConfigurationApiModelsRequestCollectiblesRevenueSplitResponse | None:
    """Get Revenue Split for collectibles.

    Args:
        target_type (GetV1CollectiblesRevenueSplitTargetType):
        target_id (str):
        collectible_item_type (GetV1CollectiblesRevenueSplitCollectibleItemType):
        minimum_price (int):
        price_offset (int):
        purchase_platform (GetV1CollectiblesRevenueSplitPurchasePlatform):
        license_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxItemConfigurationApiModelsRequestCollectiblesRevenueSplitResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            target_type=target_type,
            target_id=target_id,
            collectible_item_type=collectible_item_type,
            minimum_price=minimum_price,
            price_offset=price_offset,
            purchase_platform=purchase_platform,
            license_id=license_id,
        )
    ).parsed
