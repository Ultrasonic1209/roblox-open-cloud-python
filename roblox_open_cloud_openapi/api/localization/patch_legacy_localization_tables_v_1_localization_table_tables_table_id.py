from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_localization_tables_api_update_table_contents_request import (
    RobloxLocalizationTablesApiUpdateTableContentsRequest,
)
from ...models.roblox_localization_tables_api_update_table_contents_response import (
    RobloxLocalizationTablesApiUpdateTableContentsResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    table_id: UUID,
    *,
    body: RobloxLocalizationTablesApiUpdateTableContentsRequest
    | RobloxLocalizationTablesApiUpdateTableContentsRequest
    | Unset = UNSET,
    game_id: int | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["gameId"] = game_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/legacy-localization-tables/v1/localization-table/tables/{table_id}".format(
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
            "openapi-id": "patch_legacy-localization-tables_v1_localization-table_tables_tableId",
        },
    }

    if isinstance(body, RobloxLocalizationTablesApiUpdateTableContentsRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxLocalizationTablesApiUpdateTableContentsRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxLocalizationTablesApiUpdateTableContentsResponse | None:
    if response.status_code == 200:
        response_200 = RobloxLocalizationTablesApiUpdateTableContentsResponse.from_dict(response.json())

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
) -> Response[Any | RobloxLocalizationTablesApiUpdateTableContentsResponse]:
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
    body: RobloxLocalizationTablesApiUpdateTableContentsRequest
    | RobloxLocalizationTablesApiUpdateTableContentsRequest
    | Unset = UNSET,
    game_id: int | Unset = UNSET,
) -> Response[Any | RobloxLocalizationTablesApiUpdateTableContentsResponse]:
    """Updates the tables contents based on what is provided.

    Args:
        table_id (UUID):
        game_id (int | Unset):
        body (RobloxLocalizationTablesApiUpdateTableContentsRequest):
        body (RobloxLocalizationTablesApiUpdateTableContentsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxLocalizationTablesApiUpdateTableContentsResponse]
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
    body: RobloxLocalizationTablesApiUpdateTableContentsRequest
    | RobloxLocalizationTablesApiUpdateTableContentsRequest
    | Unset = UNSET,
    game_id: int | Unset = UNSET,
) -> Any | RobloxLocalizationTablesApiUpdateTableContentsResponse | None:
    """Updates the tables contents based on what is provided.

    Args:
        table_id (UUID):
        game_id (int | Unset):
        body (RobloxLocalizationTablesApiUpdateTableContentsRequest):
        body (RobloxLocalizationTablesApiUpdateTableContentsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxLocalizationTablesApiUpdateTableContentsResponse
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
    body: RobloxLocalizationTablesApiUpdateTableContentsRequest
    | RobloxLocalizationTablesApiUpdateTableContentsRequest
    | Unset = UNSET,
    game_id: int | Unset = UNSET,
) -> Response[Any | RobloxLocalizationTablesApiUpdateTableContentsResponse]:
    """Updates the tables contents based on what is provided.

    Args:
        table_id (UUID):
        game_id (int | Unset):
        body (RobloxLocalizationTablesApiUpdateTableContentsRequest):
        body (RobloxLocalizationTablesApiUpdateTableContentsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxLocalizationTablesApiUpdateTableContentsResponse]
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
    body: RobloxLocalizationTablesApiUpdateTableContentsRequest
    | RobloxLocalizationTablesApiUpdateTableContentsRequest
    | Unset = UNSET,
    game_id: int | Unset = UNSET,
) -> Any | RobloxLocalizationTablesApiUpdateTableContentsResponse | None:
    """Updates the tables contents based on what is provided.

    Args:
        table_id (UUID):
        game_id (int | Unset):
        body (RobloxLocalizationTablesApiUpdateTableContentsRequest):
        body (RobloxLocalizationTablesApiUpdateTableContentsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxLocalizationTablesApiUpdateTableContentsResponse
    """

    return (
        await asyncio_detailed(
            table_id=table_id,
            client=client,
            body=body,
            game_id=game_id,
        )
    ).parsed
