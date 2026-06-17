from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.thumbnails_api_roblox_web_responses_thumbnails_thumbnail_response import (
    ThumbnailsApiRobloxWebResponsesThumbnailsThumbnailResponse,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    outfit_id: int,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["outfitId"] = outfit_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://thumbnails.roblox.com/v1/users/outfit-3d",
        "params": params,
        "openapi-extensions": {
            "x-roblox-stability": "BETA",
            "x-roblox-rate-limits": {
                "perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 100},
                "perOauth2Authorization": {"period": "MINUTE", "maxInPeriod": 100},
            },
            "x-roblox-scopes": [{"name": "thumbnail:read", "targetResourceSpecifier": ""}],
            "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
        },
        "openapi-id": "get_v1_users_outfit-3d",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ThumbnailsApiRobloxWebResponsesThumbnailsThumbnailResponse | None:
    if response.status_code == 200:
        response_200 = ThumbnailsApiRobloxWebResponsesThumbnailsThumbnailResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ThumbnailsApiRobloxWebResponsesThumbnailsThumbnailResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    outfit_id: int,
) -> Response[ThumbnailsApiRobloxWebResponsesThumbnailsThumbnailResponse]:
    """Get 3d object for an outfit

    Args:
        outfit_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ThumbnailsApiRobloxWebResponsesThumbnailsThumbnailResponse]
    """

    kwargs = _get_kwargs(
        outfit_id=outfit_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    outfit_id: int,
) -> ThumbnailsApiRobloxWebResponsesThumbnailsThumbnailResponse | None:
    """Get 3d object for an outfit

    Args:
        outfit_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ThumbnailsApiRobloxWebResponsesThumbnailsThumbnailResponse
    """

    return sync_detailed(
        client=client,
        outfit_id=outfit_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    outfit_id: int,
) -> Response[ThumbnailsApiRobloxWebResponsesThumbnailsThumbnailResponse]:
    """Get 3d object for an outfit

    Args:
        outfit_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ThumbnailsApiRobloxWebResponsesThumbnailsThumbnailResponse]
    """

    kwargs = _get_kwargs(
        outfit_id=outfit_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    outfit_id: int,
) -> ThumbnailsApiRobloxWebResponsesThumbnailsThumbnailResponse | None:
    """Get 3d object for an outfit

    Args:
        outfit_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ThumbnailsApiRobloxWebResponsesThumbnailsThumbnailResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            outfit_id=outfit_id,
        )
    ).parsed
