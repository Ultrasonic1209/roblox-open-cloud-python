from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_legacy_localization_tables_v1_localization_table_tables_table_id_entries_entry_format import (
    GetLegacyLocalizationTablesV1LocalizationTableTablesTableIdEntriesEntryFormat,
)
from ...models.roblox_localization_tables_api_get_table_entries_paged_response import (
    RobloxLocalizationTablesApiGetTableEntriesPagedResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    table_id: UUID,
    *,
    cursor: str | Unset = UNSET,
    game_id: int | Unset = UNSET,
    entry_format: GetLegacyLocalizationTablesV1LocalizationTableTablesTableIdEntriesEntryFormat
    | Unset = GetLegacyLocalizationTablesV1LocalizationTableTablesTableIdEntriesEntryFormat.LEGACY,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["cursor"] = cursor

    params["gameId"] = game_id

    json_entry_format: str | Unset = UNSET
    if not isinstance(entry_format, Unset):
        json_entry_format = entry_format.value

    params["entryFormat"] = json_entry_format

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/legacy-localization-tables/v1/localization-table/tables/{table_id}/entries".format(
            table_id=quote(str(table_id), safe=""),
        ),
        "params": params,
        "extensions": {
            "openapi-extensions": {
                "x-roblox-rate-limits": {
                    "perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 100},
                    "perOauth2Authorization": {"period": "MINUTE", "maxInPeriod": 100},
                },
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
                "x-roblox-scopes": [{"name": "legacy-universe:manage"}],
            },
            "openapi-id": "get_legacy-localization-tables_v1_localization-table_tables_tableId_entries",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxLocalizationTablesApiGetTableEntriesPagedResponse | None:
    if response.status_code == 200:
        response_200 = RobloxLocalizationTablesApiGetTableEntriesPagedResponse.from_dict(response.json())

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
) -> Response[Any | RobloxLocalizationTablesApiGetTableEntriesPagedResponse]:
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
    cursor: str | Unset = UNSET,
    game_id: int | Unset = UNSET,
    entry_format: GetLegacyLocalizationTablesV1LocalizationTableTablesTableIdEntriesEntryFormat
    | Unset = GetLegacyLocalizationTablesV1LocalizationTableTablesTableIdEntriesEntryFormat.LEGACY,
) -> Response[Any | RobloxLocalizationTablesApiGetTableEntriesPagedResponse]:
    """Gets a batch of entries for a table.

    Args:
        table_id (UUID):
        cursor (str | Unset):
        game_id (int | Unset):
        entry_format
            (GetLegacyLocalizationTablesV1LocalizationTableTablesTableIdEntriesEntryFormat | Unset):
            Default:
            GetLegacyLocalizationTablesV1LocalizationTableTablesTableIdEntriesEntryFormat.LEGACY.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxLocalizationTablesApiGetTableEntriesPagedResponse]
    """

    kwargs = _get_kwargs(
        table_id=table_id,
        cursor=cursor,
        game_id=game_id,
        entry_format=entry_format,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    table_id: UUID,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    game_id: int | Unset = UNSET,
    entry_format: GetLegacyLocalizationTablesV1LocalizationTableTablesTableIdEntriesEntryFormat
    | Unset = GetLegacyLocalizationTablesV1LocalizationTableTablesTableIdEntriesEntryFormat.LEGACY,
) -> Any | RobloxLocalizationTablesApiGetTableEntriesPagedResponse | None:
    """Gets a batch of entries for a table.

    Args:
        table_id (UUID):
        cursor (str | Unset):
        game_id (int | Unset):
        entry_format
            (GetLegacyLocalizationTablesV1LocalizationTableTablesTableIdEntriesEntryFormat | Unset):
            Default:
            GetLegacyLocalizationTablesV1LocalizationTableTablesTableIdEntriesEntryFormat.LEGACY.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxLocalizationTablesApiGetTableEntriesPagedResponse
    """

    return sync_detailed(
        table_id=table_id,
        client=client,
        cursor=cursor,
        game_id=game_id,
        entry_format=entry_format,
    ).parsed


async def asyncio_detailed(
    table_id: UUID,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    game_id: int | Unset = UNSET,
    entry_format: GetLegacyLocalizationTablesV1LocalizationTableTablesTableIdEntriesEntryFormat
    | Unset = GetLegacyLocalizationTablesV1LocalizationTableTablesTableIdEntriesEntryFormat.LEGACY,
) -> Response[Any | RobloxLocalizationTablesApiGetTableEntriesPagedResponse]:
    """Gets a batch of entries for a table.

    Args:
        table_id (UUID):
        cursor (str | Unset):
        game_id (int | Unset):
        entry_format
            (GetLegacyLocalizationTablesV1LocalizationTableTablesTableIdEntriesEntryFormat | Unset):
            Default:
            GetLegacyLocalizationTablesV1LocalizationTableTablesTableIdEntriesEntryFormat.LEGACY.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxLocalizationTablesApiGetTableEntriesPagedResponse]
    """

    kwargs = _get_kwargs(
        table_id=table_id,
        cursor=cursor,
        game_id=game_id,
        entry_format=entry_format,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    table_id: UUID,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    game_id: int | Unset = UNSET,
    entry_format: GetLegacyLocalizationTablesV1LocalizationTableTablesTableIdEntriesEntryFormat
    | Unset = GetLegacyLocalizationTablesV1LocalizationTableTablesTableIdEntriesEntryFormat.LEGACY,
) -> Any | RobloxLocalizationTablesApiGetTableEntriesPagedResponse | None:
    """Gets a batch of entries for a table.

    Args:
        table_id (UUID):
        cursor (str | Unset):
        game_id (int | Unset):
        entry_format
            (GetLegacyLocalizationTablesV1LocalizationTableTablesTableIdEntriesEntryFormat | Unset):
            Default:
            GetLegacyLocalizationTablesV1LocalizationTableTablesTableIdEntriesEntryFormat.LEGACY.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxLocalizationTablesApiGetTableEntriesPagedResponse
    """

    return (
        await asyncio_detailed(
            table_id=table_id,
            client=client,
            cursor=cursor,
            game_id=game_id,
            entry_format=entry_format,
        )
    ).parsed
