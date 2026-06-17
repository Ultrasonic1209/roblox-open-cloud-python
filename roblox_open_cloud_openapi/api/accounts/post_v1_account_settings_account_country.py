from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_account_settings_api_models_response_update_account_country_response import (
    RobloxAccountSettingsApiModelsResponseUpdateAccountCountryResponse,
)
from ...models.roblox_account_settings_api_update_account_country_request import (
    RobloxAccountSettingsApiUpdateAccountCountryRequest,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: RobloxAccountSettingsApiUpdateAccountCountryRequest
    | RobloxAccountSettingsApiUpdateAccountCountryRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "https://accountsettings.roblox.com/v1/account/settings/account-country",
        "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
        "openapi-id": "post_v1_account_settings_account-country",
    }

    if isinstance(body, RobloxAccountSettingsApiUpdateAccountCountryRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxAccountSettingsApiUpdateAccountCountryRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxAccountSettingsApiModelsResponseUpdateAccountCountryResponse | None:
    if response.status_code == 200:
        response_200 = RobloxAccountSettingsApiModelsResponseUpdateAccountCountryResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxAccountSettingsApiModelsResponseUpdateAccountCountryResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxAccountSettingsApiUpdateAccountCountryRequest
    | RobloxAccountSettingsApiUpdateAccountCountryRequest
    | Unset = UNSET,
) -> Response[Any | RobloxAccountSettingsApiModelsResponseUpdateAccountCountryResponse]:
    """Updates the user's account country.

    Args:
        body (RobloxAccountSettingsApiUpdateAccountCountryRequest): Request Model for updating a
            user's account country
        body (RobloxAccountSettingsApiUpdateAccountCountryRequest): Request Model for updating a
            user's account country

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxAccountSettingsApiModelsResponseUpdateAccountCountryResponse]
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
    body: RobloxAccountSettingsApiUpdateAccountCountryRequest
    | RobloxAccountSettingsApiUpdateAccountCountryRequest
    | Unset = UNSET,
) -> Any | RobloxAccountSettingsApiModelsResponseUpdateAccountCountryResponse | None:
    """Updates the user's account country.

    Args:
        body (RobloxAccountSettingsApiUpdateAccountCountryRequest): Request Model for updating a
            user's account country
        body (RobloxAccountSettingsApiUpdateAccountCountryRequest): Request Model for updating a
            user's account country

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxAccountSettingsApiModelsResponseUpdateAccountCountryResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxAccountSettingsApiUpdateAccountCountryRequest
    | RobloxAccountSettingsApiUpdateAccountCountryRequest
    | Unset = UNSET,
) -> Response[Any | RobloxAccountSettingsApiModelsResponseUpdateAccountCountryResponse]:
    """Updates the user's account country.

    Args:
        body (RobloxAccountSettingsApiUpdateAccountCountryRequest): Request Model for updating a
            user's account country
        body (RobloxAccountSettingsApiUpdateAccountCountryRequest): Request Model for updating a
            user's account country

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxAccountSettingsApiModelsResponseUpdateAccountCountryResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RobloxAccountSettingsApiUpdateAccountCountryRequest
    | RobloxAccountSettingsApiUpdateAccountCountryRequest
    | Unset = UNSET,
) -> Any | RobloxAccountSettingsApiModelsResponseUpdateAccountCountryResponse | None:
    """Updates the user's account country.

    Args:
        body (RobloxAccountSettingsApiUpdateAccountCountryRequest): Request Model for updating a
            user's account country
        body (RobloxAccountSettingsApiUpdateAccountCountryRequest): Request Model for updating a
            user's account country

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxAccountSettingsApiModelsResponseUpdateAccountCountryResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
