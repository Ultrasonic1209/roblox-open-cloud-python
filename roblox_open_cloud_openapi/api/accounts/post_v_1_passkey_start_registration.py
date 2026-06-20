from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_authentication_api_models_request_start_passkey_registration_request import (
    RobloxAuthenticationApiModelsRequestStartPasskeyRegistrationRequest,
)
from ...models.roblox_authentication_api_models_response_start_passkey_registration_response import (
    RobloxAuthenticationApiModelsResponseStartPasskeyRegistrationResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: RobloxAuthenticationApiModelsRequestStartPasskeyRegistrationRequest
    | RobloxAuthenticationApiModelsRequestStartPasskeyRegistrationRequest
    | Unset = UNSET,
    flow: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["flow"] = flow

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "https://auth.roblox.com/v1/passkey/StartRegistration",
        "params": params,
        "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
        "openapi-id": "post_v1_passkey_StartRegistration",
    }

    if isinstance(body, RobloxAuthenticationApiModelsRequestStartPasskeyRegistrationRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxAuthenticationApiModelsRequestStartPasskeyRegistrationRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxAuthenticationApiModelsResponseStartPasskeyRegistrationResponse | None:
    if response.status_code == 200:
        response_200 = RobloxAuthenticationApiModelsResponseStartPasskeyRegistrationResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

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
) -> Response[Any | RobloxAuthenticationApiModelsResponseStartPasskeyRegistrationResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxAuthenticationApiModelsRequestStartPasskeyRegistrationRequest
    | RobloxAuthenticationApiModelsRequestStartPasskeyRegistrationRequest
    | Unset = UNSET,
    flow: str | Unset = UNSET,
) -> Response[Any | RobloxAuthenticationApiModelsResponseStartPasskeyRegistrationResponse]:
    """Initiates Passkey registration by providing credential creation options.

    Args:
        flow (str | Unset):
        body (RobloxAuthenticationApiModelsRequestStartPasskeyRegistrationRequest):
        body (RobloxAuthenticationApiModelsRequestStartPasskeyRegistrationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxAuthenticationApiModelsResponseStartPasskeyRegistrationResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        flow=flow,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: RobloxAuthenticationApiModelsRequestStartPasskeyRegistrationRequest
    | RobloxAuthenticationApiModelsRequestStartPasskeyRegistrationRequest
    | Unset = UNSET,
    flow: str | Unset = UNSET,
) -> Any | RobloxAuthenticationApiModelsResponseStartPasskeyRegistrationResponse | None:
    """Initiates Passkey registration by providing credential creation options.

    Args:
        flow (str | Unset):
        body (RobloxAuthenticationApiModelsRequestStartPasskeyRegistrationRequest):
        body (RobloxAuthenticationApiModelsRequestStartPasskeyRegistrationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxAuthenticationApiModelsResponseStartPasskeyRegistrationResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        flow=flow,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxAuthenticationApiModelsRequestStartPasskeyRegistrationRequest
    | RobloxAuthenticationApiModelsRequestStartPasskeyRegistrationRequest
    | Unset = UNSET,
    flow: str | Unset = UNSET,
) -> Response[Any | RobloxAuthenticationApiModelsResponseStartPasskeyRegistrationResponse]:
    """Initiates Passkey registration by providing credential creation options.

    Args:
        flow (str | Unset):
        body (RobloxAuthenticationApiModelsRequestStartPasskeyRegistrationRequest):
        body (RobloxAuthenticationApiModelsRequestStartPasskeyRegistrationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxAuthenticationApiModelsResponseStartPasskeyRegistrationResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        flow=flow,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RobloxAuthenticationApiModelsRequestStartPasskeyRegistrationRequest
    | RobloxAuthenticationApiModelsRequestStartPasskeyRegistrationRequest
    | Unset = UNSET,
    flow: str | Unset = UNSET,
) -> Any | RobloxAuthenticationApiModelsResponseStartPasskeyRegistrationResponse | None:
    """Initiates Passkey registration by providing credential creation options.

    Args:
        flow (str | Unset):
        body (RobloxAuthenticationApiModelsRequestStartPasskeyRegistrationRequest):
        body (RobloxAuthenticationApiModelsRequestStartPasskeyRegistrationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxAuthenticationApiModelsResponseStartPasskeyRegistrationResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            flow=flow,
        )
    ).parsed
