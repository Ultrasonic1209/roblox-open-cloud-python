from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.shutdown_game_instances_request import ShutdownGameInstancesRequest
from ...models.shutdown_game_instances_response import ShutdownGameInstancesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: ShutdownGameInstancesRequest
    | ShutdownGameInstancesRequest
    | ShutdownGameInstancesRequest
    | ShutdownGameInstancesRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/matchmaking-api/v1/game-instances/shutdown",
    }

    if isinstance(body, ShutdownGameInstancesRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, ShutdownGameInstancesRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, ShutdownGameInstancesRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"
    if isinstance(body, ShutdownGameInstancesRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ShutdownGameInstancesResponse | None:
    if response.status_code == 200:
        response_200 = ShutdownGameInstancesResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ShutdownGameInstancesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ShutdownGameInstancesRequest
    | ShutdownGameInstancesRequest
    | ShutdownGameInstancesRequest
    | ShutdownGameInstancesRequest
    | Unset = UNSET,
) -> Response[ShutdownGameInstancesResponse]:
    """Shutdown game instances.

    Args:
        body (ShutdownGameInstancesRequest | Unset): Shutdown Game Instance request.
        body (ShutdownGameInstancesRequest | Unset): Shutdown Game Instance request.
        body (ShutdownGameInstancesRequest | Unset): Shutdown Game Instance request.
        body (ShutdownGameInstancesRequest | Unset): Shutdown Game Instance request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ShutdownGameInstancesResponse]
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
    body: ShutdownGameInstancesRequest
    | ShutdownGameInstancesRequest
    | ShutdownGameInstancesRequest
    | ShutdownGameInstancesRequest
    | Unset = UNSET,
) -> ShutdownGameInstancesResponse | None:
    """Shutdown game instances.

    Args:
        body (ShutdownGameInstancesRequest | Unset): Shutdown Game Instance request.
        body (ShutdownGameInstancesRequest | Unset): Shutdown Game Instance request.
        body (ShutdownGameInstancesRequest | Unset): Shutdown Game Instance request.
        body (ShutdownGameInstancesRequest | Unset): Shutdown Game Instance request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ShutdownGameInstancesResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ShutdownGameInstancesRequest
    | ShutdownGameInstancesRequest
    | ShutdownGameInstancesRequest
    | ShutdownGameInstancesRequest
    | Unset = UNSET,
) -> Response[ShutdownGameInstancesResponse]:
    """Shutdown game instances.

    Args:
        body (ShutdownGameInstancesRequest | Unset): Shutdown Game Instance request.
        body (ShutdownGameInstancesRequest | Unset): Shutdown Game Instance request.
        body (ShutdownGameInstancesRequest | Unset): Shutdown Game Instance request.
        body (ShutdownGameInstancesRequest | Unset): Shutdown Game Instance request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ShutdownGameInstancesResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ShutdownGameInstancesRequest
    | ShutdownGameInstancesRequest
    | ShutdownGameInstancesRequest
    | ShutdownGameInstancesRequest
    | Unset = UNSET,
) -> ShutdownGameInstancesResponse | None:
    """Shutdown game instances.

    Args:
        body (ShutdownGameInstancesRequest | Unset): Shutdown Game Instance request.
        body (ShutdownGameInstancesRequest | Unset): Shutdown Game Instance request.
        body (ShutdownGameInstancesRequest | Unset): Shutdown Game Instance request.
        body (ShutdownGameInstancesRequest | Unset): Shutdown Game Instance request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ShutdownGameInstancesResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
