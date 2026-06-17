import sys
from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response

if sys.version_info >= (3, 13):
    from warnings import deprecated
else:
    from typing_extensions import deprecated

from ...models.get_v1_users_user_id_items_item_type_item_target_id_item_type import (
    GetV1UsersUserIdItemsItemTypeItemTargetIdItemType,
)
from ...models.roblox_web_web_api_models_api_page_response_roblox_inventory_api_models_i_item_model import (
    RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiModelsIItemModel,
)


def _get_kwargs(
    user_id: int,
    item_type: GetV1UsersUserIdItemsItemTypeItemTargetIdItemType,
    item_target_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://inventory.roblox.com/v1/users/{user_id}/items/{item_type}/{item_target_id}".format(
            user_id=quote(str(user_id), safe=""),
            item_type=quote(str(item_type), safe=""),
            item_target_id=quote(str(item_target_id), safe=""),
        ),
        "openapi-extensions": {
            "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            "x-roblox-recommended-alternatives": [
                {
                    "url": "https://apis.roblox.com/cloud/v2/users/{user_id}/inventory-items",
                    "httpMethod": "GET",
                    "documentationUrl": "https://create.roblox.com/docs/cloud/reference/features/inventories#Cloud_ListInventoryItems",
                }
            ],
        },
        "openapi-id": "get_v1_users_userId_items_itemType_itemTargetId",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiModelsIItemModel | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiModelsIItemModel.from_dict(response.json())

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
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiModelsIItemModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/assets#inventory_get_v1_users__userId__items__itemType___itemTargetId_"
)
def sync_detailed(
    user_id: int,
    item_type: GetV1UsersUserIdItemsItemTypeItemTargetIdItemType,
    item_target_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiModelsIItemModel]:
    """Gets owned items of the specified item type. Game Servers can make requests for any user, but can
    only make requests for game passes that belong to the place sending the request.
    Place creators can make requests as if they were the Game Server.

    Args:
        user_id (int):
        item_type (GetV1UsersUserIdItemsItemTypeItemTargetIdItemType):
        item_target_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiModelsIItemModel]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        item_type=item_type,
        item_target_id=item_target_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/assets#inventory_get_v1_users__userId__items__itemType___itemTargetId_"
)
def sync(
    user_id: int,
    item_type: GetV1UsersUserIdItemsItemTypeItemTargetIdItemType,
    item_target_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiModelsIItemModel | None:
    """Gets owned items of the specified item type. Game Servers can make requests for any user, but can
    only make requests for game passes that belong to the place sending the request.
    Place creators can make requests as if they were the Game Server.

    Args:
        user_id (int):
        item_type (GetV1UsersUserIdItemsItemTypeItemTargetIdItemType):
        item_target_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiModelsIItemModel
    """

    return sync_detailed(
        user_id=user_id,
        item_type=item_type,
        item_target_id=item_target_id,
        client=client,
    ).parsed


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/assets#inventory_get_v1_users__userId__items__itemType___itemTargetId_"
)
async def asyncio_detailed(
    user_id: int,
    item_type: GetV1UsersUserIdItemsItemTypeItemTargetIdItemType,
    item_target_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiModelsIItemModel]:
    """Gets owned items of the specified item type. Game Servers can make requests for any user, but can
    only make requests for game passes that belong to the place sending the request.
    Place creators can make requests as if they were the Game Server.

    Args:
        user_id (int):
        item_type (GetV1UsersUserIdItemsItemTypeItemTargetIdItemType):
        item_target_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiModelsIItemModel]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        item_type=item_type,
        item_target_id=item_target_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/assets#inventory_get_v1_users__userId__items__itemType___itemTargetId_"
)
async def asyncio(
    user_id: int,
    item_type: GetV1UsersUserIdItemsItemTypeItemTargetIdItemType,
    item_target_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiModelsIItemModel | None:
    """Gets owned items of the specified item type. Game Servers can make requests for any user, but can
    only make requests for game passes that belong to the place sending the request.
    Place creators can make requests as if they were the Game Server.

    Args:
        user_id (int):
        item_type (GetV1UsersUserIdItemsItemTypeItemTargetIdItemType):
        item_target_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiPageResponseRobloxInventoryApiModelsIItemModel
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            item_type=item_type,
            item_target_id=item_target_id,
            client=client,
        )
    ).parsed
