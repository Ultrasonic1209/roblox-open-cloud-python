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


from ...models.get_v1_collectibles_publishing_fees_publishing_type import GetV1CollectiblesPublishingFeesPublishingType
from ...models.get_v1_collectibles_publishing_fees_resale_restriction import (
    GetV1CollectiblesPublishingFeesResaleRestriction,
)
from ...models.get_v1_collectibles_publishing_fees_sale_location import GetV1CollectiblesPublishingFeesSaleLocation
from ...models.get_v1_collectibles_publishing_fees_target_type import GetV1CollectiblesPublishingFeesTargetType
from ...models.roblox_item_configuration_api_publishing_fee_response import (
    RobloxItemConfigurationApiPublishingFeeResponse,
)


def _get_kwargs(
    *,
    target_type: GetV1CollectiblesPublishingFeesTargetType,
    target_id: int,
    quantity: int,
    sale_location: GetV1CollectiblesPublishingFeesSaleLocation,
    resale_restriction: GetV1CollectiblesPublishingFeesResaleRestriction,
    is_free: bool,
    publishing_type: GetV1CollectiblesPublishingFeesPublishingType,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_target_type = target_type.value
    params["TargetType"] = json_target_type

    params["TargetID"] = target_id

    params["Quantity"] = quantity

    json_sale_location = sale_location.value
    params["SaleLocation"] = json_sale_location

    json_resale_restriction = resale_restriction.value
    params["ResaleRestriction"] = json_resale_restriction

    params["IsFree"] = is_free

    json_publishing_type = publishing_type.value
    params["PublishingType"] = json_publishing_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://itemconfiguration.roblox.com/v1/collectibles/publishing-fees",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxItemConfigurationApiPublishingFeeResponse | None:
    if response.status_code == 200:
        response_200 = RobloxItemConfigurationApiPublishingFeeResponse.from_dict(response.json())

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
) -> Response[Any | RobloxItemConfigurationApiPublishingFeeResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    target_type: GetV1CollectiblesPublishingFeesTargetType,
    target_id: int,
    quantity: int,
    sale_location: GetV1CollectiblesPublishingFeesSaleLocation,
    resale_restriction: GetV1CollectiblesPublishingFeesResaleRestriction,
    is_free: bool,
    publishing_type: GetV1CollectiblesPublishingFeesPublishingType,
) -> Response[Any | RobloxItemConfigurationApiPublishingFeeResponse]:
    """Gets the publishing fee required to publish a collectible item.

    Args:
        target_type (GetV1CollectiblesPublishingFeesTargetType):
        target_id (int):
        quantity (int):
        sale_location (GetV1CollectiblesPublishingFeesSaleLocation):
        resale_restriction (GetV1CollectiblesPublishingFeesResaleRestriction):
        is_free (bool):
        publishing_type (GetV1CollectiblesPublishingFeesPublishingType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxItemConfigurationApiPublishingFeeResponse]
    """

    kwargs = _get_kwargs(
        target_type=target_type,
        target_id=target_id,
        quantity=quantity,
        sale_location=sale_location,
        resale_restriction=resale_restriction,
        is_free=is_free,
        publishing_type=publishing_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    target_type: GetV1CollectiblesPublishingFeesTargetType,
    target_id: int,
    quantity: int,
    sale_location: GetV1CollectiblesPublishingFeesSaleLocation,
    resale_restriction: GetV1CollectiblesPublishingFeesResaleRestriction,
    is_free: bool,
    publishing_type: GetV1CollectiblesPublishingFeesPublishingType,
) -> Any | RobloxItemConfigurationApiPublishingFeeResponse | None:
    """Gets the publishing fee required to publish a collectible item.

    Args:
        target_type (GetV1CollectiblesPublishingFeesTargetType):
        target_id (int):
        quantity (int):
        sale_location (GetV1CollectiblesPublishingFeesSaleLocation):
        resale_restriction (GetV1CollectiblesPublishingFeesResaleRestriction):
        is_free (bool):
        publishing_type (GetV1CollectiblesPublishingFeesPublishingType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxItemConfigurationApiPublishingFeeResponse
    """

    return sync_detailed(
        client=client,
        target_type=target_type,
        target_id=target_id,
        quantity=quantity,
        sale_location=sale_location,
        resale_restriction=resale_restriction,
        is_free=is_free,
        publishing_type=publishing_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    target_type: GetV1CollectiblesPublishingFeesTargetType,
    target_id: int,
    quantity: int,
    sale_location: GetV1CollectiblesPublishingFeesSaleLocation,
    resale_restriction: GetV1CollectiblesPublishingFeesResaleRestriction,
    is_free: bool,
    publishing_type: GetV1CollectiblesPublishingFeesPublishingType,
) -> Response[Any | RobloxItemConfigurationApiPublishingFeeResponse]:
    """Gets the publishing fee required to publish a collectible item.

    Args:
        target_type (GetV1CollectiblesPublishingFeesTargetType):
        target_id (int):
        quantity (int):
        sale_location (GetV1CollectiblesPublishingFeesSaleLocation):
        resale_restriction (GetV1CollectiblesPublishingFeesResaleRestriction):
        is_free (bool):
        publishing_type (GetV1CollectiblesPublishingFeesPublishingType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxItemConfigurationApiPublishingFeeResponse]
    """

    kwargs = _get_kwargs(
        target_type=target_type,
        target_id=target_id,
        quantity=quantity,
        sale_location=sale_location,
        resale_restriction=resale_restriction,
        is_free=is_free,
        publishing_type=publishing_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    target_type: GetV1CollectiblesPublishingFeesTargetType,
    target_id: int,
    quantity: int,
    sale_location: GetV1CollectiblesPublishingFeesSaleLocation,
    resale_restriction: GetV1CollectiblesPublishingFeesResaleRestriction,
    is_free: bool,
    publishing_type: GetV1CollectiblesPublishingFeesPublishingType,
) -> Any | RobloxItemConfigurationApiPublishingFeeResponse | None:
    """Gets the publishing fee required to publish a collectible item.

    Args:
        target_type (GetV1CollectiblesPublishingFeesTargetType):
        target_id (int):
        quantity (int):
        sale_location (GetV1CollectiblesPublishingFeesSaleLocation):
        resale_restriction (GetV1CollectiblesPublishingFeesResaleRestriction):
        is_free (bool):
        publishing_type (GetV1CollectiblesPublishingFeesPublishingType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxItemConfigurationApiPublishingFeeResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            target_type=target_type,
            target_id=target_id,
            quantity=quantity,
            sale_location=sale_location,
            resale_restriction=resale_restriction,
            is_free=is_free,
            publishing_type=publishing_type,
        )
    ).parsed
