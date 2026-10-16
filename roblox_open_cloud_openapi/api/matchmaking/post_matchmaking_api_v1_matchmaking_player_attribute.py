from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_matchmaking_player_attribute_definition_request import (
    CreateMatchmakingPlayerAttributeDefinitionRequest,
)
from ...models.create_matchmaking_player_attribute_definition_response import (
    CreateMatchmakingPlayerAttributeDefinitionResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CreateMatchmakingPlayerAttributeDefinitionRequest
    | CreateMatchmakingPlayerAttributeDefinitionRequest
    | CreateMatchmakingPlayerAttributeDefinitionRequest
    | CreateMatchmakingPlayerAttributeDefinitionRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/matchmaking-api/v1/matchmaking/player-attribute",
        "extensions": {
            "openapi-extensions": {
                "x-roblox-stability": "BETA",
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            },
            "openapi-id": "post_matchmaking-api_v1_matchmaking_player-attribute",
        },
    }

    if isinstance(body, CreateMatchmakingPlayerAttributeDefinitionRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, CreateMatchmakingPlayerAttributeDefinitionRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CreateMatchmakingPlayerAttributeDefinitionRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"
    if isinstance(body, CreateMatchmakingPlayerAttributeDefinitionRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> CreateMatchmakingPlayerAttributeDefinitionResponse | None:
    if response.status_code == 200:
        response_200 = CreateMatchmakingPlayerAttributeDefinitionResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[CreateMatchmakingPlayerAttributeDefinitionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateMatchmakingPlayerAttributeDefinitionRequest
    | CreateMatchmakingPlayerAttributeDefinitionRequest
    | CreateMatchmakingPlayerAttributeDefinitionRequest
    | CreateMatchmakingPlayerAttributeDefinitionRequest
    | Unset = UNSET,
) -> Response[CreateMatchmakingPlayerAttributeDefinitionResponse]:
    """Create a PlayerAttributeDefinition.

    Args:
        body (CreateMatchmakingPlayerAttributeDefinitionRequest | Unset): Request to create a new
            MatchmakingPlayerAttributeDefinition.
        body (CreateMatchmakingPlayerAttributeDefinitionRequest | Unset): Request to create a new
            MatchmakingPlayerAttributeDefinition.
        body (CreateMatchmakingPlayerAttributeDefinitionRequest | Unset): Request to create a new
            MatchmakingPlayerAttributeDefinition.
        body (CreateMatchmakingPlayerAttributeDefinitionRequest | Unset): Request to create a new
            MatchmakingPlayerAttributeDefinition.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateMatchmakingPlayerAttributeDefinitionResponse]
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
    body: CreateMatchmakingPlayerAttributeDefinitionRequest
    | CreateMatchmakingPlayerAttributeDefinitionRequest
    | CreateMatchmakingPlayerAttributeDefinitionRequest
    | CreateMatchmakingPlayerAttributeDefinitionRequest
    | Unset = UNSET,
) -> CreateMatchmakingPlayerAttributeDefinitionResponse | None:
    """Create a PlayerAttributeDefinition.

    Args:
        body (CreateMatchmakingPlayerAttributeDefinitionRequest | Unset): Request to create a new
            MatchmakingPlayerAttributeDefinition.
        body (CreateMatchmakingPlayerAttributeDefinitionRequest | Unset): Request to create a new
            MatchmakingPlayerAttributeDefinition.
        body (CreateMatchmakingPlayerAttributeDefinitionRequest | Unset): Request to create a new
            MatchmakingPlayerAttributeDefinition.
        body (CreateMatchmakingPlayerAttributeDefinitionRequest | Unset): Request to create a new
            MatchmakingPlayerAttributeDefinition.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateMatchmakingPlayerAttributeDefinitionResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateMatchmakingPlayerAttributeDefinitionRequest
    | CreateMatchmakingPlayerAttributeDefinitionRequest
    | CreateMatchmakingPlayerAttributeDefinitionRequest
    | CreateMatchmakingPlayerAttributeDefinitionRequest
    | Unset = UNSET,
) -> Response[CreateMatchmakingPlayerAttributeDefinitionResponse]:
    """Create a PlayerAttributeDefinition.

    Args:
        body (CreateMatchmakingPlayerAttributeDefinitionRequest | Unset): Request to create a new
            MatchmakingPlayerAttributeDefinition.
        body (CreateMatchmakingPlayerAttributeDefinitionRequest | Unset): Request to create a new
            MatchmakingPlayerAttributeDefinition.
        body (CreateMatchmakingPlayerAttributeDefinitionRequest | Unset): Request to create a new
            MatchmakingPlayerAttributeDefinition.
        body (CreateMatchmakingPlayerAttributeDefinitionRequest | Unset): Request to create a new
            MatchmakingPlayerAttributeDefinition.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateMatchmakingPlayerAttributeDefinitionResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateMatchmakingPlayerAttributeDefinitionRequest
    | CreateMatchmakingPlayerAttributeDefinitionRequest
    | CreateMatchmakingPlayerAttributeDefinitionRequest
    | CreateMatchmakingPlayerAttributeDefinitionRequest
    | Unset = UNSET,
) -> CreateMatchmakingPlayerAttributeDefinitionResponse | None:
    """Create a PlayerAttributeDefinition.

    Args:
        body (CreateMatchmakingPlayerAttributeDefinitionRequest | Unset): Request to create a new
            MatchmakingPlayerAttributeDefinition.
        body (CreateMatchmakingPlayerAttributeDefinitionRequest | Unset): Request to create a new
            MatchmakingPlayerAttributeDefinition.
        body (CreateMatchmakingPlayerAttributeDefinitionRequest | Unset): Request to create a new
            MatchmakingPlayerAttributeDefinition.
        body (CreateMatchmakingPlayerAttributeDefinitionRequest | Unset): Request to create a new
            MatchmakingPlayerAttributeDefinition.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateMatchmakingPlayerAttributeDefinitionResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
