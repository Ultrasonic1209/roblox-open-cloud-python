from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.restart_universe_servers_request import RestartUniverseServersRequest
from ...models.restart_universe_servers_response import RestartUniverseServersResponse
from ...types import Response


def _get_kwargs(
    universe_id: str,
    *,
    body: RestartUniverseServersRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/cloud/v2/universes/{universe_id}:restartServers".format(
            universe_id=quote(str(universe_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> RestartUniverseServersResponse | None:
    if response.status_code == 200:
        response_200 = RestartUniverseServersResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[RestartUniverseServersResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    universe_id: str,
    *,
    client: AuthenticatedClient,
    body: RestartUniverseServersRequest,
) -> Response[RestartUniverseServersResponse]:
    """Restart Universe Servers

     Restarts active servers for a specific universe. Defaults to only
    restarting servers running older versions, but can be configured to restart
    all servers regardless of version. Used for releasing experience updates.

    Args:
        universe_id (str):
        body (RestartUniverseServersRequest): Restarts all of the universe's servers.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestartUniverseServersResponse]
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
    universe_id: str,
    *,
    client: AuthenticatedClient,
    body: RestartUniverseServersRequest,
) -> RestartUniverseServersResponse | None:
    """Restart Universe Servers

     Restarts active servers for a specific universe. Defaults to only
    restarting servers running older versions, but can be configured to restart
    all servers regardless of version. Used for releasing experience updates.

    Args:
        universe_id (str):
        body (RestartUniverseServersRequest): Restarts all of the universe's servers.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestartUniverseServersResponse
    """

    return sync_detailed(
        universe_id=universe_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    universe_id: str,
    *,
    client: AuthenticatedClient,
    body: RestartUniverseServersRequest,
) -> Response[RestartUniverseServersResponse]:
    """Restart Universe Servers

     Restarts active servers for a specific universe. Defaults to only
    restarting servers running older versions, but can be configured to restart
    all servers regardless of version. Used for releasing experience updates.

    Args:
        universe_id (str):
        body (RestartUniverseServersRequest): Restarts all of the universe's servers.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestartUniverseServersResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: str,
    *,
    client: AuthenticatedClient,
    body: RestartUniverseServersRequest,
) -> RestartUniverseServersResponse | None:
    """Restart Universe Servers

     Restarts active servers for a specific universe. Defaults to only
    restarting servers running older versions, but can be configured to restart
    all servers regardless of version. Used for releasing experience updates.

    Args:
        universe_id (str):
        body (RestartUniverseServersRequest): Restarts all of the universe's servers.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestartUniverseServersResponse
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            client=client,
            body=body,
        )
    ).parsed
