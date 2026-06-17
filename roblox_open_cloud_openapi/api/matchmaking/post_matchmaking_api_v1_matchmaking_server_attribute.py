from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_matchmaking_server_attribute_definition_request import (
    CreateMatchmakingServerAttributeDefinitionRequest,
)
from ...models.create_matchmaking_server_attribute_definition_response import (
    CreateMatchmakingServerAttributeDefinitionResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CreateMatchmakingServerAttributeDefinitionRequest
    | CreateMatchmakingServerAttributeDefinitionRequest
    | CreateMatchmakingServerAttributeDefinitionRequest
    | CreateMatchmakingServerAttributeDefinitionRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/matchmaking-api/v1/matchmaking/server-attribute",
        "openapi-extensions": {
            "x-roblox-stability": "BETA",
            "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
        },
        "openapi-id": "post_matchmaking-api_v1_matchmaking_server-attribute",
    }

    if isinstance(body, CreateMatchmakingServerAttributeDefinitionRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, CreateMatchmakingServerAttributeDefinitionRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CreateMatchmakingServerAttributeDefinitionRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"
    if isinstance(body, CreateMatchmakingServerAttributeDefinitionRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> CreateMatchmakingServerAttributeDefinitionResponse | None:
    if response.status_code == 200:
        response_200 = CreateMatchmakingServerAttributeDefinitionResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[CreateMatchmakingServerAttributeDefinitionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateMatchmakingServerAttributeDefinitionRequest
    | CreateMatchmakingServerAttributeDefinitionRequest
    | CreateMatchmakingServerAttributeDefinitionRequest
    | CreateMatchmakingServerAttributeDefinitionRequest
    | Unset = UNSET,
) -> Response[CreateMatchmakingServerAttributeDefinitionResponse]:
    """Create a ServerAttributeDefinition.

    Args:
        body (CreateMatchmakingServerAttributeDefinitionRequest | Unset): Request to create a new
            ServerAttributeDefinition.
        body (CreateMatchmakingServerAttributeDefinitionRequest | Unset): Request to create a new
            ServerAttributeDefinition.
        body (CreateMatchmakingServerAttributeDefinitionRequest | Unset): Request to create a new
            ServerAttributeDefinition.
        body (CreateMatchmakingServerAttributeDefinitionRequest | Unset): Request to create a new
            ServerAttributeDefinition.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateMatchmakingServerAttributeDefinitionResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: CreateMatchmakingServerAttributeDefinitionRequest
    | CreateMatchmakingServerAttributeDefinitionRequest
    | CreateMatchmakingServerAttributeDefinitionRequest
    | CreateMatchmakingServerAttributeDefinitionRequest
    | Unset = UNSET,
) -> CreateMatchmakingServerAttributeDefinitionResponse | None:
    """Create a ServerAttributeDefinition.

    Args:
        body (CreateMatchmakingServerAttributeDefinitionRequest | Unset): Request to create a new
            ServerAttributeDefinition.
        body (CreateMatchmakingServerAttributeDefinitionRequest | Unset): Request to create a new
            ServerAttributeDefinition.
        body (CreateMatchmakingServerAttributeDefinitionRequest | Unset): Request to create a new
            ServerAttributeDefinition.
        body (CreateMatchmakingServerAttributeDefinitionRequest | Unset): Request to create a new
            ServerAttributeDefinition.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateMatchmakingServerAttributeDefinitionResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateMatchmakingServerAttributeDefinitionRequest
    | CreateMatchmakingServerAttributeDefinitionRequest
    | CreateMatchmakingServerAttributeDefinitionRequest
    | CreateMatchmakingServerAttributeDefinitionRequest
    | Unset = UNSET,
) -> Response[CreateMatchmakingServerAttributeDefinitionResponse]:
    """Create a ServerAttributeDefinition.

    Args:
        body (CreateMatchmakingServerAttributeDefinitionRequest | Unset): Request to create a new
            ServerAttributeDefinition.
        body (CreateMatchmakingServerAttributeDefinitionRequest | Unset): Request to create a new
            ServerAttributeDefinition.
        body (CreateMatchmakingServerAttributeDefinitionRequest | Unset): Request to create a new
            ServerAttributeDefinition.
        body (CreateMatchmakingServerAttributeDefinitionRequest | Unset): Request to create a new
            ServerAttributeDefinition.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateMatchmakingServerAttributeDefinitionResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateMatchmakingServerAttributeDefinitionRequest
    | CreateMatchmakingServerAttributeDefinitionRequest
    | CreateMatchmakingServerAttributeDefinitionRequest
    | CreateMatchmakingServerAttributeDefinitionRequest
    | Unset = UNSET,
) -> CreateMatchmakingServerAttributeDefinitionResponse | None:
    """Create a ServerAttributeDefinition.

    Args:
        body (CreateMatchmakingServerAttributeDefinitionRequest | Unset): Request to create a new
            ServerAttributeDefinition.
        body (CreateMatchmakingServerAttributeDefinitionRequest | Unset): Request to create a new
            ServerAttributeDefinition.
        body (CreateMatchmakingServerAttributeDefinitionRequest | Unset): Request to create a new
            ServerAttributeDefinition.
        body (CreateMatchmakingServerAttributeDefinitionRequest | Unset): Request to create a new
            ServerAttributeDefinition.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateMatchmakingServerAttributeDefinitionResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
