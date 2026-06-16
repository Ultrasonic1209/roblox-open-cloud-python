from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_custom_matchmaking_signal_response import DeleteCustomMatchmakingSignalResponse
from ...types import Response


def _get_kwargs(
    scoring_configuration_id: str,
    signal_name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/matchmaking-api/v1/matchmaking/scoring-configuration/{scoring_configuration_id}/signals/{signal_name}".format(
            scoring_configuration_id=quote(str(scoring_configuration_id), safe=""),
            signal_name=quote(str(signal_name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DeleteCustomMatchmakingSignalResponse | None:
    if response.status_code == 200:
        response_200 = DeleteCustomMatchmakingSignalResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DeleteCustomMatchmakingSignalResponse]:
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
) -> Response[DeleteCustomMatchmakingSignalResponse]:
    """Deletes a matchmaking scoring configuration custom signal.

    Args:
        scoring_configuration_id (str):
        signal_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteCustomMatchmakingSignalResponse]
    """

    kwargs = _get_kwargs(
        scoring_configuration_id=scoring_configuration_id,
        signal_name=signal_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    scoring_configuration_id: str,
    signal_name: str,
    *,
    client: AuthenticatedClient,
) -> DeleteCustomMatchmakingSignalResponse | None:
    """Deletes a matchmaking scoring configuration custom signal.

    Args:
        scoring_configuration_id (str):
        signal_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteCustomMatchmakingSignalResponse
    """

    return sync_detailed(
        scoring_configuration_id=scoring_configuration_id,
        signal_name=signal_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    scoring_configuration_id: str,
    signal_name: str,
    *,
    client: AuthenticatedClient,
) -> Response[DeleteCustomMatchmakingSignalResponse]:
    """Deletes a matchmaking scoring configuration custom signal.

    Args:
        scoring_configuration_id (str):
        signal_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteCustomMatchmakingSignalResponse]
    """

    kwargs = _get_kwargs(
        scoring_configuration_id=scoring_configuration_id,
        signal_name=signal_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    scoring_configuration_id: str,
    signal_name: str,
    *,
    client: AuthenticatedClient,
) -> DeleteCustomMatchmakingSignalResponse | None:
    """Deletes a matchmaking scoring configuration custom signal.

    Args:
        scoring_configuration_id (str):
        signal_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteCustomMatchmakingSignalResponse
    """

    return (
        await asyncio_detailed(
            scoring_configuration_id=scoring_configuration_id,
            signal_name=signal_name,
            client=client,
        )
    ).parsed
