import sys
from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response

if sys.version_info >= (3, 13):
    from warnings import deprecated
else:
    from typing_extensions import deprecated

from ...models.post_v1_universes_universe_id_badges_body import PostV1UniversesUniverseIdBadgesBody
from ...models.roblox_web_responses_badges_badge_response_v2 import RobloxWebResponsesBadgesBadgeResponseV2
from ...types import Unset


def _get_kwargs(
    universe_id: int,
    *,
    body: PostV1UniversesUniverseIdBadgesBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/universes/{universe_id}/badges".format(
            universe_id=quote(str(universe_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["files"] = body.to_multipart()

    headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxWebResponsesBadgesBadgeResponseV2 | None:
    if response.status_code == 200:
        response_200 = RobloxWebResponsesBadgesBadgeResponseV2.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RobloxWebResponsesBadgesBadgeResponseV2]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/badges#badges_post_v1_universes__universeId__badges"
)
def sync_detailed(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    body: PostV1UniversesUniverseIdBadgesBody | Unset = UNSET,
) -> Response[Any | RobloxWebResponsesBadgesBadgeResponseV2]:
    """Creates a new badge.

    Args:
        universe_id (int):
        body (PostV1UniversesUniverseIdBadgesBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebResponsesBadgesBadgeResponseV2]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/badges#badges_post_v1_universes__universeId__badges"
)
def sync(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    body: PostV1UniversesUniverseIdBadgesBody | Unset = UNSET,
) -> Any | RobloxWebResponsesBadgesBadgeResponseV2 | None:
    """Creates a new badge.

    Args:
        universe_id (int):
        body (PostV1UniversesUniverseIdBadgesBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebResponsesBadgesBadgeResponseV2
    """

    return sync_detailed(
        universe_id=universe_id,
        client=client,
        body=body,
    ).parsed


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/badges#badges_post_v1_universes__universeId__badges"
)
async def asyncio_detailed(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    body: PostV1UniversesUniverseIdBadgesBody | Unset = UNSET,
) -> Response[Any | RobloxWebResponsesBadgesBadgeResponseV2]:
    """Creates a new badge.

    Args:
        universe_id (int):
        body (PostV1UniversesUniverseIdBadgesBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebResponsesBadgesBadgeResponseV2]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/badges#badges_post_v1_universes__universeId__badges"
)
async def asyncio(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    body: PostV1UniversesUniverseIdBadgesBody | Unset = UNSET,
) -> Any | RobloxWebResponsesBadgesBadgeResponseV2 | None:
    """Creates a new badge.

    Args:
        universe_id (int):
        body (PostV1UniversesUniverseIdBadgesBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebResponsesBadgesBadgeResponseV2
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            client=client,
            body=body,
        )
    ).parsed
