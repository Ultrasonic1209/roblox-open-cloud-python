from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.server_management_service_list_game_servers_response import (
    ServerManagementServiceListGameServersResponse,
)
from ...models.server_management_service_problem_details import ServerManagementServiceProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    universe_id: int,
    place_id: int,
    version_number: str,
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
        "url": "/server-management/v1/universes/{universe_id}/places/{place_id}/versions/{version_number}/game-servers".format(
            universe_id=quote(str(universe_id), safe=""),
            place_id=quote(str(place_id), safe=""),
            version_number=quote(str(version_number), safe=""),
        ),
        "params": params,
        "openapi-extensions": {
            "x-roblox-stability": "BETA",
            "x-roblox-rate-limits": {
                "perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 100},
                "perOauth2Authorization": {"period": "MINUTE", "maxInPeriod": 100},
            },
            "x-roblox-scopes": [{"name": "universe:read", "targetResourceSpecifier": "universes"}],
            "x-roblox-engine-usability": {"apiKeyWithHttpService": True},
        },
        "openapi-id": "GameServers_ListGameServers",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ServerManagementServiceListGameServersResponse | ServerManagementServiceProblemDetails | None:
    if response.status_code == 200:
        response_200 = ServerManagementServiceListGameServersResponse.from_dict(response.json())

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
) -> Response[ServerManagementServiceListGameServersResponse | ServerManagementServiceProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    universe_id: int,
    place_id: int,
    version_number: str,
    *,
    client: AuthenticatedClient,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    order_by: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
) -> Response[ServerManagementServiceListGameServersResponse | ServerManagementServiceProblemDetails]:
    """Lists game servers for a specific place version.

    Args:
        universe_id (int):
        place_id (int):
        version_number (str):
        max_page_size (int | Unset):
        page_token (str | Unset):
        order_by (str | Unset):
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServerManagementServiceListGameServersResponse | ServerManagementServiceProblemDetails]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        place_id=place_id,
        version_number=version_number,
        max_page_size=max_page_size,
        page_token=page_token,
        order_by=order_by,
        filter_=filter_,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: int,
    place_id: int,
    version_number: str,
    *,
    client: AuthenticatedClient,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    order_by: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
) -> ServerManagementServiceListGameServersResponse | ServerManagementServiceProblemDetails | None:
    """Lists game servers for a specific place version.

    Args:
        universe_id (int):
        place_id (int):
        version_number (str):
        max_page_size (int | Unset):
        page_token (str | Unset):
        order_by (str | Unset):
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServerManagementServiceListGameServersResponse | ServerManagementServiceProblemDetails
    """

    return sync_detailed(
        universe_id=universe_id,
        place_id=place_id,
        version_number=version_number,
        client=client,
        max_page_size=max_page_size,
        page_token=page_token,
        order_by=order_by,
        filter_=filter_,
    ).parsed


async def asyncio_detailed(
    universe_id: int,
    place_id: int,
    version_number: str,
    *,
    client: AuthenticatedClient,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    order_by: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
) -> Response[ServerManagementServiceListGameServersResponse | ServerManagementServiceProblemDetails]:
    """Lists game servers for a specific place version.

    Args:
        universe_id (int):
        place_id (int):
        version_number (str):
        max_page_size (int | Unset):
        page_token (str | Unset):
        order_by (str | Unset):
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ServerManagementServiceListGameServersResponse | ServerManagementServiceProblemDetails]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        place_id=place_id,
        version_number=version_number,
        max_page_size=max_page_size,
        page_token=page_token,
        order_by=order_by,
        filter_=filter_,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: int,
    place_id: int,
    version_number: str,
    *,
    client: AuthenticatedClient,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    order_by: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
) -> ServerManagementServiceListGameServersResponse | ServerManagementServiceProblemDetails | None:
    """Lists game servers for a specific place version.

    Args:
        universe_id (int):
        place_id (int):
        version_number (str):
        max_page_size (int | Unset):
        page_token (str | Unset):
        order_by (str | Unset):
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ServerManagementServiceListGameServersResponse | ServerManagementServiceProblemDetails
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            place_id=place_id,
            version_number=version_number,
            client=client,
            max_page_size=max_page_size,
            page_token=page_token,
            order_by=order_by,
            filter_=filter_,
        )
    ).parsed
