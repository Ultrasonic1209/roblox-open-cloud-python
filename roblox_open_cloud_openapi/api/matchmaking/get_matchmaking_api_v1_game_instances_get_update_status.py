from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_update_status_response import GetUpdateStatusResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    universe_id: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["universeId"] = universe_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/matchmaking-api/v1/game-instances/get-update-status",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> GetUpdateStatusResponse | None:
    if response.status_code == 200:
        response_200 = GetUpdateStatusResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[GetUpdateStatusResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    universe_id: int | Unset = UNSET,
) -> Response[GetUpdateStatusResponse]:
    """Get the rollout status of an update

    Args:
        universe_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUpdateStatusResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    universe_id: int | Unset = UNSET,
) -> GetUpdateStatusResponse | None:
    """Get the rollout status of an update

    Args:
        universe_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUpdateStatusResponse
    """

    return sync_detailed(
        client=client,
        universe_id=universe_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    universe_id: int | Unset = UNSET,
) -> Response[GetUpdateStatusResponse]:
    """Get the rollout status of an update

    Args:
        universe_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUpdateStatusResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    universe_id: int | Unset = UNSET,
) -> GetUpdateStatusResponse | None:
    """Get the rollout status of an update

    Args:
        universe_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUpdateStatusResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            universe_id=universe_id,
        )
    ).parsed
