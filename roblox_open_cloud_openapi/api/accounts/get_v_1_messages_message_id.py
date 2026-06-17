from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_private_messages_api_models_message_details_response import (
    RobloxPrivateMessagesApiModelsMessageDetailsResponse,
)
from ...types import Response


def _get_kwargs(
    message_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://privatemessages.roblox.com/v1/messages/{message_id}".format(
            message_id=quote(str(message_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxPrivateMessagesApiModelsMessageDetailsResponse | None:
    if response.status_code == 200:
        response_200 = RobloxPrivateMessagesApiModelsMessageDetailsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxPrivateMessagesApiModelsMessageDetailsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    message_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxPrivateMessagesApiModelsMessageDetailsResponse]:
    """Gets a message's details.

    Args:
        message_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxPrivateMessagesApiModelsMessageDetailsResponse]
    """

    kwargs = _get_kwargs(
        message_id=message_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    message_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxPrivateMessagesApiModelsMessageDetailsResponse | None:
    """Gets a message's details.

    Args:
        message_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxPrivateMessagesApiModelsMessageDetailsResponse
    """

    return sync_detailed(
        message_id=message_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    message_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxPrivateMessagesApiModelsMessageDetailsResponse]:
    """Gets a message's details.

    Args:
        message_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxPrivateMessagesApiModelsMessageDetailsResponse]
    """

    kwargs = _get_kwargs(
        message_id=message_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    message_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxPrivateMessagesApiModelsMessageDetailsResponse | None:
    """Gets a message's details.

    Args:
        message_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxPrivateMessagesApiModelsMessageDetailsResponse
    """

    return (
        await asyncio_detailed(
            message_id=message_id,
            client=client,
        )
    ).parsed
