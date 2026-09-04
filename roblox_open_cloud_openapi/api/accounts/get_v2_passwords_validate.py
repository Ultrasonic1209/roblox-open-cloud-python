from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_authentication_api_models_password_validation_response import (
    RobloxAuthenticationApiModelsPasswordValidationResponse,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    username: str,
    password: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["Username"] = username

    params["Password"] = password

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://auth.roblox.com/v2/passwords/validate",
        "params": params,
        "extensions": {
            "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
            "openapi-id": "get_v2_passwords_validate",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxAuthenticationApiModelsPasswordValidationResponse | None:
    if response.status_code == 200:
        response_200 = RobloxAuthenticationApiModelsPasswordValidationResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxAuthenticationApiModelsPasswordValidationResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    username: str,
    password: str,
) -> Response[Any | RobloxAuthenticationApiModelsPasswordValidationResponse]:
    """Endpoint for checking if a password is valid.

    Args:
        username (str):
        password (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxAuthenticationApiModelsPasswordValidationResponse]
    """

    kwargs = _get_kwargs(
        username=username,
        password=password,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    username: str,
    password: str,
) -> Any | RobloxAuthenticationApiModelsPasswordValidationResponse | None:
    """Endpoint for checking if a password is valid.

    Args:
        username (str):
        password (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxAuthenticationApiModelsPasswordValidationResponse
    """

    return sync_detailed(
        client=client,
        username=username,
        password=password,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    username: str,
    password: str,
) -> Response[Any | RobloxAuthenticationApiModelsPasswordValidationResponse]:
    """Endpoint for checking if a password is valid.

    Args:
        username (str):
        password (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxAuthenticationApiModelsPasswordValidationResponse]
    """

    kwargs = _get_kwargs(
        username=username,
        password=password,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    username: str,
    password: str,
) -> Any | RobloxAuthenticationApiModelsPasswordValidationResponse | None:
    """Endpoint for checking if a password is valid.

    Args:
        username (str):
        password (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxAuthenticationApiModelsPasswordValidationResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            username=username,
            password=password,
        )
    ).parsed
