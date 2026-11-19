from http import HTTPStatus
from typing import TYPE_CHECKING, Any

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
{'x-roblox-stability': 'BETA', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'MINUTE', 'maxInPeriod': 60}, 'perOauth2Authorization': {'period': 'MINUTE', 'maxInPeriod': 60}}, 'x-roblox-scopes': [{'name': 'ad.campaign:write'}], 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.create_campaign_request import CreateCampaignRequest
from ...models.error_envelope import ErrorEnvelope


def _get_kwargs(
    *,
    body: CreateCampaignRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/ads-management/v1/campaigns",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorEnvelope | None:
    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = ErrorEnvelope.from_dict(response.json())

        return response_403

    if response.status_code == 409:
        response_409 = ErrorEnvelope.from_dict(response.json())

        return response_409

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateCampaignRequest,
) -> Response[ErrorEnvelope]:
    """Create a campaign

     Creates an ad campaign in the billing account. Before creating, call GetCampaignOptions with
    universeId to confirm the experience is eligible and to choose values it accepts. The creatives you
    reference must already exist as Open Cloud image assets that you have permission to use; they are
    validated and saved to your account's reusable creatives when the campaign is created. On success
    the campaign is returned with deliveryStatus IN_REVIEW, meaning it is queued for ad-policy review
    and not yet serving, or NOT_SERVING with reason SCHEDULED when startTime is in the future — poll the
    campaign (or campaigns:batchGetStatus) until this changes. budget.amountMicros is the budget in
    micro-USD as a decimal string (e.g. "5000000" = $5.00). It must be at least the minimum campaign
    budget; an amount below the minimum returns 400 with the required minimum stated in the error
    message. schedule.durationInDays must not exceed 3650 (~10 years). The optional idempotencyKey body
    field must be a UUID when non-empty. If it is omitted or empty, creation runs without deduplication;
    retries can create duplicate campaigns. Generate a new key for each new campaign and whenever you
    change the request body, including the name. Reuse a key only to retry the same body. Within 24
    hours, a completed request's key returns the original campaign (200). If the body differs, the API
    ignores the changes; 200 does not mean they were applied, and this case does not return 409. A retry
    while the first request is still in progress returns 429. Use PATCH /campaigns/{id} to edit an
    existing campaign. A body field that the request does not define returns 400 with reason
    UNKNOWN_FIELD and the field path in field.

    Args:
        body (CreateCampaignRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope]
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
    body: CreateCampaignRequest,
) -> ErrorEnvelope | None:
    """Create a campaign

     Creates an ad campaign in the billing account. Before creating, call GetCampaignOptions with
    universeId to confirm the experience is eligible and to choose values it accepts. The creatives you
    reference must already exist as Open Cloud image assets that you have permission to use; they are
    validated and saved to your account's reusable creatives when the campaign is created. On success
    the campaign is returned with deliveryStatus IN_REVIEW, meaning it is queued for ad-policy review
    and not yet serving, or NOT_SERVING with reason SCHEDULED when startTime is in the future — poll the
    campaign (or campaigns:batchGetStatus) until this changes. budget.amountMicros is the budget in
    micro-USD as a decimal string (e.g. "5000000" = $5.00). It must be at least the minimum campaign
    budget; an amount below the minimum returns 400 with the required minimum stated in the error
    message. schedule.durationInDays must not exceed 3650 (~10 years). The optional idempotencyKey body
    field must be a UUID when non-empty. If it is omitted or empty, creation runs without deduplication;
    retries can create duplicate campaigns. Generate a new key for each new campaign and whenever you
    change the request body, including the name. Reuse a key only to retry the same body. Within 24
    hours, a completed request's key returns the original campaign (200). If the body differs, the API
    ignores the changes; 200 does not mean they were applied, and this case does not return 409. A retry
    while the first request is still in progress returns 429. Use PATCH /campaigns/{id} to edit an
    existing campaign. A body field that the request does not define returns 400 with reason
    UNKNOWN_FIELD and the field path in field.

    Args:
        body (CreateCampaignRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateCampaignRequest,
) -> Response[ErrorEnvelope]:
    """Create a campaign

     Creates an ad campaign in the billing account. Before creating, call GetCampaignOptions with
    universeId to confirm the experience is eligible and to choose values it accepts. The creatives you
    reference must already exist as Open Cloud image assets that you have permission to use; they are
    validated and saved to your account's reusable creatives when the campaign is created. On success
    the campaign is returned with deliveryStatus IN_REVIEW, meaning it is queued for ad-policy review
    and not yet serving, or NOT_SERVING with reason SCHEDULED when startTime is in the future — poll the
    campaign (or campaigns:batchGetStatus) until this changes. budget.amountMicros is the budget in
    micro-USD as a decimal string (e.g. "5000000" = $5.00). It must be at least the minimum campaign
    budget; an amount below the minimum returns 400 with the required minimum stated in the error
    message. schedule.durationInDays must not exceed 3650 (~10 years). The optional idempotencyKey body
    field must be a UUID when non-empty. If it is omitted or empty, creation runs without deduplication;
    retries can create duplicate campaigns. Generate a new key for each new campaign and whenever you
    change the request body, including the name. Reuse a key only to retry the same body. Within 24
    hours, a completed request's key returns the original campaign (200). If the body differs, the API
    ignores the changes; 200 does not mean they were applied, and this case does not return 409. A retry
    while the first request is still in progress returns 429. Use PATCH /campaigns/{id} to edit an
    existing campaign. A body field that the request does not define returns 400 with reason
    UNKNOWN_FIELD and the field path in field.

    Args:
        body (CreateCampaignRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateCampaignRequest,
) -> ErrorEnvelope | None:
    """Create a campaign

     Creates an ad campaign in the billing account. Before creating, call GetCampaignOptions with
    universeId to confirm the experience is eligible and to choose values it accepts. The creatives you
    reference must already exist as Open Cloud image assets that you have permission to use; they are
    validated and saved to your account's reusable creatives when the campaign is created. On success
    the campaign is returned with deliveryStatus IN_REVIEW, meaning it is queued for ad-policy review
    and not yet serving, or NOT_SERVING with reason SCHEDULED when startTime is in the future — poll the
    campaign (or campaigns:batchGetStatus) until this changes. budget.amountMicros is the budget in
    micro-USD as a decimal string (e.g. "5000000" = $5.00). It must be at least the minimum campaign
    budget; an amount below the minimum returns 400 with the required minimum stated in the error
    message. schedule.durationInDays must not exceed 3650 (~10 years). The optional idempotencyKey body
    field must be a UUID when non-empty. If it is omitted or empty, creation runs without deduplication;
    retries can create duplicate campaigns. Generate a new key for each new campaign and whenever you
    change the request body, including the name. Reuse a key only to retry the same body. Within 24
    hours, a completed request's key returns the original campaign (200). If the body differs, the API
    ignores the changes; 200 does not mean they were applied, and this case does not return 409. A retry
    while the first request is still in progress returns 429. Use PATCH /campaigns/{id} to edit an
    existing campaign. A body field that the request does not define returns 400 with reason
    UNKNOWN_FIELD and the field path in field.

    Args:
        body (CreateCampaignRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
