from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.action_result import ActionResult
from ...models.list_revisions_response import ListRevisionsResponse
from ...models.repository import Repository
from ...types import UNSET, Response, Unset


def _get_kwargs(
    universe_id: str,
    repository: Repository,
    *,
    start_time: str | Unset = UNSET,
    end_time: str | Unset = UNSET,
    max_page_size: str | Unset = UNSET,
    skip: str | Unset = UNSET,
    search_key: str | Unset = UNSET,
    sort_order: str | Unset = UNSET,
    sort_key: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["startTime"] = start_time

    params["endTime"] = end_time

    params["MaxPageSize"] = max_page_size

    params["Skip"] = skip

    params["SearchKey"] = search_key

    params["SortOrder"] = sort_order

    params["SortKey"] = sort_key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/creator-configs-public-api/v1/configs/universes/{universe_id}/repositories/{repository}/revisions".format(
            universe_id=quote(str(universe_id), safe=""),
            repository=quote(str(repository), safe=""),
        ),
        "params": params,
        "extensions": {
            "openapi-extensions": {
                "x-roblox-stability": "BETA",
                "x-roblox-rate-limits": {
                    "perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 100},
                    "perOauth2Authorization": {"period": "MINUTE", "maxInPeriod": 100},
                },
                "x-roblox-scopes": [{"name": "universe:read", "targetResourceSpecifier": "universes"}],
                "x-roblox-engine-usability": {"apiKeyWithHttpService": True},
            },
            "openapi-id": "CreatorConfigsPublicApi_ListRevisions",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ActionResult | ListRevisionsResponse | None:
    if response.status_code == 200:
        response_200 = ListRevisionsResponse.from_dict(response.json())

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
) -> Response[ActionResult | ListRevisionsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    universe_id: str,
    repository: Repository,
    *,
    client: AuthenticatedClient,
    start_time: str | Unset = UNSET,
    end_time: str | Unset = UNSET,
    max_page_size: str | Unset = UNSET,
    skip: str | Unset = UNSET,
    search_key: str | Unset = UNSET,
    sort_order: str | Unset = UNSET,
    sort_key: str | Unset = UNSET,
) -> Response[ActionResult | ListRevisionsResponse]:
    """Lists revision history.

     Returns the list of previous revisions to the repository. Supports optional start/end time and
    pagination.

    Args:
        universe_id (str):
        repository (Repository): Public API repository identifier. Only values exposed by the
            public API are included;
            internal repository types are not exposed to allow development and testing before
            enabling.

            InExperienceConfig

            RecommendationServicesConfig

            DataStoresConfig

            ExtendedServicesConfig

            LeaderboardsConfig

            ExperienceUserConfig
        start_time (str | Unset):
        end_time (str | Unset):
        max_page_size (str | Unset):
        skip (str | Unset):
        search_key (str | Unset):
        sort_order (str | Unset):
        sort_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionResult | ListRevisionsResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        repository=repository,
        start_time=start_time,
        end_time=end_time,
        max_page_size=max_page_size,
        skip=skip,
        search_key=search_key,
        sort_order=sort_order,
        sort_key=sort_key,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: str,
    repository: Repository,
    *,
    client: AuthenticatedClient,
    start_time: str | Unset = UNSET,
    end_time: str | Unset = UNSET,
    max_page_size: str | Unset = UNSET,
    skip: str | Unset = UNSET,
    search_key: str | Unset = UNSET,
    sort_order: str | Unset = UNSET,
    sort_key: str | Unset = UNSET,
) -> ActionResult | ListRevisionsResponse | None:
    """Lists revision history.

     Returns the list of previous revisions to the repository. Supports optional start/end time and
    pagination.

    Args:
        universe_id (str):
        repository (Repository): Public API repository identifier. Only values exposed by the
            public API are included;
            internal repository types are not exposed to allow development and testing before
            enabling.

            InExperienceConfig

            RecommendationServicesConfig

            DataStoresConfig

            ExtendedServicesConfig

            LeaderboardsConfig

            ExperienceUserConfig
        start_time (str | Unset):
        end_time (str | Unset):
        max_page_size (str | Unset):
        skip (str | Unset):
        search_key (str | Unset):
        sort_order (str | Unset):
        sort_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionResult | ListRevisionsResponse
    """

    return sync_detailed(
        universe_id=universe_id,
        repository=repository,
        client=client,
        start_time=start_time,
        end_time=end_time,
        max_page_size=max_page_size,
        skip=skip,
        search_key=search_key,
        sort_order=sort_order,
        sort_key=sort_key,
    ).parsed


async def asyncio_detailed(
    universe_id: str,
    repository: Repository,
    *,
    client: AuthenticatedClient,
    start_time: str | Unset = UNSET,
    end_time: str | Unset = UNSET,
    max_page_size: str | Unset = UNSET,
    skip: str | Unset = UNSET,
    search_key: str | Unset = UNSET,
    sort_order: str | Unset = UNSET,
    sort_key: str | Unset = UNSET,
) -> Response[ActionResult | ListRevisionsResponse]:
    """Lists revision history.

     Returns the list of previous revisions to the repository. Supports optional start/end time and
    pagination.

    Args:
        universe_id (str):
        repository (Repository): Public API repository identifier. Only values exposed by the
            public API are included;
            internal repository types are not exposed to allow development and testing before
            enabling.

            InExperienceConfig

            RecommendationServicesConfig

            DataStoresConfig

            ExtendedServicesConfig

            LeaderboardsConfig

            ExperienceUserConfig
        start_time (str | Unset):
        end_time (str | Unset):
        max_page_size (str | Unset):
        skip (str | Unset):
        search_key (str | Unset):
        sort_order (str | Unset):
        sort_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionResult | ListRevisionsResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        repository=repository,
        start_time=start_time,
        end_time=end_time,
        max_page_size=max_page_size,
        skip=skip,
        search_key=search_key,
        sort_order=sort_order,
        sort_key=sort_key,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: str,
    repository: Repository,
    *,
    client: AuthenticatedClient,
    start_time: str | Unset = UNSET,
    end_time: str | Unset = UNSET,
    max_page_size: str | Unset = UNSET,
    skip: str | Unset = UNSET,
    search_key: str | Unset = UNSET,
    sort_order: str | Unset = UNSET,
    sort_key: str | Unset = UNSET,
) -> ActionResult | ListRevisionsResponse | None:
    """Lists revision history.

     Returns the list of previous revisions to the repository. Supports optional start/end time and
    pagination.

    Args:
        universe_id (str):
        repository (Repository): Public API repository identifier. Only values exposed by the
            public API are included;
            internal repository types are not exposed to allow development and testing before
            enabling.

            InExperienceConfig

            RecommendationServicesConfig

            DataStoresConfig

            ExtendedServicesConfig

            LeaderboardsConfig

            ExperienceUserConfig
        start_time (str | Unset):
        end_time (str | Unset):
        max_page_size (str | Unset):
        skip (str | Unset):
        search_key (str | Unset):
        sort_order (str | Unset):
        sort_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionResult | ListRevisionsResponse
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            repository=repository,
            client=client,
            start_time=start_time,
            end_time=end_time,
            max_page_size=max_page_size,
            skip=skip,
            search_key=search_key,
            sort_order=sort_order,
            sort_key=sort_key,
        )
    ).parsed
