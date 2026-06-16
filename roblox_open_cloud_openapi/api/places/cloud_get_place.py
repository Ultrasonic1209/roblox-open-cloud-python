from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.place import Place
from ...types import Response


def _get_kwargs(
    universe_id: str,
    place_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/cloud/v2/universes/{universe_id}/places/{place_id}".format(
            universe_id=quote(str(universe_id), safe=""),
            place_id=quote(str(place_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Place | None:
    if response.status_code == 200:
        response_200 = Place.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Place]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    universe_id: str,
    place_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Place]:
    """Get Place

     Gets the specified place.

    Args:
        universe_id (str):
        place_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Place]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        place_id=place_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: str,
    place_id: str,
    *,
    client: AuthenticatedClient,
) -> Place | None:
    """Get Place

     Gets the specified place.

    Args:
        universe_id (str):
        place_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Place
    """

    return sync_detailed(
        universe_id=universe_id,
        place_id=place_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    universe_id: str,
    place_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Place]:
    """Get Place

     Gets the specified place.

    Args:
        universe_id (str):
        place_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Place]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        place_id=place_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: str,
    place_id: str,
    *,
    client: AuthenticatedClient,
) -> Place | None:
    """Get Place

     Gets the specified place.

    Args:
        universe_id (str):
        place_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Place
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            place_id=place_id,
            client=client,
        )
    ).parsed
