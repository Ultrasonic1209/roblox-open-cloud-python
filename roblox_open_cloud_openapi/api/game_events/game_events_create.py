from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_game_event_request import CreateGameEventRequest
from ...models.game_event_response import GameEventResponse
from ...models.virtual_events_api_problem_details import VirtualEventsApiProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    universe_id: int,
    *,
    body: CreateGameEventRequest
    | CreateGameEventRequest
    | CreateGameEventRequest
    | CreateGameEventRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/virtual-events/v3/universes/{universe_id}/game-events".format(
            universe_id=quote(str(universe_id), safe=""),
        ),
        "extensions": {
            "openapi-extensions": {
                "x-roblox-stability": "EXPERIMENTAL",
                "x-roblox-rate-limits": {
                    "perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 20},
                    "perOauth2Authorization": {"period": "MINUTE", "maxInPeriod": 20},
                },
                "x-roblox-scopes": [{"name": "universe.event:write", "targetResourceSpecifier": "universes"}],
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            },
            "openapi-id": "GameEvents_Create",
        },
    }

    if isinstance(body, CreateGameEventRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, CreateGameEventRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CreateGameEventRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"
    if isinstance(body, CreateGameEventRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> GameEventResponse | VirtualEventsApiProblemDetails | None:
    if response.status_code == 200:
        response_200 = GameEventResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = VirtualEventsApiProblemDetails.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = VirtualEventsApiProblemDetails.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = VirtualEventsApiProblemDetails.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[GameEventResponse | VirtualEventsApiProblemDetails]:
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
    body: CreateGameEventRequest
    | CreateGameEventRequest
    | CreateGameEventRequest
    | CreateGameEventRequest
    | Unset = UNSET,
) -> Response[GameEventResponse | VirtualEventsApiProblemDetails]:
    """Create a new game event. Returns the full resource on success.

    Args:
        universe_id (int):
        body (CreateGameEventRequest | Unset): Request body for `POST
            /v3/universes/{universeId}/game-events`.
            `universeId` comes from the URL path, not the body.
            VirtualEventsApi.Models.V3.Request.CreateGameEventRequest.Visibility is restricted to
            Public/Private — Moderated is server-side only.
            Nullable CLR properties allow JSON binding to materialize incomplete requests; required
            fields are enforced by the virtual-events gRPC service when `CreateVirtualEvent` runs.
        body (CreateGameEventRequest | Unset): Request body for `POST
            /v3/universes/{universeId}/game-events`.
            `universeId` comes from the URL path, not the body.
            VirtualEventsApi.Models.V3.Request.CreateGameEventRequest.Visibility is restricted to
            Public/Private — Moderated is server-side only.
            Nullable CLR properties allow JSON binding to materialize incomplete requests; required
            fields are enforced by the virtual-events gRPC service when `CreateVirtualEvent` runs.
        body (CreateGameEventRequest | Unset): Request body for `POST
            /v3/universes/{universeId}/game-events`.
            `universeId` comes from the URL path, not the body.
            VirtualEventsApi.Models.V3.Request.CreateGameEventRequest.Visibility is restricted to
            Public/Private — Moderated is server-side only.
            Nullable CLR properties allow JSON binding to materialize incomplete requests; required
            fields are enforced by the virtual-events gRPC service when `CreateVirtualEvent` runs.
        body (CreateGameEventRequest | Unset): Request body for `POST
            /v3/universes/{universeId}/game-events`.
            `universeId` comes from the URL path, not the body.
            VirtualEventsApi.Models.V3.Request.CreateGameEventRequest.Visibility is restricted to
            Public/Private — Moderated is server-side only.
            Nullable CLR properties allow JSON binding to materialize incomplete requests; required
            fields are enforced by the virtual-events gRPC service when `CreateVirtualEvent` runs.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GameEventResponse | VirtualEventsApiProblemDetails]
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
    body: CreateGameEventRequest
    | CreateGameEventRequest
    | CreateGameEventRequest
    | CreateGameEventRequest
    | Unset = UNSET,
) -> GameEventResponse | VirtualEventsApiProblemDetails | None:
    """Create a new game event. Returns the full resource on success.

    Args:
        universe_id (int):
        body (CreateGameEventRequest | Unset): Request body for `POST
            /v3/universes/{universeId}/game-events`.
            `universeId` comes from the URL path, not the body.
            VirtualEventsApi.Models.V3.Request.CreateGameEventRequest.Visibility is restricted to
            Public/Private — Moderated is server-side only.
            Nullable CLR properties allow JSON binding to materialize incomplete requests; required
            fields are enforced by the virtual-events gRPC service when `CreateVirtualEvent` runs.
        body (CreateGameEventRequest | Unset): Request body for `POST
            /v3/universes/{universeId}/game-events`.
            `universeId` comes from the URL path, not the body.
            VirtualEventsApi.Models.V3.Request.CreateGameEventRequest.Visibility is restricted to
            Public/Private — Moderated is server-side only.
            Nullable CLR properties allow JSON binding to materialize incomplete requests; required
            fields are enforced by the virtual-events gRPC service when `CreateVirtualEvent` runs.
        body (CreateGameEventRequest | Unset): Request body for `POST
            /v3/universes/{universeId}/game-events`.
            `universeId` comes from the URL path, not the body.
            VirtualEventsApi.Models.V3.Request.CreateGameEventRequest.Visibility is restricted to
            Public/Private — Moderated is server-side only.
            Nullable CLR properties allow JSON binding to materialize incomplete requests; required
            fields are enforced by the virtual-events gRPC service when `CreateVirtualEvent` runs.
        body (CreateGameEventRequest | Unset): Request body for `POST
            /v3/universes/{universeId}/game-events`.
            `universeId` comes from the URL path, not the body.
            VirtualEventsApi.Models.V3.Request.CreateGameEventRequest.Visibility is restricted to
            Public/Private — Moderated is server-side only.
            Nullable CLR properties allow JSON binding to materialize incomplete requests; required
            fields are enforced by the virtual-events gRPC service when `CreateVirtualEvent` runs.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GameEventResponse | VirtualEventsApiProblemDetails
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
    body: CreateGameEventRequest
    | CreateGameEventRequest
    | CreateGameEventRequest
    | CreateGameEventRequest
    | Unset = UNSET,
) -> Response[GameEventResponse | VirtualEventsApiProblemDetails]:
    """Create a new game event. Returns the full resource on success.

    Args:
        universe_id (int):
        body (CreateGameEventRequest | Unset): Request body for `POST
            /v3/universes/{universeId}/game-events`.
            `universeId` comes from the URL path, not the body.
            VirtualEventsApi.Models.V3.Request.CreateGameEventRequest.Visibility is restricted to
            Public/Private — Moderated is server-side only.
            Nullable CLR properties allow JSON binding to materialize incomplete requests; required
            fields are enforced by the virtual-events gRPC service when `CreateVirtualEvent` runs.
        body (CreateGameEventRequest | Unset): Request body for `POST
            /v3/universes/{universeId}/game-events`.
            `universeId` comes from the URL path, not the body.
            VirtualEventsApi.Models.V3.Request.CreateGameEventRequest.Visibility is restricted to
            Public/Private — Moderated is server-side only.
            Nullable CLR properties allow JSON binding to materialize incomplete requests; required
            fields are enforced by the virtual-events gRPC service when `CreateVirtualEvent` runs.
        body (CreateGameEventRequest | Unset): Request body for `POST
            /v3/universes/{universeId}/game-events`.
            `universeId` comes from the URL path, not the body.
            VirtualEventsApi.Models.V3.Request.CreateGameEventRequest.Visibility is restricted to
            Public/Private — Moderated is server-side only.
            Nullable CLR properties allow JSON binding to materialize incomplete requests; required
            fields are enforced by the virtual-events gRPC service when `CreateVirtualEvent` runs.
        body (CreateGameEventRequest | Unset): Request body for `POST
            /v3/universes/{universeId}/game-events`.
            `universeId` comes from the URL path, not the body.
            VirtualEventsApi.Models.V3.Request.CreateGameEventRequest.Visibility is restricted to
            Public/Private — Moderated is server-side only.
            Nullable CLR properties allow JSON binding to materialize incomplete requests; required
            fields are enforced by the virtual-events gRPC service when `CreateVirtualEvent` runs.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GameEventResponse | VirtualEventsApiProblemDetails]
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
    body: CreateGameEventRequest
    | CreateGameEventRequest
    | CreateGameEventRequest
    | CreateGameEventRequest
    | Unset = UNSET,
) -> GameEventResponse | VirtualEventsApiProblemDetails | None:
    """Create a new game event. Returns the full resource on success.

    Args:
        universe_id (int):
        body (CreateGameEventRequest | Unset): Request body for `POST
            /v3/universes/{universeId}/game-events`.
            `universeId` comes from the URL path, not the body.
            VirtualEventsApi.Models.V3.Request.CreateGameEventRequest.Visibility is restricted to
            Public/Private — Moderated is server-side only.
            Nullable CLR properties allow JSON binding to materialize incomplete requests; required
            fields are enforced by the virtual-events gRPC service when `CreateVirtualEvent` runs.
        body (CreateGameEventRequest | Unset): Request body for `POST
            /v3/universes/{universeId}/game-events`.
            `universeId` comes from the URL path, not the body.
            VirtualEventsApi.Models.V3.Request.CreateGameEventRequest.Visibility is restricted to
            Public/Private — Moderated is server-side only.
            Nullable CLR properties allow JSON binding to materialize incomplete requests; required
            fields are enforced by the virtual-events gRPC service when `CreateVirtualEvent` runs.
        body (CreateGameEventRequest | Unset): Request body for `POST
            /v3/universes/{universeId}/game-events`.
            `universeId` comes from the URL path, not the body.
            VirtualEventsApi.Models.V3.Request.CreateGameEventRequest.Visibility is restricted to
            Public/Private — Moderated is server-side only.
            Nullable CLR properties allow JSON binding to materialize incomplete requests; required
            fields are enforced by the virtual-events gRPC service when `CreateVirtualEvent` runs.
        body (CreateGameEventRequest | Unset): Request body for `POST
            /v3/universes/{universeId}/game-events`.
            `universeId` comes from the URL path, not the body.
            VirtualEventsApi.Models.V3.Request.CreateGameEventRequest.Visibility is restricted to
            Public/Private — Moderated is server-side only.
            Nullable CLR properties allow JSON binding to materialize incomplete requests; required
            fields are enforced by the virtual-events gRPC service when `CreateVirtualEvent` runs.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GameEventResponse | VirtualEventsApiProblemDetails
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            client=client,
            body=body,
        )
    ).parsed
