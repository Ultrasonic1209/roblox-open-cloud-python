from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_group_forum_categories_response import ListGroupForumCategoriesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    group_id: str,
    *,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["maxPageSize"] = max_page_size

    params["pageToken"] = page_token

    params["filter"] = filter_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/cloud/v2/groups/{group_id}/forum-categories".format(
            group_id=quote(str(group_id), safe=""),
        ),
        "params": params,
        "extensions": {
            "openapi-extensions": {
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
                "x-roblox-scopes": [{"name": "group-forum:read"}],
                "x-roblox-docs": {
                    "category": "Users and groups",
                    "methodProperties": {"scopes": ["group-forum:read"]},
                    "resource": {"$ref": "#/components/schemas/GroupForumCategory", "name": "GroupForumCategory"},
                },
                "x-roblox-stability": "BETA",
                "x-roblox-rate-limits": {
                    "perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 150},
                    "perOauth2Authorization": {"period": "MINUTE", "maxInPeriod": 30},
                },
            },
            "openapi-id": "Cloud_ListGroupForumCategories",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ListGroupForumCategoriesResponse | None:
    if response.status_code == 200:
        response_200 = ListGroupForumCategoriesResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ListGroupForumCategoriesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    group_id: str,
    *,
    client: AuthenticatedClient,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
) -> Response[ListGroupForumCategoriesResponse]:
    """List Group Forum Categories

     Lists forum categories in the group. Supports filtering.

    Args:
        group_id (str):
        max_page_size (int | Unset):
        page_token (str | Unset):
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListGroupForumCategoriesResponse]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        max_page_size=max_page_size,
        page_token=page_token,
        filter_=filter_,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: str,
    *,
    client: AuthenticatedClient,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
) -> ListGroupForumCategoriesResponse | None:
    """List Group Forum Categories

     Lists forum categories in the group. Supports filtering.

    Args:
        group_id (str):
        max_page_size (int | Unset):
        page_token (str | Unset):
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListGroupForumCategoriesResponse
    """

    return sync_detailed(
        group_id=group_id,
        client=client,
        max_page_size=max_page_size,
        page_token=page_token,
        filter_=filter_,
    ).parsed


async def asyncio_detailed(
    group_id: str,
    *,
    client: AuthenticatedClient,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
) -> Response[ListGroupForumCategoriesResponse]:
    """List Group Forum Categories

     Lists forum categories in the group. Supports filtering.

    Args:
        group_id (str):
        max_page_size (int | Unset):
        page_token (str | Unset):
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListGroupForumCategoriesResponse]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        max_page_size=max_page_size,
        page_token=page_token,
        filter_=filter_,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: str,
    *,
    client: AuthenticatedClient,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
) -> ListGroupForumCategoriesResponse | None:
    """List Group Forum Categories

     Lists forum categories in the group. Supports filtering.

    Args:
        group_id (str):
        max_page_size (int | Unset):
        page_token (str | Unset):
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListGroupForumCategoriesResponse
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
            max_page_size=max_page_size,
            page_token=page_token,
            filter_=filter_,
        )
    ).parsed
