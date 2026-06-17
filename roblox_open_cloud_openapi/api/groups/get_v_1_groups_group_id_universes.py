from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v1_groups_group_id_universes_limit import GetV1GroupsGroupIdUniversesLimit
from ...models.get_v1_groups_group_id_universes_sort_order import GetV1GroupsGroupIdUniversesSortOrder
from ...models.roblox_web_web_api_models_api_page_response_roblox_api_develop_models_universe_model import (
    RobloxWebWebAPIModelsApiPageResponseRobloxApiDevelopModelsUniverseModel,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    group_id: int,
    *,
    is_archived: bool | Unset = False,
    limit: GetV1GroupsGroupIdUniversesLimit | Unset = GetV1GroupsGroupIdUniversesLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1GroupsGroupIdUniversesSortOrder | Unset = GetV1GroupsGroupIdUniversesSortOrder.ASC,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["isArchived"] = is_archived

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
        "url": "https://develop.roblox.com/v1/groups/{group_id}/universes".format(
            group_id=quote(str(group_id), safe=""),
        ),
        "params": params,
        "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
        "openapi-id": "get_v1_groups_groupId_universes",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxApiDevelopModelsUniverseModel | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIModelsApiPageResponseRobloxApiDevelopModelsUniverseModel.from_dict(
            response.json()
        )

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
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxApiDevelopModelsUniverseModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    group_id: int,
    *,
    client: AuthenticatedClient,
    is_archived: bool | Unset = False,
    limit: GetV1GroupsGroupIdUniversesLimit | Unset = GetV1GroupsGroupIdUniversesLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1GroupsGroupIdUniversesSortOrder | Unset = GetV1GroupsGroupIdUniversesSortOrder.ASC,
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxApiDevelopModelsUniverseModel]:
    """Gets a list of universes for the given group.

    Args:
        group_id (int):
        is_archived (bool | Unset):  Default: False.
        limit (GetV1GroupsGroupIdUniversesLimit | Unset):  Default:
            GetV1GroupsGroupIdUniversesLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV1GroupsGroupIdUniversesSortOrder | Unset):  Default:
            GetV1GroupsGroupIdUniversesSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxApiDevelopModelsUniverseModel]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        is_archived=is_archived,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: int,
    *,
    client: AuthenticatedClient,
    is_archived: bool | Unset = False,
    limit: GetV1GroupsGroupIdUniversesLimit | Unset = GetV1GroupsGroupIdUniversesLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1GroupsGroupIdUniversesSortOrder | Unset = GetV1GroupsGroupIdUniversesSortOrder.ASC,
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxApiDevelopModelsUniverseModel | None:
    """Gets a list of universes for the given group.

    Args:
        group_id (int):
        is_archived (bool | Unset):  Default: False.
        limit (GetV1GroupsGroupIdUniversesLimit | Unset):  Default:
            GetV1GroupsGroupIdUniversesLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV1GroupsGroupIdUniversesSortOrder | Unset):  Default:
            GetV1GroupsGroupIdUniversesSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiPageResponseRobloxApiDevelopModelsUniverseModel
    """

    return sync_detailed(
        group_id=group_id,
        client=client,
        is_archived=is_archived,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
    ).parsed


async def asyncio_detailed(
    group_id: int,
    *,
    client: AuthenticatedClient,
    is_archived: bool | Unset = False,
    limit: GetV1GroupsGroupIdUniversesLimit | Unset = GetV1GroupsGroupIdUniversesLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1GroupsGroupIdUniversesSortOrder | Unset = GetV1GroupsGroupIdUniversesSortOrder.ASC,
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxApiDevelopModelsUniverseModel]:
    """Gets a list of universes for the given group.

    Args:
        group_id (int):
        is_archived (bool | Unset):  Default: False.
        limit (GetV1GroupsGroupIdUniversesLimit | Unset):  Default:
            GetV1GroupsGroupIdUniversesLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV1GroupsGroupIdUniversesSortOrder | Unset):  Default:
            GetV1GroupsGroupIdUniversesSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxApiDevelopModelsUniverseModel]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        is_archived=is_archived,
        limit=limit,
        cursor=cursor,
        sort_order=sort_order,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: int,
    *,
    client: AuthenticatedClient,
    is_archived: bool | Unset = False,
    limit: GetV1GroupsGroupIdUniversesLimit | Unset = GetV1GroupsGroupIdUniversesLimit.VALUE_10,
    cursor: str | Unset = UNSET,
    sort_order: GetV1GroupsGroupIdUniversesSortOrder | Unset = GetV1GroupsGroupIdUniversesSortOrder.ASC,
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxApiDevelopModelsUniverseModel | None:
    """Gets a list of universes for the given group.

    Args:
        group_id (int):
        is_archived (bool | Unset):  Default: False.
        limit (GetV1GroupsGroupIdUniversesLimit | Unset):  Default:
            GetV1GroupsGroupIdUniversesLimit.VALUE_10.
        cursor (str | Unset):
        sort_order (GetV1GroupsGroupIdUniversesSortOrder | Unset):  Default:
            GetV1GroupsGroupIdUniversesSortOrder.ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiPageResponseRobloxApiDevelopModelsUniverseModel
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
            is_archived=is_archived,
            limit=limit,
            cursor=cursor,
            sort_order=sort_order,
        )
    ).parsed
