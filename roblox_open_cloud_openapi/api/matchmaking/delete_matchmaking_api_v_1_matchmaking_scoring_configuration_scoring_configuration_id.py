from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_matchmaking_scoring_configuration_response import DeleteMatchmakingScoringConfigurationResponse
from ...types import Response


def _get_kwargs(
    scoring_configuration_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/matchmaking-api/v1/matchmaking/scoring-configuration/{scoring_configuration_id}".format(
            scoring_configuration_id=quote(str(scoring_configuration_id), safe=""),
        ),
        "openapi-extensions": {
            "x-roblox-stability": "BETA",
            "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
        },
        "openapi-id": "delete_matchmaking-api_v1_matchmaking_scoring-configuration_scoringConfigurationId",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> DeleteMatchmakingScoringConfigurationResponse | None:
    if response.status_code == 200:
        response_200 = DeleteMatchmakingScoringConfigurationResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[DeleteMatchmakingScoringConfigurationResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    scoring_configuration_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[DeleteMatchmakingScoringConfigurationResponse]:
    """Deletes a matchmaking scoring configuration.

    Args:
        scoring_configuration_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteMatchmakingScoringConfigurationResponse]
    """

    kwargs = _get_kwargs(
        scoring_configuration_id=scoring_configuration_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    scoring_configuration_id: str,
    *,
    client: AuthenticatedClient,
) -> DeleteMatchmakingScoringConfigurationResponse | None:
    """Deletes a matchmaking scoring configuration.

    Args:
        scoring_configuration_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteMatchmakingScoringConfigurationResponse
    """

    return sync_detailed(
        scoring_configuration_id=scoring_configuration_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    scoring_configuration_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[DeleteMatchmakingScoringConfigurationResponse]:
    """Deletes a matchmaking scoring configuration.

    Args:
        scoring_configuration_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteMatchmakingScoringConfigurationResponse]
    """

    kwargs = _get_kwargs(
        scoring_configuration_id=scoring_configuration_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    scoring_configuration_id: str,
    *,
    client: AuthenticatedClient,
) -> DeleteMatchmakingScoringConfigurationResponse | None:
    """Deletes a matchmaking scoring configuration.

    Args:
        scoring_configuration_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteMatchmakingScoringConfigurationResponse
    """

    return (
        await asyncio_detailed(
            scoring_configuration_id=scoring_configuration_id,
            client=client,
        )
    ).parsed
