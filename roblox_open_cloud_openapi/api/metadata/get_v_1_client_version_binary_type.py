import sys
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response

if sys.version_info >= (3, 13):
    from warnings import deprecated
else:
    from typing_extensions import deprecated

from ...models.roblox_client_settings_api_models_response_client_version_response import (
    RobloxClientSettingsApiModelsResponseClientVersionResponse,
)


def _get_kwargs(
    binary_type: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://clientsettings.roblox.com/v1/client-version/{binary_type}".format(
            binary_type=quote(str(binary_type), safe=""),
        ),
        "openapi-extensions": {
            "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            "x-roblox-recommended-alternatives": [
                {
                    "url": "https://clientsettings.roblox.com/v2/client-version/{binaryType}",
                    "httpMethod": "GET",
                    "documentationUrl": "https://create.roblox.com/docs/cloud/reference/features/metadata#clientsettings_get_v2_client_version__binaryType_",
                }
            ],
        },
        "openapi-id": "get_v1_client-version_binaryType",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> RobloxClientSettingsApiModelsResponseClientVersionResponse | None:
    if response.status_code == 200:
        response_200 = RobloxClientSettingsApiModelsResponseClientVersionResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[RobloxClientSettingsApiModelsResponseClientVersionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/metadata#clientsettings_get_v1_client_version__binaryType_"
)
def sync_detailed(
    binary_type: str,
    *,
    client: AuthenticatedClient,
) -> Response[RobloxClientSettingsApiModelsResponseClientVersionResponse]:
    """Get client version information for specific binary type

    Args:
        binary_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RobloxClientSettingsApiModelsResponseClientVersionResponse]
    """

    kwargs = _get_kwargs(
        binary_type=binary_type,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/metadata#clientsettings_get_v1_client_version__binaryType_"
)
def sync(
    binary_type: str,
    *,
    client: AuthenticatedClient,
) -> RobloxClientSettingsApiModelsResponseClientVersionResponse | None:
    """Get client version information for specific binary type

    Args:
        binary_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RobloxClientSettingsApiModelsResponseClientVersionResponse
    """

    return sync_detailed(
        binary_type=binary_type,
        client=client,
    ).parsed


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/metadata#clientsettings_get_v1_client_version__binaryType_"
)
async def asyncio_detailed(
    binary_type: str,
    *,
    client: AuthenticatedClient,
) -> Response[RobloxClientSettingsApiModelsResponseClientVersionResponse]:
    """Get client version information for specific binary type

    Args:
        binary_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RobloxClientSettingsApiModelsResponseClientVersionResponse]
    """

    kwargs = _get_kwargs(
        binary_type=binary_type,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/metadata#clientsettings_get_v1_client_version__binaryType_"
)
async def asyncio(
    binary_type: str,
    *,
    client: AuthenticatedClient,
) -> RobloxClientSettingsApiModelsResponseClientVersionResponse | None:
    """Get client version information for specific binary type

    Args:
        binary_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RobloxClientSettingsApiModelsResponseClientVersionResponse
    """

    return (
        await asyncio_detailed(
            binary_type=binary_type,
            client=client,
        )
    ).parsed
