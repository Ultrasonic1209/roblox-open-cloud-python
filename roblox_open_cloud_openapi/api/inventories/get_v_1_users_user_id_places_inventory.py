from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v1_users_user_id_places_inventory_places_tab import GetV1UsersUserIdPlacesInventoryPlacesTab
from ...models.roblox_web_web_api_models_api_page_response_roblox_inventory_api_models_place_model import (
    RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiModelsPlaceModel,
)
from ...types import UNSET, Response


def _get_kwargs(
    user_id: int,
    *,
    places_tab: GetV1UsersUserIdPlacesInventoryPlacesTab,
    items_per_page: int,
    cursor: int,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_places_tab = places_tab.value
    params["placesTab"] = json_places_tab

    params["itemsPerPage"] = items_per_page

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://inventory.roblox.com/v1/users/{user_id}/places/inventory".format(
            user_id=quote(str(user_id), safe=""),
        ),
        "params": params,
        "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
        "openapi-id": "get_v1_users_userId_places_inventory",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiModelsPlaceModel | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiModelsPlaceModel.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiModelsPlaceModel]:
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
    places_tab: GetV1UsersUserIdPlacesInventoryPlacesTab,
    items_per_page: int,
    cursor: int,
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiModelsPlaceModel]:
    """Gets Created, MyGames, or OtherGames places inventory for a user

    Args:
        user_id (int):
        places_tab (GetV1UsersUserIdPlacesInventoryPlacesTab):
        items_per_page (int):
        cursor (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiModelsPlaceModel]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        places_tab=places_tab,
        items_per_page=items_per_page,
        cursor=cursor,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: int,
    *,
    client: AuthenticatedClient,
    places_tab: GetV1UsersUserIdPlacesInventoryPlacesTab,
    items_per_page: int,
    cursor: int,
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiModelsPlaceModel | None:
    """Gets Created, MyGames, or OtherGames places inventory for a user

    Args:
        user_id (int):
        places_tab (GetV1UsersUserIdPlacesInventoryPlacesTab):
        items_per_page (int):
        cursor (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiModelsPlaceModel
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        places_tab=places_tab,
        items_per_page=items_per_page,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    user_id: int,
    *,
    client: AuthenticatedClient,
    places_tab: GetV1UsersUserIdPlacesInventoryPlacesTab,
    items_per_page: int,
    cursor: int,
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiModelsPlaceModel]:
    """Gets Created, MyGames, or OtherGames places inventory for a user

    Args:
        user_id (int):
        places_tab (GetV1UsersUserIdPlacesInventoryPlacesTab):
        items_per_page (int):
        cursor (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiModelsPlaceModel]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        places_tab=places_tab,
        items_per_page=items_per_page,
        cursor=cursor,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: int,
    *,
    client: AuthenticatedClient,
    places_tab: GetV1UsersUserIdPlacesInventoryPlacesTab,
    items_per_page: int,
    cursor: int,
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiModelsPlaceModel | None:
    """Gets Created, MyGames, or OtherGames places inventory for a user

    Args:
        user_id (int):
        places_tab (GetV1UsersUserIdPlacesInventoryPlacesTab):
        items_per_page (int):
        cursor (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiModelsPlaceModel
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            places_tab=places_tab,
            items_per_page=items_per_page,
            cursor=cursor,
        )
    ).parsed
