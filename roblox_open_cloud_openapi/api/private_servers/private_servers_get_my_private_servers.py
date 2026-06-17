from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.my_private_servers_response import MyPrivateServersResponse
from ...models.private_servers_tab import PrivateServersTab
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    private_servers_tab: PrivateServersTab | Unset = PrivateServersTab.MYPRIVATESERVERS,
    items_per_page: int | Unset = 25,
    cursor: str | Unset = "",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_private_servers_tab: str | Unset = UNSET
    if not isinstance(private_servers_tab, Unset):
        json_private_servers_tab = private_servers_tab.value

    params["privateServersTab"] = json_private_servers_tab

    params["itemsPerPage"] = items_per_page

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://games.roblox.com/v1/vip-servers/my-private-servers",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> MyPrivateServersResponse | None:
    if response.status_code == 200:
        response_200 = MyPrivateServersResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[MyPrivateServersResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    private_servers_tab: PrivateServersTab | Unset = PrivateServersTab.MYPRIVATESERVERS,
    items_per_page: int | Unset = 25,
    cursor: str | Unset = "",
) -> Response[MyPrivateServersResponse]:
    """
    Args:
        private_servers_tab (PrivateServersTab | Unset):  Default:
            PrivateServersTab.MYPRIVATESERVERS.
        items_per_page (int | Unset):  Default: 25.
        cursor (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MyPrivateServersResponse]
    """

    kwargs = _get_kwargs(
        private_servers_tab=private_servers_tab,
        items_per_page=items_per_page,
        cursor=cursor,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    private_servers_tab: PrivateServersTab | Unset = PrivateServersTab.MYPRIVATESERVERS,
    items_per_page: int | Unset = 25,
    cursor: str | Unset = "",
) -> MyPrivateServersResponse | None:
    """
    Args:
        private_servers_tab (PrivateServersTab | Unset):  Default:
            PrivateServersTab.MYPRIVATESERVERS.
        items_per_page (int | Unset):  Default: 25.
        cursor (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MyPrivateServersResponse
    """

    return sync_detailed(
        client=client,
        private_servers_tab=private_servers_tab,
        items_per_page=items_per_page,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    private_servers_tab: PrivateServersTab | Unset = PrivateServersTab.MYPRIVATESERVERS,
    items_per_page: int | Unset = 25,
    cursor: str | Unset = "",
) -> Response[MyPrivateServersResponse]:
    """
    Args:
        private_servers_tab (PrivateServersTab | Unset):  Default:
            PrivateServersTab.MYPRIVATESERVERS.
        items_per_page (int | Unset):  Default: 25.
        cursor (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MyPrivateServersResponse]
    """

    kwargs = _get_kwargs(
        private_servers_tab=private_servers_tab,
        items_per_page=items_per_page,
        cursor=cursor,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    private_servers_tab: PrivateServersTab | Unset = PrivateServersTab.MYPRIVATESERVERS,
    items_per_page: int | Unset = 25,
    cursor: str | Unset = "",
) -> MyPrivateServersResponse | None:
    """
    Args:
        private_servers_tab (PrivateServersTab | Unset):  Default:
            PrivateServersTab.MYPRIVATESERVERS.
        items_per_page (int | Unset):  Default: 25.
        cursor (str | Unset):  Default: ''.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MyPrivateServersResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            private_servers_tab=private_servers_tab,
            items_per_page=items_per_page,
            cursor=cursor,
        )
    ).parsed
