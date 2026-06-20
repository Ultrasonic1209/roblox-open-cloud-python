from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.user_notification import UserNotification
from ...types import Response


def _get_kwargs(
    user_id: str,
    *,
    body: UserNotification,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/cloud/v2/users/{user_id}/notifications".format(
            user_id=quote(str(user_id), safe=""),
        ),
        "extensions": {
            "openapi-extensions": {
                "x-roblox-engine-usability": {"apiKeyWithHttpService": True},
                "x-roblox-scopes": [{"name": "user.user-notification:write"}],
                "x-roblox-docs": {
                    "category": "Users and groups",
                    "methodProperties": {"scopes": ["user.user-notification:write"]},
                    "resource": {"$ref": "#/components/schemas/UserNotification", "name": "UserNotification"},
                },
                "x-roblox-stability": "STABLE",
                "x-roblox-rate-limits": {
                    "perApiKeyOwner": {"period": "SECOND", "maxInPeriod": 4000},
                    "perOauth2Authorization": {"period": "SECOND", "maxInPeriod": 4000},
                },
            },
            "openapi-id": "Cloud_CreateUserNotification",
        },
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> UserNotification | None:
    if response.status_code == 200:
        response_200 = UserNotification.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[UserNotification]:
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
    body: UserNotification,
) -> Response[UserNotification]:
    """Create User Notification

     Sends a notification to a user.

    Args:
        user_id (str):
        body (UserNotification): Represents a notification sent to a user.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UserNotification]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        body=body,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: str,
    *,
    client: AuthenticatedClient,
    body: UserNotification,
) -> UserNotification | None:
    """Create User Notification

     Sends a notification to a user.

    Args:
        user_id (str):
        body (UserNotification): Represents a notification sent to a user.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UserNotification
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
    body: UserNotification,
) -> Response[UserNotification]:
    """Create User Notification

     Sends a notification to a user.

    Args:
        user_id (str):
        body (UserNotification): Represents a notification sent to a user.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UserNotification]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    *,
    client: AuthenticatedClient,
    body: UserNotification,
) -> UserNotification | None:
    """Create User Notification

     Sends a notification to a user.

    Args:
        user_id (str):
        body (UserNotification): Represents a notification sent to a user.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UserNotification
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            body=body,
        )
    ).parsed
