import sys
from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response

if sys.version_info >= (3, 13):
    from warnings import deprecated
else:
    from typing_extensions import deprecated

from ...models.roblox_authentication_api_models_recovery_metadata_response import (
    RobloxAuthenticationApiModelsRecoveryMetadataResponse,
)


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://auth.roblox.com/v1/recovery/metadata",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxAuthenticationApiModelsRecoveryMetadataResponse | None:
    if response.status_code == 200:
        response_200 = RobloxAuthenticationApiModelsRecoveryMetadataResponse.from_dict(response.json())

        return response_200

    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxAuthenticationApiModelsRecoveryMetadataResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/accounts#auth_get_v1_recovery_metadata"
)
def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxAuthenticationApiModelsRecoveryMetadataResponse]:
    """Get metadata for forgot endpoints

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxAuthenticationApiModelsRecoveryMetadataResponse]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/accounts#auth_get_v1_recovery_metadata"
)
def sync(
    *,
    client: AuthenticatedClient,
) -> Any | RobloxAuthenticationApiModelsRecoveryMetadataResponse | None:
    """Get metadata for forgot endpoints

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxAuthenticationApiModelsRecoveryMetadataResponse
    """

    return sync_detailed(
        client=client,
    ).parsed


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/accounts#auth_get_v1_recovery_metadata"
)
async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxAuthenticationApiModelsRecoveryMetadataResponse]:
    """Get metadata for forgot endpoints

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxAuthenticationApiModelsRecoveryMetadataResponse]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/accounts#auth_get_v1_recovery_metadata"
)
async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Any | RobloxAuthenticationApiModelsRecoveryMetadataResponse | None:
    """Get metadata for forgot endpoints

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxAuthenticationApiModelsRecoveryMetadataResponse
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
