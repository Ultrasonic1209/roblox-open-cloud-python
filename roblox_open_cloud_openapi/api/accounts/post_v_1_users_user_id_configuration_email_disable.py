from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_two_step_verification_api_disable_two_step_verification_request import (
    RobloxTwoStepVerificationApiDisableTwoStepVerificationRequest,
)
from ...models.roblox_web_web_api_api_empty_response_model import RobloxWebWebAPIApiEmptyResponseModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: int,
    *,
    body: RobloxTwoStepVerificationApiDisableTwoStepVerificationRequest
    | RobloxTwoStepVerificationApiDisableTwoStepVerificationRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "https://twostepverification.roblox.com/v1/users/{user_id}/configuration/email/disable".format(
            user_id=quote(str(user_id), safe=""),
        ),
        "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
        "openapi-id": "post_v1_users_userId_configuration_email_disable",
    }

    if isinstance(body, RobloxTwoStepVerificationApiDisableTwoStepVerificationRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxTwoStepVerificationApiDisableTwoStepVerificationRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxWebWebAPIApiEmptyResponseModel | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIApiEmptyResponseModel.from_dict(response.json())

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

    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429

    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxWebWebAPIApiEmptyResponseModel]:
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
    body: RobloxTwoStepVerificationApiDisableTwoStepVerificationRequest
    | RobloxTwoStepVerificationApiDisableTwoStepVerificationRequest
    | Unset = UNSET,
) -> Response[Any | RobloxWebWebAPIApiEmptyResponseModel]:
    """Disables two step verification via email for the specified user.

    Args:
        user_id (int):
        body (RobloxTwoStepVerificationApiDisableTwoStepVerificationRequest): Request information
            needed to disable two step verification.
        body (RobloxTwoStepVerificationApiDisableTwoStepVerificationRequest): Request information
            needed to disable two step verification.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIApiEmptyResponseModel]
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
    body: RobloxTwoStepVerificationApiDisableTwoStepVerificationRequest
    | RobloxTwoStepVerificationApiDisableTwoStepVerificationRequest
    | Unset = UNSET,
) -> Any | RobloxWebWebAPIApiEmptyResponseModel | None:
    """Disables two step verification via email for the specified user.

    Args:
        user_id (int):
        body (RobloxTwoStepVerificationApiDisableTwoStepVerificationRequest): Request information
            needed to disable two step verification.
        body (RobloxTwoStepVerificationApiDisableTwoStepVerificationRequest): Request information
            needed to disable two step verification.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIApiEmptyResponseModel
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
    body: RobloxTwoStepVerificationApiDisableTwoStepVerificationRequest
    | RobloxTwoStepVerificationApiDisableTwoStepVerificationRequest
    | Unset = UNSET,
) -> Response[Any | RobloxWebWebAPIApiEmptyResponseModel]:
    """Disables two step verification via email for the specified user.

    Args:
        user_id (int):
        body (RobloxTwoStepVerificationApiDisableTwoStepVerificationRequest): Request information
            needed to disable two step verification.
        body (RobloxTwoStepVerificationApiDisableTwoStepVerificationRequest): Request information
            needed to disable two step verification.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIApiEmptyResponseModel]
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
    body: RobloxTwoStepVerificationApiDisableTwoStepVerificationRequest
    | RobloxTwoStepVerificationApiDisableTwoStepVerificationRequest
    | Unset = UNSET,
) -> Any | RobloxWebWebAPIApiEmptyResponseModel | None:
    """Disables two step verification via email for the specified user.

    Args:
        user_id (int):
        body (RobloxTwoStepVerificationApiDisableTwoStepVerificationRequest): Request information
            needed to disable two step verification.
        body (RobloxTwoStepVerificationApiDisableTwoStepVerificationRequest): Request information
            needed to disable two step verification.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIApiEmptyResponseModel
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            body=body,
        )
    ).parsed
