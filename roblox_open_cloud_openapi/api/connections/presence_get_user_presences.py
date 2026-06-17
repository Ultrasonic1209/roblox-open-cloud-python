from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.presence_api_error_response import PresenceApiErrorResponse
from ...models.user_presence_request import UserPresenceRequest
from ...models.user_presences_response import UserPresencesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: UserPresenceRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "https://presence.roblox.com/v1/presence/users",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> PresenceApiErrorResponse | UserPresencesResponse | None:
    if response.status_code == 200:
        response_200 = UserPresencesResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = PresenceApiErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = PresenceApiErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 429:
        response_429 = PresenceApiErrorResponse.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[PresenceApiErrorResponse | UserPresencesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: UserPresenceRequest | Unset = UNSET,
) -> Response[PresenceApiErrorResponse | UserPresencesResponse]:
    """
    Args:
        body (UserPresenceRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PresenceApiErrorResponse | UserPresencesResponse]
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
    body: UserPresenceRequest | Unset = UNSET,
) -> PresenceApiErrorResponse | UserPresencesResponse | None:
    """
    Args:
        body (UserPresenceRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PresenceApiErrorResponse | UserPresencesResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: UserPresenceRequest | Unset = UNSET,
) -> Response[PresenceApiErrorResponse | UserPresencesResponse]:
    """
    Args:
        body (UserPresenceRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PresenceApiErrorResponse | UserPresencesResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: UserPresenceRequest | Unset = UNSET,
) -> PresenceApiErrorResponse | UserPresencesResponse | None:
    """
    Args:
        body (UserPresenceRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PresenceApiErrorResponse | UserPresencesResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
