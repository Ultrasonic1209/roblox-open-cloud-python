from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_authentication_api_models_account_pin_request import (
    RobloxAuthenticationApiModelsAccountPinRequest,
)
from ...models.roblox_web_web_api_models_api_success_response import RobloxWebWebAPIModelsApiSuccessResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: RobloxAuthenticationApiModelsAccountPinRequest
    | RobloxAuthenticationApiModelsAccountPinRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "https://auth.roblox.com/v1/account/pin",
        "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
        "openapi-id": "patch_v1_account_pin",
    }

    if isinstance(body, RobloxAuthenticationApiModelsAccountPinRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxAuthenticationApiModelsAccountPinRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxWebWebAPIModelsApiSuccessResponse | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIModelsApiSuccessResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxWebWebAPIModelsApiSuccessResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxAuthenticationApiModelsAccountPinRequest
    | RobloxAuthenticationApiModelsAccountPinRequest
    | Unset = UNSET,
) -> Response[Any | RobloxWebWebAPIModelsApiSuccessResponse]:
    """Request made to update the account pin on the account.

    Args:
        body (RobloxAuthenticationApiModelsAccountPinRequest):
        body (RobloxAuthenticationApiModelsAccountPinRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiSuccessResponse]
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
    body: RobloxAuthenticationApiModelsAccountPinRequest
    | RobloxAuthenticationApiModelsAccountPinRequest
    | Unset = UNSET,
) -> Any | RobloxWebWebAPIModelsApiSuccessResponse | None:
    """Request made to update the account pin on the account.

    Args:
        body (RobloxAuthenticationApiModelsAccountPinRequest):
        body (RobloxAuthenticationApiModelsAccountPinRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiSuccessResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxAuthenticationApiModelsAccountPinRequest
    | RobloxAuthenticationApiModelsAccountPinRequest
    | Unset = UNSET,
) -> Response[Any | RobloxWebWebAPIModelsApiSuccessResponse]:
    """Request made to update the account pin on the account.

    Args:
        body (RobloxAuthenticationApiModelsAccountPinRequest):
        body (RobloxAuthenticationApiModelsAccountPinRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiSuccessResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RobloxAuthenticationApiModelsAccountPinRequest
    | RobloxAuthenticationApiModelsAccountPinRequest
    | Unset = UNSET,
) -> Any | RobloxWebWebAPIModelsApiSuccessResponse | None:
    """Request made to update the account pin on the account.

    Args:
        body (RobloxAuthenticationApiModelsAccountPinRequest):
        body (RobloxAuthenticationApiModelsAccountPinRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiSuccessResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
