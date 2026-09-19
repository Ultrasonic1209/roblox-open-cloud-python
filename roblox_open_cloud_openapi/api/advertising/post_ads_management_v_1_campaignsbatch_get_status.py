from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.internal_public_v1_batch_get_status_request import InternalPublicV1BatchGetStatusRequest
from ...models.internal_public_v1_batch_get_status_response import InternalPublicV1BatchGetStatusResponse
from ...models.internal_public_v1_error_envelope import InternalPublicV1ErrorEnvelope
from ...types import Response


def _get_kwargs(
    *,
    body: InternalPublicV1BatchGetStatusRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/ads-management/v1/campaigns:batchGetStatus",
        "extensions": {
            "openapi-extensions": {
                "x-roblox-stability": "EXPERIMENTAL",
                "x-roblox-rate-limits": {
                    "perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 1000},
                    "perOauth2Authorization": {"period": "MINUTE", "maxInPeriod": 1000},
                },
                "x-roblox-scopes": [{"name": "ad.campaign:read", "targetResourceSpecifier": ""}],
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            },
            "openapi-id": "post_ads-management_v1_campaigns:batchGetStatus",
        },
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> InternalPublicV1BatchGetStatusResponse | InternalPublicV1ErrorEnvelope | None:
    if response.status_code == 200:
        response_200 = InternalPublicV1BatchGetStatusResponse.from_dict(response.json())

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
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[InternalPublicV1BatchGetStatusResponse | InternalPublicV1ErrorEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: InternalPublicV1BatchGetStatusRequest,
) -> Response[InternalPublicV1BatchGetStatusResponse | InternalPublicV1ErrorEnvelope]:
    """Batch get campaign status

     Returns the status (lifecycle state) and deliveryStatus (whether the campaign is currently serving),
    along with deliveryStatusReasons, for up to 100 campaigns in a single call. This is the recommended
    way to poll the review and serving state of many campaigns at once. Provide the campaign IDs in
    campaignIds; any ID that is not found or is not owned by the caller is returned in the failures
    array with reason NOT_FOUND.

    Args:
        body (InternalPublicV1BatchGetStatusRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalPublicV1BatchGetStatusResponse | InternalPublicV1ErrorEnvelope]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: InternalPublicV1BatchGetStatusRequest,
) -> InternalPublicV1BatchGetStatusResponse | InternalPublicV1ErrorEnvelope | None:
    """Batch get campaign status

     Returns the status (lifecycle state) and deliveryStatus (whether the campaign is currently serving),
    along with deliveryStatusReasons, for up to 100 campaigns in a single call. This is the recommended
    way to poll the review and serving state of many campaigns at once. Provide the campaign IDs in
    campaignIds; any ID that is not found or is not owned by the caller is returned in the failures
    array with reason NOT_FOUND.

    Args:
        body (InternalPublicV1BatchGetStatusRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalPublicV1BatchGetStatusResponse | InternalPublicV1ErrorEnvelope
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: InternalPublicV1BatchGetStatusRequest,
) -> Response[InternalPublicV1BatchGetStatusResponse | InternalPublicV1ErrorEnvelope]:
    """Batch get campaign status

     Returns the status (lifecycle state) and deliveryStatus (whether the campaign is currently serving),
    along with deliveryStatusReasons, for up to 100 campaigns in a single call. This is the recommended
    way to poll the review and serving state of many campaigns at once. Provide the campaign IDs in
    campaignIds; any ID that is not found or is not owned by the caller is returned in the failures
    array with reason NOT_FOUND.

    Args:
        body (InternalPublicV1BatchGetStatusRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalPublicV1BatchGetStatusResponse | InternalPublicV1ErrorEnvelope]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: InternalPublicV1BatchGetStatusRequest,
) -> InternalPublicV1BatchGetStatusResponse | InternalPublicV1ErrorEnvelope | None:
    """Batch get campaign status

     Returns the status (lifecycle state) and deliveryStatus (whether the campaign is currently serving),
    along with deliveryStatusReasons, for up to 100 campaigns in a single call. This is the recommended
    way to poll the review and serving state of many campaigns at once. Provide the campaign IDs in
    campaignIds; any ID that is not found or is not owned by the caller is returned in the failures
    array with reason NOT_FOUND.

    Args:
        body (InternalPublicV1BatchGetStatusRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalPublicV1BatchGetStatusResponse | InternalPublicV1ErrorEnvelope
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
