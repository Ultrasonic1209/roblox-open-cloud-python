import datetime
from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v2_usernames_validate_context import GetV2UsernamesValidateContext
from ...models.roblox_authentication_api_models_username_validation_response import (
    RobloxAuthenticationApiModelsUsernameValidationResponse,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    username: str,
    birthday: datetime.datetime,
    context: GetV2UsernamesValidateContext,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["Username"] = username

    json_birthday = birthday.isoformat()
    params["Birthday"] = json_birthday

    json_context = context.value
    params["Context"] = json_context

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://auth.roblox.com/v2/usernames/validate",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxAuthenticationApiModelsUsernameValidationResponse | None:
    if response.status_code == 200:
        response_200 = RobloxAuthenticationApiModelsUsernameValidationResponse.from_dict(response.json())

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
    username: str,
    birthday: datetime.datetime,
    context: GetV2UsernamesValidateContext,
) -> Response[Any | RobloxAuthenticationApiModelsUsernameValidationResponse]:
    """Checks if a username is valid.

    Args:
        username (str):
        birthday (datetime.datetime):
        context (GetV2UsernamesValidateContext):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxAuthenticationApiModelsUsernameValidationResponse]
    """

    kwargs = _get_kwargs(
        username=username,
        birthday=birthday,
        context=context,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    username: str,
    birthday: datetime.datetime,
    context: GetV2UsernamesValidateContext,
) -> Any | RobloxAuthenticationApiModelsUsernameValidationResponse | None:
    """Checks if a username is valid.

    Args:
        username (str):
        birthday (datetime.datetime):
        context (GetV2UsernamesValidateContext):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxAuthenticationApiModelsUsernameValidationResponse
    """

    return sync_detailed(
        client=client,
        username=username,
        birthday=birthday,
        context=context,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    username: str,
    birthday: datetime.datetime,
    context: GetV2UsernamesValidateContext,
) -> Response[Any | RobloxAuthenticationApiModelsUsernameValidationResponse]:
    """Checks if a username is valid.

    Args:
        username (str):
        birthday (datetime.datetime):
        context (GetV2UsernamesValidateContext):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxAuthenticationApiModelsUsernameValidationResponse]
    """

    kwargs = _get_kwargs(
        username=username,
        birthday=birthday,
        context=context,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    username: str,
    birthday: datetime.datetime,
    context: GetV2UsernamesValidateContext,
) -> Any | RobloxAuthenticationApiModelsUsernameValidationResponse | None:
    """Checks if a username is valid.

    Args:
        username (str):
        birthday (datetime.datetime):
        context (GetV2UsernamesValidateContext):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxAuthenticationApiModelsUsernameValidationResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            username=username,
            birthday=birthday,
            context=context,
        )
    ).parsed
