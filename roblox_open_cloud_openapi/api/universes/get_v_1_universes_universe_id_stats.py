import datetime
from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v1_universes_universe_id_stats_type import GetV1UniversesUniverseIdStatsType
from ...models.roblox_economy_creator_stats_api_models_statistics_response import (
    RobloxEconomyCreatorStatsApiModelsStatisticsResponse,
)
from ...types import UNSET, Response


def _get_kwargs(
    universe_id: int,
    *,
    type_: GetV1UniversesUniverseIdStatsType,
    start_time: datetime.datetime,
    end_time: datetime.datetime,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_type_ = type_.value
    params["Type"] = json_type_

    json_start_time = start_time.isoformat()
    params["StartTime"] = json_start_time

    json_end_time = end_time.isoformat()
    params["EndTime"] = json_end_time

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://economycreatorstats.roblox.com/v1/universes/{universe_id}/stats".format(
            universe_id=quote(str(universe_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxEconomyCreatorStatsApiModelsStatisticsResponse | None:
    if response.status_code == 200:
        response_200 = RobloxEconomyCreatorStatsApiModelsStatisticsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxEconomyCreatorStatsApiModelsStatisticsResponse]:
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
    type_: GetV1UniversesUniverseIdStatsType,
    start_time: datetime.datetime,
    end_time: datetime.datetime,
) -> Response[Any | RobloxEconomyCreatorStatsApiModelsStatisticsResponse]:
    """Get statistics data for a universe.

    Args:
        universe_id (int):
        type_ (GetV1UniversesUniverseIdStatsType):
        start_time (datetime.datetime):
        end_time (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxEconomyCreatorStatsApiModelsStatisticsResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        type_=type_,
        start_time=start_time,
        end_time=end_time,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    type_: GetV1UniversesUniverseIdStatsType,
    start_time: datetime.datetime,
    end_time: datetime.datetime,
) -> Any | RobloxEconomyCreatorStatsApiModelsStatisticsResponse | None:
    """Get statistics data for a universe.

    Args:
        universe_id (int):
        type_ (GetV1UniversesUniverseIdStatsType):
        start_time (datetime.datetime):
        end_time (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxEconomyCreatorStatsApiModelsStatisticsResponse
    """

    return sync_detailed(
        universe_id=universe_id,
        client=client,
        type_=type_,
        start_time=start_time,
        end_time=end_time,
    ).parsed


async def asyncio_detailed(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    type_: GetV1UniversesUniverseIdStatsType,
    start_time: datetime.datetime,
    end_time: datetime.datetime,
) -> Response[Any | RobloxEconomyCreatorStatsApiModelsStatisticsResponse]:
    """Get statistics data for a universe.

    Args:
        universe_id (int):
        type_ (GetV1UniversesUniverseIdStatsType):
        start_time (datetime.datetime):
        end_time (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxEconomyCreatorStatsApiModelsStatisticsResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        type_=type_,
        start_time=start_time,
        end_time=end_time,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    type_: GetV1UniversesUniverseIdStatsType,
    start_time: datetime.datetime,
    end_time: datetime.datetime,
) -> Any | RobloxEconomyCreatorStatsApiModelsStatisticsResponse | None:
    """Get statistics data for a universe.

    Args:
        universe_id (int):
        type_ (GetV1UniversesUniverseIdStatsType):
        start_time (datetime.datetime):
        end_time (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxEconomyCreatorStatsApiModelsStatisticsResponse
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            client=client,
            type_=type_,
            start_time=start_time,
            end_time=end_time,
        )
    ).parsed
