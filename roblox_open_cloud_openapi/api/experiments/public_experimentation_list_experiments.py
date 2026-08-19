from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.action_result import ActionResult
from ...models.experiment_state import ExperimentState
from ...models.list_experiments_response import ListExperimentsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    universe_id: int,
    *,
    max_page_size: str | Unset = UNSET,
    skip: str | Unset = UNSET,
    search_key: str | Unset = UNSET,
    state_filters: list[ExperimentState] | Unset = UNSET,
    sort_order: str | Unset = UNSET,
    sort_key: str | Unset = UNSET,
    product_type_filter: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["maxPageSize"] = max_page_size

    params["skip"] = skip

    params["searchKey"] = search_key

    json_state_filters: list[str] | Unset = UNSET
    if not isinstance(state_filters, Unset):
        json_state_filters = []
        for state_filters_item_data in state_filters:
            state_filters_item = state_filters_item_data.value
            json_state_filters.append(state_filters_item)

    params["stateFilters"] = json_state_filters

    params["sortOrder"] = sort_order

    params["sortKey"] = sort_key

    params["productTypeFilter"] = product_type_filter

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/creator-configs-public-api/v1/experimentation/universes/{universe_id}/experiments".format(
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
                "x-roblox-scopes": [{"name": "universe:read", "targetResourceSpecifier": "universes"}],
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            },
            "openapi-id": "PublicExperimentation_ListExperiments",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ActionResult | ListExperimentsResponse | None:
    if response.status_code == 200:
        response_200 = ListExperimentsResponse.from_dict(response.json())

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
) -> Response[ActionResult | ListExperimentsResponse]:
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
    max_page_size: str | Unset = UNSET,
    skip: str | Unset = UNSET,
    search_key: str | Unset = UNSET,
    state_filters: list[ExperimentState] | Unset = UNSET,
    sort_order: str | Unset = UNSET,
    sort_key: str | Unset = UNSET,
    product_type_filter: str | Unset = UNSET,
) -> Response[ActionResult | ListExperimentsResponse]:
    """Lists experiments for a universe.

     Pagination is offset-based (`maxPageSize` + `skip`). The response carries the page slice plus the
    unpaginated total
    matching the filters. Request includes optional pagination, search, and filters.

    Args:
        universe_id (int):
        max_page_size (str | Unset):
        skip (str | Unset):
        search_key (str | Unset):
        state_filters (list[ExperimentState] | Unset):
        sort_order (str | Unset):
        sort_key (str | Unset):
        product_type_filter (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionResult | ListExperimentsResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        max_page_size=max_page_size,
        skip=skip,
        search_key=search_key,
        state_filters=state_filters,
        sort_order=sort_order,
        sort_key=sort_key,
        product_type_filter=product_type_filter,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    max_page_size: str | Unset = UNSET,
    skip: str | Unset = UNSET,
    search_key: str | Unset = UNSET,
    state_filters: list[ExperimentState] | Unset = UNSET,
    sort_order: str | Unset = UNSET,
    sort_key: str | Unset = UNSET,
    product_type_filter: str | Unset = UNSET,
) -> ActionResult | ListExperimentsResponse | None:
    """Lists experiments for a universe.

     Pagination is offset-based (`maxPageSize` + `skip`). The response carries the page slice plus the
    unpaginated total
    matching the filters. Request includes optional pagination, search, and filters.

    Args:
        universe_id (int):
        max_page_size (str | Unset):
        skip (str | Unset):
        search_key (str | Unset):
        state_filters (list[ExperimentState] | Unset):
        sort_order (str | Unset):
        sort_key (str | Unset):
        product_type_filter (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionResult | ListExperimentsResponse
    """

    return sync_detailed(
        universe_id=universe_id,
        client=client,
        max_page_size=max_page_size,
        skip=skip,
        search_key=search_key,
        state_filters=state_filters,
        sort_order=sort_order,
        sort_key=sort_key,
        product_type_filter=product_type_filter,
    ).parsed


async def asyncio_detailed(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    max_page_size: str | Unset = UNSET,
    skip: str | Unset = UNSET,
    search_key: str | Unset = UNSET,
    state_filters: list[ExperimentState] | Unset = UNSET,
    sort_order: str | Unset = UNSET,
    sort_key: str | Unset = UNSET,
    product_type_filter: str | Unset = UNSET,
) -> Response[ActionResult | ListExperimentsResponse]:
    """Lists experiments for a universe.

     Pagination is offset-based (`maxPageSize` + `skip`). The response carries the page slice plus the
    unpaginated total
    matching the filters. Request includes optional pagination, search, and filters.

    Args:
        universe_id (int):
        max_page_size (str | Unset):
        skip (str | Unset):
        search_key (str | Unset):
        state_filters (list[ExperimentState] | Unset):
        sort_order (str | Unset):
        sort_key (str | Unset):
        product_type_filter (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionResult | ListExperimentsResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        max_page_size=max_page_size,
        skip=skip,
        search_key=search_key,
        state_filters=state_filters,
        sort_order=sort_order,
        sort_key=sort_key,
        product_type_filter=product_type_filter,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    max_page_size: str | Unset = UNSET,
    skip: str | Unset = UNSET,
    search_key: str | Unset = UNSET,
    state_filters: list[ExperimentState] | Unset = UNSET,
    sort_order: str | Unset = UNSET,
    sort_key: str | Unset = UNSET,
    product_type_filter: str | Unset = UNSET,
) -> ActionResult | ListExperimentsResponse | None:
    """Lists experiments for a universe.

     Pagination is offset-based (`maxPageSize` + `skip`). The response carries the page slice plus the
    unpaginated total
    matching the filters. Request includes optional pagination, search, and filters.

    Args:
        universe_id (int):
        max_page_size (str | Unset):
        skip (str | Unset):
        search_key (str | Unset):
        state_filters (list[ExperimentState] | Unset):
        sort_order (str | Unset):
        sort_key (str | Unset):
        product_type_filter (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionResult | ListExperimentsResponse
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            client=client,
            max_page_size=max_page_size,
            skip=skip,
            search_key=search_key,
            state_filters=state_filters,
            sort_order=sort_order,
            sort_key=sort_key,
            product_type_filter=product_type_filter,
        )
    ).parsed
