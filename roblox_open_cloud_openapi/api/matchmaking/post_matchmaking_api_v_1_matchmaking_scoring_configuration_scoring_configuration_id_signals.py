from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_custom_matchmaking_signal_request import CreateCustomMatchmakingSignalRequest
from ...models.create_custom_matchmaking_signal_response import CreateCustomMatchmakingSignalResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    scoring_configuration_id: str,
    *,
    body: CreateCustomMatchmakingSignalRequest
    | CreateCustomMatchmakingSignalRequest
    | CreateCustomMatchmakingSignalRequest
    | CreateCustomMatchmakingSignalRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/matchmaking-api/v1/matchmaking/scoring-configuration/{scoring_configuration_id}/signals".format(
            scoring_configuration_id=quote(str(scoring_configuration_id), safe=""),
        ),
    }

    if isinstance(body, CreateCustomMatchmakingSignalRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, CreateCustomMatchmakingSignalRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CreateCustomMatchmakingSignalRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"
    if isinstance(body, CreateCustomMatchmakingSignalRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> CreateCustomMatchmakingSignalResponse | None:
    if response.status_code == 200:
        response_200 = CreateCustomMatchmakingSignalResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[CreateCustomMatchmakingSignalResponse]:
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
    body: CreateCustomMatchmakingSignalRequest
    | CreateCustomMatchmakingSignalRequest
    | CreateCustomMatchmakingSignalRequest
    | CreateCustomMatchmakingSignalRequest
    | Unset = UNSET,
) -> Response[CreateCustomMatchmakingSignalResponse]:
    """Creates a matchmaking scoring configuration signal.

    Args:
        scoring_configuration_id (str):
        body (CreateCustomMatchmakingSignalRequest | Unset): Request to create a custom
            matchmaking signal.
        body (CreateCustomMatchmakingSignalRequest | Unset): Request to create a custom
            matchmaking signal.
        body (CreateCustomMatchmakingSignalRequest | Unset): Request to create a custom
            matchmaking signal.
        body (CreateCustomMatchmakingSignalRequest | Unset): Request to create a custom
            matchmaking signal.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateCustomMatchmakingSignalResponse]
    """

    kwargs = _get_kwargs(
        scoring_configuration_id=scoring_configuration_id,
        body=body,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    scoring_configuration_id: str,
    *,
    client: AuthenticatedClient,
    body: CreateCustomMatchmakingSignalRequest
    | CreateCustomMatchmakingSignalRequest
    | CreateCustomMatchmakingSignalRequest
    | CreateCustomMatchmakingSignalRequest
    | Unset = UNSET,
) -> CreateCustomMatchmakingSignalResponse | None:
    """Creates a matchmaking scoring configuration signal.

    Args:
        scoring_configuration_id (str):
        body (CreateCustomMatchmakingSignalRequest | Unset): Request to create a custom
            matchmaking signal.
        body (CreateCustomMatchmakingSignalRequest | Unset): Request to create a custom
            matchmaking signal.
        body (CreateCustomMatchmakingSignalRequest | Unset): Request to create a custom
            matchmaking signal.
        body (CreateCustomMatchmakingSignalRequest | Unset): Request to create a custom
            matchmaking signal.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateCustomMatchmakingSignalResponse
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
    body: CreateCustomMatchmakingSignalRequest
    | CreateCustomMatchmakingSignalRequest
    | CreateCustomMatchmakingSignalRequest
    | CreateCustomMatchmakingSignalRequest
    | Unset = UNSET,
) -> Response[CreateCustomMatchmakingSignalResponse]:
    """Creates a matchmaking scoring configuration signal.

    Args:
        scoring_configuration_id (str):
        body (CreateCustomMatchmakingSignalRequest | Unset): Request to create a custom
            matchmaking signal.
        body (CreateCustomMatchmakingSignalRequest | Unset): Request to create a custom
            matchmaking signal.
        body (CreateCustomMatchmakingSignalRequest | Unset): Request to create a custom
            matchmaking signal.
        body (CreateCustomMatchmakingSignalRequest | Unset): Request to create a custom
            matchmaking signal.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateCustomMatchmakingSignalResponse]
    """

    kwargs = _get_kwargs(
        scoring_configuration_id=scoring_configuration_id,
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    scoring_configuration_id: str,
    *,
    client: AuthenticatedClient,
    body: CreateCustomMatchmakingSignalRequest
    | CreateCustomMatchmakingSignalRequest
    | CreateCustomMatchmakingSignalRequest
    | CreateCustomMatchmakingSignalRequest
    | Unset = UNSET,
) -> CreateCustomMatchmakingSignalResponse | None:
    """Creates a matchmaking scoring configuration signal.

    Args:
        scoring_configuration_id (str):
        body (CreateCustomMatchmakingSignalRequest | Unset): Request to create a custom
            matchmaking signal.
        body (CreateCustomMatchmakingSignalRequest | Unset): Request to create a custom
            matchmaking signal.
        body (CreateCustomMatchmakingSignalRequest | Unset): Request to create a custom
            matchmaking signal.
        body (CreateCustomMatchmakingSignalRequest | Unset): Request to create a custom
            matchmaking signal.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateCustomMatchmakingSignalResponse
    """

    return (
        await asyncio_detailed(
            scoring_configuration_id=scoring_configuration_id,
            client=client,
            body=body,
        )
    ).parsed
