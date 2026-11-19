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
{'x-roblox-stability': 'EXPERIMENTAL', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'MINUTE', 'maxInPeriod': 120}, 'perOauth2Authorization': {'period': 'MINUTE', 'maxInPeriod': 120}}, 'x-roblox-scopes': [{'name': 'ad.campaign:read'}], 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.campaign_recommendation_request import CampaignRecommendationRequest
from ...models.campaign_recommendation_response import CampaignRecommendationResponse
from ...models.error_envelope import ErrorEnvelope


def _get_kwargs(
    *,
    body: CampaignRecommendationRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/ads-management/v1/campaign-recommendations",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CampaignRecommendationResponse | ErrorEnvelope | None:
    if response.status_code == 200:
        response_200 = CampaignRecommendationResponse.from_dict(response.json())

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
) -> Response[CampaignRecommendationResponse | ErrorEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CampaignRecommendationRequest,
) -> Response[CampaignRecommendationResponse | ErrorEnvelope]:
    """Recommend budget and duration

     Returns non-binding daily budget and duration suggestions for the proposed campaign. campaignContext
    accepts every creatable objective (PLAYS, ENGAGEMENT, ROBUX_SPEND). targetUniverseId and
    targeting.audienceType influence the result; RETENTION and REACTIVATION get budget recommendations
    for that audience. targeting accepts only audienceType: ageGroups, countries, regions, and devices
    return 400 with reason UNSUPPORTED_VALUE.

    Args:
        body (CampaignRecommendationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CampaignRecommendationResponse | ErrorEnvelope]
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
    body: CampaignRecommendationRequest,
) -> CampaignRecommendationResponse | ErrorEnvelope | None:
    """Recommend budget and duration

     Returns non-binding daily budget and duration suggestions for the proposed campaign. campaignContext
    accepts every creatable objective (PLAYS, ENGAGEMENT, ROBUX_SPEND). targetUniverseId and
    targeting.audienceType influence the result; RETENTION and REACTIVATION get budget recommendations
    for that audience. targeting accepts only audienceType: ageGroups, countries, regions, and devices
    return 400 with reason UNSUPPORTED_VALUE.

    Args:
        body (CampaignRecommendationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CampaignRecommendationResponse | ErrorEnvelope
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CampaignRecommendationRequest,
) -> Response[CampaignRecommendationResponse | ErrorEnvelope]:
    """Recommend budget and duration

     Returns non-binding daily budget and duration suggestions for the proposed campaign. campaignContext
    accepts every creatable objective (PLAYS, ENGAGEMENT, ROBUX_SPEND). targetUniverseId and
    targeting.audienceType influence the result; RETENTION and REACTIVATION get budget recommendations
    for that audience. targeting accepts only audienceType: ageGroups, countries, regions, and devices
    return 400 with reason UNSUPPORTED_VALUE.

    Args:
        body (CampaignRecommendationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CampaignRecommendationResponse | ErrorEnvelope]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CampaignRecommendationRequest,
) -> CampaignRecommendationResponse | ErrorEnvelope | None:
    """Recommend budget and duration

     Returns non-binding daily budget and duration suggestions for the proposed campaign. campaignContext
    accepts every creatable objective (PLAYS, ENGAGEMENT, ROBUX_SPEND). targetUniverseId and
    targeting.audienceType influence the result; RETENTION and REACTIVATION get budget recommendations
    for that audience. targeting accepts only audienceType: ageGroups, countries, regions, and devices
    return 400 with reason UNSUPPORTED_VALUE.

    Args:
        body (CampaignRecommendationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CampaignRecommendationResponse | ErrorEnvelope
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
