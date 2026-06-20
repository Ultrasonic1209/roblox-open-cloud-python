from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_private_server_request import CreatePrivateServerRequest
from ...models.game_server_response import GameServerResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    universe_id: int,
    *,
    body: CreatePrivateServerRequest | CreatePrivateServerRequest | CreatePrivateServerRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "https://games.roblox.com/v1/games/vip-servers/{universe_id}".format(
            universe_id=quote(str(universe_id), safe=""),
        ),
        "extensions": {
            "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
            "openapi-id": "PrivateServers_CreatePrivateServer",
        },
    }

    if isinstance(body, CreatePrivateServerRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CreatePrivateServerRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"
    if isinstance(body, CreatePrivateServerRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> GameServerResponse | None:
    if response.status_code == 200:
        response_200 = GameServerResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[GameServerResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    body: CreatePrivateServerRequest | CreatePrivateServerRequest | CreatePrivateServerRequest | Unset = UNSET,
) -> Response[GameServerResponse]:
    """
    Args:
        universe_id (int):
        body (CreatePrivateServerRequest | Unset):
        body (CreatePrivateServerRequest | Unset):
        body (CreatePrivateServerRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GameServerResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        body=body,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    body: CreatePrivateServerRequest | CreatePrivateServerRequest | CreatePrivateServerRequest | Unset = UNSET,
) -> GameServerResponse | None:
    """
    Args:
        universe_id (int):
        body (CreatePrivateServerRequest | Unset):
        body (CreatePrivateServerRequest | Unset):
        body (CreatePrivateServerRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GameServerResponse
    """

    return sync_detailed(
        universe_id=universe_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    body: CreatePrivateServerRequest | CreatePrivateServerRequest | CreatePrivateServerRequest | Unset = UNSET,
) -> Response[GameServerResponse]:
    """
    Args:
        universe_id (int):
        body (CreatePrivateServerRequest | Unset):
        body (CreatePrivateServerRequest | Unset):
        body (CreatePrivateServerRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GameServerResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    body: CreatePrivateServerRequest | CreatePrivateServerRequest | CreatePrivateServerRequest | Unset = UNSET,
) -> GameServerResponse | None:
    """
    Args:
        universe_id (int):
        body (CreatePrivateServerRequest | Unset):
        body (CreatePrivateServerRequest | Unset):
        body (CreatePrivateServerRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GameServerResponse
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            client=client,
            body=body,
        )
    ).parsed
