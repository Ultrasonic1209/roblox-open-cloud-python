from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v1_users_search_limit import GetV1UsersSearchLimit
from ...models.roblox_web_web_api_models_api_page_response_roblox_users_api_search_get_user_response import (
    RobloxWebWebAPIModelsApiPageResponseRobloxUsersApiSearchGetUserResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    keyword: str,
    session_id: str | Unset = UNSET,
    limit: GetV1UsersSearchLimit | Unset = GetV1UsersSearchLimit.VALUE_10,
    cursor: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["keyword"] = keyword

    params["sessionId"] = session_id

    json_limit: int | Unset = UNSET
    if not isinstance(limit, Unset):
        json_limit = limit.value

    params["limit"] = json_limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://users.roblox.com/v1/users/search",
        "params": params,
        "extensions": {
            "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
            "openapi-id": "get_v1_users_search",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxUsersApiSearchGetUserResponse | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIModelsApiPageResponseRobloxUsersApiSearchGetUserResponse.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxUsersApiSearchGetUserResponse]:
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
    session_id: str | Unset = UNSET,
    limit: GetV1UsersSearchLimit | Unset = GetV1UsersSearchLimit.VALUE_10,
    cursor: str | Unset = UNSET,
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxUsersApiSearchGetUserResponse]:
    """Searches for users by keyword.

    Args:
        keyword (str):
        session_id (str | Unset):
        limit (GetV1UsersSearchLimit | Unset):  Default: GetV1UsersSearchLimit.VALUE_10.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxUsersApiSearchGetUserResponse]
    """

    kwargs = _get_kwargs(
        keyword=keyword,
        session_id=session_id,
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
    session_id: str | Unset = UNSET,
    limit: GetV1UsersSearchLimit | Unset = GetV1UsersSearchLimit.VALUE_10,
    cursor: str | Unset = UNSET,
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxUsersApiSearchGetUserResponse | None:
    """Searches for users by keyword.

    Args:
        keyword (str):
        session_id (str | Unset):
        limit (GetV1UsersSearchLimit | Unset):  Default: GetV1UsersSearchLimit.VALUE_10.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiPageResponseRobloxUsersApiSearchGetUserResponse
    """

    return sync_detailed(
        client=client,
        keyword=keyword,
        session_id=session_id,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    keyword: str,
    session_id: str | Unset = UNSET,
    limit: GetV1UsersSearchLimit | Unset = GetV1UsersSearchLimit.VALUE_10,
    cursor: str | Unset = UNSET,
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxUsersApiSearchGetUserResponse]:
    """Searches for users by keyword.

    Args:
        keyword (str):
        session_id (str | Unset):
        limit (GetV1UsersSearchLimit | Unset):  Default: GetV1UsersSearchLimit.VALUE_10.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxUsersApiSearchGetUserResponse]
    """

    kwargs = _get_kwargs(
        keyword=keyword,
        session_id=session_id,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    keyword: str,
    session_id: str | Unset = UNSET,
    limit: GetV1UsersSearchLimit | Unset = GetV1UsersSearchLimit.VALUE_10,
    cursor: str | Unset = UNSET,
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxUsersApiSearchGetUserResponse | None:
    """Searches for users by keyword.

    Args:
        keyword (str):
        session_id (str | Unset):
        limit (GetV1UsersSearchLimit | Unset):  Default: GetV1UsersSearchLimit.VALUE_10.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiPageResponseRobloxUsersApiSearchGetUserResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            keyword=keyword,
            session_id=session_id,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
