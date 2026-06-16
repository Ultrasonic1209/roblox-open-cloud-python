from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_client_settings_api_models_response_ota_version_response import (
    RobloxClientSettingsApiModelsResponseOtaVersionResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    binary_type: str,
    *,
    channel: str | Unset = UNSET,
    version: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    name: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["channel"] = channel

    params["version"] = version

    params["tag"] = tag

    params["name"] = name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/ota-version/{binary_type}".format(
            binary_type=quote(str(binary_type), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | list[RobloxClientSettingsApiModelsResponseOtaVersionResponse] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = RobloxClientSettingsApiModelsResponseOtaVersionResponse.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

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
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | list[RobloxClientSettingsApiModelsResponseOtaVersionResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    binary_type: str,
    *,
    client: AuthenticatedClient,
    channel: str | Unset = UNSET,
    version: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    name: str | Unset = UNSET,
) -> Response[Any | list[RobloxClientSettingsApiModelsResponseOtaVersionResponse]]:
    """Get OTA information for a specific binary type with a given version on some channel.
    Returns empty list if no updates are found or channel/application with the given version does not
    exist in CVS.

    Args:
        binary_type (str):
        channel (str | Unset):
        version (str | Unset):
        tag (str | Unset):
        name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[RobloxClientSettingsApiModelsResponseOtaVersionResponse]]
    """

    kwargs = _get_kwargs(
        binary_type=binary_type,
        channel=channel,
        version=version,
        tag=tag,
        name=name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    binary_type: str,
    *,
    client: AuthenticatedClient,
    channel: str | Unset = UNSET,
    version: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    name: str | Unset = UNSET,
) -> Any | list[RobloxClientSettingsApiModelsResponseOtaVersionResponse] | None:
    """Get OTA information for a specific binary type with a given version on some channel.
    Returns empty list if no updates are found or channel/application with the given version does not
    exist in CVS.

    Args:
        binary_type (str):
        channel (str | Unset):
        version (str | Unset):
        tag (str | Unset):
        name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[RobloxClientSettingsApiModelsResponseOtaVersionResponse]
    """

    return sync_detailed(
        binary_type=binary_type,
        client=client,
        channel=channel,
        version=version,
        tag=tag,
        name=name,
    ).parsed


async def asyncio_detailed(
    binary_type: str,
    *,
    client: AuthenticatedClient,
    channel: str | Unset = UNSET,
    version: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    name: str | Unset = UNSET,
) -> Response[Any | list[RobloxClientSettingsApiModelsResponseOtaVersionResponse]]:
    """Get OTA information for a specific binary type with a given version on some channel.
    Returns empty list if no updates are found or channel/application with the given version does not
    exist in CVS.

    Args:
        binary_type (str):
        channel (str | Unset):
        version (str | Unset):
        tag (str | Unset):
        name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[RobloxClientSettingsApiModelsResponseOtaVersionResponse]]
    """

    kwargs = _get_kwargs(
        binary_type=binary_type,
        channel=channel,
        version=version,
        tag=tag,
        name=name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    binary_type: str,
    *,
    client: AuthenticatedClient,
    channel: str | Unset = UNSET,
    version: str | Unset = UNSET,
    tag: str | Unset = UNSET,
    name: str | Unset = UNSET,
) -> Any | list[RobloxClientSettingsApiModelsResponseOtaVersionResponse] | None:
    """Get OTA information for a specific binary type with a given version on some channel.
    Returns empty list if no updates are found or channel/application with the given version does not
    exist in CVS.

    Args:
        binary_type (str):
        channel (str | Unset):
        version (str | Unset):
        tag (str | Unset):
        name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[RobloxClientSettingsApiModelsResponseOtaVersionResponse]
    """

    return (
        await asyncio_detailed(
            binary_type=binary_type,
            client=client,
            channel=channel,
            version=version,
            tag=tag,
            name=name,
        )
    ).parsed
