from http import HTTPStatus
from typing import TYPE_CHECKING, Any

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


from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response

"""
{'x-roblox-stability': 'EXPERIMENTAL', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'MINUTE', 'maxInPeriod': 100}}, 'x-roblox-scopes': [{'name': 'scope:read', 'firstPartyOAuthOnly': True}], 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.cloud_authentication_service_status import CloudAuthenticationServiceStatus
from ...models.get_scopes_response import GetScopesResponse
from ...types import Unset


def _get_kwargs(
    *,
    group_id_value: int | Unset = UNSET,
    locale: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["groupId.value"] = group_id_value

    params["locale"] = locale

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/cloud-authentication/v1/scopes",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CloudAuthenticationServiceStatus | GetScopesResponse:
    if response.status_code == 200:
        response_200 = GetScopesResponse.from_dict(response.json())

        return response_200

    response_default = CloudAuthenticationServiceStatus.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CloudAuthenticationServiceStatus | GetScopesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    group_id_value: int | Unset = UNSET,
    locale: str | Unset = UNSET,
) -> Response[CloudAuthenticationServiceStatus | GetScopesResponse]:
    """Gets the current scope-centric (v2) configuration, mainly for the UI.

    Args:
        group_id_value (int | Unset):
        locale (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CloudAuthenticationServiceStatus | GetScopesResponse]
    """

    kwargs = _get_kwargs(
        group_id_value=group_id_value,
        locale=locale,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    group_id_value: int | Unset = UNSET,
    locale: str | Unset = UNSET,
) -> CloudAuthenticationServiceStatus | GetScopesResponse | None:
    """Gets the current scope-centric (v2) configuration, mainly for the UI.

    Args:
        group_id_value (int | Unset):
        locale (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CloudAuthenticationServiceStatus | GetScopesResponse
    """

    return sync_detailed(
        client=client,
        group_id_value=group_id_value,
        locale=locale,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    group_id_value: int | Unset = UNSET,
    locale: str | Unset = UNSET,
) -> Response[CloudAuthenticationServiceStatus | GetScopesResponse]:
    """Gets the current scope-centric (v2) configuration, mainly for the UI.

    Args:
        group_id_value (int | Unset):
        locale (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CloudAuthenticationServiceStatus | GetScopesResponse]
    """

    kwargs = _get_kwargs(
        group_id_value=group_id_value,
        locale=locale,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    group_id_value: int | Unset = UNSET,
    locale: str | Unset = UNSET,
) -> CloudAuthenticationServiceStatus | GetScopesResponse | None:
    """Gets the current scope-centric (v2) configuration, mainly for the UI.

    Args:
        group_id_value (int | Unset):
        locale (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CloudAuthenticationServiceStatus | GetScopesResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            group_id_value=group_id_value,
            locale=locale,
        )
    ).parsed
