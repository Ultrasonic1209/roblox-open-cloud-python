from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.game_event_response import GameEventResponse
from ...models.update_game_event_request import UpdateGameEventRequest
from ...models.virtual_events_api_problem_details import VirtualEventsApiProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    event_id: int,
    *,
    body: UpdateGameEventRequest
    | UpdateGameEventRequest
    | UpdateGameEventRequest
    | UpdateGameEventRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/virtual-events/v3/game-events/{event_id}".format(
            event_id=quote(str(event_id), safe=""),
        ),
        "extensions": {
            "openapi-extensions": {
                "x-roblox-stability": "EXPERIMENTAL",
                "x-roblox-rate-limits": {
                    "perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 20},
                    "perOauth2Authorization": {"period": "MINUTE", "maxInPeriod": 20},
                },
                "x-roblox-scopes": [{"name": "universe.event:write", "targetResourceSpecifier": ""}],
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            },
            "openapi-id": "GameEvent_Update",
        },
    }

    if isinstance(body, UpdateGameEventRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, UpdateGameEventRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, UpdateGameEventRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"
    if isinstance(body, UpdateGameEventRequest):
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

    if response.status_code == 404:
        response_404 = VirtualEventsApiProblemDetails.from_dict(response.json())

        return response_404

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
    event_id: int,
    *,
    client: AuthenticatedClient,
    body: UpdateGameEventRequest
    | UpdateGameEventRequest
    | UpdateGameEventRequest
    | UpdateGameEventRequest
    | Unset = UNSET,
) -> Response[GameEventResponse | VirtualEventsApiProblemDetails]:
    """Partially update a game event. Only fields present in the request body are changed; omitted or null
    fields are left
    unchanged. Empty body is a no-op and returns the current game event resource.

    Args:
        event_id (int):
        body (UpdateGameEventRequest | Unset): Request body for `PATCH /v3/game-events/{eventId}`.
            Every field is optional; null = "no change". An empty body is a no-op and returns the
            current resource.
        body (UpdateGameEventRequest | Unset): Request body for `PATCH /v3/game-events/{eventId}`.
            Every field is optional; null = "no change". An empty body is a no-op and returns the
            current resource.
        body (UpdateGameEventRequest | Unset): Request body for `PATCH /v3/game-events/{eventId}`.
            Every field is optional; null = "no change". An empty body is a no-op and returns the
            current resource.
        body (UpdateGameEventRequest | Unset): Request body for `PATCH /v3/game-events/{eventId}`.
            Every field is optional; null = "no change". An empty body is a no-op and returns the
            current resource.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GameEventResponse | VirtualEventsApiProblemDetails]
    """

    kwargs = _get_kwargs(
        event_id=event_id,
        body=body,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    event_id: int,
    *,
    client: AuthenticatedClient,
    body: UpdateGameEventRequest
    | UpdateGameEventRequest
    | UpdateGameEventRequest
    | UpdateGameEventRequest
    | Unset = UNSET,
) -> GameEventResponse | VirtualEventsApiProblemDetails | None:
    """Partially update a game event. Only fields present in the request body are changed; omitted or null
    fields are left
    unchanged. Empty body is a no-op and returns the current game event resource.

    Args:
        event_id (int):
        body (UpdateGameEventRequest | Unset): Request body for `PATCH /v3/game-events/{eventId}`.
            Every field is optional; null = "no change". An empty body is a no-op and returns the
            current resource.
        body (UpdateGameEventRequest | Unset): Request body for `PATCH /v3/game-events/{eventId}`.
            Every field is optional; null = "no change". An empty body is a no-op and returns the
            current resource.
        body (UpdateGameEventRequest | Unset): Request body for `PATCH /v3/game-events/{eventId}`.
            Every field is optional; null = "no change". An empty body is a no-op and returns the
            current resource.
        body (UpdateGameEventRequest | Unset): Request body for `PATCH /v3/game-events/{eventId}`.
            Every field is optional; null = "no change". An empty body is a no-op and returns the
            current resource.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GameEventResponse | VirtualEventsApiProblemDetails
    """

    return sync_detailed(
        event_id=event_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    event_id: int,
    *,
    client: AuthenticatedClient,
    body: UpdateGameEventRequest
    | UpdateGameEventRequest
    | UpdateGameEventRequest
    | UpdateGameEventRequest
    | Unset = UNSET,
) -> Response[GameEventResponse | VirtualEventsApiProblemDetails]:
    """Partially update a game event. Only fields present in the request body are changed; omitted or null
    fields are left
    unchanged. Empty body is a no-op and returns the current game event resource.

    Args:
        event_id (int):
        body (UpdateGameEventRequest | Unset): Request body for `PATCH /v3/game-events/{eventId}`.
            Every field is optional; null = "no change". An empty body is a no-op and returns the
            current resource.
        body (UpdateGameEventRequest | Unset): Request body for `PATCH /v3/game-events/{eventId}`.
            Every field is optional; null = "no change". An empty body is a no-op and returns the
            current resource.
        body (UpdateGameEventRequest | Unset): Request body for `PATCH /v3/game-events/{eventId}`.
            Every field is optional; null = "no change". An empty body is a no-op and returns the
            current resource.
        body (UpdateGameEventRequest | Unset): Request body for `PATCH /v3/game-events/{eventId}`.
            Every field is optional; null = "no change". An empty body is a no-op and returns the
            current resource.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GameEventResponse | VirtualEventsApiProblemDetails]
    """

    kwargs = _get_kwargs(
        event_id=event_id,
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    event_id: int,
    *,
    client: AuthenticatedClient,
    body: UpdateGameEventRequest
    | UpdateGameEventRequest
    | UpdateGameEventRequest
    | UpdateGameEventRequest
    | Unset = UNSET,
) -> GameEventResponse | VirtualEventsApiProblemDetails | None:
    """Partially update a game event. Only fields present in the request body are changed; omitted or null
    fields are left
    unchanged. Empty body is a no-op and returns the current game event resource.

    Args:
        event_id (int):
        body (UpdateGameEventRequest | Unset): Request body for `PATCH /v3/game-events/{eventId}`.
            Every field is optional; null = "no change". An empty body is a no-op and returns the
            current resource.
        body (UpdateGameEventRequest | Unset): Request body for `PATCH /v3/game-events/{eventId}`.
            Every field is optional; null = "no change". An empty body is a no-op and returns the
            current resource.
        body (UpdateGameEventRequest | Unset): Request body for `PATCH /v3/game-events/{eventId}`.
            Every field is optional; null = "no change". An empty body is a no-op and returns the
            current resource.
        body (UpdateGameEventRequest | Unset): Request body for `PATCH /v3/game-events/{eventId}`.
            Every field is optional; null = "no change". An empty body is a no-op and returns the
            current resource.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GameEventResponse | VirtualEventsApiProblemDetails
    """

    return (
        await asyncio_detailed(
            event_id=event_id,
            client=client,
            body=body,
        )
    ).parsed
