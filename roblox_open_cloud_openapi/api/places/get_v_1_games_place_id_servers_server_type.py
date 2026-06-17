from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v1_games_place_id_servers_server_type_limit import GetV1GamesPlaceIdServersServerTypeLimit
from ...models.get_v1_games_place_id_servers_server_type_server_type import GetV1GamesPlaceIdServersServerTypeServerType
from ...models.get_v1_games_place_id_servers_server_type_sort_order import GetV1GamesPlaceIdServersServerTypeSortOrder
from ...models.roblox_web_web_api_models_api_page_response_roblox_web_responses_games_game_server_response import (
    RobloxWebWebAPIModelsApiPageResponseRobloxWebResponsesGamesGameServerResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    place_id: int,
    server_type: GetV1GamesPlaceIdServersServerTypeServerType,
    *,
    sort_order: GetV1GamesPlaceIdServersServerTypeSortOrder
    | Unset = GetV1GamesPlaceIdServersServerTypeSortOrder.VALUE_2,
    exclude_full_games: bool | Unset = False,
    limit: GetV1GamesPlaceIdServersServerTypeLimit | Unset = GetV1GamesPlaceIdServersServerTypeLimit.VALUE_10,
    cursor: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_sort_order: int | Unset = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value

    params["sortOrder"] = json_sort_order

    params["excludeFullGames"] = exclude_full_games

    json_limit: int | Unset = UNSET
    if not isinstance(limit, Unset):
        json_limit = limit.value

    params["limit"] = json_limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://games.roblox.com/v1/games/{place_id}/servers/{server_type}".format(
            place_id=quote(str(place_id), safe=""),
            server_type=quote(str(server_type), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxWebResponsesGamesGameServerResponse | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIModelsApiPageResponseRobloxWebResponsesGamesGameServerResponse.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxWebResponsesGamesGameServerResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    place_id: int,
    server_type: GetV1GamesPlaceIdServersServerTypeServerType,
    *,
    client: AuthenticatedClient,
    sort_order: GetV1GamesPlaceIdServersServerTypeSortOrder
    | Unset = GetV1GamesPlaceIdServersServerTypeSortOrder.VALUE_2,
    exclude_full_games: bool | Unset = False,
    limit: GetV1GamesPlaceIdServersServerTypeLimit | Unset = GetV1GamesPlaceIdServersServerTypeLimit.VALUE_10,
    cursor: str | Unset = UNSET,
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxWebResponsesGamesGameServerResponse]:
    """Get the game server list

    Args:
        place_id (int):
        server_type (GetV1GamesPlaceIdServersServerTypeServerType):
        sort_order (GetV1GamesPlaceIdServersServerTypeSortOrder | Unset):  Default:
            GetV1GamesPlaceIdServersServerTypeSortOrder.VALUE_2.
        exclude_full_games (bool | Unset):  Default: False.
        limit (GetV1GamesPlaceIdServersServerTypeLimit | Unset):  Default:
            GetV1GamesPlaceIdServersServerTypeLimit.VALUE_10.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxWebResponsesGamesGameServerResponse]
    """

    kwargs = _get_kwargs(
        place_id=place_id,
        server_type=server_type,
        sort_order=sort_order,
        exclude_full_games=exclude_full_games,
        limit=limit,
        cursor=cursor,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    place_id: int,
    server_type: GetV1GamesPlaceIdServersServerTypeServerType,
    *,
    client: AuthenticatedClient,
    sort_order: GetV1GamesPlaceIdServersServerTypeSortOrder
    | Unset = GetV1GamesPlaceIdServersServerTypeSortOrder.VALUE_2,
    exclude_full_games: bool | Unset = False,
    limit: GetV1GamesPlaceIdServersServerTypeLimit | Unset = GetV1GamesPlaceIdServersServerTypeLimit.VALUE_10,
    cursor: str | Unset = UNSET,
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxWebResponsesGamesGameServerResponse | None:
    """Get the game server list

    Args:
        place_id (int):
        server_type (GetV1GamesPlaceIdServersServerTypeServerType):
        sort_order (GetV1GamesPlaceIdServersServerTypeSortOrder | Unset):  Default:
            GetV1GamesPlaceIdServersServerTypeSortOrder.VALUE_2.
        exclude_full_games (bool | Unset):  Default: False.
        limit (GetV1GamesPlaceIdServersServerTypeLimit | Unset):  Default:
            GetV1GamesPlaceIdServersServerTypeLimit.VALUE_10.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiPageResponseRobloxWebResponsesGamesGameServerResponse
    """

    return sync_detailed(
        place_id=place_id,
        server_type=server_type,
        client=client,
        sort_order=sort_order,
        exclude_full_games=exclude_full_games,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    place_id: int,
    server_type: GetV1GamesPlaceIdServersServerTypeServerType,
    *,
    client: AuthenticatedClient,
    sort_order: GetV1GamesPlaceIdServersServerTypeSortOrder
    | Unset = GetV1GamesPlaceIdServersServerTypeSortOrder.VALUE_2,
    exclude_full_games: bool | Unset = False,
    limit: GetV1GamesPlaceIdServersServerTypeLimit | Unset = GetV1GamesPlaceIdServersServerTypeLimit.VALUE_10,
    cursor: str | Unset = UNSET,
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxWebResponsesGamesGameServerResponse]:
    """Get the game server list

    Args:
        place_id (int):
        server_type (GetV1GamesPlaceIdServersServerTypeServerType):
        sort_order (GetV1GamesPlaceIdServersServerTypeSortOrder | Unset):  Default:
            GetV1GamesPlaceIdServersServerTypeSortOrder.VALUE_2.
        exclude_full_games (bool | Unset):  Default: False.
        limit (GetV1GamesPlaceIdServersServerTypeLimit | Unset):  Default:
            GetV1GamesPlaceIdServersServerTypeLimit.VALUE_10.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxWebResponsesGamesGameServerResponse]
    """

    kwargs = _get_kwargs(
        place_id=place_id,
        server_type=server_type,
        sort_order=sort_order,
        exclude_full_games=exclude_full_games,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    place_id: int,
    server_type: GetV1GamesPlaceIdServersServerTypeServerType,
    *,
    client: AuthenticatedClient,
    sort_order: GetV1GamesPlaceIdServersServerTypeSortOrder
    | Unset = GetV1GamesPlaceIdServersServerTypeSortOrder.VALUE_2,
    exclude_full_games: bool | Unset = False,
    limit: GetV1GamesPlaceIdServersServerTypeLimit | Unset = GetV1GamesPlaceIdServersServerTypeLimit.VALUE_10,
    cursor: str | Unset = UNSET,
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxWebResponsesGamesGameServerResponse | None:
    """Get the game server list

    Args:
        place_id (int):
        server_type (GetV1GamesPlaceIdServersServerTypeServerType):
        sort_order (GetV1GamesPlaceIdServersServerTypeSortOrder | Unset):  Default:
            GetV1GamesPlaceIdServersServerTypeSortOrder.VALUE_2.
        exclude_full_games (bool | Unset):  Default: False.
        limit (GetV1GamesPlaceIdServersServerTypeLimit | Unset):  Default:
            GetV1GamesPlaceIdServersServerTypeLimit.VALUE_10.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiPageResponseRobloxWebResponsesGamesGameServerResponse
    """

    return (
        await asyncio_detailed(
            place_id=place_id,
            server_type=server_type,
            client=client,
            sort_order=sort_order,
            exclude_full_games=exclude_full_games,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
