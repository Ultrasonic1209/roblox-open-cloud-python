from http import HTTPStatus
from typing import TYPE_CHECKING, Any, cast
from urllib.parse import quote

if TYPE_CHECKING:
    import httpx2 as httpx
else:
    try:
        import httpx2 as httpx
    except ModuleNotFoundError:
        try:
            import httpx
        except ModuleNotFoundError:
            raise RuntimeError(
                "This module requires the httpx2 package to be installed.\n"
                "You can install it with:\n"
                "    $ pip install httpx2\n"
            ) from None


from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response

"""
{'x-roblox-stability': 'BETA', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'MINUTE', 'maxInPeriod': 100}, 'perOauth2Authorization': {'period': 'MINUTE', 'maxInPeriod': 100}}, 'x-roblox-scopes': [{'name': 'universe:read', 'targetResourceSpecifier': 'universes'}], 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.list_client_logs_response import ListClientLogsResponse
from ...models.server_management_service_problem_details import ServerManagementServiceProblemDetails
from ...types import Unset


def _get_kwargs(
    universe_id: int,
    place_id: int,
    job_id: str,
    session_id: str,
    *,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    order_by: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["MaxPageSize"] = max_page_size

    params["PageToken"] = page_token

    params["OrderBy"] = order_by

    params["Filter"] = filter_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/server-management/v1/universes/{universe_id}/places/{place_id}/game-servers/{job_id}/client-sessions/{session_id}/logs".format(
            universe_id=quote(str(universe_id), safe=""),
            place_id=quote(str(place_id), safe=""),
            job_id=quote(str(job_id), safe=""),
            session_id=quote(str(session_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ListClientLogsResponse | ServerManagementServiceProblemDetails | None:
    if response.status_code == 200:
        response_200 = ListClientLogsResponse.from_dict(response.json())

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

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ListClientLogsResponse | ServerManagementServiceProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    universe_id: int,
    place_id: int,
    job_id: str,
    session_id: str,
    *,
    client: AuthenticatedClient,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    order_by: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
) -> Response[Any | ListClientLogsResponse | ServerManagementServiceProblemDetails]:
    """Lists client log entries emitted during a play session on a game server.

     Requires an authenticated caller with read access to the universe. `sessionId` must be a
    non-zero UUID. Results default to `message_timestamp desc` when `orderBy` is omitted.

    Args:
        universe_id (int):
        place_id (int):
        job_id (str):
        session_id (str):
        max_page_size (int | Unset):
        page_token (str | Unset):
        order_by (str | Unset):
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ListClientLogsResponse | ServerManagementServiceProblemDetails]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        place_id=place_id,
        job_id=job_id,
        session_id=session_id,
        max_page_size=max_page_size,
        page_token=page_token,
        order_by=order_by,
        filter_=filter_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: int,
    place_id: int,
    job_id: str,
    session_id: str,
    *,
    client: AuthenticatedClient,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    order_by: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
) -> Any | ListClientLogsResponse | ServerManagementServiceProblemDetails | None:
    """Lists client log entries emitted during a play session on a game server.

     Requires an authenticated caller with read access to the universe. `sessionId` must be a
    non-zero UUID. Results default to `message_timestamp desc` when `orderBy` is omitted.

    Args:
        universe_id (int):
        place_id (int):
        job_id (str):
        session_id (str):
        max_page_size (int | Unset):
        page_token (str | Unset):
        order_by (str | Unset):
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ListClientLogsResponse | ServerManagementServiceProblemDetails
    """

    return sync_detailed(
        universe_id=universe_id,
        place_id=place_id,
        job_id=job_id,
        session_id=session_id,
        client=client,
        max_page_size=max_page_size,
        page_token=page_token,
        order_by=order_by,
        filter_=filter_,
    ).parsed


async def asyncio_detailed(
    universe_id: int,
    place_id: int,
    job_id: str,
    session_id: str,
    *,
    client: AuthenticatedClient,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    order_by: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
) -> Response[Any | ListClientLogsResponse | ServerManagementServiceProblemDetails]:
    """Lists client log entries emitted during a play session on a game server.

     Requires an authenticated caller with read access to the universe. `sessionId` must be a
    non-zero UUID. Results default to `message_timestamp desc` when `orderBy` is omitted.

    Args:
        universe_id (int):
        place_id (int):
        job_id (str):
        session_id (str):
        max_page_size (int | Unset):
        page_token (str | Unset):
        order_by (str | Unset):
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ListClientLogsResponse | ServerManagementServiceProblemDetails]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        place_id=place_id,
        job_id=job_id,
        session_id=session_id,
        max_page_size=max_page_size,
        page_token=page_token,
        order_by=order_by,
        filter_=filter_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: int,
    place_id: int,
    job_id: str,
    session_id: str,
    *,
    client: AuthenticatedClient,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    order_by: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
) -> Any | ListClientLogsResponse | ServerManagementServiceProblemDetails | None:
    """Lists client log entries emitted during a play session on a game server.

     Requires an authenticated caller with read access to the universe. `sessionId` must be a
    non-zero UUID. Results default to `message_timestamp desc` when `orderBy` is omitted.

    Args:
        universe_id (int):
        place_id (int):
        job_id (str):
        session_id (str):
        max_page_size (int | Unset):
        page_token (str | Unset):
        order_by (str | Unset):
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ListClientLogsResponse | ServerManagementServiceProblemDetails
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            place_id=place_id,
            job_id=job_id,
            session_id=session_id,
            client=client,
            max_page_size=max_page_size,
            page_token=page_token,
            order_by=order_by,
            filter_=filter_,
        )
    ).parsed
