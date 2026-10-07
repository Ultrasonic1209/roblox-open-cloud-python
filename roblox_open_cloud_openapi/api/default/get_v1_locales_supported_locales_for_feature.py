from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_locale_api_supported_locales_response import RobloxLocaleApiSupportedLocalesResponse
from ...types import UNSET, Response


def _get_kwargs(
    *,
    feature_name: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["featureName"] = feature_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://locale.roblox.com/v1/locales/supported-locales-for-feature",
        "params": params,
        "extensions": {
            "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
            "openapi-id": "get_v1_locales_supported-locales-for-feature",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxLocaleApiSupportedLocalesResponse | None:
    if response.status_code == 200:
        response_200 = RobloxLocaleApiSupportedLocalesResponse.from_dict(response.json())

        return response_200

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxLocaleApiSupportedLocalesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    feature_name: str,
) -> Response[Any | RobloxLocaleApiSupportedLocalesResponse]:
    """Get list of Supported locales for a specific feature.

    Args:
        feature_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxLocaleApiSupportedLocalesResponse]
    """

    kwargs = _get_kwargs(
        feature_name=feature_name,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    feature_name: str,
) -> Any | RobloxLocaleApiSupportedLocalesResponse | None:
    """Get list of Supported locales for a specific feature.

    Args:
        feature_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxLocaleApiSupportedLocalesResponse
    """

    return sync_detailed(
        client=client,
        feature_name=feature_name,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    feature_name: str,
) -> Response[Any | RobloxLocaleApiSupportedLocalesResponse]:
    """Get list of Supported locales for a specific feature.

    Args:
        feature_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxLocaleApiSupportedLocalesResponse]
    """

    kwargs = _get_kwargs(
        feature_name=feature_name,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    feature_name: str,
) -> Any | RobloxLocaleApiSupportedLocalesResponse | None:
    """Get list of Supported locales for a specific feature.

    Args:
        feature_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxLocaleApiSupportedLocalesResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            feature_name=feature_name,
        )
    ).parsed
