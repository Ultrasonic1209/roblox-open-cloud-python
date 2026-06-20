from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_authentication_api_models_signup_request import RobloxAuthenticationApiModelsSignupRequest
from ...models.roblox_authentication_api_models_signup_response import RobloxAuthenticationApiModelsSignupResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: RobloxAuthenticationApiModelsSignupRequest | RobloxAuthenticationApiModelsSignupRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "https://auth.roblox.com/v2/signup/linked",
        "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
        "openapi-id": "post_v2_signup_linked",
    }

    if isinstance(body, RobloxAuthenticationApiModelsSignupRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxAuthenticationApiModelsSignupRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxAuthenticationApiModelsSignupResponse | None:
    if response.status_code == 200:
        response_200 = RobloxAuthenticationApiModelsSignupResponse.from_dict(response.json())

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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxAuthenticationApiModelsSignupResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxAuthenticationApiModelsSignupRequest | RobloxAuthenticationApiModelsSignupRequest | Unset = UNSET,
) -> Response[Any | RobloxAuthenticationApiModelsSignupResponse]:
    """Endpoint for signing up a new user, specifically for linked
    authentication on PCGDK

    Args:
        body (RobloxAuthenticationApiModelsSignupRequest):
        body (RobloxAuthenticationApiModelsSignupRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxAuthenticationApiModelsSignupResponse]
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
    body: RobloxAuthenticationApiModelsSignupRequest | RobloxAuthenticationApiModelsSignupRequest | Unset = UNSET,
) -> Any | RobloxAuthenticationApiModelsSignupResponse | None:
    """Endpoint for signing up a new user, specifically for linked
    authentication on PCGDK

    Args:
        body (RobloxAuthenticationApiModelsSignupRequest):
        body (RobloxAuthenticationApiModelsSignupRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxAuthenticationApiModelsSignupResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxAuthenticationApiModelsSignupRequest | RobloxAuthenticationApiModelsSignupRequest | Unset = UNSET,
) -> Response[Any | RobloxAuthenticationApiModelsSignupResponse]:
    """Endpoint for signing up a new user, specifically for linked
    authentication on PCGDK

    Args:
        body (RobloxAuthenticationApiModelsSignupRequest):
        body (RobloxAuthenticationApiModelsSignupRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxAuthenticationApiModelsSignupResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RobloxAuthenticationApiModelsSignupRequest | RobloxAuthenticationApiModelsSignupRequest | Unset = UNSET,
) -> Any | RobloxAuthenticationApiModelsSignupResponse | None:
    """Endpoint for signing up a new user, specifically for linked
    authentication on PCGDK

    Args:
        body (RobloxAuthenticationApiModelsSignupRequest):
        body (RobloxAuthenticationApiModelsSignupRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxAuthenticationApiModelsSignupResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
