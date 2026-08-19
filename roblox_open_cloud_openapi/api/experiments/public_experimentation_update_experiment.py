from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.action_result import ActionResult
from ...models.update_experiment_data import UpdateExperimentData
from ...models.update_experiment_response import UpdateExperimentResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    universe_id: int,
    experiment_id: str,
    *,
    body: UpdateExperimentData | UpdateExperimentData | UpdateExperimentData | UpdateExperimentData | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/creator-configs-public-api/v1/experimentation/universes/{universe_id}/experiments/{experiment_id}".format(
            universe_id=quote(str(universe_id), safe=""),
            experiment_id=quote(str(experiment_id), safe=""),
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
            "openapi-id": "PublicExperimentation_UpdateExperiment",
        },
    }

    if isinstance(body, UpdateExperimentData):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, UpdateExperimentData):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, UpdateExperimentData):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"
    if isinstance(body, UpdateExperimentData):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ActionResult | UpdateExperimentResponse | None:
    if response.status_code == 200:
        response_200 = UpdateExperimentResponse.from_dict(response.json())

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
) -> Response[ActionResult | UpdateExperimentResponse]:
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
    body: UpdateExperimentData | UpdateExperimentData | UpdateExperimentData | UpdateExperimentData | Unset = UNSET,
) -> Response[ActionResult | UpdateExperimentResponse]:
    """Updates an existing experiment.

     The payload is a full replacement of the mutable experiment fields. Returns an
    ExperimentOperation describing the async update.

    Args:
        universe_id (int):
        experiment_id (str):
        body (UpdateExperimentData): Request body for
            `PATCH /v1/experimentation/universes/{universeId}/experiments/{experimentId}`.
            Mirrors CreatorConfigsPublicApi.Models.Experimentation.CreateExperimentData; updating is
            modeled as a full replace of these fields.
        body (UpdateExperimentData): Request body for
            `PATCH /v1/experimentation/universes/{universeId}/experiments/{experimentId}`.
            Mirrors CreatorConfigsPublicApi.Models.Experimentation.CreateExperimentData; updating is
            modeled as a full replace of these fields.
        body (UpdateExperimentData): Request body for
            `PATCH /v1/experimentation/universes/{universeId}/experiments/{experimentId}`.
            Mirrors CreatorConfigsPublicApi.Models.Experimentation.CreateExperimentData; updating is
            modeled as a full replace of these fields.
        body (UpdateExperimentData): Request body for
            `PATCH /v1/experimentation/universes/{universeId}/experiments/{experimentId}`.
            Mirrors CreatorConfigsPublicApi.Models.Experimentation.CreateExperimentData; updating is
            modeled as a full replace of these fields.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionResult | UpdateExperimentResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        experiment_id=experiment_id,
        body=body,
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
    body: UpdateExperimentData | UpdateExperimentData | UpdateExperimentData | UpdateExperimentData | Unset = UNSET,
) -> ActionResult | UpdateExperimentResponse | None:
    """Updates an existing experiment.

     The payload is a full replacement of the mutable experiment fields. Returns an
    ExperimentOperation describing the async update.

    Args:
        universe_id (int):
        experiment_id (str):
        body (UpdateExperimentData): Request body for
            `PATCH /v1/experimentation/universes/{universeId}/experiments/{experimentId}`.
            Mirrors CreatorConfigsPublicApi.Models.Experimentation.CreateExperimentData; updating is
            modeled as a full replace of these fields.
        body (UpdateExperimentData): Request body for
            `PATCH /v1/experimentation/universes/{universeId}/experiments/{experimentId}`.
            Mirrors CreatorConfigsPublicApi.Models.Experimentation.CreateExperimentData; updating is
            modeled as a full replace of these fields.
        body (UpdateExperimentData): Request body for
            `PATCH /v1/experimentation/universes/{universeId}/experiments/{experimentId}`.
            Mirrors CreatorConfigsPublicApi.Models.Experimentation.CreateExperimentData; updating is
            modeled as a full replace of these fields.
        body (UpdateExperimentData): Request body for
            `PATCH /v1/experimentation/universes/{universeId}/experiments/{experimentId}`.
            Mirrors CreatorConfigsPublicApi.Models.Experimentation.CreateExperimentData; updating is
            modeled as a full replace of these fields.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionResult | UpdateExperimentResponse
    """

    return sync_detailed(
        universe_id=universe_id,
        experiment_id=experiment_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    universe_id: int,
    experiment_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateExperimentData | UpdateExperimentData | UpdateExperimentData | UpdateExperimentData | Unset = UNSET,
) -> Response[ActionResult | UpdateExperimentResponse]:
    """Updates an existing experiment.

     The payload is a full replacement of the mutable experiment fields. Returns an
    ExperimentOperation describing the async update.

    Args:
        universe_id (int):
        experiment_id (str):
        body (UpdateExperimentData): Request body for
            `PATCH /v1/experimentation/universes/{universeId}/experiments/{experimentId}`.
            Mirrors CreatorConfigsPublicApi.Models.Experimentation.CreateExperimentData; updating is
            modeled as a full replace of these fields.
        body (UpdateExperimentData): Request body for
            `PATCH /v1/experimentation/universes/{universeId}/experiments/{experimentId}`.
            Mirrors CreatorConfigsPublicApi.Models.Experimentation.CreateExperimentData; updating is
            modeled as a full replace of these fields.
        body (UpdateExperimentData): Request body for
            `PATCH /v1/experimentation/universes/{universeId}/experiments/{experimentId}`.
            Mirrors CreatorConfigsPublicApi.Models.Experimentation.CreateExperimentData; updating is
            modeled as a full replace of these fields.
        body (UpdateExperimentData): Request body for
            `PATCH /v1/experimentation/universes/{universeId}/experiments/{experimentId}`.
            Mirrors CreatorConfigsPublicApi.Models.Experimentation.CreateExperimentData; updating is
            modeled as a full replace of these fields.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionResult | UpdateExperimentResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        experiment_id=experiment_id,
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: int,
    experiment_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateExperimentData | UpdateExperimentData | UpdateExperimentData | UpdateExperimentData | Unset = UNSET,
) -> ActionResult | UpdateExperimentResponse | None:
    """Updates an existing experiment.

     The payload is a full replacement of the mutable experiment fields. Returns an
    ExperimentOperation describing the async update.

    Args:
        universe_id (int):
        experiment_id (str):
        body (UpdateExperimentData): Request body for
            `PATCH /v1/experimentation/universes/{universeId}/experiments/{experimentId}`.
            Mirrors CreatorConfigsPublicApi.Models.Experimentation.CreateExperimentData; updating is
            modeled as a full replace of these fields.
        body (UpdateExperimentData): Request body for
            `PATCH /v1/experimentation/universes/{universeId}/experiments/{experimentId}`.
            Mirrors CreatorConfigsPublicApi.Models.Experimentation.CreateExperimentData; updating is
            modeled as a full replace of these fields.
        body (UpdateExperimentData): Request body for
            `PATCH /v1/experimentation/universes/{universeId}/experiments/{experimentId}`.
            Mirrors CreatorConfigsPublicApi.Models.Experimentation.CreateExperimentData; updating is
            modeled as a full replace of these fields.
        body (UpdateExperimentData): Request body for
            `PATCH /v1/experimentation/universes/{universeId}/experiments/{experimentId}`.
            Mirrors CreatorConfigsPublicApi.Models.Experimentation.CreateExperimentData; updating is
            modeled as a full replace of these fields.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionResult | UpdateExperimentResponse
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            experiment_id=experiment_id,
            client=client,
            body=body,
        )
    ).parsed
