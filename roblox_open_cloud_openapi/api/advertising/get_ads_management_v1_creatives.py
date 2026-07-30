from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.internal_public_v1_error_envelope import InternalPublicV1ErrorEnvelope
from ...models.internal_public_v1_list_creatives_response import InternalPublicV1ListCreativesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    is_archived: bool | Unset = UNSET,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["isArchived"] = is_archived

    params["maxPageSize"] = max_page_size

    params["pageToken"] = page_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/ads-management/v1/creatives",
        "params": params,
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
            "openapi-id": "get_ads-management_v1_creatives",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> InternalPublicV1ErrorEnvelope | InternalPublicV1ListCreativesResponse | None:
    if response.status_code == 200:
        response_200 = InternalPublicV1ListCreativesResponse.from_dict(response.json())

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
) -> Response[InternalPublicV1ErrorEnvelope | InternalPublicV1ListCreativesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    is_archived: bool | Unset = UNSET,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> Response[InternalPublicV1ErrorEnvelope | InternalPublicV1ListCreativesResponse]:
    """List creatives

     Lists the reusable creatives saved to the caller's billing account. Each creative includes its
    assetId, name, moderation status, dimensions, and source. Use isArchived to filter by archive state.
    Results are paginated with a cursor (pageToken).

    Args:
        is_archived (bool | Unset):
        max_page_size (int | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalPublicV1ErrorEnvelope | InternalPublicV1ListCreativesResponse]
    """

    kwargs = _get_kwargs(
        is_archived=is_archived,
        max_page_size=max_page_size,
        page_token=page_token,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    is_archived: bool | Unset = UNSET,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> InternalPublicV1ErrorEnvelope | InternalPublicV1ListCreativesResponse | None:
    """List creatives

     Lists the reusable creatives saved to the caller's billing account. Each creative includes its
    assetId, name, moderation status, dimensions, and source. Use isArchived to filter by archive state.
    Results are paginated with a cursor (pageToken).

    Args:
        is_archived (bool | Unset):
        max_page_size (int | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalPublicV1ErrorEnvelope | InternalPublicV1ListCreativesResponse
    """

    return sync_detailed(
        client=client,
        is_archived=is_archived,
        max_page_size=max_page_size,
        page_token=page_token,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    is_archived: bool | Unset = UNSET,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> Response[InternalPublicV1ErrorEnvelope | InternalPublicV1ListCreativesResponse]:
    """List creatives

     Lists the reusable creatives saved to the caller's billing account. Each creative includes its
    assetId, name, moderation status, dimensions, and source. Use isArchived to filter by archive state.
    Results are paginated with a cursor (pageToken).

    Args:
        is_archived (bool | Unset):
        max_page_size (int | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InternalPublicV1ErrorEnvelope | InternalPublicV1ListCreativesResponse]
    """

    kwargs = _get_kwargs(
        is_archived=is_archived,
        max_page_size=max_page_size,
        page_token=page_token,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    is_archived: bool | Unset = UNSET,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> InternalPublicV1ErrorEnvelope | InternalPublicV1ListCreativesResponse | None:
    """List creatives

     Lists the reusable creatives saved to the caller's billing account. Each creative includes its
    assetId, name, moderation status, dimensions, and source. Use isArchived to filter by archive state.
    Results are paginated with a cursor (pageToken).

    Args:
        is_archived (bool | Unset):
        max_page_size (int | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InternalPublicV1ErrorEnvelope | InternalPublicV1ListCreativesResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            is_archived=is_archived,
            max_page_size=max_page_size,
            page_token=page_token,
        )
    ).parsed
