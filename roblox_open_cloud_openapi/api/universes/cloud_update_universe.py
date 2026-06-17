from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.universe import Universe
from ...types import UNSET, Response, Unset


def _get_kwargs(
    universe_id: str,
    *,
    body: Universe,
    update_mask: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["updateMask"] = update_mask

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/cloud/v2/universes/{universe_id}".format(
            universe_id=quote(str(universe_id), safe=""),
        ),
        "params": params,
        "openapi-extensions": {
            "x-roblox-engine-usability": {"apiKeyWithHttpService": True},
            "x-roblox-scopes": [{"name": "universe:write"}],
            "x-roblox-docs": {
                "category": "Universes and places",
                "methodProperties": {"scopes": ["universe:write"]},
                "resource": {"$ref": "#/components/schemas/Universe", "name": "Universe"},
            },
            "x-roblox-stability": "STABLE",
            "x-roblox-rate-limits": {
                "perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 100},
                "perOauth2Authorization": {"period": "MINUTE", "maxInPeriod": 100},
            },
        },
        "openapi-id": "Cloud_UpdateUniverse",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Universe | None:
    if response.status_code == 200:
        response_200 = Universe.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[Universe]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    universe_id: str,
    *,
    client: AuthenticatedClient,
    body: Universe,
    update_mask: str | Unset = UNSET,
) -> Response[Universe]:
    """Update Universe

     Updates the specified universe.

    This method is guaranteed to return all updated fields.
    This method may additionally return the full resource.

    Args:
        universe_id (str):
        update_mask (str | Unset):
        body (Universe): Represents a Roblox experience.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Universe]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        body=body,
        update_mask=update_mask,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: str,
    *,
    client: AuthenticatedClient,
    body: Universe,
    update_mask: str | Unset = UNSET,
) -> Universe | None:
    """Update Universe

     Updates the specified universe.

    This method is guaranteed to return all updated fields.
    This method may additionally return the full resource.

    Args:
        universe_id (str):
        update_mask (str | Unset):
        body (Universe): Represents a Roblox experience.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Universe
    """

    return sync_detailed(
        universe_id=universe_id,
        client=client,
        body=body,
        update_mask=update_mask,
    ).parsed


async def asyncio_detailed(
    universe_id: str,
    *,
    client: AuthenticatedClient,
    body: Universe,
    update_mask: str | Unset = UNSET,
) -> Response[Universe]:
    """Update Universe

     Updates the specified universe.

    This method is guaranteed to return all updated fields.
    This method may additionally return the full resource.

    Args:
        universe_id (str):
        update_mask (str | Unset):
        body (Universe): Represents a Roblox experience.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Universe]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        body=body,
        update_mask=update_mask,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: str,
    *,
    client: AuthenticatedClient,
    body: Universe,
    update_mask: str | Unset = UNSET,
) -> Universe | None:
    """Update Universe

     Updates the specified universe.

    This method is guaranteed to return all updated fields.
    This method may additionally return the full resource.

    Args:
        universe_id (str):
        update_mask (str | Unset):
        body (Universe): Represents a Roblox experience.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Universe
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            client=client,
            body=body,
            update_mask=update_mask,
        )
    ).parsed
