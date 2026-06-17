from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_localization_tables_api_create_table_request import RobloxLocalizationTablesApiCreateTableRequest
from ...models.roblox_localization_tables_api_create_table_response import (
    RobloxLocalizationTablesApiCreateTableResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: RobloxLocalizationTablesApiCreateTableRequest | RobloxLocalizationTablesApiCreateTableRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "https://localizationtables.roblox.com/v1/localization-table/tables",
    }

    if isinstance(body, RobloxLocalizationTablesApiCreateTableRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxLocalizationTablesApiCreateTableRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxLocalizationTablesApiCreateTableResponse | None:
    if response.status_code == 200:
        response_200 = RobloxLocalizationTablesApiCreateTableResponse.from_dict(response.json())

        return response_200

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
) -> Response[Any | RobloxLocalizationTablesApiCreateTableResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxLocalizationTablesApiCreateTableRequest | RobloxLocalizationTablesApiCreateTableRequest | Unset = UNSET,
) -> Response[Any | RobloxLocalizationTablesApiCreateTableResponse]:
    """Creates a Localization Table with the given data.
    Note that this endpoint simply creates a table and does not associate it with any universe, so if
    intending to use this to create tables usable in experience more setup will be needed to grant those
    experiences access.

    Args:
        body (RobloxLocalizationTablesApiCreateTableRequest):
        body (RobloxLocalizationTablesApiCreateTableRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxLocalizationTablesApiCreateTableResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: RobloxLocalizationTablesApiCreateTableRequest | RobloxLocalizationTablesApiCreateTableRequest | Unset = UNSET,
) -> Any | RobloxLocalizationTablesApiCreateTableResponse | None:
    """Creates a Localization Table with the given data.
    Note that this endpoint simply creates a table and does not associate it with any universe, so if
    intending to use this to create tables usable in experience more setup will be needed to grant those
    experiences access.

    Args:
        body (RobloxLocalizationTablesApiCreateTableRequest):
        body (RobloxLocalizationTablesApiCreateTableRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxLocalizationTablesApiCreateTableResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxLocalizationTablesApiCreateTableRequest | RobloxLocalizationTablesApiCreateTableRequest | Unset = UNSET,
) -> Response[Any | RobloxLocalizationTablesApiCreateTableResponse]:
    """Creates a Localization Table with the given data.
    Note that this endpoint simply creates a table and does not associate it with any universe, so if
    intending to use this to create tables usable in experience more setup will be needed to grant those
    experiences access.

    Args:
        body (RobloxLocalizationTablesApiCreateTableRequest):
        body (RobloxLocalizationTablesApiCreateTableRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxLocalizationTablesApiCreateTableResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RobloxLocalizationTablesApiCreateTableRequest | RobloxLocalizationTablesApiCreateTableRequest | Unset = UNSET,
) -> Any | RobloxLocalizationTablesApiCreateTableResponse | None:
    """Creates a Localization Table with the given data.
    Note that this endpoint simply creates a table and does not associate it with any universe, so if
    intending to use this to create tables usable in experience more setup will be needed to grant those
    experiences access.

    Args:
        body (RobloxLocalizationTablesApiCreateTableRequest):
        body (RobloxLocalizationTablesApiCreateTableRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxLocalizationTablesApiCreateTableResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
