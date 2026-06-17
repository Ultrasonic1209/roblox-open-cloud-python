from http import HTTPStatus
from typing import Any

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_authentication_api_models_auth_meta_data_response import (
    RobloxAuthenticationApiModelsAuthMetaDataResponse,
)
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://auth.roblox.com/v2/auth/metadata",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> RobloxAuthenticationApiModelsAuthMetaDataResponse | None:
    if response.status_code == 200:
        response_200 = RobloxAuthenticationApiModelsAuthMetaDataResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[RobloxAuthenticationApiModelsAuthMetaDataResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[RobloxAuthenticationApiModelsAuthMetaDataResponse]:
    """Gets Auth meta data

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RobloxAuthenticationApiModelsAuthMetaDataResponse]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> RobloxAuthenticationApiModelsAuthMetaDataResponse | None:
    """Gets Auth meta data

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RobloxAuthenticationApiModelsAuthMetaDataResponse
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[RobloxAuthenticationApiModelsAuthMetaDataResponse]:
    """Gets Auth meta data

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RobloxAuthenticationApiModelsAuthMetaDataResponse]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> RobloxAuthenticationApiModelsAuthMetaDataResponse | None:
    """Gets Auth meta data

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RobloxAuthenticationApiModelsAuthMetaDataResponse
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
