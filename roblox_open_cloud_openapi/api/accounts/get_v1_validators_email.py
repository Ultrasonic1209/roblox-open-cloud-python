from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_authentication_api_models_email_validation_response import (
    RobloxAuthenticationApiModelsEmailValidationResponse,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    email: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["Email"] = email

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://auth.roblox.com/v1/validators/email",
        "params": params,
        "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
        "openapi-id": "get_v1_validators_email",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> RobloxAuthenticationApiModelsEmailValidationResponse | None:
    if response.status_code == 200:
        response_200 = RobloxAuthenticationApiModelsEmailValidationResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[RobloxAuthenticationApiModelsEmailValidationResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    email: str,
) -> Response[RobloxAuthenticationApiModelsEmailValidationResponse]:
    """Tries to check if an email is valid

    Args:
        email (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RobloxAuthenticationApiModelsEmailValidationResponse]
    """

    kwargs = _get_kwargs(
        email=email,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    email: str,
) -> RobloxAuthenticationApiModelsEmailValidationResponse | None:
    """Tries to check if an email is valid

    Args:
        email (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RobloxAuthenticationApiModelsEmailValidationResponse
    """

    return sync_detailed(
        client=client,
        email=email,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    email: str,
) -> Response[RobloxAuthenticationApiModelsEmailValidationResponse]:
    """Tries to check if an email is valid

    Args:
        email (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RobloxAuthenticationApiModelsEmailValidationResponse]
    """

    kwargs = _get_kwargs(
        email=email,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    email: str,
) -> RobloxAuthenticationApiModelsEmailValidationResponse | None:
    """Tries to check if an email is valid

    Args:
        email (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RobloxAuthenticationApiModelsEmailValidationResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            email=email,
        )
    ).parsed
