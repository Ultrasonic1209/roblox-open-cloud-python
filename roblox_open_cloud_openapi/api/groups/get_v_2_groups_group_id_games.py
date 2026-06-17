import sys
from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset

if sys.version_info >= (3, 13):
    from warnings import deprecated
else:
    from typing_extensions import deprecated

from ...models.get_v2_groups_group_id_games_access_filter import GetV2GroupsGroupIdGamesAccessFilter
from ...models.get_v2_groups_group_id_games_limit import GetV2GroupsGroupIdGamesLimit
from ...models.get_v2_groups_group_id_games_sort_order import GetV2GroupsGroupIdGamesSortOrder
from ...models.roblox_web_web_api_models_api_page_response_roblox_groups_api_models_response_group_experience_response import (
    RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiModelsResponseGroupExperienceResponse,
)


def _get_kwargs(
    group_id: int,
    *,
    access_filter: GetV2GroupsGroupIdGamesAccessFilter | Unset = GetV2GroupsGroupIdGamesAccessFilter.VALUE_1,
    limit: GetV2GroupsGroupIdGamesLimit | Unset = GetV2GroupsGroupIdGamesLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV2GroupsGroupIdGamesSortOrder | Unset = GetV2GroupsGroupIdGamesSortOrder.ASC,
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
        "url": "https://games.roblox.com/v2/groups/{group_id}/games".format(
            group_id=quote(str(group_id), safe=""),
        ),
        "params": params,
        "openapi-extensions": {
            "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            "x-roblox-recommended-alternatives": [
                {
                    "url": "https://games.roblox.com/v2/groups/{groupId}/gamesV2",
                    "httpMethod": "GET",
                    "documentationUrl": "https://create.roblox.com/docs/cloud/reference/features/groups#games_get_v2_groups__groupId__gamesV2",
                }
            ],
        },
        "openapi-id": "get_v2_groups_groupId_games",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiModelsResponseGroupExperienceResponse | None:
    if response.status_code == 200:
        response_200 = (
            RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiModelsResponseGroupExperienceResponse.from_dict(
                response.json()
            )
        )

        return response_200

    if response.status_code == 501:
        response_501 = cast(Any, None)
        return response_501

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiModelsResponseGroupExperienceResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/groups#games_get_v2_groups__groupId__games"
)
def sync_detailed(
    group_id: int,
    *,
    client: AuthenticatedClient,
    access_filter: GetV2GroupsGroupIdGamesAccessFilter | Unset = GetV2GroupsGroupIdGamesAccessFilter.VALUE_1,
    limit: GetV2GroupsGroupIdGamesLimit | Unset = GetV2GroupsGroupIdGamesLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV2GroupsGroupIdGamesSortOrder | Unset = GetV2GroupsGroupIdGamesSortOrder.ASC,
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiModelsResponseGroupExperienceResponse]:
    """Gets experiences created by the specified group id.

    Args:
        group_id (int):
        access_filter (GetV2GroupsGroupIdGamesAccessFilter | Unset):  Default:
            GetV2GroupsGroupIdGamesAccessFilter.VALUE_1.
        limit (GetV2GroupsGroupIdGamesLimit | Unset):  Default:
            GetV2GroupsGroupIdGamesLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV2GroupsGroupIdGamesSortOrder | Unset):  Default:
            GetV2GroupsGroupIdGamesSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiModelsResponseGroupExperienceResponse]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        access_filter=access_filter,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/groups#games_get_v2_groups__groupId__games"
)
def sync(
    group_id: int,
    *,
    client: AuthenticatedClient,
    access_filter: GetV2GroupsGroupIdGamesAccessFilter | Unset = GetV2GroupsGroupIdGamesAccessFilter.VALUE_1,
    limit: GetV2GroupsGroupIdGamesLimit | Unset = GetV2GroupsGroupIdGamesLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV2GroupsGroupIdGamesSortOrder | Unset = GetV2GroupsGroupIdGamesSortOrder.ASC,
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiModelsResponseGroupExperienceResponse | None:
    """Gets experiences created by the specified group id.

    Args:
        group_id (int):
        access_filter (GetV2GroupsGroupIdGamesAccessFilter | Unset):  Default:
            GetV2GroupsGroupIdGamesAccessFilter.VALUE_1.
        limit (GetV2GroupsGroupIdGamesLimit | Unset):  Default:
            GetV2GroupsGroupIdGamesLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV2GroupsGroupIdGamesSortOrder | Unset):  Default:
            GetV2GroupsGroupIdGamesSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiModelsResponseGroupExperienceResponse
    """

    return sync_detailed(
        group_id=group_id,
        client=client,
        access_filter=access_filter,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
    ).parsed


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/groups#games_get_v2_groups__groupId__games"
)
async def asyncio_detailed(
    group_id: int,
    *,
    client: AuthenticatedClient,
    access_filter: GetV2GroupsGroupIdGamesAccessFilter | Unset = GetV2GroupsGroupIdGamesAccessFilter.VALUE_1,
    limit: GetV2GroupsGroupIdGamesLimit | Unset = GetV2GroupsGroupIdGamesLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV2GroupsGroupIdGamesSortOrder | Unset = GetV2GroupsGroupIdGamesSortOrder.ASC,
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiModelsResponseGroupExperienceResponse]:
    """Gets experiences created by the specified group id.

    Args:
        group_id (int):
        access_filter (GetV2GroupsGroupIdGamesAccessFilter | Unset):  Default:
            GetV2GroupsGroupIdGamesAccessFilter.VALUE_1.
        limit (GetV2GroupsGroupIdGamesLimit | Unset):  Default:
            GetV2GroupsGroupIdGamesLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV2GroupsGroupIdGamesSortOrder | Unset):  Default:
            GetV2GroupsGroupIdGamesSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiModelsResponseGroupExperienceResponse]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        access_filter=access_filter,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/groups#games_get_v2_groups__groupId__games"
)
async def asyncio(
    group_id: int,
    *,
    client: AuthenticatedClient,
    access_filter: GetV2GroupsGroupIdGamesAccessFilter | Unset = GetV2GroupsGroupIdGamesAccessFilter.VALUE_1,
    limit: GetV2GroupsGroupIdGamesLimit | Unset = GetV2GroupsGroupIdGamesLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV2GroupsGroupIdGamesSortOrder | Unset = GetV2GroupsGroupIdGamesSortOrder.ASC,
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiModelsResponseGroupExperienceResponse | None:
    """Gets experiences created by the specified group id.

    Args:
        group_id (int):
        access_filter (GetV2GroupsGroupIdGamesAccessFilter | Unset):  Default:
            GetV2GroupsGroupIdGamesAccessFilter.VALUE_1.
        limit (GetV2GroupsGroupIdGamesLimit | Unset):  Default:
            GetV2GroupsGroupIdGamesLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV2GroupsGroupIdGamesSortOrder | Unset):  Default:
            GetV2GroupsGroupIdGamesSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiPageResponseRobloxGroupsApiModelsResponseGroupExperienceResponse
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
            access_filter=access_filter,
            limit=limit,
            cursor=cursor,
            sort_order=sort_order,
        )
    ).parsed
