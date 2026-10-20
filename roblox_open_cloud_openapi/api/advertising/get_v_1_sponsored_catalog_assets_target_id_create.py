from http import HTTPStatus
from typing import TYPE_CHECKING, Any, cast
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
{'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.roblox_ads_api_models_response_create_sponsored_item_campaign_response import (
    RobloxAdsApiModelsResponseCreateSponsoredItemCampaignResponse,
)


def _get_kwargs(
    target_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://ads.roblox.com/v1/sponsored/catalog-assets/{target_id}/create".format(
            target_id=quote(str(target_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxAdsApiModelsResponseCreateSponsoredItemCampaignResponse | None:
    if response.status_code == 200:
        response_200 = RobloxAdsApiModelsResponseCreateSponsoredItemCampaignResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RobloxAdsApiModelsResponseCreateSponsoredItemCampaignResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    target_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxAdsApiModelsResponseCreateSponsoredItemCampaignResponse]:
    """Returns the asset information for creating a new sponsored campaign.

    Args:
        target_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxAdsApiModelsResponseCreateSponsoredItemCampaignResponse]
    """

    kwargs = _get_kwargs(
        target_id=target_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    target_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxAdsApiModelsResponseCreateSponsoredItemCampaignResponse | None:
    """Returns the asset information for creating a new sponsored campaign.

    Args:
        target_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxAdsApiModelsResponseCreateSponsoredItemCampaignResponse
    """

    return sync_detailed(
        target_id=target_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    target_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxAdsApiModelsResponseCreateSponsoredItemCampaignResponse]:
    """Returns the asset information for creating a new sponsored campaign.

    Args:
        target_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxAdsApiModelsResponseCreateSponsoredItemCampaignResponse]
    """

    kwargs = _get_kwargs(
        target_id=target_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    target_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxAdsApiModelsResponseCreateSponsoredItemCampaignResponse | None:
    """Returns the asset information for creating a new sponsored campaign.

    Args:
        target_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxAdsApiModelsResponseCreateSponsoredItemCampaignResponse
    """

    return (
        await asyncio_detailed(
            target_id=target_id,
            client=client,
        )
    ).parsed
