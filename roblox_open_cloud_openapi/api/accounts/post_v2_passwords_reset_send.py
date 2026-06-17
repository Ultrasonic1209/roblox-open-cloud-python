from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_authentication_api_models_send_reset_password_request import (
    RobloxAuthenticationApiModelsSendResetPasswordRequest,
)
from ...models.roblox_authentication_api_models_send_reset_password_response import (
    RobloxAuthenticationApiModelsSendResetPasswordResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: RobloxAuthenticationApiModelsSendResetPasswordRequest
    | RobloxAuthenticationApiModelsSendResetPasswordRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "https://auth.roblox.com/v2/passwords/reset/send",
    }

    if isinstance(body, RobloxAuthenticationApiModelsSendResetPasswordRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxAuthenticationApiModelsSendResetPasswordRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxAuthenticationApiModelsSendResetPasswordResponse | None:
    if response.status_code == 200:
        response_200 = RobloxAuthenticationApiModelsSendResetPasswordResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429

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
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxAuthenticationApiModelsSendResetPasswordResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxAuthenticationApiModelsSendResetPasswordRequest
    | RobloxAuthenticationApiModelsSendResetPasswordRequest
    | Unset = UNSET,
) -> Response[Any | RobloxAuthenticationApiModelsSendResetPasswordResponse]:
    r"""Sends a password reset email or challenge to the specified target.

     Phone target must be a csv with 3 values: \"internationalPrefixNumber,nationalNumber,countryCode\"

    Args:
        body (RobloxAuthenticationApiModelsSendResetPasswordRequest):
        body (RobloxAuthenticationApiModelsSendResetPasswordRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxAuthenticationApiModelsSendResetPasswordResponse]
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
    body: RobloxAuthenticationApiModelsSendResetPasswordRequest
    | RobloxAuthenticationApiModelsSendResetPasswordRequest
    | Unset = UNSET,
) -> Any | RobloxAuthenticationApiModelsSendResetPasswordResponse | None:
    r"""Sends a password reset email or challenge to the specified target.

     Phone target must be a csv with 3 values: \"internationalPrefixNumber,nationalNumber,countryCode\"

    Args:
        body (RobloxAuthenticationApiModelsSendResetPasswordRequest):
        body (RobloxAuthenticationApiModelsSendResetPasswordRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxAuthenticationApiModelsSendResetPasswordResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxAuthenticationApiModelsSendResetPasswordRequest
    | RobloxAuthenticationApiModelsSendResetPasswordRequest
    | Unset = UNSET,
) -> Response[Any | RobloxAuthenticationApiModelsSendResetPasswordResponse]:
    r"""Sends a password reset email or challenge to the specified target.

     Phone target must be a csv with 3 values: \"internationalPrefixNumber,nationalNumber,countryCode\"

    Args:
        body (RobloxAuthenticationApiModelsSendResetPasswordRequest):
        body (RobloxAuthenticationApiModelsSendResetPasswordRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxAuthenticationApiModelsSendResetPasswordResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RobloxAuthenticationApiModelsSendResetPasswordRequest
    | RobloxAuthenticationApiModelsSendResetPasswordRequest
    | Unset = UNSET,
) -> Any | RobloxAuthenticationApiModelsSendResetPasswordResponse | None:
    r"""Sends a password reset email or challenge to the specified target.

     Phone target must be a csv with 3 values: \"internationalPrefixNumber,nationalNumber,countryCode\"

    Args:
        body (RobloxAuthenticationApiModelsSendResetPasswordRequest):
        body (RobloxAuthenticationApiModelsSendResetPasswordRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxAuthenticationApiModelsSendResetPasswordResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
