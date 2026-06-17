import sys
from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response

if sys.version_info >= (3, 13):
    from warnings import deprecated
else:
    from typing_extensions import deprecated

from ...models.create_entry_request import CreateEntryRequest
from ...models.entry import Entry


def _get_kwargs(
    universe_id: str,
    ordered_data_store: str,
    scope: str,
    *,
    body: CreateEntryRequest,
    id: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["id"] = id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/ordered-data-stores/v1/universes/{universe_id}/orderedDataStores/{ordered_data_store}/scopes/{scope}/entries".format(
            universe_id=quote(str(universe_id), safe=""),
            ordered_data_store=quote(str(ordered_data_store), safe=""),
            scope=quote(str(scope), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Any | Entry | None:
    if response.status_code == 200:
        response_200 = Entry.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[Any | Entry]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/storage#OrderedDataStores_CreateEntry"
)
def sync_detailed(
    universe_id: str,
    ordered_data_store: str,
    scope: str,
    *,
    client: AuthenticatedClient,
    body: CreateEntryRequest,
    id: str,
) -> Response[Any | Entry]:
    """Creates a new entry with the content value provided.

    Args:
        universe_id (str):
        ordered_data_store (str):
        scope (str):
        id (str):
        body (CreateEntryRequest): Creates a new entry with the value provided.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Entry]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        ordered_data_store=ordered_data_store,
        scope=scope,
        body=body,
        id=id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/storage#OrderedDataStores_CreateEntry"
)
def sync(
    universe_id: str,
    ordered_data_store: str,
    scope: str,
    *,
    client: AuthenticatedClient,
    body: CreateEntryRequest,
    id: str,
) -> Any | Entry | None:
    """Creates a new entry with the content value provided.

    Args:
        universe_id (str):
        ordered_data_store (str):
        scope (str):
        id (str):
        body (CreateEntryRequest): Creates a new entry with the value provided.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Entry
    """

    return sync_detailed(
        universe_id=universe_id,
        ordered_data_store=ordered_data_store,
        scope=scope,
        client=client,
        body=body,
        id=id,
    ).parsed


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/storage#OrderedDataStores_CreateEntry"
)
async def asyncio_detailed(
    universe_id: str,
    ordered_data_store: str,
    scope: str,
    *,
    client: AuthenticatedClient,
    body: CreateEntryRequest,
    id: str,
) -> Response[Any | Entry]:
    """Creates a new entry with the content value provided.

    Args:
        universe_id (str):
        ordered_data_store (str):
        scope (str):
        id (str):
        body (CreateEntryRequest): Creates a new entry with the value provided.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Entry]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        ordered_data_store=ordered_data_store,
        scope=scope,
        body=body,
        id=id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/storage#OrderedDataStores_CreateEntry"
)
async def asyncio(
    universe_id: str,
    ordered_data_store: str,
    scope: str,
    *,
    client: AuthenticatedClient,
    body: CreateEntryRequest,
    id: str,
) -> Any | Entry | None:
    """Creates a new entry with the content value provided.

    Args:
        universe_id (str):
        ordered_data_store (str):
        scope (str):
        id (str):
        body (CreateEntryRequest): Creates a new entry with the value provided.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Entry
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            ordered_data_store=ordered_data_store,
            scope=scope,
            client=client,
            body=body,
            id=id,
        )
    ).parsed
