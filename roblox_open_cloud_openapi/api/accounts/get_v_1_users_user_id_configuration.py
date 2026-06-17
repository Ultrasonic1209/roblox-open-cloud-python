from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v1_users_user_id_configuration_action_type import GetV1UsersUserIdConfigurationActionType
from ...models.roblox_two_step_verification_api_user_configuration import RobloxTwoStepVerificationApiUserConfiguration
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: int,
    *,
    challenge_id: str | Unset = UNSET,
    action_type: GetV1UsersUserIdConfigurationActionType | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["challengeId"] = challenge_id

    json_action_type: int | Unset = UNSET
    if not isinstance(action_type, Unset):
        json_action_type = action_type.value

    params["actionType"] = json_action_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://twostepverification.roblox.com/v1/users/{user_id}/configuration".format(
            user_id=quote(str(user_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxTwoStepVerificationApiUserConfiguration | None:
    if response.status_code == 200:
        response_200 = RobloxTwoStepVerificationApiUserConfiguration.from_dict(response.json())

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
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxTwoStepVerificationApiUserConfiguration]:
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
    challenge_id: str | Unset = UNSET,
    action_type: GetV1UsersUserIdConfigurationActionType | Unset = UNSET,
) -> Response[Any | RobloxTwoStepVerificationApiUserConfiguration]:
    """Gets two step verification configuration for the specified user.

    Args:
        user_id (int):
        challenge_id (str | Unset):
        action_type (GetV1UsersUserIdConfigurationActionType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxTwoStepVerificationApiUserConfiguration]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        challenge_id=challenge_id,
        action_type=action_type,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: int,
    *,
    client: AuthenticatedClient,
    challenge_id: str | Unset = UNSET,
    action_type: GetV1UsersUserIdConfigurationActionType | Unset = UNSET,
) -> Any | RobloxTwoStepVerificationApiUserConfiguration | None:
    """Gets two step verification configuration for the specified user.

    Args:
        user_id (int):
        challenge_id (str | Unset):
        action_type (GetV1UsersUserIdConfigurationActionType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxTwoStepVerificationApiUserConfiguration
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        challenge_id=challenge_id,
        action_type=action_type,
    ).parsed


async def asyncio_detailed(
    user_id: int,
    *,
    client: AuthenticatedClient,
    challenge_id: str | Unset = UNSET,
    action_type: GetV1UsersUserIdConfigurationActionType | Unset = UNSET,
) -> Response[Any | RobloxTwoStepVerificationApiUserConfiguration]:
    """Gets two step verification configuration for the specified user.

    Args:
        user_id (int):
        challenge_id (str | Unset):
        action_type (GetV1UsersUserIdConfigurationActionType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxTwoStepVerificationApiUserConfiguration]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        challenge_id=challenge_id,
        action_type=action_type,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: int,
    *,
    client: AuthenticatedClient,
    challenge_id: str | Unset = UNSET,
    action_type: GetV1UsersUserIdConfigurationActionType | Unset = UNSET,
) -> Any | RobloxTwoStepVerificationApiUserConfiguration | None:
    """Gets two step verification configuration for the specified user.

    Args:
        user_id (int):
        challenge_id (str | Unset):
        action_type (GetV1UsersUserIdConfigurationActionType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxTwoStepVerificationApiUserConfiguration
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            challenge_id=challenge_id,
            action_type=action_type,
        )
    ).parsed
