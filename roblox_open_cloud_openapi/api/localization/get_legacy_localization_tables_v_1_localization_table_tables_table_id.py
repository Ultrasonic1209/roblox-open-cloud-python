from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote
from uuid import UUID

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_localization_tables_api_get_table_response import RobloxLocalizationTablesApiGetTableResponse
from ...types import Response


def _get_kwargs(
    table_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/legacy-localization-tables/v1/localization-table/tables/{table_id}".format(
            table_id=quote(str(table_id), safe=""),
        ),
        "extensions": {
            "openapi-extensions": {
                "x-roblox-rate-limits": {
                    "perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 100},
                    "perOauth2Authorization": {"period": "MINUTE", "maxInPeriod": 100},
                },
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
                "x-roblox-scopes": [{"name": "legacy-universe:manage"}],
            },
            "openapi-id": "get_legacy-localization-tables_v1_localization-table_tables_tableId",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxLocalizationTablesApiGetTableResponse | None:
    if response.status_code == 200:
        response_200 = RobloxLocalizationTablesApiGetTableResponse.from_dict(response.json())

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
) -> Response[Any | RobloxLocalizationTablesApiGetTableResponse]:
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
) -> Response[Any | RobloxLocalizationTablesApiGetTableResponse]:
    """Get table information by the id of the table.

    Args:
        table_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxLocalizationTablesApiGetTableResponse]
    """

    kwargs = _get_kwargs(
        table_id=table_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    table_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxLocalizationTablesApiGetTableResponse | None:
    """Get table information by the id of the table.

    Args:
        table_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxLocalizationTablesApiGetTableResponse
    """

    return sync_detailed(
        table_id=table_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    table_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxLocalizationTablesApiGetTableResponse]:
    """Get table information by the id of the table.

    Args:
        table_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxLocalizationTablesApiGetTableResponse]
    """

    kwargs = _get_kwargs(
        table_id=table_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    table_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxLocalizationTablesApiGetTableResponse | None:
    """Get table information by the id of the table.

    Args:
        table_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxLocalizationTablesApiGetTableResponse
    """

    return (
        await asyncio_detailed(
            table_id=table_id,
            client=client,
        )
    ).parsed
