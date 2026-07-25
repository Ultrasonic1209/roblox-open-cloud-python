from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.internal_public_v1_error_envelope import InternalPublicV1ErrorEnvelope
from ...models.internal_public_v1_performance_response import InternalPublicV1PerformanceResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    period: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["period"] = period

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/ads-management/v1/campaigns/{id}/performance".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
        "extensions": {
            "openapi-extensions": {
                "x-roblox-stability": "EXPERIMENTAL",
                "x-roblox-rate-limits": {
                    "perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 300},
                    "perOauth2Authorization": {"period": "MINUTE", "maxInPeriod": 300},
                },
                "x-roblox-scopes": [{"name": "ad.campaign:read", "targetResourceSpecifier": ""}],
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            },
            "openapi-id": "get_ads-management_v1_campaigns_id_performance",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> InternalPublicV1ErrorEnvelope | InternalPublicV1PerformanceResponse | None:
    if response.status_code == 200:
        response_200 = InternalPublicV1PerformanceResponse.from_dict(response.json())

        return response_200

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
) -> Response[InternalPublicV1ErrorEnvelope | InternalPublicV1PerformanceResponse]:
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
    period: str | Unset = UNSET,
) -> Response[InternalPublicV1ErrorEnvelope | InternalPublicV1PerformanceResponse]:
    r"""Get campaign performance

     Returns aggregate performance for a single campaign over the requested period: impressions, clicks,
    plays, spend, CPM (cost per 1,000 impressions), CPP (cost per play), playRate, and CTR (click-
    through rate). Metrics are calculated in the billing account's time zone. Money fields (spendMicros,
    cpmMicros, cppMicros) are micro-USD returned as decimal strings (e.g. \"5000000\" = $5.00). Set the
    period query parameter to choose the window (defaults to LAST_7_DAYS).

    Args:
        id (str):
        period (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalPublicV1ErrorEnvelope | InternalPublicV1PerformanceResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        period=period,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    period: str | Unset = UNSET,
) -> InternalPublicV1ErrorEnvelope | InternalPublicV1PerformanceResponse | None:
    r"""Get campaign performance

     Returns aggregate performance for a single campaign over the requested period: impressions, clicks,
    plays, spend, CPM (cost per 1,000 impressions), CPP (cost per play), playRate, and CTR (click-
    through rate). Metrics are calculated in the billing account's time zone. Money fields (spendMicros,
    cpmMicros, cppMicros) are micro-USD returned as decimal strings (e.g. \"5000000\" = $5.00). Set the
    period query parameter to choose the window (defaults to LAST_7_DAYS).

    Args:
        id (str):
        period (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalPublicV1ErrorEnvelope | InternalPublicV1PerformanceResponse
    """

    return sync_detailed(
        id=id,
        client=client,
        period=period,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    period: str | Unset = UNSET,
) -> Response[InternalPublicV1ErrorEnvelope | InternalPublicV1PerformanceResponse]:
    r"""Get campaign performance

     Returns aggregate performance for a single campaign over the requested period: impressions, clicks,
    plays, spend, CPM (cost per 1,000 impressions), CPP (cost per play), playRate, and CTR (click-
    through rate). Metrics are calculated in the billing account's time zone. Money fields (spendMicros,
    cpmMicros, cppMicros) are micro-USD returned as decimal strings (e.g. \"5000000\" = $5.00). Set the
    period query parameter to choose the window (defaults to LAST_7_DAYS).

    Args:
        id (str):
        period (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalPublicV1ErrorEnvelope | InternalPublicV1PerformanceResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        period=period,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    period: str | Unset = UNSET,
) -> InternalPublicV1ErrorEnvelope | InternalPublicV1PerformanceResponse | None:
    r"""Get campaign performance

     Returns aggregate performance for a single campaign over the requested period: impressions, clicks,
    plays, spend, CPM (cost per 1,000 impressions), CPP (cost per play), playRate, and CTR (click-
    through rate). Metrics are calculated in the billing account's time zone. Money fields (spendMicros,
    cpmMicros, cppMicros) are micro-USD returned as decimal strings (e.g. \"5000000\" = $5.00). Set the
    period query parameter to choose the window (defaults to LAST_7_DAYS).

    Args:
        id (str):
        period (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalPublicV1ErrorEnvelope | InternalPublicV1PerformanceResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            period=period,
        )
    ).parsed
