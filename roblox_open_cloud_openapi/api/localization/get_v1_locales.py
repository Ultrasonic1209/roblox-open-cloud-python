from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_web_web_api_models_api_array_response_roblox_locale_api_supported_locale_locus import (
    RobloxWebWebAPIModelsApiArrayResponseRobloxLocaleApiSupportedLocaleLocus,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    display_value_locale: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["displayValueLocale"] = display_value_locale

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://locale.roblox.com/v1/locales",
        "params": params,
        "extensions": {
            "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
            "openapi-id": "get_v1_locales",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxLocaleApiSupportedLocaleLocus | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIModelsApiArrayResponseRobloxLocaleApiSupportedLocaleLocus.from_dict(
            response.json()
        )

        return response_200

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
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxLocaleApiSupportedLocaleLocus]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    display_value_locale: str | Unset = UNSET,
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxLocaleApiSupportedLocaleLocus]:
    """Get list of Supported locales with user locus information.

    Args:
        display_value_locale (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxLocaleApiSupportedLocaleLocus]
    """

    kwargs = _get_kwargs(
        display_value_locale=display_value_locale,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    display_value_locale: str | Unset = UNSET,
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxLocaleApiSupportedLocaleLocus | None:
    """Get list of Supported locales with user locus information.

    Args:
        display_value_locale (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiArrayResponseRobloxLocaleApiSupportedLocaleLocus
    """

    return sync_detailed(
        client=client,
        display_value_locale=display_value_locale,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    display_value_locale: str | Unset = UNSET,
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxLocaleApiSupportedLocaleLocus]:
    """Get list of Supported locales with user locus information.

    Args:
        display_value_locale (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxLocaleApiSupportedLocaleLocus]
    """

    kwargs = _get_kwargs(
        display_value_locale=display_value_locale,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    display_value_locale: str | Unset = UNSET,
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxLocaleApiSupportedLocaleLocus | None:
    """Get list of Supported locales with user locus information.

    Args:
        display_value_locale (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiArrayResponseRobloxLocaleApiSupportedLocaleLocus
    """

    return (
        await asyncio_detailed(
            client=client,
            display_value_locale=display_value_locale,
        )
    ).parsed
