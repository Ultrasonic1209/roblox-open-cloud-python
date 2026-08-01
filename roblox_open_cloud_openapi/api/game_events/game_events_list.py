import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.event_visibility import EventVisibility
from ...models.paginated_game_events_response import PaginatedGameEventsResponse
from ...models.virtual_events_api_problem_details import VirtualEventsApiProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    universe_id: int,
    *,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    reverse: bool | Unset = False,
    starts_before: datetime.datetime | Unset = UNSET,
    starts_after: datetime.datetime | Unset = UNSET,
    ends_before: datetime.datetime | Unset = UNSET,
    ends_after: datetime.datetime | Unset = UNSET,
    visibility: EventVisibility | Unset = UNSET,
    fields: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["pageSize"] = page_size

    params["pageToken"] = page_token

    params["reverse"] = reverse

    json_starts_before: str | Unset = UNSET
    if not isinstance(starts_before, Unset):
        json_starts_before = starts_before.isoformat()
    params["startsBefore"] = json_starts_before

    json_starts_after: str | Unset = UNSET
    if not isinstance(starts_after, Unset):
        json_starts_after = starts_after.isoformat()
    params["startsAfter"] = json_starts_after

    json_ends_before: str | Unset = UNSET
    if not isinstance(ends_before, Unset):
        json_ends_before = ends_before.isoformat()
    params["endsBefore"] = json_ends_before

    json_ends_after: str | Unset = UNSET
    if not isinstance(ends_after, Unset):
        json_ends_after = ends_after.isoformat()
    params["endsAfter"] = json_ends_after

    json_visibility: str | Unset = UNSET
    if not isinstance(visibility, Unset):
        json_visibility = visibility.value

    params["visibility"] = json_visibility

    params["fields"] = fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/virtual-events/v3/universes/{universe_id}/game-events".format(
            universe_id=quote(str(universe_id), safe=""),
        ),
        "params": params,
        "extensions": {
            "openapi-extensions": {
                "x-roblox-stability": "EXPERIMENTAL",
                "x-roblox-rate-limits": {
                    "perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 100},
                    "perOauth2Authorization": {"period": "MINUTE", "maxInPeriod": 100},
                },
                "x-roblox-scopes": [{"name": "universe.event:read", "targetResourceSpecifier": "universes"}],
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            },
            "openapi-id": "GameEvents_List",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> PaginatedGameEventsResponse | VirtualEventsApiProblemDetails | None:
    if response.status_code == 200:
        response_200 = PaginatedGameEventsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = VirtualEventsApiProblemDetails.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[PaginatedGameEventsResponse | VirtualEventsApiProblemDetails]:
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
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    reverse: bool | Unset = False,
    starts_before: datetime.datetime | Unset = UNSET,
    starts_after: datetime.datetime | Unset = UNSET,
    ends_before: datetime.datetime | Unset = UNSET,
    ends_after: datetime.datetime | Unset = UNSET,
    visibility: EventVisibility | Unset = UNSET,
    fields: str | Unset = UNSET,
) -> Response[PaginatedGameEventsResponse | VirtualEventsApiProblemDetails]:
    """List game events under a universe.
    Use `?fields=` to trim the response payload.
    Response is always 200 (empty list for unknown universe).

    Args:
        universe_id (int):
        page_size (int | Unset):
        page_token (str | Unset):
        reverse (bool | Unset):  Default: False.
        starts_before (datetime.datetime | Unset):
        starts_after (datetime.datetime | Unset):
        ends_before (datetime.datetime | Unset):
        ends_after (datetime.datetime | Unset):
        visibility (EventVisibility | Unset): The visibility of a virtual event.
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedGameEventsResponse | VirtualEventsApiProblemDetails]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        page_size=page_size,
        page_token=page_token,
        reverse=reverse,
        starts_before=starts_before,
        starts_after=starts_after,
        ends_before=ends_before,
        ends_after=ends_after,
        visibility=visibility,
        fields=fields,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    reverse: bool | Unset = False,
    starts_before: datetime.datetime | Unset = UNSET,
    starts_after: datetime.datetime | Unset = UNSET,
    ends_before: datetime.datetime | Unset = UNSET,
    ends_after: datetime.datetime | Unset = UNSET,
    visibility: EventVisibility | Unset = UNSET,
    fields: str | Unset = UNSET,
) -> PaginatedGameEventsResponse | VirtualEventsApiProblemDetails | None:
    """List game events under a universe.
    Use `?fields=` to trim the response payload.
    Response is always 200 (empty list for unknown universe).

    Args:
        universe_id (int):
        page_size (int | Unset):
        page_token (str | Unset):
        reverse (bool | Unset):  Default: False.
        starts_before (datetime.datetime | Unset):
        starts_after (datetime.datetime | Unset):
        ends_before (datetime.datetime | Unset):
        ends_after (datetime.datetime | Unset):
        visibility (EventVisibility | Unset): The visibility of a virtual event.
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedGameEventsResponse | VirtualEventsApiProblemDetails
    """

    return sync_detailed(
        universe_id=universe_id,
        client=client,
        page_size=page_size,
        page_token=page_token,
        reverse=reverse,
        starts_before=starts_before,
        starts_after=starts_after,
        ends_before=ends_before,
        ends_after=ends_after,
        visibility=visibility,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    reverse: bool | Unset = False,
    starts_before: datetime.datetime | Unset = UNSET,
    starts_after: datetime.datetime | Unset = UNSET,
    ends_before: datetime.datetime | Unset = UNSET,
    ends_after: datetime.datetime | Unset = UNSET,
    visibility: EventVisibility | Unset = UNSET,
    fields: str | Unset = UNSET,
) -> Response[PaginatedGameEventsResponse | VirtualEventsApiProblemDetails]:
    """List game events under a universe.
    Use `?fields=` to trim the response payload.
    Response is always 200 (empty list for unknown universe).

    Args:
        universe_id (int):
        page_size (int | Unset):
        page_token (str | Unset):
        reverse (bool | Unset):  Default: False.
        starts_before (datetime.datetime | Unset):
        starts_after (datetime.datetime | Unset):
        ends_before (datetime.datetime | Unset):
        ends_after (datetime.datetime | Unset):
        visibility (EventVisibility | Unset): The visibility of a virtual event.
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedGameEventsResponse | VirtualEventsApiProblemDetails]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        page_size=page_size,
        page_token=page_token,
        reverse=reverse,
        starts_before=starts_before,
        starts_after=starts_after,
        ends_before=ends_before,
        ends_after=ends_after,
        visibility=visibility,
        fields=fields,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    reverse: bool | Unset = False,
    starts_before: datetime.datetime | Unset = UNSET,
    starts_after: datetime.datetime | Unset = UNSET,
    ends_before: datetime.datetime | Unset = UNSET,
    ends_after: datetime.datetime | Unset = UNSET,
    visibility: EventVisibility | Unset = UNSET,
    fields: str | Unset = UNSET,
) -> PaginatedGameEventsResponse | VirtualEventsApiProblemDetails | None:
    """List game events under a universe.
    Use `?fields=` to trim the response payload.
    Response is always 200 (empty list for unknown universe).

    Args:
        universe_id (int):
        page_size (int | Unset):
        page_token (str | Unset):
        reverse (bool | Unset):  Default: False.
        starts_before (datetime.datetime | Unset):
        starts_after (datetime.datetime | Unset):
        ends_before (datetime.datetime | Unset):
        ends_after (datetime.datetime | Unset):
        visibility (EventVisibility | Unset): The visibility of a virtual event.
        fields (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedGameEventsResponse | VirtualEventsApiProblemDetails
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            client=client,
            page_size=page_size,
            page_token=page_token,
            reverse=reverse,
            starts_before=starts_before,
            starts_after=starts_after,
            ends_before=ends_before,
            ends_after=ends_after,
            visibility=visibility,
            fields=fields,
        )
    ).parsed
