from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.internal_public_v1_error_envelope import InternalPublicV1ErrorEnvelope
from ...models.internal_public_v1_list_advertisable_universes_response import (
    InternalPublicV1ListAdvertisableUniversesResponse,
)
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/ads-management/v1/advertisable-universes",
        "extensions": {
            "openapi-extensions": {
                "x-roblox-stability": "EXPERIMENTAL",
                "x-roblox-rate-limits": {
                    "perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 600},
                    "perOauth2Authorization": {"period": "MINUTE", "maxInPeriod": 600},
                },
                "x-roblox-scopes": [{"name": "ad.campaign:read", "targetResourceSpecifier": ""}],
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            },
            "openapi-id": "get_ads-management_v1_advertisable-universes",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> InternalPublicV1ErrorEnvelope | InternalPublicV1ListAdvertisableUniversesResponse | None:
    if response.status_code == 200:
        response_200 = InternalPublicV1ListAdvertisableUniversesResponse.from_dict(response.json())

        return response_200

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
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[InternalPublicV1ErrorEnvelope | InternalPublicV1ListAdvertisableUniversesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[InternalPublicV1ErrorEnvelope | InternalPublicV1ListAdvertisableUniversesResponse]:
    """List advertisable universes

     Returns the universe IDs of every experience the billing account is eligible to advertise. The
    complete list is returned in a single response; this endpoint is not paginated. Use these IDs to set
    targetUniverseId when creating a campaign, and resolve experience names with the Open Cloud Universe
    API.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalPublicV1ErrorEnvelope | InternalPublicV1ListAdvertisableUniversesResponse]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> InternalPublicV1ErrorEnvelope | InternalPublicV1ListAdvertisableUniversesResponse | None:
    """List advertisable universes

     Returns the universe IDs of every experience the billing account is eligible to advertise. The
    complete list is returned in a single response; this endpoint is not paginated. Use these IDs to set
    targetUniverseId when creating a campaign, and resolve experience names with the Open Cloud Universe
    API.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalPublicV1ErrorEnvelope | InternalPublicV1ListAdvertisableUniversesResponse
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[InternalPublicV1ErrorEnvelope | InternalPublicV1ListAdvertisableUniversesResponse]:
    """List advertisable universes

     Returns the universe IDs of every experience the billing account is eligible to advertise. The
    complete list is returned in a single response; this endpoint is not paginated. Use these IDs to set
    targetUniverseId when creating a campaign, and resolve experience names with the Open Cloud Universe
    API.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalPublicV1ErrorEnvelope | InternalPublicV1ListAdvertisableUniversesResponse]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> InternalPublicV1ErrorEnvelope | InternalPublicV1ListAdvertisableUniversesResponse | None:
    """List advertisable universes

     Returns the universe IDs of every experience the billing account is eligible to advertise. The
    complete list is returned in a single response; this endpoint is not paginated. Use these IDs to set
    targetUniverseId when creating a campaign, and resolve experience names with the Open Cloud Universe
    API.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalPublicV1ErrorEnvelope | InternalPublicV1ListAdvertisableUniversesResponse
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
