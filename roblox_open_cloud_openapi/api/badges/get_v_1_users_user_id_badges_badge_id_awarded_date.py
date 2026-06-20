import sys
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response

if sys.version_info >= (3, 13):
    from warnings import deprecated
else:
    from typing_extensions import deprecated


def _get_kwargs(
    user_id: int,
    badge_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://badges.roblox.com/v1/users/{user_id}/badges/{badge_id}/awarded-date".format(
            user_id=quote(str(user_id), safe=""),
            badge_id=quote(str(badge_id), safe=""),
        ),
        "extensions": {
            "openapi-extensions": {
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
                "x-roblox-recommended-alternatives": [
                    {
                        "url": "https://apis.roblox.com/cloud/v2/users/{user_id}/inventory-items",
                        "httpMethod": "GET",
                        "description": "The addTime response field corresponds with the badge awarded date",
                        "documentationUrl": "https://create.roblox.com/docs/cloud/reference/features/inventories#Cloud_ListInventoryItems",
                    }
                ],
            },
            "openapi-id": "get_v1_users_userId_badges_badgeId_awarded-date",
        },
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Any | None:
    if response.status_code == 200:
        return None

    if response.status_code == 404:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/badges#badges_get_v1_users__userId__badges__badgeId__awarded_date"
)
def sync_detailed(
    user_id: int,
    badge_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """Gets timestamp for when a single badge was awarded to a user.

    Args:
        user_id (int):
        badge_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        badge_id=badge_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/badges#badges_get_v1_users__userId__badges__badgeId__awarded_date"
)
async def asyncio_detailed(
    user_id: int,
    badge_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """Gets timestamp for when a single badge was awarded to a user.

    Args:
        user_id (int):
        badge_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        badge_id=badge_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)
