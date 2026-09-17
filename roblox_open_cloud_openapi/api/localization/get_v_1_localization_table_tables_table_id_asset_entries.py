from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_localization_tables_api_get_table_asset_entries_paged_response import (
    RobloxLocalizationTablesApiGetTableAssetEntriesPagedResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    table_id: UUID,
    *,
    cursor: str | Unset = UNSET,
    game_id: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["cursor"] = cursor

    params["gameId"] = game_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://localizationtables.roblox.com/v1/localization-table/tables/{table_id}/asset-entries".format(
            table_id=quote(str(table_id), safe=""),
        ),
        "params": params,
        "extensions": {
            "openapi-extensions": {
                "x-roblox-stability": "EXPERIMENTAL",
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            },
            "openapi-id": "get_v1_localization-table_tables_tableId_asset-entries",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxLocalizationTablesApiGetTableAssetEntriesPagedResponse | None:
    if response.status_code == 200:
        response_200 = RobloxLocalizationTablesApiGetTableAssetEntriesPagedResponse.from_dict(response.json())

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
) -> Response[Any | RobloxLocalizationTablesApiGetTableAssetEntriesPagedResponse]:
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
) -> Response[Any | RobloxLocalizationTablesApiGetTableAssetEntriesPagedResponse]:
    """Gets a page of asset (image) entries for the specified table, along with the table's
    per-locale asset translations.

    Args:
        table_id (UUID):
        cursor (str | Unset):
        game_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxLocalizationTablesApiGetTableAssetEntriesPagedResponse]
    """

    kwargs = _get_kwargs(
        table_id=table_id,
        cursor=cursor,
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
    cursor: str | Unset = UNSET,
    game_id: int | Unset = UNSET,
) -> Any | RobloxLocalizationTablesApiGetTableAssetEntriesPagedResponse | None:
    """Gets a page of asset (image) entries for the specified table, along with the table's
    per-locale asset translations.

    Args:
        table_id (UUID):
        cursor (str | Unset):
        game_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxLocalizationTablesApiGetTableAssetEntriesPagedResponse
    """

    return sync_detailed(
        table_id=table_id,
        client=client,
        cursor=cursor,
        game_id=game_id,
    ).parsed


async def asyncio_detailed(
    table_id: UUID,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    game_id: int | Unset = UNSET,
) -> Response[Any | RobloxLocalizationTablesApiGetTableAssetEntriesPagedResponse]:
    """Gets a page of asset (image) entries for the specified table, along with the table's
    per-locale asset translations.

    Args:
        table_id (UUID):
        cursor (str | Unset):
        game_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxLocalizationTablesApiGetTableAssetEntriesPagedResponse]
    """

    kwargs = _get_kwargs(
        table_id=table_id,
        cursor=cursor,
        game_id=game_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    table_id: UUID,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    game_id: int | Unset = UNSET,
) -> Any | RobloxLocalizationTablesApiGetTableAssetEntriesPagedResponse | None:
    """Gets a page of asset (image) entries for the specified table, along with the table's
    per-locale asset translations.

    Args:
        table_id (UUID):
        cursor (str | Unset):
        game_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxLocalizationTablesApiGetTableAssetEntriesPagedResponse
    """

    return (
        await asyncio_detailed(
            table_id=table_id,
            client=client,
            cursor=cursor,
            game_id=game_id,
        )
    ).parsed
