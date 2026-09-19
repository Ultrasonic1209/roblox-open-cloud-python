from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.virtual_events_api_problem_details import VirtualEventsApiProblemDetails
from ...types import Response


def _get_kwargs(
    event_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
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
            "openapi-id": "GameEvent_Delete",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | VirtualEventsApiProblemDetails | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = VirtualEventsApiProblemDetails.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = VirtualEventsApiProblemDetails.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = VirtualEventsApiProblemDetails.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = VirtualEventsApiProblemDetails.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | VirtualEventsApiProblemDetails]:
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
) -> Response[Any | VirtualEventsApiProblemDetails]:
    """Permanently delete an existing game event. Returns 204 No Content on success.
    Permission is enforced via an explicit pre-check: callers that can read but not edit
    receive 403; callers that cannot read receive 404.

    Args:
        event_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | VirtualEventsApiProblemDetails]
    """

    kwargs = _get_kwargs(
        event_id=event_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    event_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | VirtualEventsApiProblemDetails | None:
    """Permanently delete an existing game event. Returns 204 No Content on success.
    Permission is enforced via an explicit pre-check: callers that can read but not edit
    receive 403; callers that cannot read receive 404.

    Args:
        event_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | VirtualEventsApiProblemDetails
    """

    return sync_detailed(
        event_id=event_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    event_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | VirtualEventsApiProblemDetails]:
    """Permanently delete an existing game event. Returns 204 No Content on success.
    Permission is enforced via an explicit pre-check: callers that can read but not edit
    receive 403; callers that cannot read receive 404.

    Args:
        event_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | VirtualEventsApiProblemDetails]
    """

    kwargs = _get_kwargs(
        event_id=event_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    event_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | VirtualEventsApiProblemDetails | None:
    """Permanently delete an existing game event. Returns 204 No Content on success.
    Permission is enforced via an explicit pre-check: callers that can read but not edit
    receive 403; callers that cannot read receive 404.

    Args:
        event_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | VirtualEventsApiProblemDetails
    """

    return (
        await asyncio_detailed(
            event_id=event_id,
            client=client,
        )
    ).parsed
