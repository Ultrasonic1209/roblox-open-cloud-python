from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_private_messages_api_models_get_announcements_response import (
    RobloxPrivateMessagesApiModelsGetAnnouncementsResponse,
)
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/announcements",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxPrivateMessagesApiModelsGetAnnouncementsResponse | None:
    if response.status_code == 200:
        response_200 = RobloxPrivateMessagesApiModelsGetAnnouncementsResponse.from_dict(response.json())

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
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RobloxPrivateMessagesApiModelsGetAnnouncementsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxPrivateMessagesApiModelsGetAnnouncementsResponse]:
    """Migrate from RobloxWebsite project, return news notification for Private Message page

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxPrivateMessagesApiModelsGetAnnouncementsResponse]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Any | RobloxPrivateMessagesApiModelsGetAnnouncementsResponse | None:
    """Migrate from RobloxWebsite project, return news notification for Private Message page

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxPrivateMessagesApiModelsGetAnnouncementsResponse
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxPrivateMessagesApiModelsGetAnnouncementsResponse]:
    """Migrate from RobloxWebsite project, return news notification for Private Message page

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxPrivateMessagesApiModelsGetAnnouncementsResponse]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Any | RobloxPrivateMessagesApiModelsGetAnnouncementsResponse | None:
    """Migrate from RobloxWebsite project, return news notification for Private Message page

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxPrivateMessagesApiModelsGetAnnouncementsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
