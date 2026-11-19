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
{'x-roblox-stability': 'EXPERIMENTAL', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'MINUTE', 'maxInPeriod': 120}, 'perOauth2Authorization': {'period': 'MINUTE', 'maxInPeriod': 120}}, 'x-roblox-scopes': [{'name': 'ad.campaign:write'}], 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.create_campaign_request import CreateCampaignRequest
from ...models.error_envelope import ErrorEnvelope
from ...models.validate_campaign_response import ValidateCampaignResponse


def _get_kwargs(
    *,
    body: CreateCampaignRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/ads-management/v1/campaigns:validate",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorEnvelope | ValidateCampaignResponse | None:
    if response.status_code == 200:
        response_200 = ValidateCampaignResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = ErrorEnvelope.from_dict(response.json())

        return response_403

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
) -> Response[ErrorEnvelope | ValidateCampaignResponse]:
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
) -> Response[ErrorEnvelope | ValidateCampaignResponse]:
    """Validate a campaign without creating it

     Runs the same validation, permission, eligibility, and billing-account resolution as CreateCampaign,
    without creating anything. HTTP 200 means validation ran; read valid and errors, which match the
    errors CreateCampaign would return for the same body. resolvedBillingAccountId is the account the
    campaign would be created in. Malformed JSON, account-resolution failures, and dependency failures
    return the usual error envelope. The optional idempotencyKey body field is validated but does not
    reserve a key.

    Args:
        body (CreateCampaignRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | ValidateCampaignResponse]
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
) -> ErrorEnvelope | ValidateCampaignResponse | None:
    """Validate a campaign without creating it

     Runs the same validation, permission, eligibility, and billing-account resolution as CreateCampaign,
    without creating anything. HTTP 200 means validation ran; read valid and errors, which match the
    errors CreateCampaign would return for the same body. resolvedBillingAccountId is the account the
    campaign would be created in. Malformed JSON, account-resolution failures, and dependency failures
    return the usual error envelope. The optional idempotencyKey body field is validated but does not
    reserve a key.

    Args:
        body (CreateCampaignRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | ValidateCampaignResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateCampaignRequest,
) -> Response[ErrorEnvelope | ValidateCampaignResponse]:
    """Validate a campaign without creating it

     Runs the same validation, permission, eligibility, and billing-account resolution as CreateCampaign,
    without creating anything. HTTP 200 means validation ran; read valid and errors, which match the
    errors CreateCampaign would return for the same body. resolvedBillingAccountId is the account the
    campaign would be created in. Malformed JSON, account-resolution failures, and dependency failures
    return the usual error envelope. The optional idempotencyKey body field is validated but does not
    reserve a key.

    Args:
        body (CreateCampaignRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | ValidateCampaignResponse]
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
) -> ErrorEnvelope | ValidateCampaignResponse | None:
    """Validate a campaign without creating it

     Runs the same validation, permission, eligibility, and billing-account resolution as CreateCampaign,
    without creating anything. HTTP 200 means validation ran; read valid and errors, which match the
    errors CreateCampaign would return for the same body. resolvedBillingAccountId is the account the
    campaign would be created in. Malformed JSON, account-resolution failures, and dependency failures
    return the usual error envelope. The optional idempotencyKey body field is validated but does not
    reserve a key.

    Args:
        body (CreateCampaignRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | ValidateCampaignResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
