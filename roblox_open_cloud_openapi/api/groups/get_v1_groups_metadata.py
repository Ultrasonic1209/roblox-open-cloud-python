from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_groups_api_groups_display_options_response import RobloxGroupsApiGroupsDisplayOptionsResponse
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://groups.roblox.com/v1/groups/metadata",
        "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
        "openapi-id": "get_v1_groups_metadata",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> RobloxGroupsApiGroupsDisplayOptionsResponse | None:
    if response.status_code == 200:
        response_200 = RobloxGroupsApiGroupsDisplayOptionsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[RobloxGroupsApiGroupsDisplayOptionsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[RobloxGroupsApiGroupsDisplayOptionsResponse]:
    """Gets Groups contextual information:
    Max number of groups a user can be part of.
    Current number of groups a user is a member of.
    Whether to show/hide certain features based on device type.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RobloxGroupsApiGroupsDisplayOptionsResponse]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> RobloxGroupsApiGroupsDisplayOptionsResponse | None:
    """Gets Groups contextual information:
    Max number of groups a user can be part of.
    Current number of groups a user is a member of.
    Whether to show/hide certain features based on device type.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RobloxGroupsApiGroupsDisplayOptionsResponse
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[RobloxGroupsApiGroupsDisplayOptionsResponse]:
    """Gets Groups contextual information:
    Max number of groups a user can be part of.
    Current number of groups a user is a member of.
    Whether to show/hide certain features based on device type.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RobloxGroupsApiGroupsDisplayOptionsResponse]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> RobloxGroupsApiGroupsDisplayOptionsResponse | None:
    """Gets Groups contextual information:
    Max number of groups a user can be part of.
    Current number of groups a user is a member of.
    Whether to show/hide certain features based on device type.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RobloxGroupsApiGroupsDisplayOptionsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
