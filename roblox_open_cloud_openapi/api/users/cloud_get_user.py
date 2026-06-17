from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.user import User
from ...types import Response


def _get_kwargs(
    user_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/cloud/v2/users/{user_id}".format(
            user_id=quote(str(user_id), safe=""),
        ),
        "openapi-extensions": {
            "x-roblox-engine-usability": {"apiKeyWithHttpService": True},
            "x-roblox-scopes": [
                {
                    "description": "Grants access to read a user&#x27;s verification status.",
                    "name": "user.advanced:read",
                },
                {
                    "description": "Grants access to read a user&#x27;s social account information.",
                    "name": "user.social:read",
                },
            ],
            "x-roblox-docs": {
                "category": "Users and groups",
                "methodProperties": {"scopes": []},
                "resource": {"$ref": "#/components/schemas/User", "name": "User"},
            },
            "x-roblox-stability": "BETA",
            "x-roblox-rate-limits": {
                "perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 1000},
                "perOauth2Authorization": {"period": "MINUTE", "maxInPeriod": 10},
            },
        },
        "openapi-id": "Cloud_GetUser",
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> User | None:
    if response.status_code == 200:
        response_200 = User.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[User]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[User]:
    """Get User

     Gets a user's basic and advanced information.

    To access a user's public information, no additional scopes are required.

    To access a user's verification status, you need the following scopes:
    * user.advanced:read

    To access a user's social account information, you need the following
    scopes:
    * user.social:read

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[User]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: str,
    *,
    client: AuthenticatedClient,
) -> User | None:
    """Get User

     Gets a user's basic and advanced information.

    To access a user's public information, no additional scopes are required.

    To access a user's verification status, you need the following scopes:
    * user.advanced:read

    To access a user's social account information, you need the following
    scopes:
    * user.social:read

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        User
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[User]:
    """Get User

     Gets a user's basic and advanced information.

    To access a user's public information, no additional scopes are required.

    To access a user's verification status, you need the following scopes:
    * user.advanced:read

    To access a user's social account information, you need the following
    scopes:
    * user.social:read

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[User]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    *,
    client: AuthenticatedClient,
) -> User | None:
    """Get User

     Gets a user's basic and advanced information.

    To access a user's public information, no additional scopes are required.

    To access a user's verification status, you need the following scopes:
    * user.advanced:read

    To access a user's social account information, you need the following
    scopes:
    * user.social:read

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        User
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
        )
    ).parsed
