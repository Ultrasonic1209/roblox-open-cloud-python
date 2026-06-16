from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.instance import Instance
from ...models.operation import Operation
from ...types import UNSET, Response, Unset


def _get_kwargs(
    universe_id: str,
    place_id: str,
    instance_id: str,
    *,
    body: Instance,
    update_mask: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["updateMask"] = update_mask

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/cloud/v2/universes/{universe_id}/places/{place_id}/instances/{instance_id}".format(
            universe_id=quote(str(universe_id), safe=""),
            place_id=quote(str(place_id), safe=""),
            instance_id=quote(str(instance_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Operation | None:
    if response.status_code == 200:
        response_200 = Operation.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Operation]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    universe_id: str,
    place_id: str,
    instance_id: str,
    *,
    client: AuthenticatedClient,
    body: Instance,
    update_mask: str | Unset = UNSET,
) -> Response[Operation]:
    """Update Instance

     Updates an instance's property data.

    When updating a `Script` instance's source property, the maximum supported
    property size is 200,000 bytes after UTF-8 encoding.

    Args:
        universe_id (str):
        place_id (str):
        instance_id (str):
        update_mask (str | Unset):
        body (Instance): Represents a data model instance.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Operation]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        place_id=place_id,
        instance_id=instance_id,
        body=body,
        update_mask=update_mask,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: str,
    place_id: str,
    instance_id: str,
    *,
    client: AuthenticatedClient,
    body: Instance,
    update_mask: str | Unset = UNSET,
) -> Operation | None:
    """Update Instance

     Updates an instance's property data.

    When updating a `Script` instance's source property, the maximum supported
    property size is 200,000 bytes after UTF-8 encoding.

    Args:
        universe_id (str):
        place_id (str):
        instance_id (str):
        update_mask (str | Unset):
        body (Instance): Represents a data model instance.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Operation
    """

    return sync_detailed(
        universe_id=universe_id,
        place_id=place_id,
        instance_id=instance_id,
        client=client,
        body=body,
        update_mask=update_mask,
    ).parsed


async def asyncio_detailed(
    universe_id: str,
    place_id: str,
    instance_id: str,
    *,
    client: AuthenticatedClient,
    body: Instance,
    update_mask: str | Unset = UNSET,
) -> Response[Operation]:
    """Update Instance

     Updates an instance's property data.

    When updating a `Script` instance's source property, the maximum supported
    property size is 200,000 bytes after UTF-8 encoding.

    Args:
        universe_id (str):
        place_id (str):
        instance_id (str):
        update_mask (str | Unset):
        body (Instance): Represents a data model instance.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Operation]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        place_id=place_id,
        instance_id=instance_id,
        body=body,
        update_mask=update_mask,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: str,
    place_id: str,
    instance_id: str,
    *,
    client: AuthenticatedClient,
    body: Instance,
    update_mask: str | Unset = UNSET,
) -> Operation | None:
    """Update Instance

     Updates an instance's property data.

    When updating a `Script` instance's source property, the maximum supported
    property size is 200,000 bytes after UTF-8 encoding.

    Args:
        universe_id (str):
        place_id (str):
        instance_id (str):
        update_mask (str | Unset):
        body (Instance): Represents a data model instance.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Operation
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            place_id=place_id,
            instance_id=instance_id,
            client=client,
            body=body,
            update_mask=update_mask,
        )
    ).parsed
