from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_followings_api_models_user_following_universe_response import (
    RobloxFollowingsApiModelsUserFollowingUniverseResponse,
)
from ...types import Response


def _get_kwargs(
    user_id: int,
    universe_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/legacy-followings/v1/users/{user_id}/universes/{universe_id}".format(
            user_id=quote(str(user_id), safe=""),
            universe_id=quote(str(universe_id), safe=""),
        ),
        "extensions": {
            "openapi-extensions": {
                "x-roblox-rate-limits": {
                    "perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 100},
                    "perOauth2Authorization": {"period": "MINUTE", "maxInPeriod": 100},
                },
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
                "x-roblox-scopes": [{"name": "legacy-universe.following:write"}],
            },
            "openapi-id": "delete_legacy-followings_v1_users_userId_universes_universeId",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxFollowingsApiModelsUserFollowingUniverseResponse | None:
    if response.status_code == 200:
        response_200 = RobloxFollowingsApiModelsUserFollowingUniverseResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxFollowingsApiModelsUserFollowingUniverseResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: int,
    universe_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxFollowingsApiModelsUserFollowingUniverseResponse]:
    """Deletes the following between a user with userId and universe with universeId

    Args:
        user_id (int):
        universe_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxFollowingsApiModelsUserFollowingUniverseResponse]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        universe_id=universe_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: int,
    universe_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxFollowingsApiModelsUserFollowingUniverseResponse | None:
    """Deletes the following between a user with userId and universe with universeId

    Args:
        user_id (int):
        universe_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxFollowingsApiModelsUserFollowingUniverseResponse
    """

    return sync_detailed(
        user_id=user_id,
        universe_id=universe_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_id: int,
    universe_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxFollowingsApiModelsUserFollowingUniverseResponse]:
    """Deletes the following between a user with userId and universe with universeId

    Args:
        user_id (int):
        universe_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxFollowingsApiModelsUserFollowingUniverseResponse]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        universe_id=universe_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: int,
    universe_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxFollowingsApiModelsUserFollowingUniverseResponse | None:
    """Deletes the following between a user with userId and universe with universeId

    Args:
        user_id (int):
        universe_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxFollowingsApiModelsUserFollowingUniverseResponse
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            universe_id=universe_id,
            client=client,
        )
    ).parsed
