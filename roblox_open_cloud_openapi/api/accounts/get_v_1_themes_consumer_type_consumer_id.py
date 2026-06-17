from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v1_themes_consumer_type_consumer_id_consumer_type import (
    GetV1ThemesConsumerTypeConsumerIdConsumerType,
)
from ...models.roblox_account_settings_api_theme_configuration_response import (
    RobloxAccountSettingsApiThemeConfigurationResponse,
)
from ...types import Response


def _get_kwargs(
    consumer_type: GetV1ThemesConsumerTypeConsumerIdConsumerType,
    consumer_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://accountsettings.roblox.com/v1/themes/{consumer_type}/{consumer_id}".format(
            consumer_type=quote(str(consumer_type), safe=""),
            consumer_id=quote(str(consumer_id), safe=""),
        ),
        "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
        "openapi-id": "get_v1_themes_consumerType_consumerId",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxAccountSettingsApiThemeConfigurationResponse | None:
    if response.status_code == 200:
        response_200 = RobloxAccountSettingsApiThemeConfigurationResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxAccountSettingsApiThemeConfigurationResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    consumer_type: GetV1ThemesConsumerTypeConsumerIdConsumerType,
    consumer_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxAccountSettingsApiThemeConfigurationResponse]:
    """returns the theme type for a specific consumer.

    Args:
        consumer_type (GetV1ThemesConsumerTypeConsumerIdConsumerType):
        consumer_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxAccountSettingsApiThemeConfigurationResponse]
    """

    kwargs = _get_kwargs(
        consumer_type=consumer_type,
        consumer_id=consumer_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    consumer_type: GetV1ThemesConsumerTypeConsumerIdConsumerType,
    consumer_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxAccountSettingsApiThemeConfigurationResponse | None:
    """returns the theme type for a specific consumer.

    Args:
        consumer_type (GetV1ThemesConsumerTypeConsumerIdConsumerType):
        consumer_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxAccountSettingsApiThemeConfigurationResponse
    """

    return sync_detailed(
        consumer_type=consumer_type,
        consumer_id=consumer_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    consumer_type: GetV1ThemesConsumerTypeConsumerIdConsumerType,
    consumer_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxAccountSettingsApiThemeConfigurationResponse]:
    """returns the theme type for a specific consumer.

    Args:
        consumer_type (GetV1ThemesConsumerTypeConsumerIdConsumerType):
        consumer_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxAccountSettingsApiThemeConfigurationResponse]
    """

    kwargs = _get_kwargs(
        consumer_type=consumer_type,
        consumer_id=consumer_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    consumer_type: GetV1ThemesConsumerTypeConsumerIdConsumerType,
    consumer_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxAccountSettingsApiThemeConfigurationResponse | None:
    """returns the theme type for a specific consumer.

    Args:
        consumer_type (GetV1ThemesConsumerTypeConsumerIdConsumerType):
        consumer_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxAccountSettingsApiThemeConfigurationResponse
    """

    return (
        await asyncio_detailed(
            consumer_type=consumer_type,
            consumer_id=consumer_id,
            client=client,
        )
    ).parsed
