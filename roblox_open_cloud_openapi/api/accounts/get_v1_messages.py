from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v1_messages_message_tab import GetV1MessagesMessageTab
from ...models.roblox_private_messages_api_models_get_messages_response import (
    RobloxPrivateMessagesApiModelsGetMessagesResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page_number: int | Unset = 0,
    page_size: int | Unset = 20,
    message_tab: GetV1MessagesMessageTab | Unset = GetV1MessagesMessageTab.INBOX,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["pageNumber"] = page_number

    params["pageSize"] = page_size

    json_message_tab: str | Unset = UNSET
    if not isinstance(message_tab, Unset):
        json_message_tab = message_tab.value

    params["messageTab"] = json_message_tab

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://privatemessages.roblox.com/v1/messages",
        "params": params,
        "extensions": {
            "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
            "openapi-id": "get_v1_messages",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxPrivateMessagesApiModelsGetMessagesResponse | None:
    if response.status_code == 200:
        response_200 = RobloxPrivateMessagesApiModelsGetMessagesResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxPrivateMessagesApiModelsGetMessagesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    page_number: int | Unset = 0,
    page_size: int | Unset = 20,
    message_tab: GetV1MessagesMessageTab | Unset = GetV1MessagesMessageTab.INBOX,
) -> Response[Any | RobloxPrivateMessagesApiModelsGetMessagesResponse]:
    """Gets a user's messages.

    Args:
        page_number (int | Unset):  Default: 0.
        page_size (int | Unset):  Default: 20.
        message_tab (GetV1MessagesMessageTab | Unset):  Default: GetV1MessagesMessageTab.INBOX.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxPrivateMessagesApiModelsGetMessagesResponse]
    """

    kwargs = _get_kwargs(
        page_number=page_number,
        page_size=page_size,
        message_tab=message_tab,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    page_number: int | Unset = 0,
    page_size: int | Unset = 20,
    message_tab: GetV1MessagesMessageTab | Unset = GetV1MessagesMessageTab.INBOX,
) -> Any | RobloxPrivateMessagesApiModelsGetMessagesResponse | None:
    """Gets a user's messages.

    Args:
        page_number (int | Unset):  Default: 0.
        page_size (int | Unset):  Default: 20.
        message_tab (GetV1MessagesMessageTab | Unset):  Default: GetV1MessagesMessageTab.INBOX.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxPrivateMessagesApiModelsGetMessagesResponse
    """

    return sync_detailed(
        client=client,
        page_number=page_number,
        page_size=page_size,
        message_tab=message_tab,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    page_number: int | Unset = 0,
    page_size: int | Unset = 20,
    message_tab: GetV1MessagesMessageTab | Unset = GetV1MessagesMessageTab.INBOX,
) -> Response[Any | RobloxPrivateMessagesApiModelsGetMessagesResponse]:
    """Gets a user's messages.

    Args:
        page_number (int | Unset):  Default: 0.
        page_size (int | Unset):  Default: 20.
        message_tab (GetV1MessagesMessageTab | Unset):  Default: GetV1MessagesMessageTab.INBOX.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxPrivateMessagesApiModelsGetMessagesResponse]
    """

    kwargs = _get_kwargs(
        page_number=page_number,
        page_size=page_size,
        message_tab=message_tab,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    page_number: int | Unset = 0,
    page_size: int | Unset = 20,
    message_tab: GetV1MessagesMessageTab | Unset = GetV1MessagesMessageTab.INBOX,
) -> Any | RobloxPrivateMessagesApiModelsGetMessagesResponse | None:
    """Gets a user's messages.

    Args:
        page_number (int | Unset):  Default: 0.
        page_size (int | Unset):  Default: 20.
        message_tab (GetV1MessagesMessageTab | Unset):  Default: GetV1MessagesMessageTab.INBOX.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxPrivateMessagesApiModelsGetMessagesResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            page_number=page_number,
            page_size=page_size,
            message_tab=message_tab,
        )
    ).parsed
