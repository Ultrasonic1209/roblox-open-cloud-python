import sys
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response

if sys.version_info >= (3, 13):
    from warnings import deprecated
else:
    from typing_extensions import deprecated

from ...models.datastores_list_datastores_async_response_200 import DatastoresListDatastoresAsyncResponse200
from ...types import Unset


def _get_kwargs(
    universe_id: int,
    *,
    cursor: None | str | Unset = UNSET,
    limit: int | Unset = 1,
    prefix: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_cursor: None | str | Unset
    if isinstance(cursor, Unset):
        json_cursor = UNSET
    else:
        json_cursor = cursor
    params["cursor"] = json_cursor

    params["limit"] = limit

    json_prefix: None | str | Unset
    if isinstance(prefix, Unset):
        json_prefix = UNSET
    else:
        json_prefix = prefix
    params["prefix"] = json_prefix

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/datastores/v1/universes/{universe_id}/standard-datastores".format(
            universe_id=quote(str(universe_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DatastoresListDatastoresAsyncResponse200 | None:
    if response.status_code == 200:
        response_200 = DatastoresListDatastoresAsyncResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DatastoresListDatastoresAsyncResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/storage#Datastores_ListDatastoresAsync"
)
def sync_detailed(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    cursor: None | str | Unset = UNSET,
    limit: int | Unset = 1,
    prefix: None | str | Unset = UNSET,
) -> Response[DatastoresListDatastoresAsyncResponse200]:
    """List data stores in an experience

     Returns a list of an experience's data stores.

    Args:
        universe_id (int):
        cursor (None | str | Unset):
        limit (int | Unset):  Default: 1.
        prefix (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatastoresListDatastoresAsyncResponse200]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        cursor=cursor,
        limit=limit,
        prefix=prefix,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/storage#Datastores_ListDatastoresAsync"
)
def sync(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    cursor: None | str | Unset = UNSET,
    limit: int | Unset = 1,
    prefix: None | str | Unset = UNSET,
) -> DatastoresListDatastoresAsyncResponse200 | None:
    """List data stores in an experience

     Returns a list of an experience's data stores.

    Args:
        universe_id (int):
        cursor (None | str | Unset):
        limit (int | Unset):  Default: 1.
        prefix (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatastoresListDatastoresAsyncResponse200
    """

    return sync_detailed(
        universe_id=universe_id,
        client=client,
        cursor=cursor,
        limit=limit,
        prefix=prefix,
    ).parsed


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/storage#Datastores_ListDatastoresAsync"
)
async def asyncio_detailed(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    cursor: None | str | Unset = UNSET,
    limit: int | Unset = 1,
    prefix: None | str | Unset = UNSET,
) -> Response[DatastoresListDatastoresAsyncResponse200]:
    """List data stores in an experience

     Returns a list of an experience's data stores.

    Args:
        universe_id (int):
        cursor (None | str | Unset):
        limit (int | Unset):  Default: 1.
        prefix (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatastoresListDatastoresAsyncResponse200]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        cursor=cursor,
        limit=limit,
        prefix=prefix,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/storage#Datastores_ListDatastoresAsync"
)
async def asyncio(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    cursor: None | str | Unset = UNSET,
    limit: int | Unset = 1,
    prefix: None | str | Unset = UNSET,
) -> DatastoresListDatastoresAsyncResponse200 | None:
    """List data stores in an experience

     Returns a list of an experience's data stores.

    Args:
        universe_id (int):
        cursor (None | str | Unset):
        limit (int | Unset):  Default: 1.
        prefix (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatastoresListDatastoresAsyncResponse200
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            client=client,
            cursor=cursor,
            limit=limit,
            prefix=prefix,
        )
    ).parsed
