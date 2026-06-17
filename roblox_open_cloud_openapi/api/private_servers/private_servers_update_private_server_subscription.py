from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.private_server_subscription_response import PrivateServerSubscriptionResponse
from ...models.private_server_update_subscription_request import PrivateServerUpdateSubscriptionRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    body: PrivateServerUpdateSubscriptionRequest
    | PrivateServerUpdateSubscriptionRequest
    | PrivateServerUpdateSubscriptionRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "https://games.roblox.com/v1/vip-servers/{id}/subscription".format(
            id=quote(str(id), safe=""),
        ),
    }

    if isinstance(body, PrivateServerUpdateSubscriptionRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PrivateServerUpdateSubscriptionRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"
    if isinstance(body, PrivateServerUpdateSubscriptionRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> PrivateServerSubscriptionResponse | None:
    if response.status_code == 200:
        response_200 = PrivateServerSubscriptionResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[PrivateServerSubscriptionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: PrivateServerUpdateSubscriptionRequest
    | PrivateServerUpdateSubscriptionRequest
    | PrivateServerUpdateSubscriptionRequest
    | Unset = UNSET,
) -> Response[PrivateServerSubscriptionResponse]:
    """
    Args:
        id (int):
        body (PrivateServerUpdateSubscriptionRequest | Unset):
        body (PrivateServerUpdateSubscriptionRequest | Unset):
        body (PrivateServerUpdateSubscriptionRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PrivateServerSubscriptionResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    body: PrivateServerUpdateSubscriptionRequest
    | PrivateServerUpdateSubscriptionRequest
    | PrivateServerUpdateSubscriptionRequest
    | Unset = UNSET,
) -> PrivateServerSubscriptionResponse | None:
    """
    Args:
        id (int):
        body (PrivateServerUpdateSubscriptionRequest | Unset):
        body (PrivateServerUpdateSubscriptionRequest | Unset):
        body (PrivateServerUpdateSubscriptionRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PrivateServerSubscriptionResponse
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: PrivateServerUpdateSubscriptionRequest
    | PrivateServerUpdateSubscriptionRequest
    | PrivateServerUpdateSubscriptionRequest
    | Unset = UNSET,
) -> Response[PrivateServerSubscriptionResponse]:
    """
    Args:
        id (int):
        body (PrivateServerUpdateSubscriptionRequest | Unset):
        body (PrivateServerUpdateSubscriptionRequest | Unset):
        body (PrivateServerUpdateSubscriptionRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PrivateServerSubscriptionResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    body: PrivateServerUpdateSubscriptionRequest
    | PrivateServerUpdateSubscriptionRequest
    | PrivateServerUpdateSubscriptionRequest
    | Unset = UNSET,
) -> PrivateServerSubscriptionResponse | None:
    """
    Args:
        id (int):
        body (PrivateServerUpdateSubscriptionRequest | Unset):
        body (PrivateServerUpdateSubscriptionRequest | Unset):
        body (PrivateServerUpdateSubscriptionRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PrivateServerSubscriptionResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
