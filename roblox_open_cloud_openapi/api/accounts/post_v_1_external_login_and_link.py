from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_authentication_api_models_login_response import RobloxAuthenticationApiModelsLoginResponse
from ...models.roblox_authentication_api_models_request_external_login_and_link_request import (
    RobloxAuthenticationApiModelsRequestExternalLoginAndLinkRequest,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: RobloxAuthenticationApiModelsRequestExternalLoginAndLinkRequest
    | RobloxAuthenticationApiModelsRequestExternalLoginAndLinkRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "https://auth.roblox.com/v1/external/loginAndLink",
        "extensions": {
            "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
            "openapi-id": "post_v1_external_loginAndLink",
        },
    }

    if isinstance(body, RobloxAuthenticationApiModelsRequestExternalLoginAndLinkRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxAuthenticationApiModelsRequestExternalLoginAndLinkRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxAuthenticationApiModelsLoginResponse | None:
    if response.status_code == 200:
        response_200 = RobloxAuthenticationApiModelsLoginResponse.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxAuthenticationApiModelsLoginResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxAuthenticationApiModelsRequestExternalLoginAndLinkRequest
    | RobloxAuthenticationApiModelsRequestExternalLoginAndLinkRequest
    | Unset = UNSET,
) -> Response[Any | RobloxAuthenticationApiModelsLoginResponse]:
    """Deprecated endpoint
    Logins in a user to Roblox, then links the Roblox account to the external provider ID

    Args:
        body (RobloxAuthenticationApiModelsRequestExternalLoginAndLinkRequest):
        body (RobloxAuthenticationApiModelsRequestExternalLoginAndLinkRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxAuthenticationApiModelsLoginResponse]
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
    body: RobloxAuthenticationApiModelsRequestExternalLoginAndLinkRequest
    | RobloxAuthenticationApiModelsRequestExternalLoginAndLinkRequest
    | Unset = UNSET,
) -> Any | RobloxAuthenticationApiModelsLoginResponse | None:
    """Deprecated endpoint
    Logins in a user to Roblox, then links the Roblox account to the external provider ID

    Args:
        body (RobloxAuthenticationApiModelsRequestExternalLoginAndLinkRequest):
        body (RobloxAuthenticationApiModelsRequestExternalLoginAndLinkRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxAuthenticationApiModelsLoginResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxAuthenticationApiModelsRequestExternalLoginAndLinkRequest
    | RobloxAuthenticationApiModelsRequestExternalLoginAndLinkRequest
    | Unset = UNSET,
) -> Response[Any | RobloxAuthenticationApiModelsLoginResponse]:
    """Deprecated endpoint
    Logins in a user to Roblox, then links the Roblox account to the external provider ID

    Args:
        body (RobloxAuthenticationApiModelsRequestExternalLoginAndLinkRequest):
        body (RobloxAuthenticationApiModelsRequestExternalLoginAndLinkRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxAuthenticationApiModelsLoginResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RobloxAuthenticationApiModelsRequestExternalLoginAndLinkRequest
    | RobloxAuthenticationApiModelsRequestExternalLoginAndLinkRequest
    | Unset = UNSET,
) -> Any | RobloxAuthenticationApiModelsLoginResponse | None:
    """Deprecated endpoint
    Logins in a user to Roblox, then links the Roblox account to the external provider ID

    Args:
        body (RobloxAuthenticationApiModelsRequestExternalLoginAndLinkRequest):
        body (RobloxAuthenticationApiModelsRequestExternalLoginAndLinkRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxAuthenticationApiModelsLoginResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
