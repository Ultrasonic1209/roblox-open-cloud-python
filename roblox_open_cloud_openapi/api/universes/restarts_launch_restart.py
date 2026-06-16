from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.launch_restart_request import LaunchRestartRequest
from ...models.launch_restart_response import LaunchRestartResponse
from ...models.server_management_service_problem_details import ServerManagementServiceProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    universe_id: int,
    *,
    body: LaunchRestartRequest | LaunchRestartRequest | LaunchRestartRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/server-management/v1/universes/{universe_id}/restarts".format(
            universe_id=quote(str(universe_id), safe=""),
        ),
    }

    if isinstance(body, LaunchRestartRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, LaunchRestartRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"
    if isinstance(body, LaunchRestartRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> LaunchRestartResponse | ServerManagementServiceProblemDetails | None:
    if response.status_code == 200:
        response_200 = LaunchRestartResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ServerManagementServiceProblemDetails.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ServerManagementServiceProblemDetails.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ServerManagementServiceProblemDetails.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[LaunchRestartResponse | ServerManagementServiceProblemDetails]:
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
    body: LaunchRestartRequest | LaunchRestartRequest | LaunchRestartRequest | Unset = UNSET,
) -> Response[LaunchRestartResponse | ServerManagementServiceProblemDetails]:
    """Launch a game server restart for a universe.

    Args:
        universe_id (int):
        body (LaunchRestartRequest | Unset): Request model for launching a game restart.
        body (LaunchRestartRequest | Unset): Request model for launching a game restart.
        body (LaunchRestartRequest | Unset): Request model for launching a game restart.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LaunchRestartResponse | ServerManagementServiceProblemDetails]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    body: LaunchRestartRequest | LaunchRestartRequest | LaunchRestartRequest | Unset = UNSET,
) -> LaunchRestartResponse | ServerManagementServiceProblemDetails | None:
    """Launch a game server restart for a universe.

    Args:
        universe_id (int):
        body (LaunchRestartRequest | Unset): Request model for launching a game restart.
        body (LaunchRestartRequest | Unset): Request model for launching a game restart.
        body (LaunchRestartRequest | Unset): Request model for launching a game restart.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LaunchRestartResponse | ServerManagementServiceProblemDetails
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
    body: LaunchRestartRequest | LaunchRestartRequest | LaunchRestartRequest | Unset = UNSET,
) -> Response[LaunchRestartResponse | ServerManagementServiceProblemDetails]:
    """Launch a game server restart for a universe.

    Args:
        universe_id (int):
        body (LaunchRestartRequest | Unset): Request model for launching a game restart.
        body (LaunchRestartRequest | Unset): Request model for launching a game restart.
        body (LaunchRestartRequest | Unset): Request model for launching a game restart.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LaunchRestartResponse | ServerManagementServiceProblemDetails]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    body: LaunchRestartRequest | LaunchRestartRequest | LaunchRestartRequest | Unset = UNSET,
) -> LaunchRestartResponse | ServerManagementServiceProblemDetails | None:
    """Launch a game server restart for a universe.

    Args:
        universe_id (int):
        body (LaunchRestartRequest | Unset): Request model for launching a game restart.
        body (LaunchRestartRequest | Unset): Request model for launching a game restart.
        body (LaunchRestartRequest | Unset): Request model for launching a game restart.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LaunchRestartResponse | ServerManagementServiceProblemDetails
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            client=client,
            body=body,
        )
    ).parsed
