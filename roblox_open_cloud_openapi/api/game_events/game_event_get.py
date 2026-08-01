from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.game_event_response import GameEventResponse
from ...models.virtual_events_api_problem_details import VirtualEventsApiProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    event_id: int,
    *,
    fields: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["fields"] = fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/virtual-events/v3/game-events/{event_id}".format(
            event_id=quote(str(event_id), safe=""),
        ),
        "params": params,
        "extensions": {
            "openapi-extensions": {
                "x-roblox-stability": "EXPERIMENTAL",
                "x-roblox-rate-limits": {
                    "perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 100},
                    "perOauth2Authorization": {"period": "MINUTE", "maxInPeriod": 100},
                },
                "x-roblox-scopes": [{"name": "universe.event:read", "targetResourceSpecifier": ""}],
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            },
            "openapi-id": "GameEvent_Get",
        },
    }

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
    fields: str | Unset = UNSET,
) -> Response[GameEventResponse | VirtualEventsApiProblemDetails]:
    """Get a single game event by ID.
    Use `?fields=` to request a subset of fields; unknown field names return 400.

    Args:
        event_id (int):
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GameEventResponse | VirtualEventsApiProblemDetails]
    """

    kwargs = _get_kwargs(
        event_id=event_id,
        fields=fields,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    event_id: int,
    *,
    client: AuthenticatedClient,
    fields: str | Unset = UNSET,
) -> GameEventResponse | VirtualEventsApiProblemDetails | None:
    """Get a single game event by ID.
    Use `?fields=` to request a subset of fields; unknown field names return 400.

    Args:
        event_id (int):
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GameEventResponse | VirtualEventsApiProblemDetails
    """

    return sync_detailed(
        event_id=event_id,
        client=client,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    event_id: int,
    *,
    client: AuthenticatedClient,
    fields: str | Unset = UNSET,
) -> Response[GameEventResponse | VirtualEventsApiProblemDetails]:
    """Get a single game event by ID.
    Use `?fields=` to request a subset of fields; unknown field names return 400.

    Args:
        event_id (int):
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GameEventResponse | VirtualEventsApiProblemDetails]
    """

    kwargs = _get_kwargs(
        event_id=event_id,
        fields=fields,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    event_id: int,
    *,
    client: AuthenticatedClient,
    fields: str | Unset = UNSET,
) -> GameEventResponse | VirtualEventsApiProblemDetails | None:
    """Get a single game event by ID.
    Use `?fields=` to request a subset of fields; unknown field names return 400.

    Args:
        event_id (int):
        fields (str | Unset):

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
            fields=fields,
        )
    ).parsed
