from http import HTTPStatus
from typing import TYPE_CHECKING, Any, cast
from urllib.parse import quote

if TYPE_CHECKING:
    import httpx2 as httpx
else:
    try:
        import httpx2 as httpx
    except ModuleNotFoundError:
        try:
            import httpx
        except ModuleNotFoundError:
            raise RuntimeError(
                "This module requires the httpx2 package to be installed.\n"
                "You can install it with:\n"
                "    $ pip install httpx2\n"
            ) from None


from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response

"""
{'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.game_server_response_page_response import GameServerResponsePageResponse
from ...models.public_server_browser_service_server_type import PublicServerBrowserServiceServerType
from ...models.server_list_sort_option import ServerListSortOption
from ...types import Unset


def _get_kwargs(
    place_id: int,
    server_type: PublicServerBrowserServiceServerType,
    *,
    order_by: ServerListSortOption | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    exclude_full_games: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_order_by: int | Unset = UNSET
    if not isinstance(order_by, Unset):
        json_order_by = order_by.value

    params["orderBy"] = json_order_by

    params["limit"] = limit

    params["cursor"] = cursor

    params["excludeFullGames"] = exclude_full_games

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://games.roblox.com/v2/games/{place_id}/servers/{server_type}".format(
            place_id=quote(str(place_id), safe=""),
            server_type=quote(str(server_type), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GameServerResponsePageResponse | None:
    if response.status_code == 200:
        response_200 = GameServerResponsePageResponse.from_dict(response.json())

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
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GameServerResponsePageResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    place_id: int,
    server_type: PublicServerBrowserServiceServerType,
    *,
    client: AuthenticatedClient,
    order_by: ServerListSortOption | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    exclude_full_games: bool | Unset = False,
) -> Response[Any | GameServerResponsePageResponse]:
    """
    Args:
        place_id (int):
        server_type (PublicServerBrowserServiceServerType):
        order_by (ServerListSortOption | Unset):
        limit (int | Unset):
        cursor (str | Unset):
        exclude_full_games (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GameServerResponsePageResponse]
    """

    kwargs = _get_kwargs(
        place_id=place_id,
        server_type=server_type,
        order_by=order_by,
        limit=limit,
        cursor=cursor,
        exclude_full_games=exclude_full_games,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    place_id: int,
    server_type: PublicServerBrowserServiceServerType,
    *,
    client: AuthenticatedClient,
    order_by: ServerListSortOption | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    exclude_full_games: bool | Unset = False,
) -> Any | GameServerResponsePageResponse | None:
    """
    Args:
        place_id (int):
        server_type (PublicServerBrowserServiceServerType):
        order_by (ServerListSortOption | Unset):
        limit (int | Unset):
        cursor (str | Unset):
        exclude_full_games (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GameServerResponsePageResponse
    """

    return sync_detailed(
        place_id=place_id,
        server_type=server_type,
        client=client,
        order_by=order_by,
        limit=limit,
        cursor=cursor,
        exclude_full_games=exclude_full_games,
    ).parsed


async def asyncio_detailed(
    place_id: int,
    server_type: PublicServerBrowserServiceServerType,
    *,
    client: AuthenticatedClient,
    order_by: ServerListSortOption | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    exclude_full_games: bool | Unset = False,
) -> Response[Any | GameServerResponsePageResponse]:
    """
    Args:
        place_id (int):
        server_type (PublicServerBrowserServiceServerType):
        order_by (ServerListSortOption | Unset):
        limit (int | Unset):
        cursor (str | Unset):
        exclude_full_games (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GameServerResponsePageResponse]
    """

    kwargs = _get_kwargs(
        place_id=place_id,
        server_type=server_type,
        order_by=order_by,
        limit=limit,
        cursor=cursor,
        exclude_full_games=exclude_full_games,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    place_id: int,
    server_type: PublicServerBrowserServiceServerType,
    *,
    client: AuthenticatedClient,
    order_by: ServerListSortOption | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    exclude_full_games: bool | Unset = False,
) -> Any | GameServerResponsePageResponse | None:
    """
    Args:
        place_id (int):
        server_type (PublicServerBrowserServiceServerType):
        order_by (ServerListSortOption | Unset):
        limit (int | Unset):
        cursor (str | Unset):
        exclude_full_games (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GameServerResponsePageResponse
    """

    return (
        await asyncio_detailed(
            place_id=place_id,
            server_type=server_type,
            client=client,
            order_by=order_by,
            limit=limit,
            cursor=cursor,
            exclude_full_games=exclude_full_games,
        )
    ).parsed
