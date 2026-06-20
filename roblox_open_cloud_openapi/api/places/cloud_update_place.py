from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.place import Place
from ...types import UNSET, Response, Unset


def _get_kwargs(
    universe_id: str,
    place_id: str,
    *,
    body: Place,
    update_mask: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["updateMask"] = update_mask

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/cloud/v2/universes/{universe_id}/places/{place_id}".format(
            universe_id=quote(str(universe_id), safe=""),
            place_id=quote(str(place_id), safe=""),
        ),
        "params": params,
        "extensions": {
            "openapi-extensions": {
                "x-roblox-engine-usability": {"apiKeyWithHttpService": True},
                "x-roblox-scopes": [{"name": "universe.place:write"}],
                "x-roblox-docs": {
                    "category": "Universes and places",
                    "methodProperties": {"scopes": ["universe.place:write"]},
                    "resource": {"$ref": "#/components/schemas/Place", "name": "Place"},
                },
                "x-roblox-stability": "STABLE",
                "x-roblox-rate-limits": {
                    "perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 100},
                    "perOauth2Authorization": {"period": "MINUTE", "maxInPeriod": 100},
                },
            },
            "openapi-id": "Cloud_UpdatePlace",
        },
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Place | None:
    if response.status_code == 200:
        response_200 = Place.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[Place]:
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
    body: Place,
    update_mask: str | Unset = UNSET,
) -> Response[Place]:
    """Update Place

     Updates the specified place.

    Args:
        universe_id (str):
        place_id (str):
        update_mask (str | Unset):
        body (Place): Represents a Roblox place.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Place]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        place_id=place_id,
        body=body,
        update_mask=update_mask,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: str,
    place_id: str,
    *,
    client: AuthenticatedClient,
    body: Place,
    update_mask: str | Unset = UNSET,
) -> Place | None:
    """Update Place

     Updates the specified place.

    Args:
        universe_id (str):
        place_id (str):
        update_mask (str | Unset):
        body (Place): Represents a Roblox place.

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
        body=body,
        update_mask=update_mask,
    ).parsed


async def asyncio_detailed(
    universe_id: str,
    place_id: str,
    *,
    client: AuthenticatedClient,
    body: Place,
    update_mask: str | Unset = UNSET,
) -> Response[Place]:
    """Update Place

     Updates the specified place.

    Args:
        universe_id (str):
        place_id (str):
        update_mask (str | Unset):
        body (Place): Represents a Roblox place.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Place]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        place_id=place_id,
        body=body,
        update_mask=update_mask,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: str,
    place_id: str,
    *,
    client: AuthenticatedClient,
    body: Place,
    update_mask: str | Unset = UNSET,
) -> Place | None:
    """Update Place

     Updates the specified place.

    Args:
        universe_id (str):
        place_id (str):
        update_mask (str | Unset):
        body (Place): Represents a Roblox place.

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
            body=body,
            update_mask=update_mask,
        )
    ).parsed
