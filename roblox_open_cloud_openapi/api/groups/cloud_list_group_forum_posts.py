from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cloud_list_group_forum_posts_view import CloudListGroupForumPostsView
from ...models.list_group_forum_posts_response import ListGroupForumPostsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    group_id: str,
    forum_category_id: str,
    *,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
    view: CloudListGroupForumPostsView | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["maxPageSize"] = max_page_size

    params["pageToken"] = page_token

    params["filter"] = filter_

    json_view: str | Unset = UNSET
    if not isinstance(view, Unset):
        json_view = view.value

    params["view"] = json_view

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/cloud/v2/groups/{group_id}/forum-categories/{forum_category_id}/posts".format(
            group_id=quote(str(group_id), safe=""),
            forum_category_id=quote(str(forum_category_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListGroupForumPostsResponse | None:
    if response.status_code == 200:
        response_200 = ListGroupForumPostsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ListGroupForumPostsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    group_id: str,
    forum_category_id: str,
    *,
    client: AuthenticatedClient,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
    view: CloudListGroupForumPostsView | Unset = UNSET,
) -> Response[ListGroupForumPostsResponse]:
    """List Group Forum Posts

     Lists forum posts in the group's forum category.

    Args:
        group_id (str):
        forum_category_id (str):
        max_page_size (int | Unset):
        page_token (str | Unset):
        filter_ (str | Unset):
        view (CloudListGroupForumPostsView | Unset):  Example: VIEW_UNSPECIFIED.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListGroupForumPostsResponse]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        forum_category_id=forum_category_id,
        max_page_size=max_page_size,
        page_token=page_token,
        filter_=filter_,
        view=view,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: str,
    forum_category_id: str,
    *,
    client: AuthenticatedClient,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
    view: CloudListGroupForumPostsView | Unset = UNSET,
) -> ListGroupForumPostsResponse | None:
    """List Group Forum Posts

     Lists forum posts in the group's forum category.

    Args:
        group_id (str):
        forum_category_id (str):
        max_page_size (int | Unset):
        page_token (str | Unset):
        filter_ (str | Unset):
        view (CloudListGroupForumPostsView | Unset):  Example: VIEW_UNSPECIFIED.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListGroupForumPostsResponse
    """

    return sync_detailed(
        group_id=group_id,
        forum_category_id=forum_category_id,
        client=client,
        max_page_size=max_page_size,
        page_token=page_token,
        filter_=filter_,
        view=view,
    ).parsed


async def asyncio_detailed(
    group_id: str,
    forum_category_id: str,
    *,
    client: AuthenticatedClient,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
    view: CloudListGroupForumPostsView | Unset = UNSET,
) -> Response[ListGroupForumPostsResponse]:
    """List Group Forum Posts

     Lists forum posts in the group's forum category.

    Args:
        group_id (str):
        forum_category_id (str):
        max_page_size (int | Unset):
        page_token (str | Unset):
        filter_ (str | Unset):
        view (CloudListGroupForumPostsView | Unset):  Example: VIEW_UNSPECIFIED.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListGroupForumPostsResponse]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        forum_category_id=forum_category_id,
        max_page_size=max_page_size,
        page_token=page_token,
        filter_=filter_,
        view=view,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: str,
    forum_category_id: str,
    *,
    client: AuthenticatedClient,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
    view: CloudListGroupForumPostsView | Unset = UNSET,
) -> ListGroupForumPostsResponse | None:
    """List Group Forum Posts

     Lists forum posts in the group's forum category.

    Args:
        group_id (str):
        forum_category_id (str):
        max_page_size (int | Unset):
        page_token (str | Unset):
        filter_ (str | Unset):
        view (CloudListGroupForumPostsView | Unset):  Example: VIEW_UNSPECIFIED.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListGroupForumPostsResponse
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            forum_category_id=forum_category_id,
            client=client,
            max_page_size=max_page_size,
            page_token=page_token,
            filter_=filter_,
            view=view,
        )
    ).parsed
