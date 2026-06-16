from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v2_passwords_reset_target_type import GetV2PasswordsResetTargetType
from ...models.roblox_authentication_api_models_password_reset_metadata_response import (
    RobloxAuthenticationApiModelsPasswordResetMetadataResponse,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    target_type: GetV2PasswordsResetTargetType,
    ticket: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_target_type = target_type.value
    params["TargetType"] = json_target_type

    params["Ticket"] = ticket

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/passwords/reset",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxAuthenticationApiModelsPasswordResetMetadataResponse | None:
    if response.status_code == 200:
        response_200 = RobloxAuthenticationApiModelsPasswordResetMetadataResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RobloxAuthenticationApiModelsPasswordResetMetadataResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    target_type: GetV2PasswordsResetTargetType,
    ticket: str,
) -> Response[Any | RobloxAuthenticationApiModelsPasswordResetMetadataResponse]:
    """Gets metadata needed for the password reset view.

    Args:
        target_type (GetV2PasswordsResetTargetType):
        ticket (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxAuthenticationApiModelsPasswordResetMetadataResponse]
    """

    kwargs = _get_kwargs(
        target_type=target_type,
        ticket=ticket,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    target_type: GetV2PasswordsResetTargetType,
    ticket: str,
) -> Any | RobloxAuthenticationApiModelsPasswordResetMetadataResponse | None:
    """Gets metadata needed for the password reset view.

    Args:
        target_type (GetV2PasswordsResetTargetType):
        ticket (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxAuthenticationApiModelsPasswordResetMetadataResponse
    """

    return sync_detailed(
        client=client,
        target_type=target_type,
        ticket=ticket,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    target_type: GetV2PasswordsResetTargetType,
    ticket: str,
) -> Response[Any | RobloxAuthenticationApiModelsPasswordResetMetadataResponse]:
    """Gets metadata needed for the password reset view.

    Args:
        target_type (GetV2PasswordsResetTargetType):
        ticket (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxAuthenticationApiModelsPasswordResetMetadataResponse]
    """

    kwargs = _get_kwargs(
        target_type=target_type,
        ticket=ticket,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    target_type: GetV2PasswordsResetTargetType,
    ticket: str,
) -> Any | RobloxAuthenticationApiModelsPasswordResetMetadataResponse | None:
    """Gets metadata needed for the password reset view.

    Args:
        target_type (GetV2PasswordsResetTargetType):
        ticket (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxAuthenticationApiModelsPasswordResetMetadataResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            target_type=target_type,
            ticket=ticket,
        )
    ).parsed
