from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_custom_matchmaking_signal_request import UpdateCustomMatchmakingSignalRequest
from ...models.update_custom_matchmaking_signal_response import UpdateCustomMatchmakingSignalResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    scoring_configuration_id: str,
    signal_name: str,
    *,
    body: UpdateCustomMatchmakingSignalRequest
    | UpdateCustomMatchmakingSignalRequest
    | UpdateCustomMatchmakingSignalRequest
    | UpdateCustomMatchmakingSignalRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/matchmaking-api/v1/matchmaking/scoring-configuration/{scoring_configuration_id}/signals/{signal_name}".format(
            scoring_configuration_id=quote(str(scoring_configuration_id), safe=""),
            signal_name=quote(str(signal_name), safe=""),
        ),
        "openapi-extensions": {
            "x-roblox-stability": "BETA",
            "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
        },
        "openapi-id": "patch_matchmaking-api_v1_matchmaking_scoring-configuration_scoringConfigurationId_signals_signalName",
    }

    if isinstance(body, UpdateCustomMatchmakingSignalRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, UpdateCustomMatchmakingSignalRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, UpdateCustomMatchmakingSignalRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"
    if isinstance(body, UpdateCustomMatchmakingSignalRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> UpdateCustomMatchmakingSignalResponse | None:
    if response.status_code == 200:
        response_200 = UpdateCustomMatchmakingSignalResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[UpdateCustomMatchmakingSignalResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    scoring_configuration_id: str,
    signal_name: str,
    *,
    client: AuthenticatedClient,
    body: UpdateCustomMatchmakingSignalRequest
    | UpdateCustomMatchmakingSignalRequest
    | UpdateCustomMatchmakingSignalRequest
    | UpdateCustomMatchmakingSignalRequest
    | Unset = UNSET,
) -> Response[UpdateCustomMatchmakingSignalResponse]:
    """Updates a matchmaking scoring configuration signal.

    Args:
        scoring_configuration_id (str):
        signal_name (str):
        body (UpdateCustomMatchmakingSignalRequest | Unset): Request to update a custom
            matchmaking signal.
        body (UpdateCustomMatchmakingSignalRequest | Unset): Request to update a custom
            matchmaking signal.
        body (UpdateCustomMatchmakingSignalRequest | Unset): Request to update a custom
            matchmaking signal.
        body (UpdateCustomMatchmakingSignalRequest | Unset): Request to update a custom
            matchmaking signal.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateCustomMatchmakingSignalResponse]
    """

    kwargs = _get_kwargs(
        scoring_configuration_id=scoring_configuration_id,
        signal_name=signal_name,
        body=body,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    scoring_configuration_id: str,
    signal_name: str,
    *,
    client: AuthenticatedClient,
    body: UpdateCustomMatchmakingSignalRequest
    | UpdateCustomMatchmakingSignalRequest
    | UpdateCustomMatchmakingSignalRequest
    | UpdateCustomMatchmakingSignalRequest
    | Unset = UNSET,
) -> UpdateCustomMatchmakingSignalResponse | None:
    """Updates a matchmaking scoring configuration signal.

    Args:
        scoring_configuration_id (str):
        signal_name (str):
        body (UpdateCustomMatchmakingSignalRequest | Unset): Request to update a custom
            matchmaking signal.
        body (UpdateCustomMatchmakingSignalRequest | Unset): Request to update a custom
            matchmaking signal.
        body (UpdateCustomMatchmakingSignalRequest | Unset): Request to update a custom
            matchmaking signal.
        body (UpdateCustomMatchmakingSignalRequest | Unset): Request to update a custom
            matchmaking signal.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateCustomMatchmakingSignalResponse
    """

    return sync_detailed(
        scoring_configuration_id=scoring_configuration_id,
        signal_name=signal_name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    scoring_configuration_id: str,
    signal_name: str,
    *,
    client: AuthenticatedClient,
    body: UpdateCustomMatchmakingSignalRequest
    | UpdateCustomMatchmakingSignalRequest
    | UpdateCustomMatchmakingSignalRequest
    | UpdateCustomMatchmakingSignalRequest
    | Unset = UNSET,
) -> Response[UpdateCustomMatchmakingSignalResponse]:
    """Updates a matchmaking scoring configuration signal.

    Args:
        scoring_configuration_id (str):
        signal_name (str):
        body (UpdateCustomMatchmakingSignalRequest | Unset): Request to update a custom
            matchmaking signal.
        body (UpdateCustomMatchmakingSignalRequest | Unset): Request to update a custom
            matchmaking signal.
        body (UpdateCustomMatchmakingSignalRequest | Unset): Request to update a custom
            matchmaking signal.
        body (UpdateCustomMatchmakingSignalRequest | Unset): Request to update a custom
            matchmaking signal.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateCustomMatchmakingSignalResponse]
    """

    kwargs = _get_kwargs(
        scoring_configuration_id=scoring_configuration_id,
        signal_name=signal_name,
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    scoring_configuration_id: str,
    signal_name: str,
    *,
    client: AuthenticatedClient,
    body: UpdateCustomMatchmakingSignalRequest
    | UpdateCustomMatchmakingSignalRequest
    | UpdateCustomMatchmakingSignalRequest
    | UpdateCustomMatchmakingSignalRequest
    | Unset = UNSET,
) -> UpdateCustomMatchmakingSignalResponse | None:
    """Updates a matchmaking scoring configuration signal.

    Args:
        scoring_configuration_id (str):
        signal_name (str):
        body (UpdateCustomMatchmakingSignalRequest | Unset): Request to update a custom
            matchmaking signal.
        body (UpdateCustomMatchmakingSignalRequest | Unset): Request to update a custom
            matchmaking signal.
        body (UpdateCustomMatchmakingSignalRequest | Unset): Request to update a custom
            matchmaking signal.
        body (UpdateCustomMatchmakingSignalRequest | Unset): Request to update a custom
            matchmaking signal.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateCustomMatchmakingSignalResponse
    """

    return (
        await asyncio_detailed(
            scoring_configuration_id=scoring_configuration_id,
            signal_name=signal_name,
            client=client,
            body=body,
        )
    ).parsed
