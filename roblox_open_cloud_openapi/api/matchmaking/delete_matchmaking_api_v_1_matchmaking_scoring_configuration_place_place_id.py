from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.remove_place_matchmaking_scoring_configuration_response import (
    RemovePlaceMatchmakingScoringConfigurationResponse,
)
from ...types import Response


def _get_kwargs(
    place_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/matchmaking-api/v1/matchmaking/scoring-configuration/place/{place_id}".format(
            place_id=quote(str(place_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> RemovePlaceMatchmakingScoringConfigurationResponse | None:
    if response.status_code == 200:
        response_200 = RemovePlaceMatchmakingScoringConfigurationResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[RemovePlaceMatchmakingScoringConfigurationResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    place_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[RemovePlaceMatchmakingScoringConfigurationResponse]:
    """Removes the matchmaking scoring configuration for a place.

    Args:
        place_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RemovePlaceMatchmakingScoringConfigurationResponse]
    """

    kwargs = _get_kwargs(
        place_id=place_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    place_id: int,
    *,
    client: AuthenticatedClient,
) -> RemovePlaceMatchmakingScoringConfigurationResponse | None:
    """Removes the matchmaking scoring configuration for a place.

    Args:
        place_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RemovePlaceMatchmakingScoringConfigurationResponse
    """

    return sync_detailed(
        place_id=place_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    place_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[RemovePlaceMatchmakingScoringConfigurationResponse]:
    """Removes the matchmaking scoring configuration for a place.

    Args:
        place_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RemovePlaceMatchmakingScoringConfigurationResponse]
    """

    kwargs = _get_kwargs(
        place_id=place_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    place_id: int,
    *,
    client: AuthenticatedClient,
) -> RemovePlaceMatchmakingScoringConfigurationResponse | None:
    """Removes the matchmaking scoring configuration for a place.

    Args:
        place_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RemovePlaceMatchmakingScoringConfigurationResponse
    """

    return (
        await asyncio_detailed(
            place_id=place_id,
            client=client,
        )
    ).parsed
