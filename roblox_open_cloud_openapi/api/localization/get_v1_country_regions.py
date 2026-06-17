from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_locale_api_country_region_list_response import RobloxLocaleApiCountryRegionListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    locale: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["locale"] = locale

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://locale.roblox.com/v1/country-regions",
        "params": params,
        "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
        "openapi-id": "get_v1_country-regions",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxLocaleApiCountryRegionListResponse | None:
    if response.status_code == 200:
        response_200 = RobloxLocaleApiCountryRegionListResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxLocaleApiCountryRegionListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    locale: str | Unset = UNSET,
) -> Response[Any | RobloxLocaleApiCountryRegionListResponse]:
    """Get list of country regions sorted by localized name

    Args:
        locale (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxLocaleApiCountryRegionListResponse]
    """

    kwargs = _get_kwargs(
        locale=locale,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    locale: str | Unset = UNSET,
) -> Any | RobloxLocaleApiCountryRegionListResponse | None:
    """Get list of country regions sorted by localized name

    Args:
        locale (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxLocaleApiCountryRegionListResponse
    """

    return sync_detailed(
        client=client,
        locale=locale,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    locale: str | Unset = UNSET,
) -> Response[Any | RobloxLocaleApiCountryRegionListResponse]:
    """Get list of country regions sorted by localized name

    Args:
        locale (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxLocaleApiCountryRegionListResponse]
    """

    kwargs = _get_kwargs(
        locale=locale,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    locale: str | Unset = UNSET,
) -> Any | RobloxLocaleApiCountryRegionListResponse | None:
    """Get list of country regions sorted by localized name

    Args:
        locale (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxLocaleApiCountryRegionListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            locale=locale,
        )
    ).parsed
