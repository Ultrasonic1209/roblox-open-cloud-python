from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_locale_api_set_show_roblox_translations_request import (
    RobloxLocaleApiSetShowRobloxTranslationsRequest,
)
from ...models.roblox_locale_api_success_response import RobloxLocaleApiSuccessResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: RobloxLocaleApiSetShowRobloxTranslationsRequest
    | RobloxLocaleApiSetShowRobloxTranslationsRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "https://locale.roblox.com/v1/locales/set-show-roblox-translations",
        "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
        "openapi-id": "post_v1_locales_set-show-roblox-translations",
    }

    if isinstance(body, RobloxLocaleApiSetShowRobloxTranslationsRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxLocaleApiSetShowRobloxTranslationsRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxLocaleApiSuccessResponse | None:
    if response.status_code == 200:
        response_200 = RobloxLocaleApiSuccessResponse.from_dict(response.json())

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

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxLocaleApiSuccessResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxLocaleApiSetShowRobloxTranslationsRequest
    | RobloxLocaleApiSetShowRobloxTranslationsRequest
    | Unset = UNSET,
) -> Response[Any | RobloxLocaleApiSuccessResponse]:
    """Sets whether translations suggested by Roblox will be shown to the user.

    Args:
        body (RobloxLocaleApiSetShowRobloxTranslationsRequest): Request entity to set the
            ShowRobloxTranslations field for an account
        body (RobloxLocaleApiSetShowRobloxTranslationsRequest): Request entity to set the
            ShowRobloxTranslations field for an account

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxLocaleApiSuccessResponse]
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
    body: RobloxLocaleApiSetShowRobloxTranslationsRequest
    | RobloxLocaleApiSetShowRobloxTranslationsRequest
    | Unset = UNSET,
) -> Any | RobloxLocaleApiSuccessResponse | None:
    """Sets whether translations suggested by Roblox will be shown to the user.

    Args:
        body (RobloxLocaleApiSetShowRobloxTranslationsRequest): Request entity to set the
            ShowRobloxTranslations field for an account
        body (RobloxLocaleApiSetShowRobloxTranslationsRequest): Request entity to set the
            ShowRobloxTranslations field for an account

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxLocaleApiSuccessResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RobloxLocaleApiSetShowRobloxTranslationsRequest
    | RobloxLocaleApiSetShowRobloxTranslationsRequest
    | Unset = UNSET,
) -> Response[Any | RobloxLocaleApiSuccessResponse]:
    """Sets whether translations suggested by Roblox will be shown to the user.

    Args:
        body (RobloxLocaleApiSetShowRobloxTranslationsRequest): Request entity to set the
            ShowRobloxTranslations field for an account
        body (RobloxLocaleApiSetShowRobloxTranslationsRequest): Request entity to set the
            ShowRobloxTranslations field for an account

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxLocaleApiSuccessResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RobloxLocaleApiSetShowRobloxTranslationsRequest
    | RobloxLocaleApiSetShowRobloxTranslationsRequest
    | Unset = UNSET,
) -> Any | RobloxLocaleApiSuccessResponse | None:
    """Sets whether translations suggested by Roblox will be shown to the user.

    Args:
        body (RobloxLocaleApiSetShowRobloxTranslationsRequest): Request entity to set the
            ShowRobloxTranslations field for an account
        body (RobloxLocaleApiSetShowRobloxTranslationsRequest): Request entity to set the
            ShowRobloxTranslations field for an account

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxLocaleApiSuccessResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
