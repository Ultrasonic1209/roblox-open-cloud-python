from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_authentication_api_models_username_validation_request import (
    RobloxAuthenticationApiModelsUsernameValidationRequest,
)
from ...models.roblox_authentication_api_models_username_validation_response import (
    RobloxAuthenticationApiModelsUsernameValidationResponse,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: RobloxAuthenticationApiModelsUsernameValidationRequest
    | RobloxAuthenticationApiModelsUsernameValidationRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/usernames/validate",
    }

    if isinstance(body, RobloxAuthenticationApiModelsUsernameValidationRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxAuthenticationApiModelsUsernameValidationRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxAuthenticationApiModelsUsernameValidationResponse | None:
    if response.status_code == 200:
        response_200 = RobloxAuthenticationApiModelsUsernameValidationResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RobloxAuthenticationApiModelsUsernameValidationResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxAuthenticationApiModelsUsernameValidationRequest
    | RobloxAuthenticationApiModelsUsernameValidationRequest
    | Unset = UNSET,
) -> Response[Any | RobloxAuthenticationApiModelsUsernameValidationResponse]:
    """Checks if a username is valid.

    Args:
        body (RobloxAuthenticationApiModelsUsernameValidationRequest):
        body (RobloxAuthenticationApiModelsUsernameValidationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxAuthenticationApiModelsUsernameValidationResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: RobloxAuthenticationApiModelsUsernameValidationRequest
    | RobloxAuthenticationApiModelsUsernameValidationRequest
    | Unset = UNSET,
) -> Any | RobloxAuthenticationApiModelsUsernameValidationResponse | None:
    """Checks if a username is valid.

    Args:
        body (RobloxAuthenticationApiModelsUsernameValidationRequest):
        body (RobloxAuthenticationApiModelsUsernameValidationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxAuthenticationApiModelsUsernameValidationResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxAuthenticationApiModelsUsernameValidationRequest
    | RobloxAuthenticationApiModelsUsernameValidationRequest
    | Unset = UNSET,
) -> Response[Any | RobloxAuthenticationApiModelsUsernameValidationResponse]:
    """Checks if a username is valid.

    Args:
        body (RobloxAuthenticationApiModelsUsernameValidationRequest):
        body (RobloxAuthenticationApiModelsUsernameValidationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxAuthenticationApiModelsUsernameValidationResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RobloxAuthenticationApiModelsUsernameValidationRequest
    | RobloxAuthenticationApiModelsUsernameValidationRequest
    | Unset = UNSET,
) -> Any | RobloxAuthenticationApiModelsUsernameValidationResponse | None:
    """Checks if a username is valid.

    Args:
        body (RobloxAuthenticationApiModelsUsernameValidationRequest):
        body (RobloxAuthenticationApiModelsUsernameValidationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxAuthenticationApiModelsUsernameValidationResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
