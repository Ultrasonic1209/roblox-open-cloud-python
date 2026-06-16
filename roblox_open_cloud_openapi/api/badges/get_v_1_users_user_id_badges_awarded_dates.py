from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_web_web_api_models_api_array_response_roblox_badges_api_badge_award_response import (
    RobloxWebWebAPIModelsApiArrayResponseRobloxBadgesApiBadgeAwardResponse,
)
from ...types import UNSET, Response


def _get_kwargs(
    user_id: int,
    *,
    badge_ids: list[int],
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_badge_ids = badge_ids

    params["badgeIds"] = json_badge_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/users/{user_id}/badges/awarded-dates".format(
            user_id=quote(str(user_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxBadgesApiBadgeAwardResponse | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIModelsApiArrayResponseRobloxBadgesApiBadgeAwardResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxBadgesApiBadgeAwardResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: int,
    *,
    client: AuthenticatedClient,
    badge_ids: list[int],
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxBadgesApiBadgeAwardResponse]:
    """Gets timestamps for when badges were awarded to a user.

    Args:
        user_id (int):
        badge_ids (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxBadgesApiBadgeAwardResponse]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        badge_ids=badge_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: int,
    *,
    client: AuthenticatedClient,
    badge_ids: list[int],
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxBadgesApiBadgeAwardResponse | None:
    """Gets timestamps for when badges were awarded to a user.

    Args:
        user_id (int):
        badge_ids (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiArrayResponseRobloxBadgesApiBadgeAwardResponse
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        badge_ids=badge_ids,
    ).parsed


async def asyncio_detailed(
    user_id: int,
    *,
    client: AuthenticatedClient,
    badge_ids: list[int],
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxBadgesApiBadgeAwardResponse]:
    """Gets timestamps for when badges were awarded to a user.

    Args:
        user_id (int):
        badge_ids (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxBadgesApiBadgeAwardResponse]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        badge_ids=badge_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: int,
    *,
    client: AuthenticatedClient,
    badge_ids: list[int],
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxBadgesApiBadgeAwardResponse | None:
    """Gets timestamps for when badges were awarded to a user.

    Args:
        user_id (int):
        badge_ids (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiArrayResponseRobloxBadgesApiBadgeAwardResponse
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            badge_ids=badge_ids,
        )
    ).parsed
