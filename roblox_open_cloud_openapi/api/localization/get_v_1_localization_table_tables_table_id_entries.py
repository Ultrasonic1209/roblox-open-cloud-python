import sys
from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset

if sys.version_info >= (3, 13):
    from warnings import deprecated
else:
    from typing_extensions import deprecated

from uuid import UUID

from ...models.get_v1_localization_table_tables_table_id_entries_entry_format import (
    GetV1LocalizationTableTablesTableIdEntriesEntryFormat,
)
from ...models.roblox_localization_tables_api_get_table_entries_paged_response import (
    RobloxLocalizationTablesApiGetTableEntriesPagedResponse,
)


def _get_kwargs(
    table_id: UUID,
    *,
    cursor: str | Unset = UNSET,
    game_id: int | Unset = UNSET,
    entry_format: GetV1LocalizationTableTablesTableIdEntriesEntryFormat
    | Unset = GetV1LocalizationTableTablesTableIdEntriesEntryFormat.LEGACY,
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
        "url": "https://localizationtables.roblox.com/v1/localization-table/tables/{table_id}/entries".format(
            table_id=quote(str(table_id), safe=""),
        ),
        "params": params,
        "extensions": {
            "openapi-extensions": {
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
                "x-roblox-recommended-alternatives": [
                    {
                        "url": "https://apis.roblox.com/legacy-localization-tables/v1/localization-table/tables/{tableId}/entries",
                        "httpMethod": "GET",
                        "documentationUrl": "https://create.roblox.com/docs/cloud/reference/features/localization#get_legacy_localization_tables_v1_localization_table_tables__tableId__entries",
                    }
                ],
            },
            "openapi-id": "get_v1_localization-table_tables_tableId_entries",
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


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/localization#localizationtables_get_v1_localization_table_tables__tableId__entries"
)
def sync_detailed(
    table_id: UUID,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    game_id: int | Unset = UNSET,
    entry_format: GetV1LocalizationTableTablesTableIdEntriesEntryFormat
    | Unset = GetV1LocalizationTableTablesTableIdEntriesEntryFormat.LEGACY,
) -> Response[Any | RobloxLocalizationTablesApiGetTableEntriesPagedResponse]:
    """Gets a batch of entries for a table.

    Args:
        table_id (UUID):
        cursor (str | Unset):
        game_id (int | Unset):
        entry_format (GetV1LocalizationTableTablesTableIdEntriesEntryFormat | Unset):  Default:
            GetV1LocalizationTableTablesTableIdEntriesEntryFormat.LEGACY.

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


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/localization#localizationtables_get_v1_localization_table_tables__tableId__entries"
)
def sync(
    table_id: UUID,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    game_id: int | Unset = UNSET,
    entry_format: GetV1LocalizationTableTablesTableIdEntriesEntryFormat
    | Unset = GetV1LocalizationTableTablesTableIdEntriesEntryFormat.LEGACY,
) -> Any | RobloxLocalizationTablesApiGetTableEntriesPagedResponse | None:
    """Gets a batch of entries for a table.

    Args:
        table_id (UUID):
        cursor (str | Unset):
        game_id (int | Unset):
        entry_format (GetV1LocalizationTableTablesTableIdEntriesEntryFormat | Unset):  Default:
            GetV1LocalizationTableTablesTableIdEntriesEntryFormat.LEGACY.

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


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/localization#localizationtables_get_v1_localization_table_tables__tableId__entries"
)
async def asyncio_detailed(
    table_id: UUID,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    game_id: int | Unset = UNSET,
    entry_format: GetV1LocalizationTableTablesTableIdEntriesEntryFormat
    | Unset = GetV1LocalizationTableTablesTableIdEntriesEntryFormat.LEGACY,
) -> Response[Any | RobloxLocalizationTablesApiGetTableEntriesPagedResponse]:
    """Gets a batch of entries for a table.

    Args:
        table_id (UUID):
        cursor (str | Unset):
        game_id (int | Unset):
        entry_format (GetV1LocalizationTableTablesTableIdEntriesEntryFormat | Unset):  Default:
            GetV1LocalizationTableTablesTableIdEntriesEntryFormat.LEGACY.

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


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/localization#localizationtables_get_v1_localization_table_tables__tableId__entries"
)
async def asyncio(
    table_id: UUID,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    game_id: int | Unset = UNSET,
    entry_format: GetV1LocalizationTableTablesTableIdEntriesEntryFormat
    | Unset = GetV1LocalizationTableTablesTableIdEntriesEntryFormat.LEGACY,
) -> Any | RobloxLocalizationTablesApiGetTableEntriesPagedResponse | None:
    """Gets a batch of entries for a table.

    Args:
        table_id (UUID):
        cursor (str | Unset):
        game_id (int | Unset):
        entry_format (GetV1LocalizationTableTablesTableIdEntriesEntryFormat | Unset):  Default:
            GetV1LocalizationTableTablesTableIdEntriesEntryFormat.LEGACY.

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
