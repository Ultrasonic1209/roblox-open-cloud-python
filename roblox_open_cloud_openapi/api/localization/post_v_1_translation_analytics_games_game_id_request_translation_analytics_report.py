from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_game_internationalization_api_request_translation_analytics_report_request import (
    RobloxGameInternationalizationApiRequestTranslationAnalyticsReportRequest,
)
from ...models.roblox_game_internationalization_api_request_translation_analytics_report_response import (
    RobloxGameInternationalizationApiRequestTranslationAnalyticsReportResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    game_id: int,
    *,
    body: RobloxGameInternationalizationApiRequestTranslationAnalyticsReportRequest
    | RobloxGameInternationalizationApiRequestTranslationAnalyticsReportRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "https://gameinternationalization.roblox.com/v1/translation-analytics/games/{game_id}/request-translation-analytics-report".format(
            game_id=quote(str(game_id), safe=""),
        ),
        "extensions": {
            "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
            "openapi-id": "post_v1_translation-analytics_games_gameId_request-translation-analytics-report",
        },
    }

    if isinstance(body, RobloxGameInternationalizationApiRequestTranslationAnalyticsReportRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxGameInternationalizationApiRequestTranslationAnalyticsReportRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxGameInternationalizationApiRequestTranslationAnalyticsReportResponse | None:
    if response.status_code == 200:
        response_200 = RobloxGameInternationalizationApiRequestTranslationAnalyticsReportResponse.from_dict(
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
) -> Response[Any | RobloxGameInternationalizationApiRequestTranslationAnalyticsReportResponse]:
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
    body: RobloxGameInternationalizationApiRequestTranslationAnalyticsReportRequest
    | RobloxGameInternationalizationApiRequestTranslationAnalyticsReportRequest
    | Unset = UNSET,
) -> Response[Any | RobloxGameInternationalizationApiRequestTranslationAnalyticsReportResponse]:
    """Request translation analytics report to be generated

    Args:
        game_id (int):
        body (RobloxGameInternationalizationApiRequestTranslationAnalyticsReportRequest):
        body (RobloxGameInternationalizationApiRequestTranslationAnalyticsReportRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxGameInternationalizationApiRequestTranslationAnalyticsReportResponse]
    """

    kwargs = _get_kwargs(
        game_id=game_id,
        body=body,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    game_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxGameInternationalizationApiRequestTranslationAnalyticsReportRequest
    | RobloxGameInternationalizationApiRequestTranslationAnalyticsReportRequest
    | Unset = UNSET,
) -> Any | RobloxGameInternationalizationApiRequestTranslationAnalyticsReportResponse | None:
    """Request translation analytics report to be generated

    Args:
        game_id (int):
        body (RobloxGameInternationalizationApiRequestTranslationAnalyticsReportRequest):
        body (RobloxGameInternationalizationApiRequestTranslationAnalyticsReportRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxGameInternationalizationApiRequestTranslationAnalyticsReportResponse
    """

    return sync_detailed(
        game_id=game_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    game_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxGameInternationalizationApiRequestTranslationAnalyticsReportRequest
    | RobloxGameInternationalizationApiRequestTranslationAnalyticsReportRequest
    | Unset = UNSET,
) -> Response[Any | RobloxGameInternationalizationApiRequestTranslationAnalyticsReportResponse]:
    """Request translation analytics report to be generated

    Args:
        game_id (int):
        body (RobloxGameInternationalizationApiRequestTranslationAnalyticsReportRequest):
        body (RobloxGameInternationalizationApiRequestTranslationAnalyticsReportRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxGameInternationalizationApiRequestTranslationAnalyticsReportResponse]
    """

    kwargs = _get_kwargs(
        game_id=game_id,
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    game_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxGameInternationalizationApiRequestTranslationAnalyticsReportRequest
    | RobloxGameInternationalizationApiRequestTranslationAnalyticsReportRequest
    | Unset = UNSET,
) -> Any | RobloxGameInternationalizationApiRequestTranslationAnalyticsReportResponse | None:
    """Request translation analytics report to be generated

    Args:
        game_id (int):
        body (RobloxGameInternationalizationApiRequestTranslationAnalyticsReportRequest):
        body (RobloxGameInternationalizationApiRequestTranslationAnalyticsReportRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxGameInternationalizationApiRequestTranslationAnalyticsReportResponse
    """

    return (
        await asyncio_detailed(
            game_id=game_id,
            client=client,
            body=body,
        )
    ).parsed
