from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.action_result import ActionResult
from ...models.create_experiment_data import CreateExperimentData
from ...models.create_experiment_response import CreateExperimentResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    universe_id: int,
    *,
    body: CreateExperimentData | CreateExperimentData | CreateExperimentData | CreateExperimentData | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/creator-configs-public-api/v1/experimentation/universes/{universe_id}/experiments".format(
            universe_id=quote(str(universe_id), safe=""),
        ),
        "extensions": {
            "openapi-extensions": {
                "x-roblox-stability": "EXPERIMENTAL",
                "x-roblox-rate-limits": {
                    "perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 10},
                    "perOauth2Authorization": {"period": "MINUTE", "maxInPeriod": 10},
                },
                "x-roblox-scopes": [{"name": "universe:write", "targetResourceSpecifier": "universes"}],
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            },
            "openapi-id": "PublicExperimentation_CreateExperiment",
        },
    }

    if isinstance(body, CreateExperimentData):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, CreateExperimentData):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CreateExperimentData):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"
    if isinstance(body, CreateExperimentData):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ActionResult | CreateExperimentResponse | None:
    if response.status_code == 200:
        response_200 = CreateExperimentResponse.from_dict(response.json())

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
) -> Response[ActionResult | CreateExperimentResponse]:
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
    body: CreateExperimentData | CreateExperimentData | CreateExperimentData | CreateExperimentData | Unset = UNSET,
) -> Response[ActionResult | CreateExperimentResponse]:
    """Creates a new experiment for a universe.

     Returns an ExperimentOperation describing the async create call.

    Args:
        universe_id (int):
        body (CreateExperimentData): Request body for `POST
            /v1/experimentation/universes/{universeId}/experiments`.
            Payload describing a new experiment.
        body (CreateExperimentData): Request body for `POST
            /v1/experimentation/universes/{universeId}/experiments`.
            Payload describing a new experiment.
        body (CreateExperimentData): Request body for `POST
            /v1/experimentation/universes/{universeId}/experiments`.
            Payload describing a new experiment.
        body (CreateExperimentData): Request body for `POST
            /v1/experimentation/universes/{universeId}/experiments`.
            Payload describing a new experiment.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionResult | CreateExperimentResponse]
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
    body: CreateExperimentData | CreateExperimentData | CreateExperimentData | CreateExperimentData | Unset = UNSET,
) -> ActionResult | CreateExperimentResponse | None:
    """Creates a new experiment for a universe.

     Returns an ExperimentOperation describing the async create call.

    Args:
        universe_id (int):
        body (CreateExperimentData): Request body for `POST
            /v1/experimentation/universes/{universeId}/experiments`.
            Payload describing a new experiment.
        body (CreateExperimentData): Request body for `POST
            /v1/experimentation/universes/{universeId}/experiments`.
            Payload describing a new experiment.
        body (CreateExperimentData): Request body for `POST
            /v1/experimentation/universes/{universeId}/experiments`.
            Payload describing a new experiment.
        body (CreateExperimentData): Request body for `POST
            /v1/experimentation/universes/{universeId}/experiments`.
            Payload describing a new experiment.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionResult | CreateExperimentResponse
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
    body: CreateExperimentData | CreateExperimentData | CreateExperimentData | CreateExperimentData | Unset = UNSET,
) -> Response[ActionResult | CreateExperimentResponse]:
    """Creates a new experiment for a universe.

     Returns an ExperimentOperation describing the async create call.

    Args:
        universe_id (int):
        body (CreateExperimentData): Request body for `POST
            /v1/experimentation/universes/{universeId}/experiments`.
            Payload describing a new experiment.
        body (CreateExperimentData): Request body for `POST
            /v1/experimentation/universes/{universeId}/experiments`.
            Payload describing a new experiment.
        body (CreateExperimentData): Request body for `POST
            /v1/experimentation/universes/{universeId}/experiments`.
            Payload describing a new experiment.
        body (CreateExperimentData): Request body for `POST
            /v1/experimentation/universes/{universeId}/experiments`.
            Payload describing a new experiment.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionResult | CreateExperimentResponse]
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
    body: CreateExperimentData | CreateExperimentData | CreateExperimentData | CreateExperimentData | Unset = UNSET,
) -> ActionResult | CreateExperimentResponse | None:
    """Creates a new experiment for a universe.

     Returns an ExperimentOperation describing the async create call.

    Args:
        universe_id (int):
        body (CreateExperimentData): Request body for `POST
            /v1/experimentation/universes/{universeId}/experiments`.
            Payload describing a new experiment.
        body (CreateExperimentData): Request body for `POST
            /v1/experimentation/universes/{universeId}/experiments`.
            Payload describing a new experiment.
        body (CreateExperimentData): Request body for `POST
            /v1/experimentation/universes/{universeId}/experiments`.
            Payload describing a new experiment.
        body (CreateExperimentData): Request body for `POST
            /v1/experimentation/universes/{universeId}/experiments`.
            Payload describing a new experiment.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionResult | CreateExperimentResponse
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            client=client,
            body=body,
        )
    ).parsed
