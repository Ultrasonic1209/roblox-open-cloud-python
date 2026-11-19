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
from ...types import Response

"""
{'x-roblox-stability': 'EXPERIMENTAL', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'MINUTE', 'maxInPeriod': 600}, 'perOauth2Authorization': {'period': 'MINUTE', 'maxInPeriod': 600}}, 'x-roblox-scopes': [{'name': 'ad.campaign:read'}], 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.campaign_ad import CampaignAd
from ...models.error_envelope import ErrorEnvelope


def _get_kwargs(
    campaign_id: str,
    ad_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/ads-management/v1/campaigns/{campaign_id}/ads/{ad_id}".format(
            campaign_id=quote(str(campaign_id), safe=""),
            ad_id=quote(str(ad_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CampaignAd | ErrorEnvelope | None:
    if response.status_code == 200:
        response_200 = CampaignAd.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = ErrorEnvelope.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ErrorEnvelope.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = ErrorEnvelope.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = ErrorEnvelope.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CampaignAd | ErrorEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    campaign_id: str,
    ad_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[CampaignAd | ErrorEnvelope]:
    """Get one ad

     Returns one ad in a campaign. Returns 404 if the campaign or ad does not exist, the caller cannot
    manage the campaign, or adId does not belong to campaignId.

    Args:
        campaign_id (str):
        ad_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CampaignAd | ErrorEnvelope]
    """

    kwargs = _get_kwargs(
        campaign_id=campaign_id,
        ad_id=ad_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    campaign_id: str,
    ad_id: str,
    *,
    client: AuthenticatedClient,
) -> CampaignAd | ErrorEnvelope | None:
    """Get one ad

     Returns one ad in a campaign. Returns 404 if the campaign or ad does not exist, the caller cannot
    manage the campaign, or adId does not belong to campaignId.

    Args:
        campaign_id (str):
        ad_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CampaignAd | ErrorEnvelope
    """

    return sync_detailed(
        campaign_id=campaign_id,
        ad_id=ad_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    campaign_id: str,
    ad_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[CampaignAd | ErrorEnvelope]:
    """Get one ad

     Returns one ad in a campaign. Returns 404 if the campaign or ad does not exist, the caller cannot
    manage the campaign, or adId does not belong to campaignId.

    Args:
        campaign_id (str):
        ad_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CampaignAd | ErrorEnvelope]
    """

    kwargs = _get_kwargs(
        campaign_id=campaign_id,
        ad_id=ad_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    campaign_id: str,
    ad_id: str,
    *,
    client: AuthenticatedClient,
) -> CampaignAd | ErrorEnvelope | None:
    """Get one ad

     Returns one ad in a campaign. Returns 404 if the campaign or ad does not exist, the caller cannot
    manage the campaign, or adId does not belong to campaignId.

    Args:
        campaign_id (str):
        ad_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CampaignAd | ErrorEnvelope
    """

    return (
        await asyncio_detailed(
            campaign_id=campaign_id,
            ad_id=ad_id,
            client=client,
        )
    ).parsed
