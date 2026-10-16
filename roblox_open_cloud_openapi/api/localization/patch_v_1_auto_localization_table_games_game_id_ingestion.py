from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_v1_auto_localization_table_games_game_id_ingestion_response_200 import (
    PatchV1AutoLocalizationTableGamesGameIdIngestionResponse200,
)
from ...models.roblox_localization_tables_api_ingest_auto_scraped_content_for_game_request import (
    RobloxLocalizationTablesApiIngestAutoScrapedContentForGameRequest,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    game_id: int,
    *,
    body: RobloxLocalizationTablesApiIngestAutoScrapedContentForGameRequest
    | RobloxLocalizationTablesApiIngestAutoScrapedContentForGameRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "https://localizationtables.roblox.com/v1/auto-localization-table/games/{game_id}/ingestion".format(
            game_id=quote(str(game_id), safe=""),
        ),
        "extensions": {
            "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
            "openapi-id": "patch_v1_auto-localization-table_games_gameId_ingestion",
        },
    }

    if isinstance(body, RobloxLocalizationTablesApiIngestAutoScrapedContentForGameRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxLocalizationTablesApiIngestAutoScrapedContentForGameRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | PatchV1AutoLocalizationTableGamesGameIdIngestionResponse200 | None:
    if response.status_code == 200:
        response_200 = PatchV1AutoLocalizationTableGamesGameIdIngestionResponse200.from_dict(response.json())

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

    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | PatchV1AutoLocalizationTableGamesGameIdIngestionResponse200]:
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
    body: RobloxLocalizationTablesApiIngestAutoScrapedContentForGameRequest
    | RobloxLocalizationTablesApiIngestAutoScrapedContentForGameRequest
    | Unset = UNSET,
) -> Response[Any | PatchV1AutoLocalizationTableGamesGameIdIngestionResponse200]:
    """Ingests entries for auto localization. Needs to be an authorized user.

    Args:
        game_id (int):
        body (RobloxLocalizationTablesApiIngestAutoScrapedContentForGameRequest): An ingest
            content request to IngestAutoScrapedContentForGame.
        body (RobloxLocalizationTablesApiIngestAutoScrapedContentForGameRequest): An ingest
            content request to IngestAutoScrapedContentForGame.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PatchV1AutoLocalizationTableGamesGameIdIngestionResponse200]
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
    body: RobloxLocalizationTablesApiIngestAutoScrapedContentForGameRequest
    | RobloxLocalizationTablesApiIngestAutoScrapedContentForGameRequest
    | Unset = UNSET,
) -> Any | PatchV1AutoLocalizationTableGamesGameIdIngestionResponse200 | None:
    """Ingests entries for auto localization. Needs to be an authorized user.

    Args:
        game_id (int):
        body (RobloxLocalizationTablesApiIngestAutoScrapedContentForGameRequest): An ingest
            content request to IngestAutoScrapedContentForGame.
        body (RobloxLocalizationTablesApiIngestAutoScrapedContentForGameRequest): An ingest
            content request to IngestAutoScrapedContentForGame.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PatchV1AutoLocalizationTableGamesGameIdIngestionResponse200
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
    body: RobloxLocalizationTablesApiIngestAutoScrapedContentForGameRequest
    | RobloxLocalizationTablesApiIngestAutoScrapedContentForGameRequest
    | Unset = UNSET,
) -> Response[Any | PatchV1AutoLocalizationTableGamesGameIdIngestionResponse200]:
    """Ingests entries for auto localization. Needs to be an authorized user.

    Args:
        game_id (int):
        body (RobloxLocalizationTablesApiIngestAutoScrapedContentForGameRequest): An ingest
            content request to IngestAutoScrapedContentForGame.
        body (RobloxLocalizationTablesApiIngestAutoScrapedContentForGameRequest): An ingest
            content request to IngestAutoScrapedContentForGame.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PatchV1AutoLocalizationTableGamesGameIdIngestionResponse200]
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
    body: RobloxLocalizationTablesApiIngestAutoScrapedContentForGameRequest
    | RobloxLocalizationTablesApiIngestAutoScrapedContentForGameRequest
    | Unset = UNSET,
) -> Any | PatchV1AutoLocalizationTableGamesGameIdIngestionResponse200 | None:
    """Ingests entries for auto localization. Needs to be an authorized user.

    Args:
        game_id (int):
        body (RobloxLocalizationTablesApiIngestAutoScrapedContentForGameRequest): An ingest
            content request to IngestAutoScrapedContentForGame.
        body (RobloxLocalizationTablesApiIngestAutoScrapedContentForGameRequest): An ingest
            content request to IngestAutoScrapedContentForGame.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PatchV1AutoLocalizationTableGamesGameIdIngestionResponse200
    """

    return (
        await asyncio_detailed(
            game_id=game_id,
            client=client,
            body=body,
        )
    ).parsed
