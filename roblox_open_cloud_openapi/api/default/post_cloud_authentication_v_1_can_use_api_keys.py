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
{'x-roblox-stability': 'EXPERIMENTAL', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'MINUTE', 'maxInPeriod': 100}}, 'x-roblox-scopes': [{'name': 'group.permission:read', 'firstPartyOAuthOnly': True}], 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.can_use_api_keys_request import CanUseApiKeysRequest
from ...models.can_use_api_keys_response import CanUseApiKeysResponse
from ...models.cloud_authentication_service_status import CloudAuthenticationServiceStatus
from ...types import Unset


def _get_kwargs(
    *,
    body: CanUseApiKeysRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/cloud-authentication/v1/canUseApiKeys",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CanUseApiKeysResponse | CloudAuthenticationServiceStatus:
    if response.status_code == 200:
        response_200 = CanUseApiKeysResponse.from_dict(response.json())

        return response_200

    response_default = CloudAuthenticationServiceStatus.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CanUseApiKeysResponse | CloudAuthenticationServiceStatus]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CanUseApiKeysRequest | Unset = UNSET,
) -> Response[CanUseApiKeysResponse | CloudAuthenticationServiceStatus]:
    """Checks whether the current user can create and use API keys under the group.

    Args:
        body (CanUseApiKeysRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CanUseApiKeysResponse | CloudAuthenticationServiceStatus]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: CanUseApiKeysRequest | Unset = UNSET,
) -> CanUseApiKeysResponse | CloudAuthenticationServiceStatus | None:
    """Checks whether the current user can create and use API keys under the group.

    Args:
        body (CanUseApiKeysRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CanUseApiKeysResponse | CloudAuthenticationServiceStatus
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CanUseApiKeysRequest | Unset = UNSET,
) -> Response[CanUseApiKeysResponse | CloudAuthenticationServiceStatus]:
    """Checks whether the current user can create and use API keys under the group.

    Args:
        body (CanUseApiKeysRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CanUseApiKeysResponse | CloudAuthenticationServiceStatus]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CanUseApiKeysRequest | Unset = UNSET,
) -> CanUseApiKeysResponse | CloudAuthenticationServiceStatus | None:
    """Checks whether the current user can create and use API keys under the group.

    Args:
        body (CanUseApiKeysRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CanUseApiKeysResponse | CloudAuthenticationServiceStatus
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
