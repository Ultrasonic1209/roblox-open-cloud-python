from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.forecast_restart_response import ForecastRestartResponse
from ...models.server_management_service_problem_details import ServerManagementServiceProblemDetails
from ...types import Response


def _get_kwargs(
    universe_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/server-management/v1/universes/{universe_id}/restarts:forecast".format(
            universe_id=quote(str(universe_id), safe=""),
        ),
        "openapi-extensions": {
            "x-roblox-stability": "BETA",
            "x-roblox-rate-limits": {
                "perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 100},
                "perOauth2Authorization": {"period": "MINUTE", "maxInPeriod": 100},
            },
            "x-roblox-scopes": [{"name": "universe:read", "targetResourceSpecifier": "universes"}],
            "x-roblox-engine-usability": {"apiKeyWithHttpService": True},
        },
        "openapi-id": "Restarts_ForecastRestart",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ForecastRestartResponse | ServerManagementServiceProblemDetails | None:
    if response.status_code == 200:
        response_200 = ForecastRestartResponse.from_dict(response.json())

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
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ForecastRestartResponse | ServerManagementServiceProblemDetails]:
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
) -> Response[ForecastRestartResponse | ServerManagementServiceProblemDetails]:
    """Forecast the impact of restarting game servers for a universe.

    Args:
        universe_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ForecastRestartResponse | ServerManagementServiceProblemDetails]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: int,
    *,
    client: AuthenticatedClient,
) -> ForecastRestartResponse | ServerManagementServiceProblemDetails | None:
    """Forecast the impact of restarting game servers for a universe.

    Args:
        universe_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ForecastRestartResponse | ServerManagementServiceProblemDetails
    """

    return sync_detailed(
        universe_id=universe_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    universe_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[ForecastRestartResponse | ServerManagementServiceProblemDetails]:
    """Forecast the impact of restarting game servers for a universe.

    Args:
        universe_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ForecastRestartResponse | ServerManagementServiceProblemDetails]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: int,
    *,
    client: AuthenticatedClient,
) -> ForecastRestartResponse | ServerManagementServiceProblemDetails | None:
    """Forecast the impact of restarting game servers for a universe.

    Args:
        universe_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ForecastRestartResponse | ServerManagementServiceProblemDetails
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            client=client,
        )
    ).parsed
