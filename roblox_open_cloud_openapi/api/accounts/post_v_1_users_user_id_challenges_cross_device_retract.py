from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_two_step_verification_api_retract_dialog_request import (
    RobloxTwoStepVerificationApiRetractDialogRequest,
)
from ...models.roblox_two_step_verification_api_retract_dialog_response import (
    RobloxTwoStepVerificationApiRetractDialogResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: int,
    *,
    body: RobloxTwoStepVerificationApiRetractDialogRequest
    | RobloxTwoStepVerificationApiRetractDialogRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "https://twostepverification.roblox.com/v1/users/{user_id}/challenges/cross-device/retract".format(
            user_id=quote(str(user_id), safe=""),
        ),
        "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
        "openapi-id": "post_v1_users_userId_challenges_cross-device_retract",
    }

    if isinstance(body, RobloxTwoStepVerificationApiRetractDialogRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxTwoStepVerificationApiRetractDialogRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxTwoStepVerificationApiRetractDialogResponse | None:
    if response.status_code == 200:
        response_200 = RobloxTwoStepVerificationApiRetractDialogResponse.from_dict(response.json())

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
) -> Response[Any | RobloxTwoStepVerificationApiRetractDialogResponse]:
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
    body: RobloxTwoStepVerificationApiRetractDialogRequest
    | RobloxTwoStepVerificationApiRetractDialogRequest
    | Unset = UNSET,
) -> Response[Any | RobloxTwoStepVerificationApiRetractDialogResponse]:
    """Reverts a user's dialog state from ACTIVE to PENDING.

    Args:
        user_id (int):
        body (RobloxTwoStepVerificationApiRetractDialogRequest): Request parameters for retracting
            a Cross Device dialog from state ACTIVE to PENDING.
        body (RobloxTwoStepVerificationApiRetractDialogRequest): Request parameters for retracting
            a Cross Device dialog from state ACTIVE to PENDING.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxTwoStepVerificationApiRetractDialogResponse]
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
    body: RobloxTwoStepVerificationApiRetractDialogRequest
    | RobloxTwoStepVerificationApiRetractDialogRequest
    | Unset = UNSET,
) -> Any | RobloxTwoStepVerificationApiRetractDialogResponse | None:
    """Reverts a user's dialog state from ACTIVE to PENDING.

    Args:
        user_id (int):
        body (RobloxTwoStepVerificationApiRetractDialogRequest): Request parameters for retracting
            a Cross Device dialog from state ACTIVE to PENDING.
        body (RobloxTwoStepVerificationApiRetractDialogRequest): Request parameters for retracting
            a Cross Device dialog from state ACTIVE to PENDING.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxTwoStepVerificationApiRetractDialogResponse
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
    body: RobloxTwoStepVerificationApiRetractDialogRequest
    | RobloxTwoStepVerificationApiRetractDialogRequest
    | Unset = UNSET,
) -> Response[Any | RobloxTwoStepVerificationApiRetractDialogResponse]:
    """Reverts a user's dialog state from ACTIVE to PENDING.

    Args:
        user_id (int):
        body (RobloxTwoStepVerificationApiRetractDialogRequest): Request parameters for retracting
            a Cross Device dialog from state ACTIVE to PENDING.
        body (RobloxTwoStepVerificationApiRetractDialogRequest): Request parameters for retracting
            a Cross Device dialog from state ACTIVE to PENDING.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxTwoStepVerificationApiRetractDialogResponse]
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
    body: RobloxTwoStepVerificationApiRetractDialogRequest
    | RobloxTwoStepVerificationApiRetractDialogRequest
    | Unset = UNSET,
) -> Any | RobloxTwoStepVerificationApiRetractDialogResponse | None:
    """Reverts a user's dialog state from ACTIVE to PENDING.

    Args:
        user_id (int):
        body (RobloxTwoStepVerificationApiRetractDialogRequest): Request parameters for retracting
            a Cross Device dialog from state ACTIVE to PENDING.
        body (RobloxTwoStepVerificationApiRetractDialogRequest): Request parameters for retracting
            a Cross Device dialog from state ACTIVE to PENDING.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxTwoStepVerificationApiRetractDialogResponse
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            body=body,
        )
    ).parsed
