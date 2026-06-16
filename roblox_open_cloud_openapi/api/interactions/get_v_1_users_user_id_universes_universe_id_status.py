import sys
from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response

if sys.version_info >= (3, 13):
    from warnings import deprecated
else:
    from typing_extensions import deprecated

from ...models.roblox_followings_api_models_user_following_universe_status_response import (
    RobloxFollowingsApiModelsUserFollowingUniverseStatusResponse,
)


def _get_kwargs(
    user_id: int,
    universe_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/users/{user_id}/universes/{universe_id}/status".format(
            user_id=quote(str(user_id), safe=""),
            universe_id=quote(str(universe_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxFollowingsApiModelsUserFollowingUniverseStatusResponse | None:
    if response.status_code == 200:
        response_200 = RobloxFollowingsApiModelsUserFollowingUniverseStatusResponse.from_dict(response.json())

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
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RobloxFollowingsApiModelsUserFollowingUniverseStatusResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/interactions#followings_get_v1_users__userId__universes__universeId__status"
)
def sync_detailed(
    user_id: int,
    universe_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxFollowingsApiModelsUserFollowingUniverseStatusResponse]:
    """Gets the status of a following relationship between a user and a universe.

    Args:
        user_id (int):
        universe_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxFollowingsApiModelsUserFollowingUniverseStatusResponse]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        universe_id=universe_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/interactions#followings_get_v1_users__userId__universes__universeId__status"
)
def sync(
    user_id: int,
    universe_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxFollowingsApiModelsUserFollowingUniverseStatusResponse | None:
    """Gets the status of a following relationship between a user and a universe.

    Args:
        user_id (int):
        universe_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxFollowingsApiModelsUserFollowingUniverseStatusResponse
    """

    return sync_detailed(
        user_id=user_id,
        universe_id=universe_id,
        client=client,
    ).parsed


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/interactions#followings_get_v1_users__userId__universes__universeId__status"
)
async def asyncio_detailed(
    user_id: int,
    universe_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxFollowingsApiModelsUserFollowingUniverseStatusResponse]:
    """Gets the status of a following relationship between a user and a universe.

    Args:
        user_id (int):
        universe_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxFollowingsApiModelsUserFollowingUniverseStatusResponse]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        universe_id=universe_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/interactions#followings_get_v1_users__userId__universes__universeId__status"
)
async def asyncio(
    user_id: int,
    universe_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxFollowingsApiModelsUserFollowingUniverseStatusResponse | None:
    """Gets the status of a following relationship between a user and a universe.

    Args:
        user_id (int):
        universe_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxFollowingsApiModelsUserFollowingUniverseStatusResponse
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            universe_id=universe_id,
            client=client,
        )
    ).parsed
