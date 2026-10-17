from http import HTTPStatus
from typing import TYPE_CHECKING, Any
from urllib.parse import quote

if TYPE_CHECKING:
    import httpx2 as httpx
else:
    try:
        import httpx2 as httpx
    except ModuleNotFoundError:
        try:
            import httpx
        except ModuleNotFoundError:
            raise RuntimeError(
                "This module requires the httpx2 package to be installed.\n"
                "You can install it with:\n"
                "    $ pip install httpx2\n"
            ) from None


from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response

"""
{'x-roblox-stability': 'EXPERIMENTAL', 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.roblox_client_settings_api_models_response_client_version_response import (
    RobloxClientSettingsApiModelsResponseClientVersionResponse,
)


def _get_kwargs(
    binary_type: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://clientsettings.roblox.com/v2/client-version/{binary_type}".format(
            binary_type=quote(str(binary_type), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RobloxClientSettingsApiModelsResponseClientVersionResponse | None:
    if response.status_code == 200:
        response_200 = RobloxClientSettingsApiModelsResponseClientVersionResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RobloxClientSettingsApiModelsResponseClientVersionResponse]:
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

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


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

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


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
