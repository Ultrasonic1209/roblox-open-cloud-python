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

from ...models.roblox_localization_tables_api_get_table_entries_translation_history_request import (
    RobloxLocalizationTablesApiGetTableEntriesTranslationHistoryRequest,
)
from ...models.roblox_localization_tables_api_get_table_entries_translation_history_response import (
    RobloxLocalizationTablesApiGetTableEntriesTranslationHistoryResponse,
)


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
        "url": "https://localizationtables.roblox.com/v1/localization-table/tables/{table_id}/entries/translation-history".format(
            table_id=quote(str(table_id), safe=""),
        ),
        "params": params,
        "openapi-extensions": {
            "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            "x-roblox-recommended-alternatives": [
                {
                    "url": "https://apis.roblox.com/legacy-localization-tables/v1/localization-table/tables/{tableId}/entries/translation-history",
                    "httpMethod": "POST",
                    "documentationUrl": "https://create.roblox.com/docs/cloud/reference/features/localization#post_legacy_localization_tables_v1_localization_table_tables__tableId__entries_translation_history",
                }
            ],
        },
        "openapi-id": "post_v1_localization-table_tables_tableId_entries_translation-history",
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


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/localization#localizationtables_post_v1_localization_table_tables__tableId__entries_translation_history"
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


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/localization#localizationtables_post_v1_localization_table_tables__tableId__entries_translation_history"
)
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


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/localization#localizationtables_post_v1_localization_table_tables__tableId__entries_translation_history"
)
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


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/localization#localizationtables_post_v1_localization_table_tables__tableId__entries_translation_history"
)
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
