from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_matchmaking_player_attribute_definition_request import (
    UpdateMatchmakingPlayerAttributeDefinitionRequest,
)
from ...models.update_matchmaking_player_attribute_definition_response import (
    UpdateMatchmakingPlayerAttributeDefinitionResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    attribute_id: str,
    *,
    body: UpdateMatchmakingPlayerAttributeDefinitionRequest
    | UpdateMatchmakingPlayerAttributeDefinitionRequest
    | UpdateMatchmakingPlayerAttributeDefinitionRequest
    | UpdateMatchmakingPlayerAttributeDefinitionRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/matchmaking-api/v1/matchmaking/player-attribute/{attribute_id}".format(
            attribute_id=quote(str(attribute_id), safe=""),
        ),
    }

    if isinstance(body, UpdateMatchmakingPlayerAttributeDefinitionRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, UpdateMatchmakingPlayerAttributeDefinitionRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, UpdateMatchmakingPlayerAttributeDefinitionRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"
    if isinstance(body, UpdateMatchmakingPlayerAttributeDefinitionRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> UpdateMatchmakingPlayerAttributeDefinitionResponse | None:
    if response.status_code == 200:
        response_200 = UpdateMatchmakingPlayerAttributeDefinitionResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[UpdateMatchmakingPlayerAttributeDefinitionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    attribute_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateMatchmakingPlayerAttributeDefinitionRequest
    | UpdateMatchmakingPlayerAttributeDefinitionRequest
    | UpdateMatchmakingPlayerAttributeDefinitionRequest
    | UpdateMatchmakingPlayerAttributeDefinitionRequest
    | Unset = UNSET,
) -> Response[UpdateMatchmakingPlayerAttributeDefinitionResponse]:
    """Update the PlayerAttributeDefinition specified by attributeId.

    Args:
        attribute_id (str):
        body (UpdateMatchmakingPlayerAttributeDefinitionRequest | Unset): Request model for
            updating a PlayerAttributeDefinition.
        body (UpdateMatchmakingPlayerAttributeDefinitionRequest | Unset): Request model for
            updating a PlayerAttributeDefinition.
        body (UpdateMatchmakingPlayerAttributeDefinitionRequest | Unset): Request model for
            updating a PlayerAttributeDefinition.
        body (UpdateMatchmakingPlayerAttributeDefinitionRequest | Unset): Request model for
            updating a PlayerAttributeDefinition.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateMatchmakingPlayerAttributeDefinitionResponse]
    """

    kwargs = _get_kwargs(
        attribute_id=attribute_id,
        body=body,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    attribute_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateMatchmakingPlayerAttributeDefinitionRequest
    | UpdateMatchmakingPlayerAttributeDefinitionRequest
    | UpdateMatchmakingPlayerAttributeDefinitionRequest
    | UpdateMatchmakingPlayerAttributeDefinitionRequest
    | Unset = UNSET,
) -> UpdateMatchmakingPlayerAttributeDefinitionResponse | None:
    """Update the PlayerAttributeDefinition specified by attributeId.

    Args:
        attribute_id (str):
        body (UpdateMatchmakingPlayerAttributeDefinitionRequest | Unset): Request model for
            updating a PlayerAttributeDefinition.
        body (UpdateMatchmakingPlayerAttributeDefinitionRequest | Unset): Request model for
            updating a PlayerAttributeDefinition.
        body (UpdateMatchmakingPlayerAttributeDefinitionRequest | Unset): Request model for
            updating a PlayerAttributeDefinition.
        body (UpdateMatchmakingPlayerAttributeDefinitionRequest | Unset): Request model for
            updating a PlayerAttributeDefinition.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateMatchmakingPlayerAttributeDefinitionResponse
    """

    return sync_detailed(
        attribute_id=attribute_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    attribute_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateMatchmakingPlayerAttributeDefinitionRequest
    | UpdateMatchmakingPlayerAttributeDefinitionRequest
    | UpdateMatchmakingPlayerAttributeDefinitionRequest
    | UpdateMatchmakingPlayerAttributeDefinitionRequest
    | Unset = UNSET,
) -> Response[UpdateMatchmakingPlayerAttributeDefinitionResponse]:
    """Update the PlayerAttributeDefinition specified by attributeId.

    Args:
        attribute_id (str):
        body (UpdateMatchmakingPlayerAttributeDefinitionRequest | Unset): Request model for
            updating a PlayerAttributeDefinition.
        body (UpdateMatchmakingPlayerAttributeDefinitionRequest | Unset): Request model for
            updating a PlayerAttributeDefinition.
        body (UpdateMatchmakingPlayerAttributeDefinitionRequest | Unset): Request model for
            updating a PlayerAttributeDefinition.
        body (UpdateMatchmakingPlayerAttributeDefinitionRequest | Unset): Request model for
            updating a PlayerAttributeDefinition.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateMatchmakingPlayerAttributeDefinitionResponse]
    """

    kwargs = _get_kwargs(
        attribute_id=attribute_id,
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    attribute_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateMatchmakingPlayerAttributeDefinitionRequest
    | UpdateMatchmakingPlayerAttributeDefinitionRequest
    | UpdateMatchmakingPlayerAttributeDefinitionRequest
    | UpdateMatchmakingPlayerAttributeDefinitionRequest
    | Unset = UNSET,
) -> UpdateMatchmakingPlayerAttributeDefinitionResponse | None:
    """Update the PlayerAttributeDefinition specified by attributeId.

    Args:
        attribute_id (str):
        body (UpdateMatchmakingPlayerAttributeDefinitionRequest | Unset): Request model for
            updating a PlayerAttributeDefinition.
        body (UpdateMatchmakingPlayerAttributeDefinitionRequest | Unset): Request model for
            updating a PlayerAttributeDefinition.
        body (UpdateMatchmakingPlayerAttributeDefinitionRequest | Unset): Request model for
            updating a PlayerAttributeDefinition.
        body (UpdateMatchmakingPlayerAttributeDefinitionRequest | Unset): Request model for
            updating a PlayerAttributeDefinition.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateMatchmakingPlayerAttributeDefinitionResponse
    """

    return (
        await asyncio_detailed(
            attribute_id=attribute_id,
            client=client,
            body=body,
        )
    ).parsed
