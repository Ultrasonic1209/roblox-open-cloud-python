from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_matchmaking_scoring_configuration_response import GetMatchmakingScoringConfigurationResponse
from ...types import Response


def _get_kwargs(
    scoring_configuration_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/matchmaking-api/v1/matchmaking/scoring-configuration/{scoring_configuration_id}".format(
            scoring_configuration_id=quote(str(scoring_configuration_id), safe=""),
        ),
        "extensions": {
            "openapi-extensions": {
                "x-roblox-stability": "BETA",
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            },
            "openapi-id": "get_matchmaking-api_v1_matchmaking_scoring-configuration_scoringConfigurationId",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> GetMatchmakingScoringConfigurationResponse | None:
    if response.status_code == 200:
        response_200 = GetMatchmakingScoringConfigurationResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[GetMatchmakingScoringConfigurationResponse]:
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
) -> Response[GetMatchmakingScoringConfigurationResponse]:
    """Updates a matchmaking scoring configuration.

    Args:
        scoring_configuration_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMatchmakingScoringConfigurationResponse]
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
) -> GetMatchmakingScoringConfigurationResponse | None:
    """Updates a matchmaking scoring configuration.

    Args:
        scoring_configuration_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMatchmakingScoringConfigurationResponse
    """

    return sync_detailed(
        scoring_configuration_id=scoring_configuration_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    scoring_configuration_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[GetMatchmakingScoringConfigurationResponse]:
    """Updates a matchmaking scoring configuration.

    Args:
        scoring_configuration_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMatchmakingScoringConfigurationResponse]
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
) -> GetMatchmakingScoringConfigurationResponse | None:
    """Updates a matchmaking scoring configuration.

    Args:
        scoring_configuration_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMatchmakingScoringConfigurationResponse
    """

    return (
        await asyncio_detailed(
            scoring_configuration_id=scoring_configuration_id,
            client=client,
        )
    ).parsed
