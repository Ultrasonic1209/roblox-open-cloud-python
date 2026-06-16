from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.game_vote_response_api_array_response import GameVoteResponseApiArrayResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    universe_ids: list[int] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_universe_ids: list[int] | Unset = UNSET
    if not isinstance(universe_ids, Unset):
        json_universe_ids = universe_ids

    params["universeIds"] = json_universe_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/games/votes",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GameVoteResponseApiArrayResponse | None:
    if response.status_code == 200:
        response_200 = GameVoteResponseApiArrayResponse.from_dict(response.text)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GameVoteResponseApiArrayResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    universe_ids: list[int] | Unset = UNSET,
) -> Response[GameVoteResponseApiArrayResponse]:
    """
    Args:
        universe_ids (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GameVoteResponseApiArrayResponse]
    """

    kwargs = _get_kwargs(
        universe_ids=universe_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    universe_ids: list[int] | Unset = UNSET,
) -> GameVoteResponseApiArrayResponse | None:
    """
    Args:
        universe_ids (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GameVoteResponseApiArrayResponse
    """

    return sync_detailed(
        client=client,
        universe_ids=universe_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    universe_ids: list[int] | Unset = UNSET,
) -> Response[GameVoteResponseApiArrayResponse]:
    """
    Args:
        universe_ids (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GameVoteResponseApiArrayResponse]
    """

    kwargs = _get_kwargs(
        universe_ids=universe_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    universe_ids: list[int] | Unset = UNSET,
) -> GameVoteResponseApiArrayResponse | None:
    """
    Args:
        universe_ids (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GameVoteResponseApiArrayResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            universe_ids=universe_ids,
        )
    ).parsed
