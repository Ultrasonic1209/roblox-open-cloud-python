from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_v1_collections_items_item_type_item_target_id_item_type import (
    DeleteV1CollectionsItemsItemTypeItemTargetIdItemType,
)
from ...models.roblox_web_web_api_api_empty_response_model import RobloxWebWebAPIApiEmptyResponseModel
from ...types import Response


def _get_kwargs(
    item_type: DeleteV1CollectionsItemsItemTypeItemTargetIdItemType,
    item_target_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "https://inventory.roblox.com/v1/collections/items/{item_type}/{item_target_id}".format(
            item_type=quote(str(item_type), safe=""),
            item_target_id=quote(str(item_target_id), safe=""),
        ),
        "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
        "openapi-id": "delete_v1_collections_items_itemType_itemTargetId",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxWebWebAPIApiEmptyResponseModel | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIApiEmptyResponseModel.from_dict(response.json())

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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxWebWebAPIApiEmptyResponseModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    item_type: DeleteV1CollectionsItemsItemTypeItemTargetIdItemType,
    item_target_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxWebWebAPIApiEmptyResponseModel]:
    """Removes an item to the appropriate collection

    Args:
        item_type (DeleteV1CollectionsItemsItemTypeItemTargetIdItemType):
        item_target_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIApiEmptyResponseModel]
    """

    kwargs = _get_kwargs(
        item_type=item_type,
        item_target_id=item_target_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    item_type: DeleteV1CollectionsItemsItemTypeItemTargetIdItemType,
    item_target_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxWebWebAPIApiEmptyResponseModel | None:
    """Removes an item to the appropriate collection

    Args:
        item_type (DeleteV1CollectionsItemsItemTypeItemTargetIdItemType):
        item_target_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIApiEmptyResponseModel
    """

    return sync_detailed(
        item_type=item_type,
        item_target_id=item_target_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    item_type: DeleteV1CollectionsItemsItemTypeItemTargetIdItemType,
    item_target_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxWebWebAPIApiEmptyResponseModel]:
    """Removes an item to the appropriate collection

    Args:
        item_type (DeleteV1CollectionsItemsItemTypeItemTargetIdItemType):
        item_target_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIApiEmptyResponseModel]
    """

    kwargs = _get_kwargs(
        item_type=item_type,
        item_target_id=item_target_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    item_type: DeleteV1CollectionsItemsItemTypeItemTargetIdItemType,
    item_target_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxWebWebAPIApiEmptyResponseModel | None:
    """Removes an item to the appropriate collection

    Args:
        item_type (DeleteV1CollectionsItemsItemTypeItemTargetIdItemType):
        item_target_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIApiEmptyResponseModel
    """

    return (
        await asyncio_detailed(
            item_type=item_type,
            item_target_id=item_target_id,
            client=client,
        )
    ).parsed
