from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v2_users_user_id_games_access_filter import GetV2UsersUserIdGamesAccessFilter
from ...models.get_v2_users_user_id_games_limit import GetV2UsersUserIdGamesLimit
from ...models.get_v2_users_user_id_games_sort_order import GetV2UsersUserIdGamesSortOrder
from ...models.roblox_web_web_api_models_api_page_response_roblox_web_responses_games_game_response_v2 import (
    RobloxWebWebAPIModelsApiPageResponseRobloxWebResponsesGamesGameResponseV2,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: int,
    *,
    access_filter: GetV2UsersUserIdGamesAccessFilter | Unset = GetV2UsersUserIdGamesAccessFilter.VALUE_2,
    limit: GetV2UsersUserIdGamesLimit | Unset = GetV2UsersUserIdGamesLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV2UsersUserIdGamesSortOrder | Unset = GetV2UsersUserIdGamesSortOrder.ASC,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_access_filter: int | Unset = UNSET
    if not isinstance(access_filter, Unset):
        json_access_filter = access_filter.value

    params["accessFilter"] = json_access_filter

    json_limit: int | Unset = UNSET
    if not isinstance(limit, Unset):
        json_limit = limit.value

    params["limit"] = json_limit

    params["cursor"] = cursor

    json_sort_order: str | Unset = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value

    params["sortOrder"] = json_sort_order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://games.roblox.com/v2/users/{user_id}/games".format(
            user_id=quote(str(user_id), safe=""),
        ),
        "params": params,
        "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
        "openapi-id": "get_v2_users_userId_games",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> RobloxWebWebAPIModelsApiPageResponseRobloxWebResponsesGamesGameResponseV2 | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIModelsApiPageResponseRobloxWebResponsesGamesGameResponseV2.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[RobloxWebWebAPIModelsApiPageResponseRobloxWebResponsesGamesGameResponseV2]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: int,
    *,
    client: AuthenticatedClient,
    access_filter: GetV2UsersUserIdGamesAccessFilter | Unset = GetV2UsersUserIdGamesAccessFilter.VALUE_2,
    limit: GetV2UsersUserIdGamesLimit | Unset = GetV2UsersUserIdGamesLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV2UsersUserIdGamesSortOrder | Unset = GetV2UsersUserIdGamesSortOrder.ASC,
) -> Response[RobloxWebWebAPIModelsApiPageResponseRobloxWebResponsesGamesGameResponseV2]:
    """Gets games created by the specified user.

    Args:
        user_id (int):
        access_filter (GetV2UsersUserIdGamesAccessFilter | Unset):  Default:
            GetV2UsersUserIdGamesAccessFilter.VALUE_2.
        limit (GetV2UsersUserIdGamesLimit | Unset):  Default: GetV2UsersUserIdGamesLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV2UsersUserIdGamesSortOrder | Unset):  Default:
            GetV2UsersUserIdGamesSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RobloxWebWebAPIModelsApiPageResponseRobloxWebResponsesGamesGameResponseV2]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        access_filter=access_filter,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: int,
    *,
    client: AuthenticatedClient,
    access_filter: GetV2UsersUserIdGamesAccessFilter | Unset = GetV2UsersUserIdGamesAccessFilter.VALUE_2,
    limit: GetV2UsersUserIdGamesLimit | Unset = GetV2UsersUserIdGamesLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV2UsersUserIdGamesSortOrder | Unset = GetV2UsersUserIdGamesSortOrder.ASC,
) -> RobloxWebWebAPIModelsApiPageResponseRobloxWebResponsesGamesGameResponseV2 | None:
    """Gets games created by the specified user.

    Args:
        user_id (int):
        access_filter (GetV2UsersUserIdGamesAccessFilter | Unset):  Default:
            GetV2UsersUserIdGamesAccessFilter.VALUE_2.
        limit (GetV2UsersUserIdGamesLimit | Unset):  Default: GetV2UsersUserIdGamesLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV2UsersUserIdGamesSortOrder | Unset):  Default:
            GetV2UsersUserIdGamesSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RobloxWebWebAPIModelsApiPageResponseRobloxWebResponsesGamesGameResponseV2
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        access_filter=access_filter,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
    ).parsed


async def asyncio_detailed(
    user_id: int,
    *,
    client: AuthenticatedClient,
    access_filter: GetV2UsersUserIdGamesAccessFilter | Unset = GetV2UsersUserIdGamesAccessFilter.VALUE_2,
    limit: GetV2UsersUserIdGamesLimit | Unset = GetV2UsersUserIdGamesLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV2UsersUserIdGamesSortOrder | Unset = GetV2UsersUserIdGamesSortOrder.ASC,
) -> Response[RobloxWebWebAPIModelsApiPageResponseRobloxWebResponsesGamesGameResponseV2]:
    """Gets games created by the specified user.

    Args:
        user_id (int):
        access_filter (GetV2UsersUserIdGamesAccessFilter | Unset):  Default:
            GetV2UsersUserIdGamesAccessFilter.VALUE_2.
        limit (GetV2UsersUserIdGamesLimit | Unset):  Default: GetV2UsersUserIdGamesLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV2UsersUserIdGamesSortOrder | Unset):  Default:
            GetV2UsersUserIdGamesSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RobloxWebWebAPIModelsApiPageResponseRobloxWebResponsesGamesGameResponseV2]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        access_filter=access_filter,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: int,
    *,
    client: AuthenticatedClient,
    access_filter: GetV2UsersUserIdGamesAccessFilter | Unset = GetV2UsersUserIdGamesAccessFilter.VALUE_2,
    limit: GetV2UsersUserIdGamesLimit | Unset = GetV2UsersUserIdGamesLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV2UsersUserIdGamesSortOrder | Unset = GetV2UsersUserIdGamesSortOrder.ASC,
) -> RobloxWebWebAPIModelsApiPageResponseRobloxWebResponsesGamesGameResponseV2 | None:
    """Gets games created by the specified user.

    Args:
        user_id (int):
        access_filter (GetV2UsersUserIdGamesAccessFilter | Unset):  Default:
            GetV2UsersUserIdGamesAccessFilter.VALUE_2.
        limit (GetV2UsersUserIdGamesLimit | Unset):  Default: GetV2UsersUserIdGamesLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV2UsersUserIdGamesSortOrder | Unset):  Default:
            GetV2UsersUserIdGamesSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RobloxWebWebAPIModelsApiPageResponseRobloxWebResponsesGamesGameResponseV2
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            access_filter=access_filter,
            limit=limit,
            cursor=cursor,
            sort_order=sort_order,
        )
    ).parsed
