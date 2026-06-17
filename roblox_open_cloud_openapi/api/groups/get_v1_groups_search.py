from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v1_groups_search_limit import GetV1GroupsSearchLimit
from ...models.roblox_groups_api_group_search_page_response import RobloxGroupsApiGroupSearchPageResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    keyword: str,
    prioritize_exact_match: bool | Unset = False,
    limit: GetV1GroupsSearchLimit | Unset = GetV1GroupsSearchLimit.VALUE_10,
    cursor: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["keyword"] = keyword

    params["prioritizeExactMatch"] = prioritize_exact_match

    json_limit: int | Unset = UNSET
    if not isinstance(limit, Unset):
        json_limit = limit.value

    params["limit"] = json_limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://groups.roblox.com/v1/groups/search",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxGroupsApiGroupSearchPageResponse | None:
    if response.status_code == 200:
        response_200 = RobloxGroupsApiGroupSearchPageResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxGroupsApiGroupSearchPageResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    keyword: str,
    prioritize_exact_match: bool | Unset = False,
    limit: GetV1GroupsSearchLimit | Unset = GetV1GroupsSearchLimit.VALUE_10,
    cursor: str | Unset = UNSET,
) -> Response[Any | RobloxGroupsApiGroupSearchPageResponse]:
    """Search for groups by keyword.

    Args:
        keyword (str):
        prioritize_exact_match (bool | Unset):  Default: False.
        limit (GetV1GroupsSearchLimit | Unset):  Default: GetV1GroupsSearchLimit.VALUE_10.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxGroupsApiGroupSearchPageResponse]
    """

    kwargs = _get_kwargs(
        keyword=keyword,
        prioritize_exact_match=prioritize_exact_match,
        limit=limit,
        cursor=cursor,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    keyword: str,
    prioritize_exact_match: bool | Unset = False,
    limit: GetV1GroupsSearchLimit | Unset = GetV1GroupsSearchLimit.VALUE_10,
    cursor: str | Unset = UNSET,
) -> Any | RobloxGroupsApiGroupSearchPageResponse | None:
    """Search for groups by keyword.

    Args:
        keyword (str):
        prioritize_exact_match (bool | Unset):  Default: False.
        limit (GetV1GroupsSearchLimit | Unset):  Default: GetV1GroupsSearchLimit.VALUE_10.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxGroupsApiGroupSearchPageResponse
    """

    return sync_detailed(
        client=client,
        keyword=keyword,
        prioritize_exact_match=prioritize_exact_match,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    keyword: str,
    prioritize_exact_match: bool | Unset = False,
    limit: GetV1GroupsSearchLimit | Unset = GetV1GroupsSearchLimit.VALUE_10,
    cursor: str | Unset = UNSET,
) -> Response[Any | RobloxGroupsApiGroupSearchPageResponse]:
    """Search for groups by keyword.

    Args:
        keyword (str):
        prioritize_exact_match (bool | Unset):  Default: False.
        limit (GetV1GroupsSearchLimit | Unset):  Default: GetV1GroupsSearchLimit.VALUE_10.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxGroupsApiGroupSearchPageResponse]
    """

    kwargs = _get_kwargs(
        keyword=keyword,
        prioritize_exact_match=prioritize_exact_match,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    keyword: str,
    prioritize_exact_match: bool | Unset = False,
    limit: GetV1GroupsSearchLimit | Unset = GetV1GroupsSearchLimit.VALUE_10,
    cursor: str | Unset = UNSET,
) -> Any | RobloxGroupsApiGroupSearchPageResponse | None:
    """Search for groups by keyword.

    Args:
        keyword (str):
        prioritize_exact_match (bool | Unset):  Default: False.
        limit (GetV1GroupsSearchLimit | Unset):  Default: GetV1GroupsSearchLimit.VALUE_10.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxGroupsApiGroupSearchPageResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            keyword=keyword,
            prioritize_exact_match=prioritize_exact_match,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
