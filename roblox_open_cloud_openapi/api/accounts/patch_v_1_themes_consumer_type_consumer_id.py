from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_v1_themes_consumer_type_consumer_id_consumer_type import (
    PatchV1ThemesConsumerTypeConsumerIdConsumerType,
)
from ...models.roblox_account_settings_api_theme_configuration_request import (
    RobloxAccountSettingsApiThemeConfigurationRequest,
)
from ...models.roblox_web_web_api_api_empty_response_model import RobloxWebWebAPIApiEmptyResponseModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    consumer_type: PatchV1ThemesConsumerTypeConsumerIdConsumerType,
    consumer_id: int = 0,
    *,
    body: RobloxAccountSettingsApiThemeConfigurationRequest
    | RobloxAccountSettingsApiThemeConfigurationRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "https://accountsettings.roblox.com/v1/themes/{consumer_type}/{consumer_id}".format(
            consumer_type=quote(str(consumer_type), safe=""),
            consumer_id=quote(str(consumer_id), safe=""),
        ),
        "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
        "openapi-id": "patch_v1_themes_consumerType_consumerId",
    }

    if isinstance(body, RobloxAccountSettingsApiThemeConfigurationRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxAccountSettingsApiThemeConfigurationRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxWebWebAPIApiEmptyResponseModel | None:
    if response.status_code == 200:
        response_200 = RobloxWebWebAPIApiEmptyResponseModel.from_dict(response.json())

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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxWebWebAPIApiEmptyResponseModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    consumer_type: PatchV1ThemesConsumerTypeConsumerIdConsumerType,
    consumer_id: int = 0,
    *,
    client: AuthenticatedClient,
    body: RobloxAccountSettingsApiThemeConfigurationRequest
    | RobloxAccountSettingsApiThemeConfigurationRequest
    | Unset = UNSET,
) -> Response[Any | RobloxWebWebAPIApiEmptyResponseModel]:
    """Modify the theme type for consumer.

    Args:
        consumer_type (PatchV1ThemesConsumerTypeConsumerIdConsumerType):
        consumer_id (int):  Default: 0.
        body (RobloxAccountSettingsApiThemeConfigurationRequest): Response model for get user's
            theme type
        body (RobloxAccountSettingsApiThemeConfigurationRequest): Response model for get user's
            theme type

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIApiEmptyResponseModel]
    """

    kwargs = _get_kwargs(
        consumer_type=consumer_type,
        consumer_id=consumer_id,
        body=body,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    consumer_type: PatchV1ThemesConsumerTypeConsumerIdConsumerType,
    consumer_id: int = 0,
    *,
    client: AuthenticatedClient,
    body: RobloxAccountSettingsApiThemeConfigurationRequest
    | RobloxAccountSettingsApiThemeConfigurationRequest
    | Unset = UNSET,
) -> Any | RobloxWebWebAPIApiEmptyResponseModel | None:
    """Modify the theme type for consumer.

    Args:
        consumer_type (PatchV1ThemesConsumerTypeConsumerIdConsumerType):
        consumer_id (int):  Default: 0.
        body (RobloxAccountSettingsApiThemeConfigurationRequest): Response model for get user's
            theme type
        body (RobloxAccountSettingsApiThemeConfigurationRequest): Response model for get user's
            theme type

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIApiEmptyResponseModel
    """

    return sync_detailed(
        consumer_type=consumer_type,
        consumer_id=consumer_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    consumer_type: PatchV1ThemesConsumerTypeConsumerIdConsumerType,
    consumer_id: int = 0,
    *,
    client: AuthenticatedClient,
    body: RobloxAccountSettingsApiThemeConfigurationRequest
    | RobloxAccountSettingsApiThemeConfigurationRequest
    | Unset = UNSET,
) -> Response[Any | RobloxWebWebAPIApiEmptyResponseModel]:
    """Modify the theme type for consumer.

    Args:
        consumer_type (PatchV1ThemesConsumerTypeConsumerIdConsumerType):
        consumer_id (int):  Default: 0.
        body (RobloxAccountSettingsApiThemeConfigurationRequest): Response model for get user's
            theme type
        body (RobloxAccountSettingsApiThemeConfigurationRequest): Response model for get user's
            theme type

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIApiEmptyResponseModel]
    """

    kwargs = _get_kwargs(
        consumer_type=consumer_type,
        consumer_id=consumer_id,
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    consumer_type: PatchV1ThemesConsumerTypeConsumerIdConsumerType,
    consumer_id: int = 0,
    *,
    client: AuthenticatedClient,
    body: RobloxAccountSettingsApiThemeConfigurationRequest
    | RobloxAccountSettingsApiThemeConfigurationRequest
    | Unset = UNSET,
) -> Any | RobloxWebWebAPIApiEmptyResponseModel | None:
    """Modify the theme type for consumer.

    Args:
        consumer_type (PatchV1ThemesConsumerTypeConsumerIdConsumerType):
        consumer_id (int):  Default: 0.
        body (RobloxAccountSettingsApiThemeConfigurationRequest): Response model for get user's
            theme type
        body (RobloxAccountSettingsApiThemeConfigurationRequest): Response model for get user's
            theme type

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIApiEmptyResponseModel
    """

    return (
        await asyncio_detailed(
            consumer_type=consumer_type,
            consumer_id=consumer_id,
            client=client,
            body=body,
        )
    ).parsed
