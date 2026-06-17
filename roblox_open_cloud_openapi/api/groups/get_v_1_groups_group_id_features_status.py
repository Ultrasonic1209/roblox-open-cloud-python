from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_groups_api_has_group_features_blocked_response import (
    RobloxGroupsApiHasGroupFeaturesBlockedResponse,
)
from ...types import Response


def _get_kwargs(
    group_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://groups.roblox.com/v1/groups/{group_id}/features/status".format(
            group_id=quote(str(group_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxGroupsApiHasGroupFeaturesBlockedResponse | None:
    if response.status_code == 200:
        response_200 = RobloxGroupsApiHasGroupFeaturesBlockedResponse.from_dict(response.json())

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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxGroupsApiHasGroupFeaturesBlockedResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    group_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxGroupsApiHasGroupFeaturesBlockedResponse]:
    """Checks whether a group has ANY feature disabled (includes feature freezes and group lock).
    Used to display a banner on Creator Hub/Studio to inform group members that some features may not be
    available.

    Args:
        group_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxGroupsApiHasGroupFeaturesBlockedResponse]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxGroupsApiHasGroupFeaturesBlockedResponse | None:
    """Checks whether a group has ANY feature disabled (includes feature freezes and group lock).
    Used to display a banner on Creator Hub/Studio to inform group members that some features may not be
    available.

    Args:
        group_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxGroupsApiHasGroupFeaturesBlockedResponse
    """

    return sync_detailed(
        group_id=group_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    group_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxGroupsApiHasGroupFeaturesBlockedResponse]:
    """Checks whether a group has ANY feature disabled (includes feature freezes and group lock).
    Used to display a banner on Creator Hub/Studio to inform group members that some features may not be
    available.

    Args:
        group_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxGroupsApiHasGroupFeaturesBlockedResponse]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxGroupsApiHasGroupFeaturesBlockedResponse | None:
    """Checks whether a group has ANY feature disabled (includes feature freezes and group lock).
    Used to display a banner on Creator Hub/Studio to inform group members that some features may not be
    available.

    Args:
        group_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxGroupsApiHasGroupFeaturesBlockedResponse
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
        )
    ).parsed
