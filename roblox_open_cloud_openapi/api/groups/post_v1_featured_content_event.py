from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_groups_client_group_featured_content_response import (
    RobloxGroupsClientGroupFeaturedContentResponse,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    group_id: int,
    event_id: int,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["groupId"] = group_id

    params["eventId"] = event_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "https://groups.roblox.com/v1/featured-content/event",
        "params": params,
        "extensions": {
            "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
            "openapi-id": "post_v1_featured-content_event",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxGroupsClientGroupFeaturedContentResponse | None:
    if response.status_code == 200:
        response_200 = RobloxGroupsClientGroupFeaturedContentResponse.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxGroupsClientGroupFeaturedContentResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    group_id: int,
    event_id: int,
) -> Response[Any | RobloxGroupsClientGroupFeaturedContentResponse]:
    """Sets the featured event for a group

    Args:
        group_id (int):
        event_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxGroupsClientGroupFeaturedContentResponse]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        event_id=event_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    group_id: int,
    event_id: int,
) -> Any | RobloxGroupsClientGroupFeaturedContentResponse | None:
    """Sets the featured event for a group

    Args:
        group_id (int):
        event_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxGroupsClientGroupFeaturedContentResponse
    """

    return sync_detailed(
        client=client,
        group_id=group_id,
        event_id=event_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    group_id: int,
    event_id: int,
) -> Response[Any | RobloxGroupsClientGroupFeaturedContentResponse]:
    """Sets the featured event for a group

    Args:
        group_id (int):
        event_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxGroupsClientGroupFeaturedContentResponse]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        event_id=event_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    group_id: int,
    event_id: int,
) -> Any | RobloxGroupsClientGroupFeaturedContentResponse | None:
    """Sets the featured event for a group

    Args:
        group_id (int):
        event_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxGroupsClientGroupFeaturedContentResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            group_id=group_id,
            event_id=event_id,
        )
    ).parsed
