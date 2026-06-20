from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v2_users_user_id_favorite_games_access_filter import GetV2UsersUserIdFavoriteGamesAccessFilter
from ...models.get_v2_users_user_id_favorite_games_limit import GetV2UsersUserIdFavoriteGamesLimit
from ...models.get_v2_users_user_id_favorite_games_sort_order import GetV2UsersUserIdFavoriteGamesSortOrder
from ...models.roblox_web_web_api_models_api_page_response_roblox_web_responses_games_game_favorite_response_model import (
    RobloxWebWebAPIModelsApiPageResponseRobloxWebResponsesGamesGameFavoriteResponseModel,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: int,
    *,
    access_filter: GetV2UsersUserIdFavoriteGamesAccessFilter
    | Unset = GetV2UsersUserIdFavoriteGamesAccessFilter.VALUE_2,
    limit: GetV2UsersUserIdFavoriteGamesLimit | Unset = GetV2UsersUserIdFavoriteGamesLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV2UsersUserIdFavoriteGamesSortOrder | Unset = GetV2UsersUserIdFavoriteGamesSortOrder.DESC,
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
        "url": "https://games.roblox.com/v2/users/{user_id}/favorite/games".format(
            user_id=quote(str(user_id), safe=""),
        ),
        "params": params,
        "extensions": {
            "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
            "openapi-id": "get_v2_users_userId_favorite_games",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> RobloxWebWebAPIModelsApiPageResponseRobloxWebResponsesGamesGameFavoriteResponseModel | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIModelsApiPageResponseRobloxWebResponsesGamesGameFavoriteResponseModel.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[RobloxWebWebAPIModelsApiPageResponseRobloxWebResponsesGamesGameFavoriteResponseModel]:
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
    access_filter: GetV2UsersUserIdFavoriteGamesAccessFilter
    | Unset = GetV2UsersUserIdFavoriteGamesAccessFilter.VALUE_2,
    limit: GetV2UsersUserIdFavoriteGamesLimit | Unset = GetV2UsersUserIdFavoriteGamesLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV2UsersUserIdFavoriteGamesSortOrder | Unset = GetV2UsersUserIdFavoriteGamesSortOrder.DESC,
) -> Response[RobloxWebWebAPIModelsApiPageResponseRobloxWebResponsesGamesGameFavoriteResponseModel]:
    """Gets users favorite games.

    Args:
        user_id (int):
        access_filter (GetV2UsersUserIdFavoriteGamesAccessFilter | Unset):  Default:
            GetV2UsersUserIdFavoriteGamesAccessFilter.VALUE_2.
        limit (GetV2UsersUserIdFavoriteGamesLimit | Unset):  Default:
            GetV2UsersUserIdFavoriteGamesLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV2UsersUserIdFavoriteGamesSortOrder | Unset):  Default:
            GetV2UsersUserIdFavoriteGamesSortOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RobloxWebWebAPIModelsApiPageResponseRobloxWebResponsesGamesGameFavoriteResponseModel]
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
    access_filter: GetV2UsersUserIdFavoriteGamesAccessFilter
    | Unset = GetV2UsersUserIdFavoriteGamesAccessFilter.VALUE_2,
    limit: GetV2UsersUserIdFavoriteGamesLimit | Unset = GetV2UsersUserIdFavoriteGamesLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV2UsersUserIdFavoriteGamesSortOrder | Unset = GetV2UsersUserIdFavoriteGamesSortOrder.DESC,
) -> RobloxWebWebAPIModelsApiPageResponseRobloxWebResponsesGamesGameFavoriteResponseModel | None:
    """Gets users favorite games.

    Args:
        user_id (int):
        access_filter (GetV2UsersUserIdFavoriteGamesAccessFilter | Unset):  Default:
            GetV2UsersUserIdFavoriteGamesAccessFilter.VALUE_2.
        limit (GetV2UsersUserIdFavoriteGamesLimit | Unset):  Default:
            GetV2UsersUserIdFavoriteGamesLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV2UsersUserIdFavoriteGamesSortOrder | Unset):  Default:
            GetV2UsersUserIdFavoriteGamesSortOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RobloxWebWebAPIModelsApiPageResponseRobloxWebResponsesGamesGameFavoriteResponseModel
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
    access_filter: GetV2UsersUserIdFavoriteGamesAccessFilter
    | Unset = GetV2UsersUserIdFavoriteGamesAccessFilter.VALUE_2,
    limit: GetV2UsersUserIdFavoriteGamesLimit | Unset = GetV2UsersUserIdFavoriteGamesLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV2UsersUserIdFavoriteGamesSortOrder | Unset = GetV2UsersUserIdFavoriteGamesSortOrder.DESC,
) -> Response[RobloxWebWebAPIModelsApiPageResponseRobloxWebResponsesGamesGameFavoriteResponseModel]:
    """Gets users favorite games.

    Args:
        user_id (int):
        access_filter (GetV2UsersUserIdFavoriteGamesAccessFilter | Unset):  Default:
            GetV2UsersUserIdFavoriteGamesAccessFilter.VALUE_2.
        limit (GetV2UsersUserIdFavoriteGamesLimit | Unset):  Default:
            GetV2UsersUserIdFavoriteGamesLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV2UsersUserIdFavoriteGamesSortOrder | Unset):  Default:
            GetV2UsersUserIdFavoriteGamesSortOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RobloxWebWebAPIModelsApiPageResponseRobloxWebResponsesGamesGameFavoriteResponseModel]
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
    access_filter: GetV2UsersUserIdFavoriteGamesAccessFilter
    | Unset = GetV2UsersUserIdFavoriteGamesAccessFilter.VALUE_2,
    limit: GetV2UsersUserIdFavoriteGamesLimit | Unset = GetV2UsersUserIdFavoriteGamesLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV2UsersUserIdFavoriteGamesSortOrder | Unset = GetV2UsersUserIdFavoriteGamesSortOrder.DESC,
) -> RobloxWebWebAPIModelsApiPageResponseRobloxWebResponsesGamesGameFavoriteResponseModel | None:
    """Gets users favorite games.

    Args:
        user_id (int):
        access_filter (GetV2UsersUserIdFavoriteGamesAccessFilter | Unset):  Default:
            GetV2UsersUserIdFavoriteGamesAccessFilter.VALUE_2.
        limit (GetV2UsersUserIdFavoriteGamesLimit | Unset):  Default:
            GetV2UsersUserIdFavoriteGamesLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV2UsersUserIdFavoriteGamesSortOrder | Unset):  Default:
            GetV2UsersUserIdFavoriteGamesSortOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RobloxWebWebAPIModelsApiPageResponseRobloxWebResponsesGamesGameFavoriteResponseModel
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
