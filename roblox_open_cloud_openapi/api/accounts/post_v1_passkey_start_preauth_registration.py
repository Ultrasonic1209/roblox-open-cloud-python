from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_authentication_api_models_request_start_passkey_preauth_registration_request import (
    RobloxAuthenticationApiModelsRequestStartPasskeyPreauthRegistrationRequest,
)
from ...models.roblox_authentication_api_models_response_start_passkey_preauth_registration_response import (
    RobloxAuthenticationApiModelsResponseStartPasskeyPreauthRegistrationResponse,
)
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: RobloxAuthenticationApiModelsRequestStartPasskeyPreauthRegistrationRequest
    | RobloxAuthenticationApiModelsRequestStartPasskeyPreauthRegistrationRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/passkey/start-preauth-registration",
    }

    if isinstance(body, RobloxAuthenticationApiModelsRequestStartPasskeyPreauthRegistrationRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxAuthenticationApiModelsRequestStartPasskeyPreauthRegistrationRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxAuthenticationApiModelsResponseStartPasskeyPreauthRegistrationResponse | None:
    if response.status_code == 200:
        response_200 = RobloxAuthenticationApiModelsResponseStartPasskeyPreauthRegistrationResponse.from_dict(
            response.json()
        )

        return response_200

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
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RobloxAuthenticationApiModelsResponseStartPasskeyPreauthRegistrationResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxAuthenticationApiModelsRequestStartPasskeyPreauthRegistrationRequest
    | RobloxAuthenticationApiModelsRequestStartPasskeyPreauthRegistrationRequest
    | Unset = UNSET,
) -> Response[Any | RobloxAuthenticationApiModelsResponseStartPasskeyPreauthRegistrationResponse]:
    """Initiates  Passkey preauthenticated registration by providing credential creation options.

    Args:
        body (RobloxAuthenticationApiModelsRequestStartPasskeyPreauthRegistrationRequest):
        body (RobloxAuthenticationApiModelsRequestStartPasskeyPreauthRegistrationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxAuthenticationApiModelsResponseStartPasskeyPreauthRegistrationResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: RobloxAuthenticationApiModelsRequestStartPasskeyPreauthRegistrationRequest
    | RobloxAuthenticationApiModelsRequestStartPasskeyPreauthRegistrationRequest
    | Unset = UNSET,
) -> Any | RobloxAuthenticationApiModelsResponseStartPasskeyPreauthRegistrationResponse | None:
    """Initiates  Passkey preauthenticated registration by providing credential creation options.

    Args:
        body (RobloxAuthenticationApiModelsRequestStartPasskeyPreauthRegistrationRequest):
        body (RobloxAuthenticationApiModelsRequestStartPasskeyPreauthRegistrationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxAuthenticationApiModelsResponseStartPasskeyPreauthRegistrationResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxAuthenticationApiModelsRequestStartPasskeyPreauthRegistrationRequest
    | RobloxAuthenticationApiModelsRequestStartPasskeyPreauthRegistrationRequest
    | Unset = UNSET,
) -> Response[Any | RobloxAuthenticationApiModelsResponseStartPasskeyPreauthRegistrationResponse]:
    """Initiates  Passkey preauthenticated registration by providing credential creation options.

    Args:
        body (RobloxAuthenticationApiModelsRequestStartPasskeyPreauthRegistrationRequest):
        body (RobloxAuthenticationApiModelsRequestStartPasskeyPreauthRegistrationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxAuthenticationApiModelsResponseStartPasskeyPreauthRegistrationResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RobloxAuthenticationApiModelsRequestStartPasskeyPreauthRegistrationRequest
    | RobloxAuthenticationApiModelsRequestStartPasskeyPreauthRegistrationRequest
    | Unset = UNSET,
) -> Any | RobloxAuthenticationApiModelsResponseStartPasskeyPreauthRegistrationResponse | None:
    """Initiates  Passkey preauthenticated registration by providing credential creation options.

    Args:
        body (RobloxAuthenticationApiModelsRequestStartPasskeyPreauthRegistrationRequest):
        body (RobloxAuthenticationApiModelsRequestStartPasskeyPreauthRegistrationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxAuthenticationApiModelsResponseStartPasskeyPreauthRegistrationResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
