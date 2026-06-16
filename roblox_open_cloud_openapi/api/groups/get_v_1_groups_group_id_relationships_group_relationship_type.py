from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_groups_api_group_relationships_response import RobloxGroupsApiGroupRelationshipsResponse
from ...types import UNSET, Response


def _get_kwargs(
    group_id: int,
    group_relationship_type: str,
    *,
    start_row_index: int,
    max_rows: int,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["StartRowIndex"] = start_row_index

    params["MaxRows"] = max_rows

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/groups/{group_id}/relationships/{group_relationship_type}".format(
            group_id=quote(str(group_id), safe=""),
            group_relationship_type=quote(str(group_relationship_type), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxGroupsApiGroupRelationshipsResponse | None:
    if response.status_code == 200:
        response_200 = RobloxGroupsApiGroupRelationshipsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RobloxGroupsApiGroupRelationshipsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    group_id: int,
    group_relationship_type: str,
    *,
    client: AuthenticatedClient,
    start_row_index: int,
    max_rows: int,
) -> Response[Any | RobloxGroupsApiGroupRelationshipsResponse]:
    """Gets a group's relationships

    Args:
        group_id (int):
        group_relationship_type (str):
        start_row_index (int):
        max_rows (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxGroupsApiGroupRelationshipsResponse]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        group_relationship_type=group_relationship_type,
        start_row_index=start_row_index,
        max_rows=max_rows,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: int,
    group_relationship_type: str,
    *,
    client: AuthenticatedClient,
    start_row_index: int,
    max_rows: int,
) -> Any | RobloxGroupsApiGroupRelationshipsResponse | None:
    """Gets a group's relationships

    Args:
        group_id (int):
        group_relationship_type (str):
        start_row_index (int):
        max_rows (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxGroupsApiGroupRelationshipsResponse
    """

    return sync_detailed(
        group_id=group_id,
        group_relationship_type=group_relationship_type,
        client=client,
        start_row_index=start_row_index,
        max_rows=max_rows,
    ).parsed


async def asyncio_detailed(
    group_id: int,
    group_relationship_type: str,
    *,
    client: AuthenticatedClient,
    start_row_index: int,
    max_rows: int,
) -> Response[Any | RobloxGroupsApiGroupRelationshipsResponse]:
    """Gets a group's relationships

    Args:
        group_id (int):
        group_relationship_type (str):
        start_row_index (int):
        max_rows (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxGroupsApiGroupRelationshipsResponse]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        group_relationship_type=group_relationship_type,
        start_row_index=start_row_index,
        max_rows=max_rows,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: int,
    group_relationship_type: str,
    *,
    client: AuthenticatedClient,
    start_row_index: int,
    max_rows: int,
) -> Any | RobloxGroupsApiGroupRelationshipsResponse | None:
    """Gets a group's relationships

    Args:
        group_id (int):
        group_relationship_type (str):
        start_row_index (int):
        max_rows (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxGroupsApiGroupRelationshipsResponse
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            group_relationship_type=group_relationship_type,
            client=client,
            start_row_index=start_row_index,
            max_rows=max_rows,
        )
    ).parsed
