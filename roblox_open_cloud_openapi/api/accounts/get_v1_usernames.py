from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_authentication_api_models_usernames_response import RobloxAuthenticationApiModelsUsernamesResponse
from ...types import UNSET, Response


def _get_kwargs(
    *,
    username: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["username"] = username

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://auth.roblox.com/v1/usernames",
        "params": params,
        "extensions": {
            "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
            "openapi-id": "get_v1_usernames",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> RobloxAuthenticationApiModelsUsernamesResponse | None:
    if response.status_code == 200:
        response_200 = RobloxAuthenticationApiModelsUsernamesResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[RobloxAuthenticationApiModelsUsernamesResponse]:
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
) -> Response[RobloxAuthenticationApiModelsUsernamesResponse]:
    r"""Gets a list of existing usernames on Roblox based on the query parameters

     This endpoint can be expanded in the future to include other query parameters such as \"startsWith\"

    Args:
        username (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RobloxAuthenticationApiModelsUsernamesResponse]
    """

    kwargs = _get_kwargs(
        username=username,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    username: str,
) -> RobloxAuthenticationApiModelsUsernamesResponse | None:
    r"""Gets a list of existing usernames on Roblox based on the query parameters

     This endpoint can be expanded in the future to include other query parameters such as \"startsWith\"

    Args:
        username (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RobloxAuthenticationApiModelsUsernamesResponse
    """

    return sync_detailed(
        client=client,
        username=username,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    username: str,
) -> Response[RobloxAuthenticationApiModelsUsernamesResponse]:
    r"""Gets a list of existing usernames on Roblox based on the query parameters

     This endpoint can be expanded in the future to include other query parameters such as \"startsWith\"

    Args:
        username (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RobloxAuthenticationApiModelsUsernamesResponse]
    """

    kwargs = _get_kwargs(
        username=username,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    username: str,
) -> RobloxAuthenticationApiModelsUsernamesResponse | None:
    r"""Gets a list of existing usernames on Roblox based on the query parameters

     This endpoint can be expanded in the future to include other query parameters such as \"startsWith\"

    Args:
        username (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RobloxAuthenticationApiModelsUsernamesResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            username=username,
        )
    ).parsed
