from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_user_restrictions_response import ListUserRestrictionsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    universe_id: str,
    *,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["maxPageSize"] = max_page_size

    params["pageToken"] = page_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/cloud/v2/universes/{universe_id}/user-restrictions".format(
            universe_id=quote(str(universe_id), safe=""),
        ),
        "params": params,
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
            "openapi-id": "Cloud_ListUserRestrictions",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ListUserRestrictionsResponse | None:
    if response.status_code == 200:
        response_200 = ListUserRestrictionsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ListUserRestrictionsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    universe_id: str,
    *,
    client: AuthenticatedClient,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> Response[ListUserRestrictionsResponse]:
    """List User Restrictions

     List user restrictions for users that have ever been banned in either a
    universe or a specific place.

    Args:
        universe_id (str):
        max_page_size (int | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListUserRestrictionsResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        max_page_size=max_page_size,
        page_token=page_token,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: str,
    *,
    client: AuthenticatedClient,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> ListUserRestrictionsResponse | None:
    """List User Restrictions

     List user restrictions for users that have ever been banned in either a
    universe or a specific place.

    Args:
        universe_id (str):
        max_page_size (int | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListUserRestrictionsResponse
    """

    return sync_detailed(
        universe_id=universe_id,
        client=client,
        max_page_size=max_page_size,
        page_token=page_token,
    ).parsed


async def asyncio_detailed(
    universe_id: str,
    *,
    client: AuthenticatedClient,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> Response[ListUserRestrictionsResponse]:
    """List User Restrictions

     List user restrictions for users that have ever been banned in either a
    universe or a specific place.

    Args:
        universe_id (str):
        max_page_size (int | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListUserRestrictionsResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        max_page_size=max_page_size,
        page_token=page_token,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: str,
    *,
    client: AuthenticatedClient,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> ListUserRestrictionsResponse | None:
    """List User Restrictions

     List user restrictions for users that have ever been banned in either a
    universe or a specific place.

    Args:
        universe_id (str):
        max_page_size (int | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListUserRestrictionsResponse
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            client=client,
            max_page_size=max_page_size,
            page_token=page_token,
        )
    ).parsed
