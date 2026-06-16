from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_matchmaking_api_v1_game_instances_shutdown_all_body import (
    PostMatchmakingApiV1GameInstancesShutdownAllBody,
)
from ...models.shutdown_all_game_instances_response import ShutdownAllGameInstancesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostMatchmakingApiV1GameInstancesShutdownAllBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/matchmaking-api/v1/game-instances/shutdown-all",
    }

    if not isinstance(body, Unset):
        _kwargs["files"] = body.to_multipart()

    headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ShutdownAllGameInstancesResponse | None:
    if response.status_code == 200:
        response_200 = ShutdownAllGameInstancesResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ShutdownAllGameInstancesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostMatchmakingApiV1GameInstancesShutdownAllBody | Unset = UNSET,
) -> Response[ShutdownAllGameInstancesResponse]:
    """Shutdown all game instances.

    Args:
        body (PostMatchmakingApiV1GameInstancesShutdownAllBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ShutdownAllGameInstancesResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: PostMatchmakingApiV1GameInstancesShutdownAllBody | Unset = UNSET,
) -> ShutdownAllGameInstancesResponse | None:
    """Shutdown all game instances.

    Args:
        body (PostMatchmakingApiV1GameInstancesShutdownAllBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ShutdownAllGameInstancesResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostMatchmakingApiV1GameInstancesShutdownAllBody | Unset = UNSET,
) -> Response[ShutdownAllGameInstancesResponse]:
    """Shutdown all game instances.

    Args:
        body (PostMatchmakingApiV1GameInstancesShutdownAllBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ShutdownAllGameInstancesResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostMatchmakingApiV1GameInstancesShutdownAllBody | Unset = UNSET,
) -> ShutdownAllGameInstancesResponse | None:
    """Shutdown all game instances.

    Args:
        body (PostMatchmakingApiV1GameInstancesShutdownAllBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ShutdownAllGameInstancesResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
