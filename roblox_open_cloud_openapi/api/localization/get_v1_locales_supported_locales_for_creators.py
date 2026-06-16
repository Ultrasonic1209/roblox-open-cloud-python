from http import HTTPStatus
from typing import Any

import httpx

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
        "url": "/v1/locales/supported-locales-for-creators",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RobloxWebWebAPIModelsApiArrayResponseRobloxLocaleApiSupportedLocaleLocus | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIModelsApiArrayResponseRobloxLocaleApiSupportedLocaleLocus.from_dict(
            response.json()
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RobloxWebWebAPIModelsApiArrayResponseRobloxLocaleApiSupportedLocaleLocus]:
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
) -> Response[RobloxWebWebAPIModelsApiArrayResponseRobloxLocaleApiSupportedLocaleLocus]:
    """
    Args:
        display_value_locale (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RobloxWebWebAPIModelsApiArrayResponseRobloxLocaleApiSupportedLocaleLocus]
    """

    kwargs = _get_kwargs(
        display_value_locale=display_value_locale,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    display_value_locale: str | Unset = UNSET,
) -> RobloxWebWebAPIModelsApiArrayResponseRobloxLocaleApiSupportedLocaleLocus | None:
    """
    Args:
        display_value_locale (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RobloxWebWebAPIModelsApiArrayResponseRobloxLocaleApiSupportedLocaleLocus
    """

    return sync_detailed(
        client=client,
        display_value_locale=display_value_locale,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    display_value_locale: str | Unset = UNSET,
) -> Response[RobloxWebWebAPIModelsApiArrayResponseRobloxLocaleApiSupportedLocaleLocus]:
    """
    Args:
        display_value_locale (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RobloxWebWebAPIModelsApiArrayResponseRobloxLocaleApiSupportedLocaleLocus]
    """

    kwargs = _get_kwargs(
        display_value_locale=display_value_locale,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    display_value_locale: str | Unset = UNSET,
) -> RobloxWebWebAPIModelsApiArrayResponseRobloxLocaleApiSupportedLocaleLocus | None:
    """
    Args:
        display_value_locale (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RobloxWebWebAPIModelsApiArrayResponseRobloxLocaleApiSupportedLocaleLocus
    """

    return (
        await asyncio_detailed(
            client=client,
            display_value_locale=display_value_locale,
        )
    ).parsed
