from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_matchmaking_server_attribute_definitions_response import (
    ListMatchmakingServerAttributeDefinitionsResponse,
)
from ...types import Response


def _get_kwargs(
    universe_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/matchmaking-api/v1/matchmaking/server-attributes/{universe_id}".format(
            universe_id=quote(str(universe_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ListMatchmakingServerAttributeDefinitionsResponse | None:
    if response.status_code == 200:
        response_200 = ListMatchmakingServerAttributeDefinitionsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ListMatchmakingServerAttributeDefinitionsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    universe_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[ListMatchmakingServerAttributeDefinitionsResponse]:
    """List all ServerAttributeDefinitions of a universe.

    Args:
        universe_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListMatchmakingServerAttributeDefinitionsResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: int,
    *,
    client: AuthenticatedClient,
) -> ListMatchmakingServerAttributeDefinitionsResponse | None:
    """List all ServerAttributeDefinitions of a universe.

    Args:
        universe_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListMatchmakingServerAttributeDefinitionsResponse
    """

    return sync_detailed(
        universe_id=universe_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    universe_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[ListMatchmakingServerAttributeDefinitionsResponse]:
    """List all ServerAttributeDefinitions of a universe.

    Args:
        universe_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListMatchmakingServerAttributeDefinitionsResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: int,
    *,
    client: AuthenticatedClient,
) -> ListMatchmakingServerAttributeDefinitionsResponse | None:
    """List all ServerAttributeDefinitions of a universe.

    Args:
        universe_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListMatchmakingServerAttributeDefinitionsResponse
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            client=client,
        )
    ).parsed
