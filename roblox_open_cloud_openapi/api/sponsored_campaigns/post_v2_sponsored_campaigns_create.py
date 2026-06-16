from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_ad_configuration_api_models_create_sponsored_campaign_request import (
    RobloxAdConfigurationApiModelsCreateSponsoredCampaignRequest,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: RobloxAdConfigurationApiModelsCreateSponsoredCampaignRequest
    | RobloxAdConfigurationApiModelsCreateSponsoredCampaignRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/sponsored-campaigns/create",
    }

    if isinstance(body, RobloxAdConfigurationApiModelsCreateSponsoredCampaignRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxAdConfigurationApiModelsCreateSponsoredCampaignRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | int | None:
    if response.status_code == 200:
        response_200 = cast(int, response.json())
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

    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | int]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxAdConfigurationApiModelsCreateSponsoredCampaignRequest
    | RobloxAdConfigurationApiModelsCreateSponsoredCampaignRequest
    | Unset = UNSET,
) -> Response[Any | int]:
    """Creates a complete ad. Including ad campaign, ad set, escrow, and the ad.
    Currently intended for creation of sponsorships only.

    Args:
        body (RobloxAdConfigurationApiModelsCreateSponsoredCampaignRequest): A request model for
            creating a sponsored game
        body (RobloxAdConfigurationApiModelsCreateSponsoredCampaignRequest): A request model for
            creating a sponsored game

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | int]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: RobloxAdConfigurationApiModelsCreateSponsoredCampaignRequest
    | RobloxAdConfigurationApiModelsCreateSponsoredCampaignRequest
    | Unset = UNSET,
) -> Any | int | None:
    """Creates a complete ad. Including ad campaign, ad set, escrow, and the ad.
    Currently intended for creation of sponsorships only.

    Args:
        body (RobloxAdConfigurationApiModelsCreateSponsoredCampaignRequest): A request model for
            creating a sponsored game
        body (RobloxAdConfigurationApiModelsCreateSponsoredCampaignRequest): A request model for
            creating a sponsored game

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | int
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxAdConfigurationApiModelsCreateSponsoredCampaignRequest
    | RobloxAdConfigurationApiModelsCreateSponsoredCampaignRequest
    | Unset = UNSET,
) -> Response[Any | int]:
    """Creates a complete ad. Including ad campaign, ad set, escrow, and the ad.
    Currently intended for creation of sponsorships only.

    Args:
        body (RobloxAdConfigurationApiModelsCreateSponsoredCampaignRequest): A request model for
            creating a sponsored game
        body (RobloxAdConfigurationApiModelsCreateSponsoredCampaignRequest): A request model for
            creating a sponsored game

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | int]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RobloxAdConfigurationApiModelsCreateSponsoredCampaignRequest
    | RobloxAdConfigurationApiModelsCreateSponsoredCampaignRequest
    | Unset = UNSET,
) -> Any | int | None:
    """Creates a complete ad. Including ad campaign, ad set, escrow, and the ad.
    Currently intended for creation of sponsorships only.

    Args:
        body (RobloxAdConfigurationApiModelsCreateSponsoredCampaignRequest): A request model for
            creating a sponsored game
        body (RobloxAdConfigurationApiModelsCreateSponsoredCampaignRequest): A request model for
            creating a sponsored game

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | int
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
