from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.thumbnails_api_roblox_web_responses_thumbnails_thumbnail_response import (
    ThumbnailsApiRobloxWebResponsesThumbnailsThumbnailResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    asset_id: int,
    roblox_place_id: int | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(roblox_place_id, Unset):
        headers["Roblox-Place-Id"] = str(roblox_place_id)

    params: dict[str, Any] = {}

    params["assetId"] = asset_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://thumbnails.roblox.com/v1/asset-thumbnail-animated",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | ThumbnailsApiRobloxWebResponsesThumbnailsThumbnailResponse | None:
    if response.status_code == 200:
        response_200 = ThumbnailsApiRobloxWebResponsesThumbnailsThumbnailResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | ThumbnailsApiRobloxWebResponsesThumbnailsThumbnailResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    asset_id: int,
    roblox_place_id: int | Unset = UNSET,
) -> Response[Any | ThumbnailsApiRobloxWebResponsesThumbnailsThumbnailResponse]:
    """Thumbnails asset animated.

    Args:
        asset_id (int):
        roblox_place_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ThumbnailsApiRobloxWebResponsesThumbnailsThumbnailResponse]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        roblox_place_id=roblox_place_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    asset_id: int,
    roblox_place_id: int | Unset = UNSET,
) -> Any | ThumbnailsApiRobloxWebResponsesThumbnailsThumbnailResponse | None:
    """Thumbnails asset animated.

    Args:
        asset_id (int):
        roblox_place_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ThumbnailsApiRobloxWebResponsesThumbnailsThumbnailResponse
    """

    return sync_detailed(
        client=client,
        asset_id=asset_id,
        roblox_place_id=roblox_place_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    asset_id: int,
    roblox_place_id: int | Unset = UNSET,
) -> Response[Any | ThumbnailsApiRobloxWebResponsesThumbnailsThumbnailResponse]:
    """Thumbnails asset animated.

    Args:
        asset_id (int):
        roblox_place_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ThumbnailsApiRobloxWebResponsesThumbnailsThumbnailResponse]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        roblox_place_id=roblox_place_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    asset_id: int,
    roblox_place_id: int | Unset = UNSET,
) -> Any | ThumbnailsApiRobloxWebResponsesThumbnailsThumbnailResponse | None:
    """Thumbnails asset animated.

    Args:
        asset_id (int):
        roblox_place_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ThumbnailsApiRobloxWebResponsesThumbnailsThumbnailResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            asset_id=asset_id,
            roblox_place_id=roblox_place_id,
        )
    ).parsed
