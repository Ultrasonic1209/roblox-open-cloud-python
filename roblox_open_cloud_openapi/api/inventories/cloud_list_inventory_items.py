from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_inventory_items_response import ListInventoryItemsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: str,
    *,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["maxPageSize"] = max_page_size

    params["pageToken"] = page_token

    params["filter"] = filter_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/cloud/v2/users/{user_id}/inventory-items".format(
            user_id=quote(str(user_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ListInventoryItemsResponse | None:
    if response.status_code == 200:
        response_200 = ListInventoryItemsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ListInventoryItemsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
) -> Response[ListInventoryItemsResponse]:
    r"""List Inventory Items

     List the inventory items in a user's inventory.

    The inventory items returned depend on the target user’s choice under
    **Settings > Privacy > Who can see my inventory?**:
    * If the user granted inventory visibility to \"Everyone,\" then any API key
    or OAuth2 token can be used to view the target’s inventory, no matter what
    scopes it has or who created it.
    * If the user has not granted inventory visibility to \"Everyone\":
      * Their inventory can still be viewed with an API key created by the
      target user with **Inventory: Read** permission.
      * Their inventory can still be viewed with an OAuth2 token if the target
      user authorizes an app requesting permissions for the
      `user.inventory-item:read` scope.

    Args:
        user_id (str):
        max_page_size (int | Unset):
        page_token (str | Unset):
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListInventoryItemsResponse]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        max_page_size=max_page_size,
        page_token=page_token,
        filter_=filter_,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: str,
    *,
    client: AuthenticatedClient,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
) -> ListInventoryItemsResponse | None:
    r"""List Inventory Items

     List the inventory items in a user's inventory.

    The inventory items returned depend on the target user’s choice under
    **Settings > Privacy > Who can see my inventory?**:
    * If the user granted inventory visibility to \"Everyone,\" then any API key
    or OAuth2 token can be used to view the target’s inventory, no matter what
    scopes it has or who created it.
    * If the user has not granted inventory visibility to \"Everyone\":
      * Their inventory can still be viewed with an API key created by the
      target user with **Inventory: Read** permission.
      * Their inventory can still be viewed with an OAuth2 token if the target
      user authorizes an app requesting permissions for the
      `user.inventory-item:read` scope.

    Args:
        user_id (str):
        max_page_size (int | Unset):
        page_token (str | Unset):
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListInventoryItemsResponse
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        max_page_size=max_page_size,
        page_token=page_token,
        filter_=filter_,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
) -> Response[ListInventoryItemsResponse]:
    r"""List Inventory Items

     List the inventory items in a user's inventory.

    The inventory items returned depend on the target user’s choice under
    **Settings > Privacy > Who can see my inventory?**:
    * If the user granted inventory visibility to \"Everyone,\" then any API key
    or OAuth2 token can be used to view the target’s inventory, no matter what
    scopes it has or who created it.
    * If the user has not granted inventory visibility to \"Everyone\":
      * Their inventory can still be viewed with an API key created by the
      target user with **Inventory: Read** permission.
      * Their inventory can still be viewed with an OAuth2 token if the target
      user authorizes an app requesting permissions for the
      `user.inventory-item:read` scope.

    Args:
        user_id (str):
        max_page_size (int | Unset):
        page_token (str | Unset):
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListInventoryItemsResponse]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        max_page_size=max_page_size,
        page_token=page_token,
        filter_=filter_,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    *,
    client: AuthenticatedClient,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
) -> ListInventoryItemsResponse | None:
    r"""List Inventory Items

     List the inventory items in a user's inventory.

    The inventory items returned depend on the target user’s choice under
    **Settings > Privacy > Who can see my inventory?**:
    * If the user granted inventory visibility to \"Everyone,\" then any API key
    or OAuth2 token can be used to view the target’s inventory, no matter what
    scopes it has or who created it.
    * If the user has not granted inventory visibility to \"Everyone\":
      * Their inventory can still be viewed with an API key created by the
      target user with **Inventory: Read** permission.
      * Their inventory can still be viewed with an OAuth2 token if the target
      user authorizes an app requesting permissions for the
      `user.inventory-item:read` scope.

    Args:
        user_id (str):
        max_page_size (int | Unset):
        page_token (str | Unset):
        filter_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListInventoryItemsResponse
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            max_page_size=max_page_size,
            page_token=page_token,
            filter_=filter_,
        )
    ).parsed
