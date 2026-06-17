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

from ...models.roblox_groups_api_create_wall_post_request import RobloxGroupsApiCreateWallPostRequest
from ...models.roblox_groups_api_models_response_group_wall_post_model import (
    RobloxGroupsApiModelsResponseGroupWallPostModel,
)


def _get_kwargs(
    group_id: int,
    *,
    body: RobloxGroupsApiCreateWallPostRequest | RobloxGroupsApiCreateWallPostRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "https://groups.roblox.com/v1/groups/{group_id}/wall/posts".format(
            group_id=quote(str(group_id), safe=""),
        ),
        "openapi-extensions": {
            "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            "x-roblox-recommended-alternatives": [
                {
                    "url": "https://groups.roblox.com/v2/groups/{groupId}/wall/posts",
                    "httpMethod": "POST",
                    "documentationUrl": "https://create.roblox.com/docs/cloud/reference/features/groups#groups_post_v2_groups__groupId__wall_posts",
                }
            ],
        },
        "openapi-id": "post_v1_groups_groupId_wall_posts",
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
) -> Any | RobloxGroupsApiModelsResponseGroupWallPostModel | None:
    if response.status_code == 200:
        response_200 = RobloxGroupsApiModelsResponseGroupWallPostModel.from_dict(response.json())

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

    if response.status_code == 405:
        response_405 = cast(Any, None)
        return response_405

    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxGroupsApiModelsResponseGroupWallPostModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/groups#groups_post_v1_groups__groupId__wall_posts"
)
def sync_detailed(
    group_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxGroupsApiCreateWallPostRequest | RobloxGroupsApiCreateWallPostRequest | Unset = UNSET,
) -> Response[Any | RobloxGroupsApiModelsResponseGroupWallPostModel]:
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
        Response[Any | RobloxGroupsApiModelsResponseGroupWallPostModel]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        body=body,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/groups#groups_post_v1_groups__groupId__wall_posts"
)
def sync(
    group_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxGroupsApiCreateWallPostRequest | RobloxGroupsApiCreateWallPostRequest | Unset = UNSET,
) -> Any | RobloxGroupsApiModelsResponseGroupWallPostModel | None:
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
        Any | RobloxGroupsApiModelsResponseGroupWallPostModel
    """

    return sync_detailed(
        group_id=group_id,
        client=client,
        body=body,
    ).parsed


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/groups#groups_post_v1_groups__groupId__wall_posts"
)
async def asyncio_detailed(
    group_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxGroupsApiCreateWallPostRequest | RobloxGroupsApiCreateWallPostRequest | Unset = UNSET,
) -> Response[Any | RobloxGroupsApiModelsResponseGroupWallPostModel]:
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
        Response[Any | RobloxGroupsApiModelsResponseGroupWallPostModel]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/groups#groups_post_v1_groups__groupId__wall_posts"
)
async def asyncio(
    group_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxGroupsApiCreateWallPostRequest | RobloxGroupsApiCreateWallPostRequest | Unset = UNSET,
) -> Any | RobloxGroupsApiModelsResponseGroupWallPostModel | None:
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
        Any | RobloxGroupsApiModelsResponseGroupWallPostModel
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
            body=body,
        )
    ).parsed
