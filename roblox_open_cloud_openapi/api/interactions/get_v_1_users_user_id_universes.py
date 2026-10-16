import sys
from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response

if sys.version_info >= (3, 13):
    from warnings import deprecated
else:
    from typing_extensions import deprecated

from ...models.roblox_followings_api_models_user_following_universe_response import (
    RobloxFollowingsApiModelsUserFollowingUniverseResponse,
)


def _get_kwargs(
    user_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://followings.roblox.com/v1/users/{user_id}/universes".format(
            user_id=quote(str(user_id), safe=""),
        ),
        "extensions": {
            "openapi-extensions": {
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
                "x-roblox-recommended-alternatives": [
                    {
                        "url": "https://apis.roblox.com/legacy-followings/v1/users/{userId}/universes",
                        "httpMethod": "GET",
                        "documentationUrl": "https://create.roblox.com/docs/cloud/reference/features/interactions#get_legacy_followings_v1_users__userId__universes",
                    }
                ],
            },
            "openapi-id": "get_v1_users_userId_universes",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | list[RobloxFollowingsApiModelsUserFollowingUniverseResponse] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = RobloxFollowingsApiModelsUserFollowingUniverseResponse.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Any | list[RobloxFollowingsApiModelsUserFollowingUniverseResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/interactions#followings_get_v1_users__userId__universes"
)
def sync_detailed(
    user_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | list[RobloxFollowingsApiModelsUserFollowingUniverseResponse]]:
    """Gets all the followings between a user with userId and universes

    Args:
        user_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[RobloxFollowingsApiModelsUserFollowingUniverseResponse]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/interactions#followings_get_v1_users__userId__universes"
)
def sync(
    user_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | list[RobloxFollowingsApiModelsUserFollowingUniverseResponse] | None:
    """Gets all the followings between a user with userId and universes

    Args:
        user_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[RobloxFollowingsApiModelsUserFollowingUniverseResponse]
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
    ).parsed


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/interactions#followings_get_v1_users__userId__universes"
)
async def asyncio_detailed(
    user_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | list[RobloxFollowingsApiModelsUserFollowingUniverseResponse]]:
    """Gets all the followings between a user with userId and universes

    Args:
        user_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[RobloxFollowingsApiModelsUserFollowingUniverseResponse]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/interactions#followings_get_v1_users__userId__universes"
)
async def asyncio(
    user_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | list[RobloxFollowingsApiModelsUserFollowingUniverseResponse] | None:
    """Gets all the followings between a user with userId and universes

    Args:
        user_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[RobloxFollowingsApiModelsUserFollowingUniverseResponse]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
        )
    ).parsed
