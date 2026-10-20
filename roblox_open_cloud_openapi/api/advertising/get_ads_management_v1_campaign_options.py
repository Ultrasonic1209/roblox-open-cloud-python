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
from ...types import UNSET, Response

"""
{'x-roblox-stability': 'BETA', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'MINUTE', 'maxInPeriod': 600}, 'perOauth2Authorization': {'period': 'MINUTE', 'maxInPeriod': 600}}, 'x-roblox-scopes': [{'name': 'ad.campaign:read', 'targetResourceSpecifier': ''}], 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.get_ads_management_v1_campaign_options_objective import GetAdsManagementV1CampaignOptionsObjective
from ...models.internal_public_v1_campaign_options_response import InternalPublicV1CampaignOptionsResponse
from ...models.internal_public_v1_error_envelope import InternalPublicV1ErrorEnvelope
from ...types import Unset


def _get_kwargs(
    *,
    universe_id: str | Unset = UNSET,
    objective: GetAdsManagementV1CampaignOptionsObjective | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["universeId"] = universe_id

    json_objective: str | Unset = UNSET
    if not isinstance(objective, Unset):
        json_objective = objective.value

    params["objective"] = json_objective

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/ads-management/v1/campaign-options",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> InternalPublicV1CampaignOptionsResponse | InternalPublicV1ErrorEnvelope | None:
    if response.status_code == 200:
        response_200 = InternalPublicV1CampaignOptionsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = InternalPublicV1ErrorEnvelope.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = InternalPublicV1ErrorEnvelope.from_dict(response.json())

        return response_403

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
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[InternalPublicV1CampaignOptionsResponse | InternalPublicV1ErrorEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    universe_id: str | Unset = UNSET,
    objective: GetAdsManagementV1CampaignOptionsObjective | Unset = UNSET,
) -> Response[InternalPublicV1CampaignOptionsResponse | InternalPublicV1ErrorEnvelope]:
    """Get campaign options

     Returns the values accepted when creating a campaign: supported objectives, payment types, ad
    formats, and targeting dimensions. When universeId is supplied, the response also includes an
    eligibility block indicating whether that experience can currently be advertised, along with the
    reasons when it cannot.

    Args:
        universe_id (str | Unset):
        objective (GetAdsManagementV1CampaignOptionsObjective | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalPublicV1CampaignOptionsResponse | InternalPublicV1ErrorEnvelope]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        objective=objective,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    universe_id: str | Unset = UNSET,
    objective: GetAdsManagementV1CampaignOptionsObjective | Unset = UNSET,
) -> InternalPublicV1CampaignOptionsResponse | InternalPublicV1ErrorEnvelope | None:
    """Get campaign options

     Returns the values accepted when creating a campaign: supported objectives, payment types, ad
    formats, and targeting dimensions. When universeId is supplied, the response also includes an
    eligibility block indicating whether that experience can currently be advertised, along with the
    reasons when it cannot.

    Args:
        universe_id (str | Unset):
        objective (GetAdsManagementV1CampaignOptionsObjective | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalPublicV1CampaignOptionsResponse | InternalPublicV1ErrorEnvelope
    """

    return sync_detailed(
        client=client,
        universe_id=universe_id,
        objective=objective,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    universe_id: str | Unset = UNSET,
    objective: GetAdsManagementV1CampaignOptionsObjective | Unset = UNSET,
) -> Response[InternalPublicV1CampaignOptionsResponse | InternalPublicV1ErrorEnvelope]:
    """Get campaign options

     Returns the values accepted when creating a campaign: supported objectives, payment types, ad
    formats, and targeting dimensions. When universeId is supplied, the response also includes an
    eligibility block indicating whether that experience can currently be advertised, along with the
    reasons when it cannot.

    Args:
        universe_id (str | Unset):
        objective (GetAdsManagementV1CampaignOptionsObjective | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalPublicV1CampaignOptionsResponse | InternalPublicV1ErrorEnvelope]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        objective=objective,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    universe_id: str | Unset = UNSET,
    objective: GetAdsManagementV1CampaignOptionsObjective | Unset = UNSET,
) -> InternalPublicV1CampaignOptionsResponse | InternalPublicV1ErrorEnvelope | None:
    """Get campaign options

     Returns the values accepted when creating a campaign: supported objectives, payment types, ad
    formats, and targeting dimensions. When universeId is supplied, the response also includes an
    eligibility block indicating whether that experience can currently be advertised, along with the
    reasons when it cannot.

    Args:
        universe_id (str | Unset):
        objective (GetAdsManagementV1CampaignOptionsObjective | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalPublicV1CampaignOptionsResponse | InternalPublicV1ErrorEnvelope
    """

    return (
        await asyncio_detailed(
            client=client,
            universe_id=universe_id,
            objective=objective,
        )
    ).parsed
