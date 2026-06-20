from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v1_universes_universe_id_places_limit import GetV1UniversesUniverseIdPlacesLimit
from ...models.get_v1_universes_universe_id_places_sort_order import GetV1UniversesUniverseIdPlacesSortOrder
from ...models.roblox_web_web_api_models_api_page_response_roblox_api_develop_models_i_place_model import (
    RobloxWebWebAPIModelsApiPageResponseRobloxApiDevelopModelsIPlaceModel,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    universe_id: int,
    *,
    is_universe_creation: bool | Unset = False,
    limit: GetV1UniversesUniverseIdPlacesLimit | Unset = GetV1UniversesUniverseIdPlacesLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1UniversesUniverseIdPlacesSortOrder | Unset = GetV1UniversesUniverseIdPlacesSortOrder.ASC,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["isUniverseCreation"] = is_universe_creation

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
        "url": "https://develop.roblox.com/v1/universes/{universe_id}/places".format(
            universe_id=quote(str(universe_id), safe=""),
        ),
        "params": params,
        "extensions": {
            "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
            "openapi-id": "get_v1_universes_universeId_places",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> RobloxWebWebAPIModelsApiPageResponseRobloxApiDevelopModelsIPlaceModel | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIModelsApiPageResponseRobloxApiDevelopModelsIPlaceModel.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[RobloxWebWebAPIModelsApiPageResponseRobloxApiDevelopModelsIPlaceModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    is_universe_creation: bool | Unset = False,
    limit: GetV1UniversesUniverseIdPlacesLimit | Unset = GetV1UniversesUniverseIdPlacesLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1UniversesUniverseIdPlacesSortOrder | Unset = GetV1UniversesUniverseIdPlacesSortOrder.ASC,
) -> Response[RobloxWebWebAPIModelsApiPageResponseRobloxApiDevelopModelsIPlaceModel]:
    """Gets a list of places for a universe.

    Args:
        universe_id (int):
        is_universe_creation (bool | Unset):  Default: False.
        limit (GetV1UniversesUniverseIdPlacesLimit | Unset):  Default:
            GetV1UniversesUniverseIdPlacesLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV1UniversesUniverseIdPlacesSortOrder | Unset):  Default:
            GetV1UniversesUniverseIdPlacesSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RobloxWebWebAPIModelsApiPageResponseRobloxApiDevelopModelsIPlaceModel]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        is_universe_creation=is_universe_creation,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    is_universe_creation: bool | Unset = False,
    limit: GetV1UniversesUniverseIdPlacesLimit | Unset = GetV1UniversesUniverseIdPlacesLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1UniversesUniverseIdPlacesSortOrder | Unset = GetV1UniversesUniverseIdPlacesSortOrder.ASC,
) -> RobloxWebWebAPIModelsApiPageResponseRobloxApiDevelopModelsIPlaceModel | None:
    """Gets a list of places for a universe.

    Args:
        universe_id (int):
        is_universe_creation (bool | Unset):  Default: False.
        limit (GetV1UniversesUniverseIdPlacesLimit | Unset):  Default:
            GetV1UniversesUniverseIdPlacesLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV1UniversesUniverseIdPlacesSortOrder | Unset):  Default:
            GetV1UniversesUniverseIdPlacesSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RobloxWebWebAPIModelsApiPageResponseRobloxApiDevelopModelsIPlaceModel
    """

    return sync_detailed(
        universe_id=universe_id,
        client=client,
        is_universe_creation=is_universe_creation,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
    ).parsed


async def asyncio_detailed(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    is_universe_creation: bool | Unset = False,
    limit: GetV1UniversesUniverseIdPlacesLimit | Unset = GetV1UniversesUniverseIdPlacesLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1UniversesUniverseIdPlacesSortOrder | Unset = GetV1UniversesUniverseIdPlacesSortOrder.ASC,
) -> Response[RobloxWebWebAPIModelsApiPageResponseRobloxApiDevelopModelsIPlaceModel]:
    """Gets a list of places for a universe.

    Args:
        universe_id (int):
        is_universe_creation (bool | Unset):  Default: False.
        limit (GetV1UniversesUniverseIdPlacesLimit | Unset):  Default:
            GetV1UniversesUniverseIdPlacesLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV1UniversesUniverseIdPlacesSortOrder | Unset):  Default:
            GetV1UniversesUniverseIdPlacesSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RobloxWebWebAPIModelsApiPageResponseRobloxApiDevelopModelsIPlaceModel]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        is_universe_creation=is_universe_creation,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    is_universe_creation: bool | Unset = False,
    limit: GetV1UniversesUniverseIdPlacesLimit | Unset = GetV1UniversesUniverseIdPlacesLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1UniversesUniverseIdPlacesSortOrder | Unset = GetV1UniversesUniverseIdPlacesSortOrder.ASC,
) -> RobloxWebWebAPIModelsApiPageResponseRobloxApiDevelopModelsIPlaceModel | None:
    """Gets a list of places for a universe.

    Args:
        universe_id (int):
        is_universe_creation (bool | Unset):  Default: False.
        limit (GetV1UniversesUniverseIdPlacesLimit | Unset):  Default:
            GetV1UniversesUniverseIdPlacesLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV1UniversesUniverseIdPlacesSortOrder | Unset):  Default:
            GetV1UniversesUniverseIdPlacesSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RobloxWebWebAPIModelsApiPageResponseRobloxApiDevelopModelsIPlaceModel
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            client=client,
            is_universe_creation=is_universe_creation,
            limit=limit,
            cursor=cursor,
            sort_order=sort_order,
        )
    ).parsed
