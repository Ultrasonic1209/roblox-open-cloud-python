import datetime
from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_authentication_api_models_recommended_username_response import (
    RobloxAuthenticationApiModelsRecommendedUsernameResponse,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    display_name: str,
    birth_day: datetime.datetime,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["DisplayName"] = display_name

    json_birth_day = birth_day.isoformat()
    params["BirthDay"] = json_birth_day

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://auth.roblox.com/v1/validators/recommendedUsernameFromDisplayName",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> RobloxAuthenticationApiModelsRecommendedUsernameResponse | None:
    if response.status_code == 200:
        response_200 = RobloxAuthenticationApiModelsRecommendedUsernameResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[RobloxAuthenticationApiModelsRecommendedUsernameResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    display_name: str,
    birth_day: datetime.datetime,
) -> Response[RobloxAuthenticationApiModelsRecommendedUsernameResponse]:
    """Validates the given display name, and if valid, will convert it to a valid username and return
    suggested username(s) if available.

    Args:
        display_name (str):
        birth_day (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RobloxAuthenticationApiModelsRecommendedUsernameResponse]
    """

    kwargs = _get_kwargs(
        display_name=display_name,
        birth_day=birth_day,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    display_name: str,
    birth_day: datetime.datetime,
) -> RobloxAuthenticationApiModelsRecommendedUsernameResponse | None:
    """Validates the given display name, and if valid, will convert it to a valid username and return
    suggested username(s) if available.

    Args:
        display_name (str):
        birth_day (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RobloxAuthenticationApiModelsRecommendedUsernameResponse
    """

    return sync_detailed(
        client=client,
        display_name=display_name,
        birth_day=birth_day,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    display_name: str,
    birth_day: datetime.datetime,
) -> Response[RobloxAuthenticationApiModelsRecommendedUsernameResponse]:
    """Validates the given display name, and if valid, will convert it to a valid username and return
    suggested username(s) if available.

    Args:
        display_name (str):
        birth_day (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RobloxAuthenticationApiModelsRecommendedUsernameResponse]
    """

    kwargs = _get_kwargs(
        display_name=display_name,
        birth_day=birth_day,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    display_name: str,
    birth_day: datetime.datetime,
) -> RobloxAuthenticationApiModelsRecommendedUsernameResponse | None:
    """Validates the given display name, and if valid, will convert it to a valid username and return
    suggested username(s) if available.

    Args:
        display_name (str):
        birth_day (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RobloxAuthenticationApiModelsRecommendedUsernameResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            display_name=display_name,
            birth_day=birth_day,
        )
    ).parsed
