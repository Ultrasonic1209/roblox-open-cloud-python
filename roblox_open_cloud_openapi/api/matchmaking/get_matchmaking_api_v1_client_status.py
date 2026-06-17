from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.client_status_get_request import ClientStatusGetRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: ClientStatusGetRequest
    | ClientStatusGetRequest
    | ClientStatusGetRequest
    | ClientStatusGetRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/matchmaking-api/v1/client-status",
        "openapi-extensions": {
            "x-roblox-stability": "BETA",
            "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
        },
        "openapi-id": "get_matchmaking-api_v1_client-status",
    }

    if isinstance(body, ClientStatusGetRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, ClientStatusGetRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, ClientStatusGetRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"
    if isinstance(body, ClientStatusGetRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Any | None:
    if response.status_code == 200:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ClientStatusGetRequest
    | ClientStatusGetRequest
    | ClientStatusGetRequest
    | ClientStatusGetRequest
    | Unset = UNSET,
) -> Response[Any]:
    """Get the client-status

    Args:
        body (ClientStatusGetRequest | Unset): Get Client Status request.
        body (ClientStatusGetRequest | Unset): Get Client Status request.
        body (ClientStatusGetRequest | Unset): Get Client Status request.
        body (ClientStatusGetRequest | Unset): Get Client Status request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ClientStatusGetRequest
    | ClientStatusGetRequest
    | ClientStatusGetRequest
    | ClientStatusGetRequest
    | Unset = UNSET,
) -> Response[Any]:
    """Get the client-status

    Args:
        body (ClientStatusGetRequest | Unset): Get Client Status request.
        body (ClientStatusGetRequest | Unset): Get Client Status request.
        body (ClientStatusGetRequest | Unset): Get Client Status request.
        body (ClientStatusGetRequest | Unset): Get Client Status request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)
