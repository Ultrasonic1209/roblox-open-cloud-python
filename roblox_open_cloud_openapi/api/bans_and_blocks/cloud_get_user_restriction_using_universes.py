from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.user_restriction import UserRestriction
from ...types import Response


def _get_kwargs(
    universe_id: str,
    user_restriction_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/cloud/v2/universes/{universe_id}/user-restrictions/{user_restriction_id}".format(
            universe_id=quote(str(universe_id), safe=""),
            user_restriction_id=quote(str(user_restriction_id), safe=""),
        ),
        "extensions": {
            "openapi-extensions": {
                "x-roblox-engine-usability": {"apiKeyWithHttpService": True},
                "x-roblox-rate-limits": {
                    "description": "User Restrictions are subject to the additional rate limits, applied per universe\n\n* Get User Restriction: 50 req/s\n* List User Restrictions: 50 req/s\n* Update User Restrictions: 10 req/s\n* List User Restriction Logs: 50 req/s\n\nAdditionally, we impose the following rate limit for the same user within a universe:\n\n* Update User Restriction: 2 req/min\n\nFor example, Update User Restriction may not be called for user 123 more than twice every minute.",
                    "perApiKeyOwner": {"period": "SECOND", "maxInPeriod": 150},
                    "perOauth2Authorization": {"period": "SECOND", "maxInPeriod": 30},
                },
                "x-roblox-scopes": [{"name": "universe.user-restriction:read"}],
                "x-roblox-docs": {
                    "category": "Users and groups",
                    "methodProperties": {"scopes": ["universe.user-restriction:read"]},
                    "resource": {"$ref": "#/components/schemas/UserRestriction", "name": "UserRestriction"},
                },
                "x-roblox-stability": "BETA",
            },
            "openapi-id": "Cloud_GetUserRestriction__Using_Universes",
        },
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> UserRestriction | None:
    if response.status_code == 200:
        response_200 = UserRestriction.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[UserRestriction]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    universe_id: str,
    user_restriction_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[UserRestriction]:
    """Get User Restriction

     Get the user restriction.

    Args:
        universe_id (str):
        user_restriction_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UserRestriction]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        user_restriction_id=user_restriction_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: str,
    user_restriction_id: str,
    *,
    client: AuthenticatedClient,
) -> UserRestriction | None:
    """Get User Restriction

     Get the user restriction.

    Args:
        universe_id (str):
        user_restriction_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UserRestriction
    """

    return sync_detailed(
        universe_id=universe_id,
        user_restriction_id=user_restriction_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    universe_id: str,
    user_restriction_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[UserRestriction]:
    """Get User Restriction

     Get the user restriction.

    Args:
        universe_id (str):
        user_restriction_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UserRestriction]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        user_restriction_id=user_restriction_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: str,
    user_restriction_id: str,
    *,
    client: AuthenticatedClient,
) -> UserRestriction | None:
    """Get User Restriction

     Get the user restriction.

    Args:
        universe_id (str):
        user_restriction_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UserRestriction
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            user_restriction_id=user_restriction_id,
            client=client,
        )
    ).parsed
