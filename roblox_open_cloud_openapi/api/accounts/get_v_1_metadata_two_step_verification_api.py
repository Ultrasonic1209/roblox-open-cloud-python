from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v1_metadata_two_step_verification_api_action_type import (
    GetV1MetadataTwoStepVerificationApiActionType,
)
from ...models.roblox_two_step_verification_api_metadata_response import RobloxTwoStepVerificationApiMetadataResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    user_id: int | Unset = UNSET,
    challenge_id: str | Unset = UNSET,
    action_type: GetV1MetadataTwoStepVerificationApiActionType | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["userId"] = user_id

    params["challengeId"] = challenge_id

    json_action_type: int | Unset = UNSET
    if not isinstance(action_type, Unset):
        json_action_type = action_type.value

    params["actionType"] = json_action_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/metadata#TwoStepVerificationApi",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RobloxTwoStepVerificationApiMetadataResponse | None:
    if response.status_code == 200:
        response_200 = RobloxTwoStepVerificationApiMetadataResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RobloxTwoStepVerificationApiMetadataResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    user_id: int | Unset = UNSET,
    challenge_id: str | Unset = UNSET,
    action_type: GetV1MetadataTwoStepVerificationApiActionType | Unset = UNSET,
) -> Response[RobloxTwoStepVerificationApiMetadataResponse]:
    """Gets two step verification system metadata.

     The metadata endpoint takes in optional request parameters to output additional context
    for when the user is unauthenticated but attempting to login with two step verification.

    When supplied, all three request parameters must be sent and match up.

    Args:
        user_id (int | Unset):
        challenge_id (str | Unset):
        action_type (GetV1MetadataTwoStepVerificationApiActionType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RobloxTwoStepVerificationApiMetadataResponse]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        challenge_id=challenge_id,
        action_type=action_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    user_id: int | Unset = UNSET,
    challenge_id: str | Unset = UNSET,
    action_type: GetV1MetadataTwoStepVerificationApiActionType | Unset = UNSET,
) -> RobloxTwoStepVerificationApiMetadataResponse | None:
    """Gets two step verification system metadata.

     The metadata endpoint takes in optional request parameters to output additional context
    for when the user is unauthenticated but attempting to login with two step verification.

    When supplied, all three request parameters must be sent and match up.

    Args:
        user_id (int | Unset):
        challenge_id (str | Unset):
        action_type (GetV1MetadataTwoStepVerificationApiActionType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RobloxTwoStepVerificationApiMetadataResponse
    """

    return sync_detailed(
        client=client,
        user_id=user_id,
        challenge_id=challenge_id,
        action_type=action_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    user_id: int | Unset = UNSET,
    challenge_id: str | Unset = UNSET,
    action_type: GetV1MetadataTwoStepVerificationApiActionType | Unset = UNSET,
) -> Response[RobloxTwoStepVerificationApiMetadataResponse]:
    """Gets two step verification system metadata.

     The metadata endpoint takes in optional request parameters to output additional context
    for when the user is unauthenticated but attempting to login with two step verification.

    When supplied, all three request parameters must be sent and match up.

    Args:
        user_id (int | Unset):
        challenge_id (str | Unset):
        action_type (GetV1MetadataTwoStepVerificationApiActionType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RobloxTwoStepVerificationApiMetadataResponse]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        challenge_id=challenge_id,
        action_type=action_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    user_id: int | Unset = UNSET,
    challenge_id: str | Unset = UNSET,
    action_type: GetV1MetadataTwoStepVerificationApiActionType | Unset = UNSET,
) -> RobloxTwoStepVerificationApiMetadataResponse | None:
    """Gets two step verification system metadata.

     The metadata endpoint takes in optional request parameters to output additional context
    for when the user is unauthenticated but attempting to login with two step verification.

    When supplied, all three request parameters must be sent and match up.

    Args:
        user_id (int | Unset):
        challenge_id (str | Unset):
        action_type (GetV1MetadataTwoStepVerificationApiActionType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RobloxTwoStepVerificationApiMetadataResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            user_id=user_id,
            challenge_id=challenge_id,
            action_type=action_type,
        )
    ).parsed
