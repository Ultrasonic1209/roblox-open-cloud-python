from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_matchmaking_scoring_configuration_request import UpdateMatchmakingScoringConfigurationRequest
from ...models.update_matchmaking_scoring_configuration_response import UpdateMatchmakingScoringConfigurationResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    scoring_configuration_id: str,
    *,
    body: UpdateMatchmakingScoringConfigurationRequest
    | UpdateMatchmakingScoringConfigurationRequest
    | UpdateMatchmakingScoringConfigurationRequest
    | UpdateMatchmakingScoringConfigurationRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/matchmaking-api/v1/matchmaking/scoring-configuration/{scoring_configuration_id}".format(
            scoring_configuration_id=quote(str(scoring_configuration_id), safe=""),
        ),
    }

    if isinstance(body, UpdateMatchmakingScoringConfigurationRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, UpdateMatchmakingScoringConfigurationRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, UpdateMatchmakingScoringConfigurationRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"
    if isinstance(body, UpdateMatchmakingScoringConfigurationRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> UpdateMatchmakingScoringConfigurationResponse | None:
    if response.status_code == 200:
        response_200 = UpdateMatchmakingScoringConfigurationResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[UpdateMatchmakingScoringConfigurationResponse]:
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
    body: UpdateMatchmakingScoringConfigurationRequest
    | UpdateMatchmakingScoringConfigurationRequest
    | UpdateMatchmakingScoringConfigurationRequest
    | UpdateMatchmakingScoringConfigurationRequest
    | Unset = UNSET,
) -> Response[UpdateMatchmakingScoringConfigurationResponse]:
    """Updates a matchmaking scoring configuration.

    Args:
        scoring_configuration_id (str):
        body (UpdateMatchmakingScoringConfigurationRequest | Unset): Request to update a custom
            matchmaking signal.
        body (UpdateMatchmakingScoringConfigurationRequest | Unset): Request to update a custom
            matchmaking signal.
        body (UpdateMatchmakingScoringConfigurationRequest | Unset): Request to update a custom
            matchmaking signal.
        body (UpdateMatchmakingScoringConfigurationRequest | Unset): Request to update a custom
            matchmaking signal.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateMatchmakingScoringConfigurationResponse]
    """

    kwargs = _get_kwargs(
        scoring_configuration_id=scoring_configuration_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    scoring_configuration_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateMatchmakingScoringConfigurationRequest
    | UpdateMatchmakingScoringConfigurationRequest
    | UpdateMatchmakingScoringConfigurationRequest
    | UpdateMatchmakingScoringConfigurationRequest
    | Unset = UNSET,
) -> UpdateMatchmakingScoringConfigurationResponse | None:
    """Updates a matchmaking scoring configuration.

    Args:
        scoring_configuration_id (str):
        body (UpdateMatchmakingScoringConfigurationRequest | Unset): Request to update a custom
            matchmaking signal.
        body (UpdateMatchmakingScoringConfigurationRequest | Unset): Request to update a custom
            matchmaking signal.
        body (UpdateMatchmakingScoringConfigurationRequest | Unset): Request to update a custom
            matchmaking signal.
        body (UpdateMatchmakingScoringConfigurationRequest | Unset): Request to update a custom
            matchmaking signal.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateMatchmakingScoringConfigurationResponse
    """

    return sync_detailed(
        scoring_configuration_id=scoring_configuration_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    scoring_configuration_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateMatchmakingScoringConfigurationRequest
    | UpdateMatchmakingScoringConfigurationRequest
    | UpdateMatchmakingScoringConfigurationRequest
    | UpdateMatchmakingScoringConfigurationRequest
    | Unset = UNSET,
) -> Response[UpdateMatchmakingScoringConfigurationResponse]:
    """Updates a matchmaking scoring configuration.

    Args:
        scoring_configuration_id (str):
        body (UpdateMatchmakingScoringConfigurationRequest | Unset): Request to update a custom
            matchmaking signal.
        body (UpdateMatchmakingScoringConfigurationRequest | Unset): Request to update a custom
            matchmaking signal.
        body (UpdateMatchmakingScoringConfigurationRequest | Unset): Request to update a custom
            matchmaking signal.
        body (UpdateMatchmakingScoringConfigurationRequest | Unset): Request to update a custom
            matchmaking signal.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateMatchmakingScoringConfigurationResponse]
    """

    kwargs = _get_kwargs(
        scoring_configuration_id=scoring_configuration_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    scoring_configuration_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateMatchmakingScoringConfigurationRequest
    | UpdateMatchmakingScoringConfigurationRequest
    | UpdateMatchmakingScoringConfigurationRequest
    | UpdateMatchmakingScoringConfigurationRequest
    | Unset = UNSET,
) -> UpdateMatchmakingScoringConfigurationResponse | None:
    """Updates a matchmaking scoring configuration.

    Args:
        scoring_configuration_id (str):
        body (UpdateMatchmakingScoringConfigurationRequest | Unset): Request to update a custom
            matchmaking signal.
        body (UpdateMatchmakingScoringConfigurationRequest | Unset): Request to update a custom
            matchmaking signal.
        body (UpdateMatchmakingScoringConfigurationRequest | Unset): Request to update a custom
            matchmaking signal.
        body (UpdateMatchmakingScoringConfigurationRequest | Unset): Request to update a custom
            matchmaking signal.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateMatchmakingScoringConfigurationResponse
    """

    return (
        await asyncio_detailed(
            scoring_configuration_id=scoring_configuration_id,
            client=client,
            body=body,
        )
    ).parsed
