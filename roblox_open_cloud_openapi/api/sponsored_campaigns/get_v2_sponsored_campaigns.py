from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v2_sponsored_campaigns_campaign_target_type import GetV2SponsoredCampaignsCampaignTargetType
from ...models.roblox_ad_configuration_api_get_sponsored_campaigns_response import (
    RobloxAdConfigurationApiGetSponsoredCampaignsResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    campaign_target_type: GetV2SponsoredCampaignsCampaignTargetType,
    campaign_target_id: int,
    include_reporting_stats: bool | Unset = False,
    is_archived: bool | Unset = False,
    page_cursor: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_campaign_target_type = campaign_target_type.value
    params["campaignTargetType"] = json_campaign_target_type

    params["campaignTargetId"] = campaign_target_id

    params["includeReportingStats"] = include_reporting_stats

    params["isArchived"] = is_archived

    params["pageCursor"] = page_cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://adconfiguration.roblox.com/v2/sponsored-campaigns",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxAdConfigurationApiGetSponsoredCampaignsResponse | None:
    if response.status_code == 200:
        response_200 = RobloxAdConfigurationApiGetSponsoredCampaignsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxAdConfigurationApiGetSponsoredCampaignsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    campaign_target_type: GetV2SponsoredCampaignsCampaignTargetType,
    campaign_target_id: int,
    include_reporting_stats: bool | Unset = False,
    is_archived: bool | Unset = False,
    page_cursor: str | Unset = UNSET,
) -> Response[Any | RobloxAdConfigurationApiGetSponsoredCampaignsResponse]:
    """Gets a page of Roblox.AdConfiguration.Api.SponsoredCampaignModel with specified input parameters.

    Args:
        campaign_target_type (GetV2SponsoredCampaignsCampaignTargetType):
        campaign_target_id (int):
        include_reporting_stats (bool | Unset):  Default: False.
        is_archived (bool | Unset):  Default: False.
        page_cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxAdConfigurationApiGetSponsoredCampaignsResponse]
    """

    kwargs = _get_kwargs(
        campaign_target_type=campaign_target_type,
        campaign_target_id=campaign_target_id,
        include_reporting_stats=include_reporting_stats,
        is_archived=is_archived,
        page_cursor=page_cursor,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    campaign_target_type: GetV2SponsoredCampaignsCampaignTargetType,
    campaign_target_id: int,
    include_reporting_stats: bool | Unset = False,
    is_archived: bool | Unset = False,
    page_cursor: str | Unset = UNSET,
) -> Any | RobloxAdConfigurationApiGetSponsoredCampaignsResponse | None:
    """Gets a page of Roblox.AdConfiguration.Api.SponsoredCampaignModel with specified input parameters.

    Args:
        campaign_target_type (GetV2SponsoredCampaignsCampaignTargetType):
        campaign_target_id (int):
        include_reporting_stats (bool | Unset):  Default: False.
        is_archived (bool | Unset):  Default: False.
        page_cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxAdConfigurationApiGetSponsoredCampaignsResponse
    """

    return sync_detailed(
        client=client,
        campaign_target_type=campaign_target_type,
        campaign_target_id=campaign_target_id,
        include_reporting_stats=include_reporting_stats,
        is_archived=is_archived,
        page_cursor=page_cursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    campaign_target_type: GetV2SponsoredCampaignsCampaignTargetType,
    campaign_target_id: int,
    include_reporting_stats: bool | Unset = False,
    is_archived: bool | Unset = False,
    page_cursor: str | Unset = UNSET,
) -> Response[Any | RobloxAdConfigurationApiGetSponsoredCampaignsResponse]:
    """Gets a page of Roblox.AdConfiguration.Api.SponsoredCampaignModel with specified input parameters.

    Args:
        campaign_target_type (GetV2SponsoredCampaignsCampaignTargetType):
        campaign_target_id (int):
        include_reporting_stats (bool | Unset):  Default: False.
        is_archived (bool | Unset):  Default: False.
        page_cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxAdConfigurationApiGetSponsoredCampaignsResponse]
    """

    kwargs = _get_kwargs(
        campaign_target_type=campaign_target_type,
        campaign_target_id=campaign_target_id,
        include_reporting_stats=include_reporting_stats,
        is_archived=is_archived,
        page_cursor=page_cursor,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    campaign_target_type: GetV2SponsoredCampaignsCampaignTargetType,
    campaign_target_id: int,
    include_reporting_stats: bool | Unset = False,
    is_archived: bool | Unset = False,
    page_cursor: str | Unset = UNSET,
) -> Any | RobloxAdConfigurationApiGetSponsoredCampaignsResponse | None:
    """Gets a page of Roblox.AdConfiguration.Api.SponsoredCampaignModel with specified input parameters.

    Args:
        campaign_target_type (GetV2SponsoredCampaignsCampaignTargetType):
        campaign_target_id (int):
        include_reporting_stats (bool | Unset):  Default: False.
        is_archived (bool | Unset):  Default: False.
        page_cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxAdConfigurationApiGetSponsoredCampaignsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            campaign_target_type=campaign_target_type,
            campaign_target_id=campaign_target_id,
            include_reporting_stats=include_reporting_stats,
            is_archived=is_archived,
            page_cursor=page_cursor,
        )
    ).parsed
