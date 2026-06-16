from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.entry import Entry
from ...models.update_entry_request import UpdateEntryRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    universe_id: str,
    ordered_data_store: str,
    scope: str,
    entry: str,
    *,
    body: UpdateEntryRequest,
    allow_missing: bool | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["allow_missing"] = allow_missing

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/ordered-data-stores/v1/universes/{universe_id}/orderedDataStores/{ordered_data_store}/scopes/{scope}/entries/{entry}".format(
            universe_id=quote(str(universe_id), safe=""),
            ordered_data_store=quote(str(ordered_data_store), safe=""),
            scope=quote(str(scope), safe=""),
            entry=quote(str(entry), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Entry | None:
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

    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409

    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | Entry]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    universe_id: str,
    ordered_data_store: str,
    scope: str,
    entry: str,
    *,
    client: AuthenticatedClient,
    body: UpdateEntryRequest,
    allow_missing: bool | Unset = UNSET,
) -> Response[Any | Entry]:
    """Updates an entry value and returns the updated entry.

    Args:
        universe_id (str):
        ordered_data_store (str):
        scope (str):
        entry (str):
        allow_missing (bool | Unset):
        body (UpdateEntryRequest): Updates the entry provided with a new value.

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
        entry=entry,
        body=body,
        allow_missing=allow_missing,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: str,
    ordered_data_store: str,
    scope: str,
    entry: str,
    *,
    client: AuthenticatedClient,
    body: UpdateEntryRequest,
    allow_missing: bool | Unset = UNSET,
) -> Any | Entry | None:
    """Updates an entry value and returns the updated entry.

    Args:
        universe_id (str):
        ordered_data_store (str):
        scope (str):
        entry (str):
        allow_missing (bool | Unset):
        body (UpdateEntryRequest): Updates the entry provided with a new value.

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
        entry=entry,
        client=client,
        body=body,
        allow_missing=allow_missing,
    ).parsed


async def asyncio_detailed(
    universe_id: str,
    ordered_data_store: str,
    scope: str,
    entry: str,
    *,
    client: AuthenticatedClient,
    body: UpdateEntryRequest,
    allow_missing: bool | Unset = UNSET,
) -> Response[Any | Entry]:
    """Updates an entry value and returns the updated entry.

    Args:
        universe_id (str):
        ordered_data_store (str):
        scope (str):
        entry (str):
        allow_missing (bool | Unset):
        body (UpdateEntryRequest): Updates the entry provided with a new value.

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
        entry=entry,
        body=body,
        allow_missing=allow_missing,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: str,
    ordered_data_store: str,
    scope: str,
    entry: str,
    *,
    client: AuthenticatedClient,
    body: UpdateEntryRequest,
    allow_missing: bool | Unset = UNSET,
) -> Any | Entry | None:
    """Updates an entry value and returns the updated entry.

    Args:
        universe_id (str):
        ordered_data_store (str):
        scope (str):
        entry (str):
        allow_missing (bool | Unset):
        body (UpdateEntryRequest): Updates the entry provided with a new value.

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
            entry=entry,
            client=client,
            body=body,
            allow_missing=allow_missing,
        )
    ).parsed
