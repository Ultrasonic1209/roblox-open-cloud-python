from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_two_step_verification_api_verify_code_request import RobloxTwoStepVerificationApiVerifyCodeRequest
from ...models.roblox_two_step_verification_api_verify_code_response import (
    RobloxTwoStepVerificationApiVerifyCodeResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: int,
    *,
    body: RobloxTwoStepVerificationApiVerifyCodeRequest | RobloxTwoStepVerificationApiVerifyCodeRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "https://twostepverification.roblox.com/v1/users/{user_id}/challenges/security-key/verify-finish".format(
            user_id=quote(str(user_id), safe=""),
        ),
        "extensions": {
            "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
            "openapi-id": "post_v1_users_userId_challenges_security-key_verify-finish",
        },
    }

    if isinstance(body, RobloxTwoStepVerificationApiVerifyCodeRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxTwoStepVerificationApiVerifyCodeRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxTwoStepVerificationApiVerifyCodeResponse | None:
    if response.status_code == 200:
        response_200 = RobloxTwoStepVerificationApiVerifyCodeResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxTwoStepVerificationApiVerifyCodeResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxTwoStepVerificationApiVerifyCodeRequest | RobloxTwoStepVerificationApiVerifyCodeRequest | Unset = UNSET,
) -> Response[Any | RobloxTwoStepVerificationApiVerifyCodeResponse]:
    """Validates the assertion data returned by the security key.

    Args:
        user_id (int):
        body (RobloxTwoStepVerificationApiVerifyCodeRequest): Request parameters for verifying a
            two step verification code.
        body (RobloxTwoStepVerificationApiVerifyCodeRequest): Request parameters for verifying a
            two step verification code.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxTwoStepVerificationApiVerifyCodeResponse]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        body=body,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxTwoStepVerificationApiVerifyCodeRequest | RobloxTwoStepVerificationApiVerifyCodeRequest | Unset = UNSET,
) -> Any | RobloxTwoStepVerificationApiVerifyCodeResponse | None:
    """Validates the assertion data returned by the security key.

    Args:
        user_id (int):
        body (RobloxTwoStepVerificationApiVerifyCodeRequest): Request parameters for verifying a
            two step verification code.
        body (RobloxTwoStepVerificationApiVerifyCodeRequest): Request parameters for verifying a
            two step verification code.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxTwoStepVerificationApiVerifyCodeResponse
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    user_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxTwoStepVerificationApiVerifyCodeRequest | RobloxTwoStepVerificationApiVerifyCodeRequest | Unset = UNSET,
) -> Response[Any | RobloxTwoStepVerificationApiVerifyCodeResponse]:
    """Validates the assertion data returned by the security key.

    Args:
        user_id (int):
        body (RobloxTwoStepVerificationApiVerifyCodeRequest): Request parameters for verifying a
            two step verification code.
        body (RobloxTwoStepVerificationApiVerifyCodeRequest): Request parameters for verifying a
            two step verification code.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxTwoStepVerificationApiVerifyCodeResponse]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: int,
    *,
    client: AuthenticatedClient,
    body: RobloxTwoStepVerificationApiVerifyCodeRequest | RobloxTwoStepVerificationApiVerifyCodeRequest | Unset = UNSET,
) -> Any | RobloxTwoStepVerificationApiVerifyCodeResponse | None:
    """Validates the assertion data returned by the security key.

    Args:
        user_id (int):
        body (RobloxTwoStepVerificationApiVerifyCodeRequest): Request parameters for verifying a
            two step verification code.
        body (RobloxTwoStepVerificationApiVerifyCodeRequest): Request parameters for verifying a
            two step verification code.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxTwoStepVerificationApiVerifyCodeResponse
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            body=body,
        )
    ).parsed
