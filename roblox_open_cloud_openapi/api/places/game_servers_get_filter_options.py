from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.filter_field import FilterField
from ...models.filter_options_response import FilterOptionsResponse
from ...models.server_management_service_problem_details import ServerManagementServiceProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    universe_id: int,
    place_id: int,
    *,
    filter_: FilterField | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_filter_: str | Unset = UNSET
    if not isinstance(filter_, Unset):
        json_filter_ = filter_.value

    params["Filter"] = json_filter_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/server-management/v1/universes/{universe_id}/places/{place_id}/game-servers:filter-options".format(
            universe_id=quote(str(universe_id), safe=""),
            place_id=quote(str(place_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FilterOptionsResponse | ServerManagementServiceProblemDetails | None:
    if response.status_code == 200:
        response_200 = FilterOptionsResponse.from_dict(response.json())

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
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[FilterOptionsResponse | ServerManagementServiceProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    universe_id: int,
    place_id: int,
    *,
    client: AuthenticatedClient,
    filter_: FilterField | Unset = UNSET,
) -> Response[FilterOptionsResponse | ServerManagementServiceProblemDetails]:
    """Gets available filter options for game servers.

    Args:
        universe_id (int):
        place_id (int):
        filter_ (FilterField | Unset): Enum describing the different available filter fields.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FilterOptionsResponse | ServerManagementServiceProblemDetails]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        place_id=place_id,
        filter_=filter_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: int,
    place_id: int,
    *,
    client: AuthenticatedClient,
    filter_: FilterField | Unset = UNSET,
) -> FilterOptionsResponse | ServerManagementServiceProblemDetails | None:
    """Gets available filter options for game servers.

    Args:
        universe_id (int):
        place_id (int):
        filter_ (FilterField | Unset): Enum describing the different available filter fields.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FilterOptionsResponse | ServerManagementServiceProblemDetails
    """

    return sync_detailed(
        universe_id=universe_id,
        place_id=place_id,
        client=client,
        filter_=filter_,
    ).parsed


async def asyncio_detailed(
    universe_id: int,
    place_id: int,
    *,
    client: AuthenticatedClient,
    filter_: FilterField | Unset = UNSET,
) -> Response[FilterOptionsResponse | ServerManagementServiceProblemDetails]:
    """Gets available filter options for game servers.

    Args:
        universe_id (int):
        place_id (int):
        filter_ (FilterField | Unset): Enum describing the different available filter fields.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FilterOptionsResponse | ServerManagementServiceProblemDetails]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        place_id=place_id,
        filter_=filter_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: int,
    place_id: int,
    *,
    client: AuthenticatedClient,
    filter_: FilterField | Unset = UNSET,
) -> FilterOptionsResponse | ServerManagementServiceProblemDetails | None:
    """Gets available filter options for game servers.

    Args:
        universe_id (int):
        place_id (int):
        filter_ (FilterField | Unset): Enum describing the different available filter fields.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FilterOptionsResponse | ServerManagementServiceProblemDetails
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            place_id=place_id,
            client=client,
            filter_=filter_,
        )
    ).parsed
