import datetime
from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v1_translation_analytics_games_game_id_download_translation_analytics_report_report_type import (
    GetV1TranslationAnalyticsGamesGameIdDownloadTranslationAnalyticsReportReportType,
)
from ...models.get_v1_translation_analytics_games_game_id_download_translation_analytics_report_response_200 import (
    GetV1TranslationAnalyticsGamesGameIdDownloadTranslationAnalyticsReportResponse200,
)
from ...types import UNSET, Response


def _get_kwargs(
    game_id: int,
    *,
    start_date_time: datetime.datetime,
    end_date_time: datetime.datetime,
    report_type: GetV1TranslationAnalyticsGamesGameIdDownloadTranslationAnalyticsReportReportType,
    report_subject_target_id: int,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_start_date_time = start_date_time.isoformat()
    params["startDateTime"] = json_start_date_time

    json_end_date_time = end_date_time.isoformat()
    params["endDateTime"] = json_end_date_time

    json_report_type = report_type.value
    params["reportType"] = json_report_type

    params["reportSubjectTargetId"] = report_subject_target_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://gameinternationalization.roblox.com/v1/translation-analytics/games/{game_id}/download-translation-analytics-report".format(
            game_id=quote(str(game_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | GetV1TranslationAnalyticsGamesGameIdDownloadTranslationAnalyticsReportResponse200 | None:
    if response.status_code == 200:
        response_200 = GetV1TranslationAnalyticsGamesGameIdDownloadTranslationAnalyticsReportResponse200.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | GetV1TranslationAnalyticsGamesGameIdDownloadTranslationAnalyticsReportResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    game_id: int,
    *,
    client: AuthenticatedClient,
    start_date_time: datetime.datetime,
    end_date_time: datetime.datetime,
    report_type: GetV1TranslationAnalyticsGamesGameIdDownloadTranslationAnalyticsReportReportType,
    report_subject_target_id: int,
) -> Response[Any | GetV1TranslationAnalyticsGamesGameIdDownloadTranslationAnalyticsReportResponse200]:
    """Download translation analytics report after the report is ready

    Args:
        game_id (int):
        start_date_time (datetime.datetime):
        end_date_time (datetime.datetime):
        report_type
            (GetV1TranslationAnalyticsGamesGameIdDownloadTranslationAnalyticsReportReportType):
        report_subject_target_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetV1TranslationAnalyticsGamesGameIdDownloadTranslationAnalyticsReportResponse200]
    """

    kwargs = _get_kwargs(
        game_id=game_id,
        start_date_time=start_date_time,
        end_date_time=end_date_time,
        report_type=report_type,
        report_subject_target_id=report_subject_target_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    game_id: int,
    *,
    client: AuthenticatedClient,
    start_date_time: datetime.datetime,
    end_date_time: datetime.datetime,
    report_type: GetV1TranslationAnalyticsGamesGameIdDownloadTranslationAnalyticsReportReportType,
    report_subject_target_id: int,
) -> Any | GetV1TranslationAnalyticsGamesGameIdDownloadTranslationAnalyticsReportResponse200 | None:
    """Download translation analytics report after the report is ready

    Args:
        game_id (int):
        start_date_time (datetime.datetime):
        end_date_time (datetime.datetime):
        report_type
            (GetV1TranslationAnalyticsGamesGameIdDownloadTranslationAnalyticsReportReportType):
        report_subject_target_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetV1TranslationAnalyticsGamesGameIdDownloadTranslationAnalyticsReportResponse200
    """

    return sync_detailed(
        game_id=game_id,
        client=client,
        start_date_time=start_date_time,
        end_date_time=end_date_time,
        report_type=report_type,
        report_subject_target_id=report_subject_target_id,
    ).parsed


async def asyncio_detailed(
    game_id: int,
    *,
    client: AuthenticatedClient,
    start_date_time: datetime.datetime,
    end_date_time: datetime.datetime,
    report_type: GetV1TranslationAnalyticsGamesGameIdDownloadTranslationAnalyticsReportReportType,
    report_subject_target_id: int,
) -> Response[Any | GetV1TranslationAnalyticsGamesGameIdDownloadTranslationAnalyticsReportResponse200]:
    """Download translation analytics report after the report is ready

    Args:
        game_id (int):
        start_date_time (datetime.datetime):
        end_date_time (datetime.datetime):
        report_type
            (GetV1TranslationAnalyticsGamesGameIdDownloadTranslationAnalyticsReportReportType):
        report_subject_target_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetV1TranslationAnalyticsGamesGameIdDownloadTranslationAnalyticsReportResponse200]
    """

    kwargs = _get_kwargs(
        game_id=game_id,
        start_date_time=start_date_time,
        end_date_time=end_date_time,
        report_type=report_type,
        report_subject_target_id=report_subject_target_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    game_id: int,
    *,
    client: AuthenticatedClient,
    start_date_time: datetime.datetime,
    end_date_time: datetime.datetime,
    report_type: GetV1TranslationAnalyticsGamesGameIdDownloadTranslationAnalyticsReportReportType,
    report_subject_target_id: int,
) -> Any | GetV1TranslationAnalyticsGamesGameIdDownloadTranslationAnalyticsReportResponse200 | None:
    """Download translation analytics report after the report is ready

    Args:
        game_id (int):
        start_date_time (datetime.datetime):
        end_date_time (datetime.datetime):
        report_type
            (GetV1TranslationAnalyticsGamesGameIdDownloadTranslationAnalyticsReportReportType):
        report_subject_target_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetV1TranslationAnalyticsGamesGameIdDownloadTranslationAnalyticsReportResponse200
    """

    return (
        await asyncio_detailed(
            game_id=game_id,
            client=client,
            start_date_time=start_date_time,
            end_date_time=end_date_time,
            report_type=report_type,
            report_subject_target_id=report_subject_target_id,
        )
    ).parsed
