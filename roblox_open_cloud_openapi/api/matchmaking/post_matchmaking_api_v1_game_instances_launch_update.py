from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.launch_update_request import LaunchUpdateRequest
from ...models.launch_update_response import LaunchUpdateResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: LaunchUpdateRequest | LaunchUpdateRequest | LaunchUpdateRequest | LaunchUpdateRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/matchmaking-api/v1/game-instances/launch-update",
    }

    if isinstance(body, LaunchUpdateRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, LaunchUpdateRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, LaunchUpdateRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"
    if isinstance(body, LaunchUpdateRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> LaunchUpdateResponse | None:
    if response.status_code == 200:
        response_200 = LaunchUpdateResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[LaunchUpdateResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: LaunchUpdateRequest | LaunchUpdateRequest | LaunchUpdateRequest | LaunchUpdateRequest | Unset = UNSET,
) -> Response[LaunchUpdateResponse]:
    """Launch a game update

    Args:
        body (LaunchUpdateRequest | Unset): Launch Update Request. Contains specification for how
            update should roll out
        body (LaunchUpdateRequest | Unset): Launch Update Request. Contains specification for how
            update should roll out
        body (LaunchUpdateRequest | Unset): Launch Update Request. Contains specification for how
            update should roll out
        body (LaunchUpdateRequest | Unset): Launch Update Request. Contains specification for how
            update should roll out

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LaunchUpdateResponse]
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
    body: LaunchUpdateRequest | LaunchUpdateRequest | LaunchUpdateRequest | LaunchUpdateRequest | Unset = UNSET,
) -> LaunchUpdateResponse | None:
    """Launch a game update

    Args:
        body (LaunchUpdateRequest | Unset): Launch Update Request. Contains specification for how
            update should roll out
        body (LaunchUpdateRequest | Unset): Launch Update Request. Contains specification for how
            update should roll out
        body (LaunchUpdateRequest | Unset): Launch Update Request. Contains specification for how
            update should roll out
        body (LaunchUpdateRequest | Unset): Launch Update Request. Contains specification for how
            update should roll out

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LaunchUpdateResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: LaunchUpdateRequest | LaunchUpdateRequest | LaunchUpdateRequest | LaunchUpdateRequest | Unset = UNSET,
) -> Response[LaunchUpdateResponse]:
    """Launch a game update

    Args:
        body (LaunchUpdateRequest | Unset): Launch Update Request. Contains specification for how
            update should roll out
        body (LaunchUpdateRequest | Unset): Launch Update Request. Contains specification for how
            update should roll out
        body (LaunchUpdateRequest | Unset): Launch Update Request. Contains specification for how
            update should roll out
        body (LaunchUpdateRequest | Unset): Launch Update Request. Contains specification for how
            update should roll out

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LaunchUpdateResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: LaunchUpdateRequest | LaunchUpdateRequest | LaunchUpdateRequest | LaunchUpdateRequest | Unset = UNSET,
) -> LaunchUpdateResponse | None:
    """Launch a game update

    Args:
        body (LaunchUpdateRequest | Unset): Launch Update Request. Contains specification for how
            update should roll out
        body (LaunchUpdateRequest | Unset): Launch Update Request. Contains specification for how
            update should roll out
        body (LaunchUpdateRequest | Unset): Launch Update Request. Contains specification for how
            update should roll out
        body (LaunchUpdateRequest | Unset): Launch Update Request. Contains specification for how
            update should roll out

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LaunchUpdateResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
