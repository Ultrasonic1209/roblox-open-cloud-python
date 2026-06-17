from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v1_users_user_id_items_item_type_item_target_id_is_owned_item_type import (
    GetV1UsersUserIdItemsItemTypeItemTargetIdIsOwnedItemType,
)
from ...types import Response


def _get_kwargs(
    user_id: int,
    item_type: GetV1UsersUserIdItemsItemTypeItemTargetIdIsOwnedItemType,
    item_target_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://inventory.roblox.com/v1/users/{user_id}/items/{item_type}/{item_target_id}/is-owned".format(
            user_id=quote(str(user_id), safe=""),
            item_type=quote(str(item_type), safe=""),
            item_target_id=quote(str(item_target_id), safe=""),
        ),
        "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
        "openapi-id": "get_v1_users_userId_items_itemType_itemTargetId_is-owned",
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Any | bool | None:
    if response.status_code == 200:
        response_200 = cast(bool, response.json())
        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[Any | bool]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: int,
    item_type: GetV1UsersUserIdItemsItemTypeItemTargetIdIsOwnedItemType,
    item_target_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | bool]:
    """Gets whether a user owns an item of type itemType with id itemTargetId.

    Args:
        user_id (int):
        item_type (GetV1UsersUserIdItemsItemTypeItemTargetIdIsOwnedItemType):
        item_target_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | bool]
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


def sync(
    user_id: int,
    item_type: GetV1UsersUserIdItemsItemTypeItemTargetIdIsOwnedItemType,
    item_target_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | bool | None:
    """Gets whether a user owns an item of type itemType with id itemTargetId.

    Args:
        user_id (int):
        item_type (GetV1UsersUserIdItemsItemTypeItemTargetIdIsOwnedItemType):
        item_target_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | bool
    """

    return sync_detailed(
        user_id=user_id,
        item_type=item_type,
        item_target_id=item_target_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_id: int,
    item_type: GetV1UsersUserIdItemsItemTypeItemTargetIdIsOwnedItemType,
    item_target_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | bool]:
    """Gets whether a user owns an item of type itemType with id itemTargetId.

    Args:
        user_id (int):
        item_type (GetV1UsersUserIdItemsItemTypeItemTargetIdIsOwnedItemType):
        item_target_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | bool]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        item_type=item_type,
        item_target_id=item_target_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: int,
    item_type: GetV1UsersUserIdItemsItemTypeItemTargetIdIsOwnedItemType,
    item_target_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | bool | None:
    """Gets whether a user owns an item of type itemType with id itemTargetId.

    Args:
        user_id (int):
        item_type (GetV1UsersUserIdItemsItemTypeItemTargetIdIsOwnedItemType):
        item_target_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | bool
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            item_type=item_type,
            item_target_id=item_target_id,
            client=client,
        )
    ).parsed
