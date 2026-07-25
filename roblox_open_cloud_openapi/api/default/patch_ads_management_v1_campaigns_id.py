from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.internal_public_v1_error_envelope import InternalPublicV1ErrorEnvelope
from ...models.internal_public_v1_update_campaign_request import InternalPublicV1UpdateCampaignRequest
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: InternalPublicV1UpdateCampaignRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/ads-management/v1/campaigns/{id}".format(
            id=quote(str(id), safe=""),
        ),
        "extensions": {
            "openapi-extensions": {
                "x-roblox-stability": "EXPERIMENTAL",
                "x-roblox-rate-limits": {
                    "perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 60},
                    "perOauth2Authorization": {"period": "MINUTE", "maxInPeriod": 60},
                },
                "x-roblox-scopes": [{"name": "ad.campaign:write", "targetResourceSpecifier": ""}],
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            },
            "openapi-id": "patch_ads-management_v1_campaigns_id",
        },
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> InternalPublicV1ErrorEnvelope | None:
    if response.status_code == 400:
        response_400 = InternalPublicV1ErrorEnvelope.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = InternalPublicV1ErrorEnvelope.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = InternalPublicV1ErrorEnvelope.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = InternalPublicV1ErrorEnvelope.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = InternalPublicV1ErrorEnvelope.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[InternalPublicV1ErrorEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: InternalPublicV1UpdateCampaignRequest,
) -> Response[InternalPublicV1ErrorEnvelope]:
    """Update a campaign

     Updates the mutable fields of a campaign. You can change: name, budget.amountMicros,
    schedule.startTime and schedule.durationInDays (schedule changes are only allowed before the
    campaign starts), and status. Set status to ACTIVE to run or resume the campaign, PAUSED to pause
    it, or CANCELLED to cancel it permanently. budget.type cannot be changed — only the amount. A budget
    increase takes effect immediately, but a budget decrease on a running campaign is scheduled for the
    next midnight in the account's time zone; while a decrease is pending, the response reports it in
    budget.scheduledAmountMicros and budget.scheduledEffectiveTime. The fields objective, paymentType,
    targeting, creativeAssetIds, and bid are fixed after creation and return 400 if included. The
    updated campaign is returned with its recomputed deliveryStatus.

    Args:
        id (str):
        body (InternalPublicV1UpdateCampaignRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalPublicV1ErrorEnvelope]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: InternalPublicV1UpdateCampaignRequest,
) -> InternalPublicV1ErrorEnvelope | None:
    """Update a campaign

     Updates the mutable fields of a campaign. You can change: name, budget.amountMicros,
    schedule.startTime and schedule.durationInDays (schedule changes are only allowed before the
    campaign starts), and status. Set status to ACTIVE to run or resume the campaign, PAUSED to pause
    it, or CANCELLED to cancel it permanently. budget.type cannot be changed — only the amount. A budget
    increase takes effect immediately, but a budget decrease on a running campaign is scheduled for the
    next midnight in the account's time zone; while a decrease is pending, the response reports it in
    budget.scheduledAmountMicros and budget.scheduledEffectiveTime. The fields objective, paymentType,
    targeting, creativeAssetIds, and bid are fixed after creation and return 400 if included. The
    updated campaign is returned with its recomputed deliveryStatus.

    Args:
        id (str):
        body (InternalPublicV1UpdateCampaignRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalPublicV1ErrorEnvelope
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: InternalPublicV1UpdateCampaignRequest,
) -> Response[InternalPublicV1ErrorEnvelope]:
    """Update a campaign

     Updates the mutable fields of a campaign. You can change: name, budget.amountMicros,
    schedule.startTime and schedule.durationInDays (schedule changes are only allowed before the
    campaign starts), and status. Set status to ACTIVE to run or resume the campaign, PAUSED to pause
    it, or CANCELLED to cancel it permanently. budget.type cannot be changed — only the amount. A budget
    increase takes effect immediately, but a budget decrease on a running campaign is scheduled for the
    next midnight in the account's time zone; while a decrease is pending, the response reports it in
    budget.scheduledAmountMicros and budget.scheduledEffectiveTime. The fields objective, paymentType,
    targeting, creativeAssetIds, and bid are fixed after creation and return 400 if included. The
    updated campaign is returned with its recomputed deliveryStatus.

    Args:
        id (str):
        body (InternalPublicV1UpdateCampaignRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalPublicV1ErrorEnvelope]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: InternalPublicV1UpdateCampaignRequest,
) -> InternalPublicV1ErrorEnvelope | None:
    """Update a campaign

     Updates the mutable fields of a campaign. You can change: name, budget.amountMicros,
    schedule.startTime and schedule.durationInDays (schedule changes are only allowed before the
    campaign starts), and status. Set status to ACTIVE to run or resume the campaign, PAUSED to pause
    it, or CANCELLED to cancel it permanently. budget.type cannot be changed — only the amount. A budget
    increase takes effect immediately, but a budget decrease on a running campaign is scheduled for the
    next midnight in the account's time zone; while a decrease is pending, the response reports it in
    budget.scheduledAmountMicros and budget.scheduledEffectiveTime. The fields objective, paymentType,
    targeting, creativeAssetIds, and bid are fixed after creation and return 400 if included. The
    updated campaign is returned with its recomputed deliveryStatus.

    Args:
        id (str):
        body (InternalPublicV1UpdateCampaignRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalPublicV1ErrorEnvelope
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
