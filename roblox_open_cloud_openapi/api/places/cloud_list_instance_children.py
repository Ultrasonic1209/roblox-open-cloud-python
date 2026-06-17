from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.operation import Operation
from ...types import UNSET, Response, Unset


def _get_kwargs(
    universe_id: str,
    place_id: str,
    instance_id: str,
    *,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["maxPageSize"] = max_page_size

    params["pageToken"] = page_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/cloud/v2/universes/{universe_id}/places/{place_id}/instances/{instance_id}:listChildren".format(
            universe_id=quote(str(universe_id), safe=""),
            place_id=quote(str(place_id), safe=""),
            instance_id=quote(str(instance_id), safe=""),
        ),
        "params": params,
        "openapi-extensions": {
            "x-long-running-operation-parameters": {
                "metadata": {"$ref": "#/components/schemas/ListInstanceChildrenMetadata"},
                "response": {"$ref": "#/components/schemas/ListInstanceChildrenResponse"},
            },
            "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            "x-roblox-scopes": [{"name": "universe.place.instance:read"}],
            "x-roblox-docs": {
                "category": "Universes and places",
                "methodProperties": {"scopes": ["universe.place.instance:read"]},
                "resource": {"$ref": "#/components/schemas/Instance", "name": "Instance"},
            },
            "x-roblox-stability": "BETA",
            "x-roblox-rate-limits": {"perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 45}},
        },
        "openapi-id": "Cloud_ListInstanceChildren",
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Operation | None:
    if response.status_code == 200:
        response_200 = Operation.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[Operation]:
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
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> Response[Operation]:
    """List Instance Children

     Lists an instance's children.

    The maximum supported response data size is 500,000 bytes. If this limit is
    exceeded, the returned `Operation` will be completed with an error result
    that has an error code of `422`.


    Args:
        universe_id (str):
        place_id (str):
        instance_id (str):
        max_page_size (int | Unset):
        page_token (str | Unset):

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
        max_page_size=max_page_size,
        page_token=page_token,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: str,
    place_id: str,
    instance_id: str,
    *,
    client: AuthenticatedClient,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> Operation | None:
    """List Instance Children

     Lists an instance's children.

    The maximum supported response data size is 500,000 bytes. If this limit is
    exceeded, the returned `Operation` will be completed with an error result
    that has an error code of `422`.


    Args:
        universe_id (str):
        place_id (str):
        instance_id (str):
        max_page_size (int | Unset):
        page_token (str | Unset):

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
        max_page_size=max_page_size,
        page_token=page_token,
    ).parsed


async def asyncio_detailed(
    universe_id: str,
    place_id: str,
    instance_id: str,
    *,
    client: AuthenticatedClient,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> Response[Operation]:
    """List Instance Children

     Lists an instance's children.

    The maximum supported response data size is 500,000 bytes. If this limit is
    exceeded, the returned `Operation` will be completed with an error result
    that has an error code of `422`.


    Args:
        universe_id (str):
        place_id (str):
        instance_id (str):
        max_page_size (int | Unset):
        page_token (str | Unset):

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
        max_page_size=max_page_size,
        page_token=page_token,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: str,
    place_id: str,
    instance_id: str,
    *,
    client: AuthenticatedClient,
    max_page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> Operation | None:
    """List Instance Children

     Lists an instance's children.

    The maximum supported response data size is 500,000 bytes. If this limit is
    exceeded, the returned `Operation` will be completed with an error result
    that has an error code of `422`.


    Args:
        universe_id (str):
        place_id (str):
        instance_id (str):
        max_page_size (int | Unset):
        page_token (str | Unset):

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
            max_page_size=max_page_size,
            page_token=page_token,
        )
    ).parsed
