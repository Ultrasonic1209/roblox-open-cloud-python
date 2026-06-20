from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_authentication_api_models_request_external_signup_request import (
    RobloxAuthenticationApiModelsRequestExternalSignupRequest,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: RobloxAuthenticationApiModelsRequestExternalSignupRequest
    | RobloxAuthenticationApiModelsRequestExternalSignupRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "https://auth.roblox.com/v1/external/signup",
        "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
        "openapi-id": "post_v1_external_signup",
    }

    if isinstance(body, RobloxAuthenticationApiModelsRequestExternalSignupRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxAuthenticationApiModelsRequestExternalSignupRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx2.Response) -> Any | None:
    if response.status_code == 200:
        return None

    if response.status_code == 403:
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
    body: RobloxAuthenticationApiModelsRequestExternalSignupRequest
    | RobloxAuthenticationApiModelsRequestExternalSignupRequest
    | Unset = UNSET,
) -> Response[Any]:
    """Signs a user up for Roblox and links the account to the authenticated external provider ID

    Args:
        body (RobloxAuthenticationApiModelsRequestExternalSignupRequest):
        body (RobloxAuthenticationApiModelsRequestExternalSignupRequest):

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
    body: RobloxAuthenticationApiModelsRequestExternalSignupRequest
    | RobloxAuthenticationApiModelsRequestExternalSignupRequest
    | Unset = UNSET,
) -> Response[Any]:
    """Signs a user up for Roblox and links the account to the authenticated external provider ID

    Args:
        body (RobloxAuthenticationApiModelsRequestExternalSignupRequest):
        body (RobloxAuthenticationApiModelsRequestExternalSignupRequest):

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
