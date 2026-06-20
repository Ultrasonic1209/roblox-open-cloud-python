from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_authentication_api_models_request_external_login_request import (
    RobloxAuthenticationApiModelsRequestExternalLoginRequest,
)
from ...models.roblox_authentication_api_models_response_external_identity_gateway_external_login_response import (
    RobloxAuthenticationApiModelsResponseExternalIdentityGatewayExternalLoginResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: RobloxAuthenticationApiModelsRequestExternalLoginRequest
    | RobloxAuthenticationApiModelsRequestExternalLoginRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "https://auth.roblox.com/v1/external/login",
        "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
        "openapi-id": "post_v1_external_login",
    }

    if isinstance(body, RobloxAuthenticationApiModelsRequestExternalLoginRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxAuthenticationApiModelsRequestExternalLoginRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxAuthenticationApiModelsResponseExternalIdentityGatewayExternalLoginResponse | None:
    if response.status_code == 200:
        response_200 = RobloxAuthenticationApiModelsResponseExternalIdentityGatewayExternalLoginResponse.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if response.status_code == 501:
        response_501 = cast(Any, None)
        return response_501

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxAuthenticationApiModelsResponseExternalIdentityGatewayExternalLoginResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxAuthenticationApiModelsRequestExternalLoginRequest
    | RobloxAuthenticationApiModelsRequestExternalLoginRequest
    | Unset = UNSET,
) -> Response[Any | RobloxAuthenticationApiModelsResponseExternalIdentityGatewayExternalLoginResponse]:
    """Logs in a user to Roblox based on the user's authenticated external provider session

    Args:
        body (RobloxAuthenticationApiModelsRequestExternalLoginRequest):
        body (RobloxAuthenticationApiModelsRequestExternalLoginRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxAuthenticationApiModelsResponseExternalIdentityGatewayExternalLoginResponse]
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
    body: RobloxAuthenticationApiModelsRequestExternalLoginRequest
    | RobloxAuthenticationApiModelsRequestExternalLoginRequest
    | Unset = UNSET,
) -> Any | RobloxAuthenticationApiModelsResponseExternalIdentityGatewayExternalLoginResponse | None:
    """Logs in a user to Roblox based on the user's authenticated external provider session

    Args:
        body (RobloxAuthenticationApiModelsRequestExternalLoginRequest):
        body (RobloxAuthenticationApiModelsRequestExternalLoginRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxAuthenticationApiModelsResponseExternalIdentityGatewayExternalLoginResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxAuthenticationApiModelsRequestExternalLoginRequest
    | RobloxAuthenticationApiModelsRequestExternalLoginRequest
    | Unset = UNSET,
) -> Response[Any | RobloxAuthenticationApiModelsResponseExternalIdentityGatewayExternalLoginResponse]:
    """Logs in a user to Roblox based on the user's authenticated external provider session

    Args:
        body (RobloxAuthenticationApiModelsRequestExternalLoginRequest):
        body (RobloxAuthenticationApiModelsRequestExternalLoginRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxAuthenticationApiModelsResponseExternalIdentityGatewayExternalLoginResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RobloxAuthenticationApiModelsRequestExternalLoginRequest
    | RobloxAuthenticationApiModelsRequestExternalLoginRequest
    | Unset = UNSET,
) -> Any | RobloxAuthenticationApiModelsResponseExternalIdentityGatewayExternalLoginResponse | None:
    """Logs in a user to Roblox based on the user's authenticated external provider session

    Args:
        body (RobloxAuthenticationApiModelsRequestExternalLoginRequest):
        body (RobloxAuthenticationApiModelsRequestExternalLoginRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxAuthenticationApiModelsResponseExternalIdentityGatewayExternalLoginResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
