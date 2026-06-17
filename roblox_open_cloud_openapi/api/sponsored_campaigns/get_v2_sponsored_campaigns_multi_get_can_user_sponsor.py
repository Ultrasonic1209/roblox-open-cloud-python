from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v2_sponsored_campaigns_multi_get_can_user_sponsor_campaign_target_type import (
    GetV2SponsoredCampaignsMultiGetCanUserSponsorCampaignTargetType,
)
from ...models.get_v2_sponsored_campaigns_multi_get_can_user_sponsor_response_200 import (
    GetV2SponsoredCampaignsMultiGetCanUserSponsorResponse200,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    campaign_target_type: GetV2SponsoredCampaignsMultiGetCanUserSponsorCampaignTargetType,
    campaign_target_ids: list[int],
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_campaign_target_type = campaign_target_type.value
    params["campaignTargetType"] = json_campaign_target_type

    json_campaign_target_ids = campaign_target_ids

    params["campaignTargetIds"] = json_campaign_target_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://adconfiguration.roblox.com/v2/sponsored-campaigns/multi-get-can-user-sponsor",
        "params": params,
        "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
        "openapi-id": "get_v2_sponsored-campaigns_multi-get-can-user-sponsor",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | GetV2SponsoredCampaignsMultiGetCanUserSponsorResponse200 | None:
    if response.status_code == 200:
        response_200 = GetV2SponsoredCampaignsMultiGetCanUserSponsorResponse200.from_dict(response.json())

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

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | GetV2SponsoredCampaignsMultiGetCanUserSponsorResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    campaign_target_type: GetV2SponsoredCampaignsMultiGetCanUserSponsorCampaignTargetType,
    campaign_target_ids: list[int],
) -> Response[Any | GetV2SponsoredCampaignsMultiGetCanUserSponsorResponse200]:
    """Checks whether the targets are eligible for sponsorship, and
    if the user is authorized to sponsor the targets.

    Args:
        campaign_target_type (GetV2SponsoredCampaignsMultiGetCanUserSponsorCampaignTargetType):
        campaign_target_ids (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetV2SponsoredCampaignsMultiGetCanUserSponsorResponse200]
    """

    kwargs = _get_kwargs(
        campaign_target_type=campaign_target_type,
        campaign_target_ids=campaign_target_ids,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    campaign_target_type: GetV2SponsoredCampaignsMultiGetCanUserSponsorCampaignTargetType,
    campaign_target_ids: list[int],
) -> Any | GetV2SponsoredCampaignsMultiGetCanUserSponsorResponse200 | None:
    """Checks whether the targets are eligible for sponsorship, and
    if the user is authorized to sponsor the targets.

    Args:
        campaign_target_type (GetV2SponsoredCampaignsMultiGetCanUserSponsorCampaignTargetType):
        campaign_target_ids (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetV2SponsoredCampaignsMultiGetCanUserSponsorResponse200
    """

    return sync_detailed(
        client=client,
        campaign_target_type=campaign_target_type,
        campaign_target_ids=campaign_target_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    campaign_target_type: GetV2SponsoredCampaignsMultiGetCanUserSponsorCampaignTargetType,
    campaign_target_ids: list[int],
) -> Response[Any | GetV2SponsoredCampaignsMultiGetCanUserSponsorResponse200]:
    """Checks whether the targets are eligible for sponsorship, and
    if the user is authorized to sponsor the targets.

    Args:
        campaign_target_type (GetV2SponsoredCampaignsMultiGetCanUserSponsorCampaignTargetType):
        campaign_target_ids (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetV2SponsoredCampaignsMultiGetCanUserSponsorResponse200]
    """

    kwargs = _get_kwargs(
        campaign_target_type=campaign_target_type,
        campaign_target_ids=campaign_target_ids,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    campaign_target_type: GetV2SponsoredCampaignsMultiGetCanUserSponsorCampaignTargetType,
    campaign_target_ids: list[int],
) -> Any | GetV2SponsoredCampaignsMultiGetCanUserSponsorResponse200 | None:
    """Checks whether the targets are eligible for sponsorship, and
    if the user is authorized to sponsor the targets.

    Args:
        campaign_target_type (GetV2SponsoredCampaignsMultiGetCanUserSponsorCampaignTargetType):
        campaign_target_ids (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetV2SponsoredCampaignsMultiGetCanUserSponsorResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            campaign_target_type=campaign_target_type,
            campaign_target_ids=campaign_target_ids,
        )
    ).parsed
