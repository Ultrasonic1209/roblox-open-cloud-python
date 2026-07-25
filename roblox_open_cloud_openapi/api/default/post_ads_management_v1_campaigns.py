from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.internal_public_v1_create_campaign_request import InternalPublicV1CreateCampaignRequest
from ...models.internal_public_v1_error_envelope import InternalPublicV1ErrorEnvelope
from ...types import Response


def _get_kwargs(
    *,
    body: InternalPublicV1CreateCampaignRequest,
    x_idempotency_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["x-idempotency-key"] = x_idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/ads-management/v1/campaigns",
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
            "openapi-id": "post_ads-management_v1_campaigns",
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

    if response.status_code == 409:
        response_409 = InternalPublicV1ErrorEnvelope.from_dict(response.json())

        return response_409

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
    *,
    client: AuthenticatedClient,
    body: InternalPublicV1CreateCampaignRequest,
    x_idempotency_key: str,
) -> Response[InternalPublicV1ErrorEnvelope]:
    r"""Create a campaign

     Creates an ad campaign in the billing account. The creatives you reference must already exist as
    Open Cloud image assets that you have permission to use; they are validated and saved to your
    account's reusable creatives when the campaign is created. On success the campaign is returned with
    deliveryStatus IN_REVIEW, meaning it is queued for ad-policy review and not yet serving — poll the
    campaign (or campaigns:batchGetStatus) until this changes. budget.amountMicros is the budget in
    micro-USD as a decimal string (e.g. \"5000000\" = $5.00). It must be at least the minimum campaign
    budget; an amount below the minimum returns 400 with the required minimum stated in the error
    message. schedule.durationInDays must not exceed 3650 (~10 years). The x-idempotency-key header is
    required and must be a UUID: retrying the same key with an identical body within 24 hours returns
    the original campaign (200), while reusing a key with a different body returns 409.

    Args:
        x_idempotency_key (str):
        body (InternalPublicV1CreateCampaignRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalPublicV1ErrorEnvelope]
    """

    kwargs = _get_kwargs(
        body=body,
        x_idempotency_key=x_idempotency_key,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: InternalPublicV1CreateCampaignRequest,
    x_idempotency_key: str,
) -> InternalPublicV1ErrorEnvelope | None:
    r"""Create a campaign

     Creates an ad campaign in the billing account. The creatives you reference must already exist as
    Open Cloud image assets that you have permission to use; they are validated and saved to your
    account's reusable creatives when the campaign is created. On success the campaign is returned with
    deliveryStatus IN_REVIEW, meaning it is queued for ad-policy review and not yet serving — poll the
    campaign (or campaigns:batchGetStatus) until this changes. budget.amountMicros is the budget in
    micro-USD as a decimal string (e.g. \"5000000\" = $5.00). It must be at least the minimum campaign
    budget; an amount below the minimum returns 400 with the required minimum stated in the error
    message. schedule.durationInDays must not exceed 3650 (~10 years). The x-idempotency-key header is
    required and must be a UUID: retrying the same key with an identical body within 24 hours returns
    the original campaign (200), while reusing a key with a different body returns 409.

    Args:
        x_idempotency_key (str):
        body (InternalPublicV1CreateCampaignRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalPublicV1ErrorEnvelope
    """

    return sync_detailed(
        client=client,
        body=body,
        x_idempotency_key=x_idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: InternalPublicV1CreateCampaignRequest,
    x_idempotency_key: str,
) -> Response[InternalPublicV1ErrorEnvelope]:
    r"""Create a campaign

     Creates an ad campaign in the billing account. The creatives you reference must already exist as
    Open Cloud image assets that you have permission to use; they are validated and saved to your
    account's reusable creatives when the campaign is created. On success the campaign is returned with
    deliveryStatus IN_REVIEW, meaning it is queued for ad-policy review and not yet serving — poll the
    campaign (or campaigns:batchGetStatus) until this changes. budget.amountMicros is the budget in
    micro-USD as a decimal string (e.g. \"5000000\" = $5.00). It must be at least the minimum campaign
    budget; an amount below the minimum returns 400 with the required minimum stated in the error
    message. schedule.durationInDays must not exceed 3650 (~10 years). The x-idempotency-key header is
    required and must be a UUID: retrying the same key with an identical body within 24 hours returns
    the original campaign (200), while reusing a key with a different body returns 409.

    Args:
        x_idempotency_key (str):
        body (InternalPublicV1CreateCampaignRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalPublicV1ErrorEnvelope]
    """

    kwargs = _get_kwargs(
        body=body,
        x_idempotency_key=x_idempotency_key,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: InternalPublicV1CreateCampaignRequest,
    x_idempotency_key: str,
) -> InternalPublicV1ErrorEnvelope | None:
    r"""Create a campaign

     Creates an ad campaign in the billing account. The creatives you reference must already exist as
    Open Cloud image assets that you have permission to use; they are validated and saved to your
    account's reusable creatives when the campaign is created. On success the campaign is returned with
    deliveryStatus IN_REVIEW, meaning it is queued for ad-policy review and not yet serving — poll the
    campaign (or campaigns:batchGetStatus) until this changes. budget.amountMicros is the budget in
    micro-USD as a decimal string (e.g. \"5000000\" = $5.00). It must be at least the minimum campaign
    budget; an amount below the minimum returns 400 with the required minimum stated in the error
    message. schedule.durationInDays must not exceed 3650 (~10 years). The x-idempotency-key header is
    required and must be a UUID: retrying the same key with an identical body within 24 hours returns
    the original campaign (200), while reusing a key with a different body returns 409.

    Args:
        x_idempotency_key (str):
        body (InternalPublicV1CreateCampaignRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalPublicV1ErrorEnvelope
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_idempotency_key=x_idempotency_key,
        )
    ).parsed
