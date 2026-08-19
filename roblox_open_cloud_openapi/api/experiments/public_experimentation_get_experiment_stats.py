from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.action_result import ActionResult
from ...models.get_experiment_stats_response import GetExperimentStatsResponse
from ...types import Response


def _get_kwargs(
    universe_id: int,
    experiment_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/creator-configs-public-api/v1/experimentation/universes/{universe_id}/experiments/{experiment_id}/stats".format(
            universe_id=quote(str(universe_id), safe=""),
            experiment_id=quote(str(experiment_id), safe=""),
        ),
        "extensions": {
            "openapi-extensions": {
                "x-roblox-stability": "EXPERIMENTAL",
                "x-roblox-rate-limits": {
                    "perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 100},
                    "perOauth2Authorization": {"period": "MINUTE", "maxInPeriod": 100},
                },
                "x-roblox-scopes": [{"name": "universe:read", "targetResourceSpecifier": "universes"}],
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            },
            "openapi-id": "PublicExperimentation_GetExperimentStats",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ActionResult | GetExperimentStatsResponse | None:
    if response.status_code == 200:
        response_200 = GetExperimentStatsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ActionResult.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ActionResult.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ActionResult.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ActionResult | GetExperimentStatsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    universe_id: int,
    experiment_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ActionResult | GetExperimentStatsResponse]:
    """Gets diagnostic stats for an experiment.

    Args:
        universe_id (int):
        experiment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionResult | GetExperimentStatsResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        experiment_id=experiment_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: int,
    experiment_id: str,
    *,
    client: AuthenticatedClient,
) -> ActionResult | GetExperimentStatsResponse | None:
    """Gets diagnostic stats for an experiment.

    Args:
        universe_id (int):
        experiment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionResult | GetExperimentStatsResponse
    """

    return sync_detailed(
        universe_id=universe_id,
        experiment_id=experiment_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    universe_id: int,
    experiment_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ActionResult | GetExperimentStatsResponse]:
    """Gets diagnostic stats for an experiment.

    Args:
        universe_id (int):
        experiment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionResult | GetExperimentStatsResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        experiment_id=experiment_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: int,
    experiment_id: str,
    *,
    client: AuthenticatedClient,
) -> ActionResult | GetExperimentStatsResponse | None:
    """Gets diagnostic stats for an experiment.

    Args:
        universe_id (int):
        experiment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionResult | GetExperimentStatsResponse
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            experiment_id=experiment_id,
            client=client,
        )
    ).parsed
