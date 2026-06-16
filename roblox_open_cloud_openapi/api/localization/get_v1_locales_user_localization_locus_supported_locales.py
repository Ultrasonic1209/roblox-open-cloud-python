from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_locale_api_user_localization_locus_locales_response import (
    RobloxLocaleApiUserLocalizationLocusLocalesResponse,
)
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/locales/user-localization-locus-supported-locales",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxLocaleApiUserLocalizationLocusLocalesResponse | None:
    if response.status_code == 200:
        response_200 = RobloxLocaleApiUserLocalizationLocusLocalesResponse.from_dict(response.json())

        return response_200

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RobloxLocaleApiUserLocalizationLocusLocalesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxLocaleApiUserLocalizationLocusLocalesResponse]:
    """Gets each of a user's localization locus supported locales. A localization locus supported locale is
    a page (or group of pages) that
    have been defined by the International team which need independent locale support.
    If the user is null we will attempt to return the locales appropriate for the user's device
    language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxLocaleApiUserLocalizationLocusLocalesResponse]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Any | RobloxLocaleApiUserLocalizationLocusLocalesResponse | None:
    """Gets each of a user's localization locus supported locales. A localization locus supported locale is
    a page (or group of pages) that
    have been defined by the International team which need independent locale support.
    If the user is null we will attempt to return the locales appropriate for the user's device
    language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxLocaleApiUserLocalizationLocusLocalesResponse
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxLocaleApiUserLocalizationLocusLocalesResponse]:
    """Gets each of a user's localization locus supported locales. A localization locus supported locale is
    a page (or group of pages) that
    have been defined by the International team which need independent locale support.
    If the user is null we will attempt to return the locales appropriate for the user's device
    language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxLocaleApiUserLocalizationLocusLocalesResponse]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Any | RobloxLocaleApiUserLocalizationLocusLocalesResponse | None:
    """Gets each of a user's localization locus supported locales. A localization locus supported locale is
    a page (or group of pages) that
    have been defined by the International team which need independent locale support.
    If the user is null we will attempt to return the locales appropriate for the user's device
    language.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxLocaleApiUserLocalizationLocusLocalesResponse
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
