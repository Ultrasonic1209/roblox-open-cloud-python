from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_matchmaking_player_attribute_definition_response import (
    DeleteMatchmakingPlayerAttributeDefinitionResponse,
)
from ...types import Response


def _get_kwargs(
    attribute_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/matchmaking-api/v1/matchmaking/player-attribute/{attribute_id}".format(
            attribute_id=quote(str(attribute_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DeleteMatchmakingPlayerAttributeDefinitionResponse | None:
    if response.status_code == 200:
        response_200 = DeleteMatchmakingPlayerAttributeDefinitionResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DeleteMatchmakingPlayerAttributeDefinitionResponse]:
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
) -> Response[DeleteMatchmakingPlayerAttributeDefinitionResponse]:
    """Delete the PlayerAttributeDefinition specified by attributeId.

    Args:
        attribute_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteMatchmakingPlayerAttributeDefinitionResponse]
    """

    kwargs = _get_kwargs(
        attribute_id=attribute_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    attribute_id: str,
    *,
    client: AuthenticatedClient,
) -> DeleteMatchmakingPlayerAttributeDefinitionResponse | None:
    """Delete the PlayerAttributeDefinition specified by attributeId.

    Args:
        attribute_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteMatchmakingPlayerAttributeDefinitionResponse
    """

    return sync_detailed(
        attribute_id=attribute_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    attribute_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[DeleteMatchmakingPlayerAttributeDefinitionResponse]:
    """Delete the PlayerAttributeDefinition specified by attributeId.

    Args:
        attribute_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteMatchmakingPlayerAttributeDefinitionResponse]
    """

    kwargs = _get_kwargs(
        attribute_id=attribute_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    attribute_id: str,
    *,
    client: AuthenticatedClient,
) -> DeleteMatchmakingPlayerAttributeDefinitionResponse | None:
    """Delete the PlayerAttributeDefinition specified by attributeId.

    Args:
        attribute_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteMatchmakingPlayerAttributeDefinitionResponse
    """

    return (
        await asyncio_detailed(
            attribute_id=attribute_id,
            client=client,
        )
    ).parsed
