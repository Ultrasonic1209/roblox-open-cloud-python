from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.action_result import ActionResult
from ...models.find_thumbnails_response import FindThumbnailsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    universe_id: int,
    *,
    limit: int | Unset = UNSET,
    next_cursor: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["nextCursor"] = next_cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/thumbnail-personalization-api/v1/universes/{universe_id}/thumbnails".format(
            universe_id=quote(str(universe_id), safe=""),
        ),
        "params": params,
        "extensions": {
            "openapi-extensions": {
                "x-roblox-stability": "EXPERIMENTAL",
                "x-roblox-rate-limits": {
                    "perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 100},
                    "perOauth2Authorization": {"period": "MINUTE", "maxInPeriod": 100},
                },
                "x-roblox-scopes": [{"name": "universe.thumbnail:read", "targetResourceSpecifier": "universes"}],
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            },
            "openapi-id": "ThumbnailPersonalizationApi.HomepageThumbnail_GetHomepageThumbnails",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ActionResult | FindThumbnailsResponse | None:
    if response.status_code == 200:
        response_200 = FindThumbnailsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ActionResult.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ActionResult.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ActionResult.from_dict(response.json())

        return response_403

    if response.status_code == 500:
        response_500 = ActionResult.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ActionResult | FindThumbnailsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    next_cursor: str | Unset = UNSET,
) -> Response[ActionResult | FindThumbnailsResponse]:
    """
    Args:
        universe_id (int):
        limit (int | Unset):
        next_cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionResult | FindThumbnailsResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        limit=limit,
        next_cursor=next_cursor,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    next_cursor: str | Unset = UNSET,
) -> ActionResult | FindThumbnailsResponse | None:
    """
    Args:
        universe_id (int):
        limit (int | Unset):
        next_cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionResult | FindThumbnailsResponse
    """

    return sync_detailed(
        universe_id=universe_id,
        client=client,
        limit=limit,
        next_cursor=next_cursor,
    ).parsed


async def asyncio_detailed(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    next_cursor: str | Unset = UNSET,
) -> Response[ActionResult | FindThumbnailsResponse]:
    """
    Args:
        universe_id (int):
        limit (int | Unset):
        next_cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionResult | FindThumbnailsResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        limit=limit,
        next_cursor=next_cursor,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    next_cursor: str | Unset = UNSET,
) -> ActionResult | FindThumbnailsResponse | None:
    """
    Args:
        universe_id (int):
        limit (int | Unset):
        next_cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionResult | FindThumbnailsResponse
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            client=client,
            limit=limit,
            next_cursor=next_cursor,
        )
    ).parsed
