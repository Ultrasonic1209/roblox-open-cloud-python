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
{'x-roblox-stability': 'BETA', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'MINUTE', 'maxInPeriod': 120}, 'perOauth2Authorization': {'period': 'MINUTE', 'maxInPeriod': 120}}, 'x-roblox-scopes': [{'name': 'ad.campaign:read'}], 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.campaign_options_response import CampaignOptionsResponse
from ...models.error_envelope import ErrorEnvelope
from ...models.get_campaign_options_objective import GetCampaignOptionsObjective
from ...types import Unset


def _get_kwargs(
    *,
    universe_id: str | Unset = UNSET,
    objective: GetCampaignOptionsObjective | Unset = UNSET,
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
) -> CampaignOptionsResponse | ErrorEnvelope | None:
    if response.status_code == 200:
        response_200 = CampaignOptionsResponse.from_dict(response.json())

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
) -> Response[CampaignOptionsResponse | ErrorEnvelope]:
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
    objective: GetCampaignOptionsObjective | Unset = UNSET,
) -> Response[CampaignOptionsResponse | ErrorEnvelope]:
    """Get campaign options

     Returns the values accepted when creating a campaign: supported objectives, payment types, ad
    formats, and targeting dimensions. Call this before CreateCampaign. When universeId is supplied, the
    response also includes an eligibility block indicating whether that experience can currently be
    advertised, along with the reasons when it cannot. universeId is optional; without it, account-level
    options are returned without eligibility or billing-account resolution, and paymentTypes is a static
    menu that does not check payment setup. A caller without permission to advertise the supplied
    experience gets 403 with reason UNIVERSE_NOT_ADVERTISABLE. It works without a billing account and
    lists in billingAccounts the accounts you can create a campaign for the experience in, each with the
    payment types it can use now: CREDIT_CARD only for your own account with a verified card, ADS_CREDIT
    only with activated ad credit of at least the minimum daily budget, and only ADS_CREDIT for a
    group's account. paymentTypes is then the payment types at least one of those accounts can use, and
    is empty when there are none. Each account also has paymentStatus, paymentStatusReason, and
    paymentSetupUrl. Create also checks that the ad credit balance covers the daily budget. Sponsored
    video tiles follow the billing account's owner: video is present when the request's account or at
    least one listed billing account allows video, and mutableFields lists video only when a campaign's
    video can be changed.

    Args:
        universe_id (str | Unset):
        objective (GetCampaignOptionsObjective | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CampaignOptionsResponse | ErrorEnvelope]
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
    objective: GetCampaignOptionsObjective | Unset = UNSET,
) -> CampaignOptionsResponse | ErrorEnvelope | None:
    """Get campaign options

     Returns the values accepted when creating a campaign: supported objectives, payment types, ad
    formats, and targeting dimensions. Call this before CreateCampaign. When universeId is supplied, the
    response also includes an eligibility block indicating whether that experience can currently be
    advertised, along with the reasons when it cannot. universeId is optional; without it, account-level
    options are returned without eligibility or billing-account resolution, and paymentTypes is a static
    menu that does not check payment setup. A caller without permission to advertise the supplied
    experience gets 403 with reason UNIVERSE_NOT_ADVERTISABLE. It works without a billing account and
    lists in billingAccounts the accounts you can create a campaign for the experience in, each with the
    payment types it can use now: CREDIT_CARD only for your own account with a verified card, ADS_CREDIT
    only with activated ad credit of at least the minimum daily budget, and only ADS_CREDIT for a
    group's account. paymentTypes is then the payment types at least one of those accounts can use, and
    is empty when there are none. Each account also has paymentStatus, paymentStatusReason, and
    paymentSetupUrl. Create also checks that the ad credit balance covers the daily budget. Sponsored
    video tiles follow the billing account's owner: video is present when the request's account or at
    least one listed billing account allows video, and mutableFields lists video only when a campaign's
    video can be changed.

    Args:
        universe_id (str | Unset):
        objective (GetCampaignOptionsObjective | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CampaignOptionsResponse | ErrorEnvelope
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
    objective: GetCampaignOptionsObjective | Unset = UNSET,
) -> Response[CampaignOptionsResponse | ErrorEnvelope]:
    """Get campaign options

     Returns the values accepted when creating a campaign: supported objectives, payment types, ad
    formats, and targeting dimensions. Call this before CreateCampaign. When universeId is supplied, the
    response also includes an eligibility block indicating whether that experience can currently be
    advertised, along with the reasons when it cannot. universeId is optional; without it, account-level
    options are returned without eligibility or billing-account resolution, and paymentTypes is a static
    menu that does not check payment setup. A caller without permission to advertise the supplied
    experience gets 403 with reason UNIVERSE_NOT_ADVERTISABLE. It works without a billing account and
    lists in billingAccounts the accounts you can create a campaign for the experience in, each with the
    payment types it can use now: CREDIT_CARD only for your own account with a verified card, ADS_CREDIT
    only with activated ad credit of at least the minimum daily budget, and only ADS_CREDIT for a
    group's account. paymentTypes is then the payment types at least one of those accounts can use, and
    is empty when there are none. Each account also has paymentStatus, paymentStatusReason, and
    paymentSetupUrl. Create also checks that the ad credit balance covers the daily budget. Sponsored
    video tiles follow the billing account's owner: video is present when the request's account or at
    least one listed billing account allows video, and mutableFields lists video only when a campaign's
    video can be changed.

    Args:
        universe_id (str | Unset):
        objective (GetCampaignOptionsObjective | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CampaignOptionsResponse | ErrorEnvelope]
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
    objective: GetCampaignOptionsObjective | Unset = UNSET,
) -> CampaignOptionsResponse | ErrorEnvelope | None:
    """Get campaign options

     Returns the values accepted when creating a campaign: supported objectives, payment types, ad
    formats, and targeting dimensions. Call this before CreateCampaign. When universeId is supplied, the
    response also includes an eligibility block indicating whether that experience can currently be
    advertised, along with the reasons when it cannot. universeId is optional; without it, account-level
    options are returned without eligibility or billing-account resolution, and paymentTypes is a static
    menu that does not check payment setup. A caller without permission to advertise the supplied
    experience gets 403 with reason UNIVERSE_NOT_ADVERTISABLE. It works without a billing account and
    lists in billingAccounts the accounts you can create a campaign for the experience in, each with the
    payment types it can use now: CREDIT_CARD only for your own account with a verified card, ADS_CREDIT
    only with activated ad credit of at least the minimum daily budget, and only ADS_CREDIT for a
    group's account. paymentTypes is then the payment types at least one of those accounts can use, and
    is empty when there are none. Each account also has paymentStatus, paymentStatusReason, and
    paymentSetupUrl. Create also checks that the ad credit balance covers the daily budget. Sponsored
    video tiles follow the billing account's owner: video is present when the request's account or at
    least one listed billing account allows video, and mutableFields lists video only when a campaign's
    video can be changed.

    Args:
        universe_id (str | Unset):
        objective (GetCampaignOptionsObjective | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CampaignOptionsResponse | ErrorEnvelope
    """

    return (
        await asyncio_detailed(
            client=client,
            universe_id=universe_id,
            objective=objective,
        )
    ).parsed
