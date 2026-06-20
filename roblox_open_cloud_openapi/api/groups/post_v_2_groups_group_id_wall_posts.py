from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_groups_api_create_wall_post_request import RobloxGroupsApiCreateWallPostRequest
from ...models.roblox_groups_api_group_wall_post_v2_model import RobloxGroupsApiGroupWallPostV2Model
from ...types import UNSET, Response, Unset


def _get_kwargs(
    group_id: int,
    *,
    body: RobloxGroupsApiCreateWallPostRequest | RobloxGroupsApiCreateWallPostRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "https://groups.roblox.com/v2/groups/{group_id}/wall/posts".format(
            group_id=quote(str(group_id), safe=""),
        ),
        "extensions": {
            "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
            "openapi-id": "post_v2_groups_groupId_wall_posts",
        },
    }

    if isinstance(body, RobloxGroupsApiCreateWallPostRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxGroupsApiCreateWallPostRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxGroupsApiGroupWallPostV2Model | None:
    if response.status_code == 200:
        response_200 = RobloxGroupsApiGroupWallPostV2Model.from_dict(response.json())

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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxGroupsApiGroupWallPostV2Model]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    group_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxGroupsApiCreateWallPostRequest | RobloxGroupsApiCreateWallPostRequest | Unset = UNSET,
) -> Response[Any | RobloxGroupsApiGroupWallPostV2Model]:
    """Creates a post on a group wall

    Args:
        group_id (int):
        body (RobloxGroupsApiCreateWallPostRequest): A request model for creating a group wall
            post
        body (RobloxGroupsApiCreateWallPostRequest): A request model for creating a group wall
            post

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxGroupsApiGroupWallPostV2Model]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        body=body,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxGroupsApiCreateWallPostRequest | RobloxGroupsApiCreateWallPostRequest | Unset = UNSET,
) -> Any | RobloxGroupsApiGroupWallPostV2Model | None:
    """Creates a post on a group wall

    Args:
        group_id (int):
        body (RobloxGroupsApiCreateWallPostRequest): A request model for creating a group wall
            post
        body (RobloxGroupsApiCreateWallPostRequest): A request model for creating a group wall
            post

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxGroupsApiGroupWallPostV2Model
    """

    return sync_detailed(
        group_id=group_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    group_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxGroupsApiCreateWallPostRequest | RobloxGroupsApiCreateWallPostRequest | Unset = UNSET,
) -> Response[Any | RobloxGroupsApiGroupWallPostV2Model]:
    """Creates a post on a group wall

    Args:
        group_id (int):
        body (RobloxGroupsApiCreateWallPostRequest): A request model for creating a group wall
            post
        body (RobloxGroupsApiCreateWallPostRequest): A request model for creating a group wall
            post

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxGroupsApiGroupWallPostV2Model]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxGroupsApiCreateWallPostRequest | RobloxGroupsApiCreateWallPostRequest | Unset = UNSET,
) -> Any | RobloxGroupsApiGroupWallPostV2Model | None:
    """Creates a post on a group wall

    Args:
        group_id (int):
        body (RobloxGroupsApiCreateWallPostRequest): A request model for creating a group wall
            post
        body (RobloxGroupsApiCreateWallPostRequest): A request model for creating a group wall
            post

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxGroupsApiGroupWallPostV2Model
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
            body=body,
        )
    ).parsed
