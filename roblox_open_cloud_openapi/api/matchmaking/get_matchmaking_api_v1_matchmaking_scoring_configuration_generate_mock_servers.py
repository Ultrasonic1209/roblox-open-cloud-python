from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.generate_mock_server_signal_values_response import GenerateMockServerSignalValuesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    count: int | Unset = 1,
    capacity: int | Unset = 6,
    player_age: int | Unset = 25,
    player_play_history: float | Unset = 2.0,
    is_player_voice_chat_enabled: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["count"] = count

    params["capacity"] = capacity

    params["playerAge"] = player_age

    params["playerPlayHistory"] = player_play_history

    params["isPlayerVoiceChatEnabled"] = is_player_voice_chat_enabled

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/matchmaking-api/v1/matchmaking/scoring-configuration/generate-mock-servers",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GenerateMockServerSignalValuesResponse | None:
    if response.status_code == 200:
        response_200 = GenerateMockServerSignalValuesResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GenerateMockServerSignalValuesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    count: int | Unset = 1,
    capacity: int | Unset = 6,
    player_age: int | Unset = 25,
    player_play_history: float | Unset = 2.0,
    is_player_voice_chat_enabled: bool | Unset = False,
) -> Response[GenerateMockServerSignalValuesResponse]:
    """
    Args:
        count (int | Unset):  Default: 1.
        capacity (int | Unset):  Default: 6.
        player_age (int | Unset):  Default: 25.
        player_play_history (float | Unset):  Default: 2.0.
        is_player_voice_chat_enabled (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GenerateMockServerSignalValuesResponse]
    """

    kwargs = _get_kwargs(
        count=count,
        capacity=capacity,
        player_age=player_age,
        player_play_history=player_play_history,
        is_player_voice_chat_enabled=is_player_voice_chat_enabled,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    count: int | Unset = 1,
    capacity: int | Unset = 6,
    player_age: int | Unset = 25,
    player_play_history: float | Unset = 2.0,
    is_player_voice_chat_enabled: bool | Unset = False,
) -> GenerateMockServerSignalValuesResponse | None:
    """
    Args:
        count (int | Unset):  Default: 1.
        capacity (int | Unset):  Default: 6.
        player_age (int | Unset):  Default: 25.
        player_play_history (float | Unset):  Default: 2.0.
        is_player_voice_chat_enabled (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GenerateMockServerSignalValuesResponse
    """

    return sync_detailed(
        client=client,
        count=count,
        capacity=capacity,
        player_age=player_age,
        player_play_history=player_play_history,
        is_player_voice_chat_enabled=is_player_voice_chat_enabled,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    count: int | Unset = 1,
    capacity: int | Unset = 6,
    player_age: int | Unset = 25,
    player_play_history: float | Unset = 2.0,
    is_player_voice_chat_enabled: bool | Unset = False,
) -> Response[GenerateMockServerSignalValuesResponse]:
    """
    Args:
        count (int | Unset):  Default: 1.
        capacity (int | Unset):  Default: 6.
        player_age (int | Unset):  Default: 25.
        player_play_history (float | Unset):  Default: 2.0.
        is_player_voice_chat_enabled (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GenerateMockServerSignalValuesResponse]
    """

    kwargs = _get_kwargs(
        count=count,
        capacity=capacity,
        player_age=player_age,
        player_play_history=player_play_history,
        is_player_voice_chat_enabled=is_player_voice_chat_enabled,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    count: int | Unset = 1,
    capacity: int | Unset = 6,
    player_age: int | Unset = 25,
    player_play_history: float | Unset = 2.0,
    is_player_voice_chat_enabled: bool | Unset = False,
) -> GenerateMockServerSignalValuesResponse | None:
    """
    Args:
        count (int | Unset):  Default: 1.
        capacity (int | Unset):  Default: 6.
        player_age (int | Unset):  Default: 25.
        player_play_history (float | Unset):  Default: 2.0.
        is_player_voice_chat_enabled (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GenerateMockServerSignalValuesResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            count=count,
            capacity=capacity,
            player_age=player_age,
            player_play_history=player_play_history,
            is_player_voice_chat_enabled=is_player_voice_chat_enabled,
        )
    ).parsed
