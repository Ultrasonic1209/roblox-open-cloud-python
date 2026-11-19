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
{'x-roblox-stability': 'EXPERIMENTAL', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'MINUTE', 'maxInPeriod': 120}, 'perOauth2Authorization': {'period': 'MINUTE', 'maxInPeriod': 120}}, 'x-roblox-scopes': [{'name': 'ad.campaign:read'}], 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.error_envelope import ErrorEnvelope
from ...models.list_campaign_ads_response import ListCampaignAdsResponse
from ...types import Unset


def _get_kwargs(
    campaign_id: str,
    *,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["maxPageSize"] = max_page_size

    params["pageToken"] = page_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/ads-management/v1/campaigns/{campaign_id}/ads".format(
            campaign_id=quote(str(campaign_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorEnvelope | ListCampaignAdsResponse | None:
    if response.status_code == 200:
        response_200 = ListCampaignAdsResponse.from_dict(response.json())

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
) -> Response[ErrorEnvelope | ListCampaignAdsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    campaign_id: str,
    *,
    client: AuthenticatedClient,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> Response[ErrorEnvelope | ListCampaignAdsResponse]:
    """List a campaign's ads

     Lists every ad the campaign has had, one per creative, including PAUSED and REMOVED ads, in creation
    order (oldest first). id matches the ad ID reported by analytics-query-api.

    Args:
        campaign_id (str):
        max_page_size (int | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | ListCampaignAdsResponse]
    """

    kwargs = _get_kwargs(
        campaign_id=campaign_id,
        max_page_size=max_page_size,
        page_token=page_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    campaign_id: str,
    *,
    client: AuthenticatedClient,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> ErrorEnvelope | ListCampaignAdsResponse | None:
    """List a campaign's ads

     Lists every ad the campaign has had, one per creative, including PAUSED and REMOVED ads, in creation
    order (oldest first). id matches the ad ID reported by analytics-query-api.

    Args:
        campaign_id (str):
        max_page_size (int | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | ListCampaignAdsResponse
    """

    return sync_detailed(
        campaign_id=campaign_id,
        client=client,
        max_page_size=max_page_size,
        page_token=page_token,
    ).parsed


async def asyncio_detailed(
    campaign_id: str,
    *,
    client: AuthenticatedClient,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> Response[ErrorEnvelope | ListCampaignAdsResponse]:
    """List a campaign's ads

     Lists every ad the campaign has had, one per creative, including PAUSED and REMOVED ads, in creation
    order (oldest first). id matches the ad ID reported by analytics-query-api.

    Args:
        campaign_id (str):
        max_page_size (int | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | ListCampaignAdsResponse]
    """

    kwargs = _get_kwargs(
        campaign_id=campaign_id,
        max_page_size=max_page_size,
        page_token=page_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    campaign_id: str,
    *,
    client: AuthenticatedClient,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> ErrorEnvelope | ListCampaignAdsResponse | None:
    """List a campaign's ads

     Lists every ad the campaign has had, one per creative, including PAUSED and REMOVED ads, in creation
    order (oldest first). id matches the ad ID reported by analytics-query-api.

    Args:
        campaign_id (str):
        max_page_size (int | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | ListCampaignAdsResponse
    """

    return (
        await asyncio_detailed(
            campaign_id=campaign_id,
            client=client,
            max_page_size=max_page_size,
            page_token=page_token,
        )
    ).parsed
