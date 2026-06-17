import sys
from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response

if sys.version_info >= (3, 13):
    from warnings import deprecated
else:
    from typing_extensions import deprecated

from ...models.roblox_authentication_api_models_login_request import RobloxAuthenticationApiModelsLoginRequest
from ...models.roblox_authentication_api_models_login_response import RobloxAuthenticationApiModelsLoginResponse


def _get_kwargs(
    *,
    body: RobloxAuthenticationApiModelsLoginRequest | RobloxAuthenticationApiModelsLoginRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/login",
    }

    if isinstance(body, RobloxAuthenticationApiModelsLoginRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxAuthenticationApiModelsLoginRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxAuthenticationApiModelsLoginResponse | None:
    if response.status_code == 200:
        response_200 = RobloxAuthenticationApiModelsLoginResponse.from_dict(response.json())

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

    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RobloxAuthenticationApiModelsLoginResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/accounts#auth_post_v1_login"
)
def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxAuthenticationApiModelsLoginRequest | RobloxAuthenticationApiModelsLoginRequest | Unset = UNSET,
) -> Response[Any | RobloxAuthenticationApiModelsLoginResponse]:
    """Authenticates a user.

    Args:
        body (RobloxAuthenticationApiModelsLoginRequest):
        body (RobloxAuthenticationApiModelsLoginRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxAuthenticationApiModelsLoginResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/accounts#auth_post_v1_login"
)
def sync(
    *,
    client: AuthenticatedClient,
    body: RobloxAuthenticationApiModelsLoginRequest | RobloxAuthenticationApiModelsLoginRequest | Unset = UNSET,
) -> Any | RobloxAuthenticationApiModelsLoginResponse | None:
    """Authenticates a user.

    Args:
        body (RobloxAuthenticationApiModelsLoginRequest):
        body (RobloxAuthenticationApiModelsLoginRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxAuthenticationApiModelsLoginResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/accounts#auth_post_v1_login"
)
async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxAuthenticationApiModelsLoginRequest | RobloxAuthenticationApiModelsLoginRequest | Unset = UNSET,
) -> Response[Any | RobloxAuthenticationApiModelsLoginResponse]:
    """Authenticates a user.

    Args:
        body (RobloxAuthenticationApiModelsLoginRequest):
        body (RobloxAuthenticationApiModelsLoginRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxAuthenticationApiModelsLoginResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/accounts#auth_post_v1_login"
)
async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RobloxAuthenticationApiModelsLoginRequest | RobloxAuthenticationApiModelsLoginRequest | Unset = UNSET,
) -> Any | RobloxAuthenticationApiModelsLoginResponse | None:
    """Authenticates a user.

    Args:
        body (RobloxAuthenticationApiModelsLoginRequest):
        body (RobloxAuthenticationApiModelsLoginRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxAuthenticationApiModelsLoginResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
