from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_badges_api_badge_response import RobloxBadgesApiBadgeResponse
from ...types import Response


def _get_kwargs(
    badge_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://badges.roblox.com/v1/badges/{badge_id}".format(
            badge_id=quote(str(badge_id), safe=""),
        ),
        "extensions": {
            "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
            "openapi-id": "get_v1_badges_badgeId",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxBadgesApiBadgeResponse | None:
    if response.status_code == 200:
        response_200 = RobloxBadgesApiBadgeResponse.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxBadgesApiBadgeResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    badge_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxBadgesApiBadgeResponse]:
    """Gets badge information by the badge Id.

    Args:
        badge_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxBadgesApiBadgeResponse]
    """

    kwargs = _get_kwargs(
        badge_id=badge_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    badge_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxBadgesApiBadgeResponse | None:
    """Gets badge information by the badge Id.

    Args:
        badge_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxBadgesApiBadgeResponse
    """

    return sync_detailed(
        badge_id=badge_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    badge_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxBadgesApiBadgeResponse]:
    """Gets badge information by the badge Id.

    Args:
        badge_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxBadgesApiBadgeResponse]
    """

    kwargs = _get_kwargs(
        badge_id=badge_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    badge_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxBadgesApiBadgeResponse | None:
    """Gets badge information by the badge Id.

    Args:
        badge_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxBadgesApiBadgeResponse
    """

    return (
        await asyncio_detailed(
            badge_id=badge_id,
            client=client,
        )
    ).parsed
