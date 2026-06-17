from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_groups_api_group_search_metadata_response import RobloxGroupsApiGroupSearchMetadataResponse
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://groups.roblox.com/v1/groups/search/metadata",
        "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
        "openapi-id": "get_v1_groups_search_metadata",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxGroupsApiGroupSearchMetadataResponse | None:
    if response.status_code == 200:
        response_200 = RobloxGroupsApiGroupSearchMetadataResponse.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxGroupsApiGroupSearchMetadataResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxGroupsApiGroupSearchMetadataResponse]:
    """Get suggested groups and other miscellaneous information needed for the group/join page like flags

     Although there is no reason for this to require an authenticated user right now, in the future,
    we will use coco to return different suggested groups based upon that user's request context

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxGroupsApiGroupSearchMetadataResponse]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Any | RobloxGroupsApiGroupSearchMetadataResponse | None:
    """Get suggested groups and other miscellaneous information needed for the group/join page like flags

     Although there is no reason for this to require an authenticated user right now, in the future,
    we will use coco to return different suggested groups based upon that user's request context

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxGroupsApiGroupSearchMetadataResponse
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxGroupsApiGroupSearchMetadataResponse]:
    """Get suggested groups and other miscellaneous information needed for the group/join page like flags

     Although there is no reason for this to require an authenticated user right now, in the future,
    we will use coco to return different suggested groups based upon that user's request context

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxGroupsApiGroupSearchMetadataResponse]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Any | RobloxGroupsApiGroupSearchMetadataResponse | None:
    """Get suggested groups and other miscellaneous information needed for the group/join page like flags

     Although there is no reason for this to require an authenticated user right now, in the future,
    we will use coco to return different suggested groups based upon that user's request context

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxGroupsApiGroupSearchMetadataResponse
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
