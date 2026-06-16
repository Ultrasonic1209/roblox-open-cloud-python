from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v1_creations_get_assets_limit import GetV1CreationsGetAssetsLimit
from ...models.roblox_web_web_api_models_api_page_response_roblox_item_configuration_api_asset_creations_response import (
    RobloxWebWebAPIModelsApiPageResponseRobloxItemConfigurationApiAssetCreationsResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    asset_type: str,
    is_archived: bool | Unset = UNSET,
    group_id: int | Unset = UNSET,
    limit: GetV1CreationsGetAssetsLimit | Unset = GetV1CreationsGetAssetsLimit.VALUE_10,
    cursor: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["assetType"] = asset_type

    params["isArchived"] = is_archived

    params["groupId"] = group_id

    json_limit: int | Unset = UNSET
    if not isinstance(limit, Unset):
        json_limit = limit.value

    params["limit"] = json_limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/creations/get-assets",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxItemConfigurationApiAssetCreationsResponse | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIModelsApiPageResponseRobloxItemConfigurationApiAssetCreationsResponse.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429

    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxItemConfigurationApiAssetCreationsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    asset_type: str,
    is_archived: bool | Unset = UNSET,
    group_id: int | Unset = UNSET,
    limit: GetV1CreationsGetAssetsLimit | Unset = GetV1CreationsGetAssetsLimit.VALUE_10,
    cursor: str | Unset = UNSET,
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxItemConfigurationApiAssetCreationsResponse]:
    """Gets the user created asset information filtered by the given asset type.

    Args:
        asset_type (str):
        is_archived (bool | Unset):
        group_id (int | Unset):
        limit (GetV1CreationsGetAssetsLimit | Unset):  Default:
            GetV1CreationsGetAssetsLimit.VALUE_10.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxItemConfigurationApiAssetCreationsResponse]
    """

    kwargs = _get_kwargs(
        asset_type=asset_type,
        is_archived=is_archived,
        group_id=group_id,
        limit=limit,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    asset_type: str,
    is_archived: bool | Unset = UNSET,
    group_id: int | Unset = UNSET,
    limit: GetV1CreationsGetAssetsLimit | Unset = GetV1CreationsGetAssetsLimit.VALUE_10,
    cursor: str | Unset = UNSET,
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxItemConfigurationApiAssetCreationsResponse | None:
    """Gets the user created asset information filtered by the given asset type.

    Args:
        asset_type (str):
        is_archived (bool | Unset):
        group_id (int | Unset):
        limit (GetV1CreationsGetAssetsLimit | Unset):  Default:
            GetV1CreationsGetAssetsLimit.VALUE_10.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiPageResponseRobloxItemConfigurationApiAssetCreationsResponse
    """

    return sync_detailed(
        client=client,
        asset_type=asset_type,
        is_archived=is_archived,
        group_id=group_id,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    asset_type: str,
    is_archived: bool | Unset = UNSET,
    group_id: int | Unset = UNSET,
    limit: GetV1CreationsGetAssetsLimit | Unset = GetV1CreationsGetAssetsLimit.VALUE_10,
    cursor: str | Unset = UNSET,
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxItemConfigurationApiAssetCreationsResponse]:
    """Gets the user created asset information filtered by the given asset type.

    Args:
        asset_type (str):
        is_archived (bool | Unset):
        group_id (int | Unset):
        limit (GetV1CreationsGetAssetsLimit | Unset):  Default:
            GetV1CreationsGetAssetsLimit.VALUE_10.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxItemConfigurationApiAssetCreationsResponse]
    """

    kwargs = _get_kwargs(
        asset_type=asset_type,
        is_archived=is_archived,
        group_id=group_id,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    asset_type: str,
    is_archived: bool | Unset = UNSET,
    group_id: int | Unset = UNSET,
    limit: GetV1CreationsGetAssetsLimit | Unset = GetV1CreationsGetAssetsLimit.VALUE_10,
    cursor: str | Unset = UNSET,
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxItemConfigurationApiAssetCreationsResponse | None:
    """Gets the user created asset information filtered by the given asset type.

    Args:
        asset_type (str):
        is_archived (bool | Unset):
        group_id (int | Unset):
        limit (GetV1CreationsGetAssetsLimit | Unset):  Default:
            GetV1CreationsGetAssetsLimit.VALUE_10.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiPageResponseRobloxItemConfigurationApiAssetCreationsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            asset_type=asset_type,
            is_archived=is_archived,
            group_id=group_id,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
