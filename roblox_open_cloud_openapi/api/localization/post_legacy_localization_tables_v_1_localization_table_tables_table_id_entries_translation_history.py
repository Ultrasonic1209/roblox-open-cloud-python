from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_localization_tables_api_get_table_entries_translation_history_request import (
    RobloxLocalizationTablesApiGetTableEntriesTranslationHistoryRequest,
)
from ...models.roblox_localization_tables_api_get_table_entries_translation_history_response import (
    RobloxLocalizationTablesApiGetTableEntriesTranslationHistoryResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    table_id: UUID,
    *,
    body: RobloxLocalizationTablesApiGetTableEntriesTranslationHistoryRequest
    | RobloxLocalizationTablesApiGetTableEntriesTranslationHistoryRequest
    | Unset = UNSET,
    game_id: int | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["gameId"] = game_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/legacy-localization-tables/v1/localization-table/tables/{table_id}/entries/translation-history".format(
            table_id=quote(str(table_id), safe=""),
        ),
        "params": params,
    }

    if isinstance(body, RobloxLocalizationTablesApiGetTableEntriesTranslationHistoryRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxLocalizationTablesApiGetTableEntriesTranslationHistoryRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxLocalizationTablesApiGetTableEntriesTranslationHistoryResponse | None:
    if response.status_code == 200:
        response_200 = RobloxLocalizationTablesApiGetTableEntriesTranslationHistoryResponse.from_dict(response.json())

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

    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429

    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxLocalizationTablesApiGetTableEntriesTranslationHistoryResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    table_id: UUID,
    *,
    client: AuthenticatedClient,
    body: RobloxLocalizationTablesApiGetTableEntriesTranslationHistoryRequest
    | RobloxLocalizationTablesApiGetTableEntriesTranslationHistoryRequest
    | Unset = UNSET,
    game_id: int | Unset = UNSET,
) -> Response[Any | RobloxLocalizationTablesApiGetTableEntriesTranslationHistoryResponse]:
    """Gets the translation history for each entry passed in.

    Args:
        table_id (UUID):
        game_id (int | Unset):
        body (RobloxLocalizationTablesApiGetTableEntriesTranslationHistoryRequest):
        body (RobloxLocalizationTablesApiGetTableEntriesTranslationHistoryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxLocalizationTablesApiGetTableEntriesTranslationHistoryResponse]
    """

    kwargs = _get_kwargs(
        table_id=table_id,
        body=body,
        game_id=game_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    table_id: UUID,
    *,
    client: AuthenticatedClient,
    body: RobloxLocalizationTablesApiGetTableEntriesTranslationHistoryRequest
    | RobloxLocalizationTablesApiGetTableEntriesTranslationHistoryRequest
    | Unset = UNSET,
    game_id: int | Unset = UNSET,
) -> Any | RobloxLocalizationTablesApiGetTableEntriesTranslationHistoryResponse | None:
    """Gets the translation history for each entry passed in.

    Args:
        table_id (UUID):
        game_id (int | Unset):
        body (RobloxLocalizationTablesApiGetTableEntriesTranslationHistoryRequest):
        body (RobloxLocalizationTablesApiGetTableEntriesTranslationHistoryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxLocalizationTablesApiGetTableEntriesTranslationHistoryResponse
    """

    return sync_detailed(
        table_id=table_id,
        client=client,
        body=body,
        game_id=game_id,
    ).parsed


async def asyncio_detailed(
    table_id: UUID,
    *,
    client: AuthenticatedClient,
    body: RobloxLocalizationTablesApiGetTableEntriesTranslationHistoryRequest
    | RobloxLocalizationTablesApiGetTableEntriesTranslationHistoryRequest
    | Unset = UNSET,
    game_id: int | Unset = UNSET,
) -> Response[Any | RobloxLocalizationTablesApiGetTableEntriesTranslationHistoryResponse]:
    """Gets the translation history for each entry passed in.

    Args:
        table_id (UUID):
        game_id (int | Unset):
        body (RobloxLocalizationTablesApiGetTableEntriesTranslationHistoryRequest):
        body (RobloxLocalizationTablesApiGetTableEntriesTranslationHistoryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxLocalizationTablesApiGetTableEntriesTranslationHistoryResponse]
    """

    kwargs = _get_kwargs(
        table_id=table_id,
        body=body,
        game_id=game_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    table_id: UUID,
    *,
    client: AuthenticatedClient,
    body: RobloxLocalizationTablesApiGetTableEntriesTranslationHistoryRequest
    | RobloxLocalizationTablesApiGetTableEntriesTranslationHistoryRequest
    | Unset = UNSET,
    game_id: int | Unset = UNSET,
) -> Any | RobloxLocalizationTablesApiGetTableEntriesTranslationHistoryResponse | None:
    """Gets the translation history for each entry passed in.

    Args:
        table_id (UUID):
        game_id (int | Unset):
        body (RobloxLocalizationTablesApiGetTableEntriesTranslationHistoryRequest):
        body (RobloxLocalizationTablesApiGetTableEntriesTranslationHistoryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxLocalizationTablesApiGetTableEntriesTranslationHistoryResponse
    """

    return (
        await asyncio_detailed(
            table_id=table_id,
            client=client,
            body=body,
            game_id=game_id,
        )
    ).parsed
