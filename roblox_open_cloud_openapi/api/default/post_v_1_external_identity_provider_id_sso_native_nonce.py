from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_authentication_api_models_response_external_identity_gateway_external_identity_nonce_response import (
    RobloxAuthenticationApiModelsResponseExternalIdentityGatewayExternalIdentityNonceResponse,
)
from ...types import Response


def _get_kwargs(
    identity_provider_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "https://auth.roblox.com/v1/external/{identity_provider_id}/sso/native/nonce".format(
            identity_provider_id=quote(str(identity_provider_id), safe=""),
        ),
        "extensions": {
            "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
            "openapi-id": "post_v1_external_identityProviderId_sso_native_nonce",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> RobloxAuthenticationApiModelsResponseExternalIdentityGatewayExternalIdentityNonceResponse | None:
    if response.status_code == 200:
        response_200 = (
            RobloxAuthenticationApiModelsResponseExternalIdentityGatewayExternalIdentityNonceResponse.from_dict(
                response.json()
            )
        )

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[RobloxAuthenticationApiModelsResponseExternalIdentityGatewayExternalIdentityNonceResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    identity_provider_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[RobloxAuthenticationApiModelsResponseExternalIdentityGatewayExternalIdentityNonceResponse]:
    """Reserves a nonce for a native SSO sign-in attempt.

     The web flow gets its nonce from M:Roblox.Authentication.Api.Controllers.V1.ExternalIdentitiesGatewa
    yController.OAuthInit(System.Int64,System.Threading.CancellationToken), which native clients never
    call
    because they have no authorization redirect. They call this instead, pass the nonce to the
    provider SDK, and post the resulting id_token to /access.

    The client must pass this value to the SDK verbatim. Both providers treat the nonce as an
    opaque string and echo it into the id_token unchanged, and redemption looks the value up as
    issued. The SHA256(nonce) convention seen in Apple examples belongs to Firebase, which hashes
    on its own side before comparing; hashing here would make the lookup miss.

    Args:
        identity_provider_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RobloxAuthenticationApiModelsResponseExternalIdentityGatewayExternalIdentityNonceResponse]
    """

    kwargs = _get_kwargs(
        identity_provider_id=identity_provider_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    identity_provider_id: int,
    *,
    client: AuthenticatedClient,
) -> RobloxAuthenticationApiModelsResponseExternalIdentityGatewayExternalIdentityNonceResponse | None:
    """Reserves a nonce for a native SSO sign-in attempt.

     The web flow gets its nonce from M:Roblox.Authentication.Api.Controllers.V1.ExternalIdentitiesGatewa
    yController.OAuthInit(System.Int64,System.Threading.CancellationToken), which native clients never
    call
    because they have no authorization redirect. They call this instead, pass the nonce to the
    provider SDK, and post the resulting id_token to /access.

    The client must pass this value to the SDK verbatim. Both providers treat the nonce as an
    opaque string and echo it into the id_token unchanged, and redemption looks the value up as
    issued. The SHA256(nonce) convention seen in Apple examples belongs to Firebase, which hashes
    on its own side before comparing; hashing here would make the lookup miss.

    Args:
        identity_provider_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RobloxAuthenticationApiModelsResponseExternalIdentityGatewayExternalIdentityNonceResponse
    """

    return sync_detailed(
        identity_provider_id=identity_provider_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    identity_provider_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[RobloxAuthenticationApiModelsResponseExternalIdentityGatewayExternalIdentityNonceResponse]:
    """Reserves a nonce for a native SSO sign-in attempt.

     The web flow gets its nonce from M:Roblox.Authentication.Api.Controllers.V1.ExternalIdentitiesGatewa
    yController.OAuthInit(System.Int64,System.Threading.CancellationToken), which native clients never
    call
    because they have no authorization redirect. They call this instead, pass the nonce to the
    provider SDK, and post the resulting id_token to /access.

    The client must pass this value to the SDK verbatim. Both providers treat the nonce as an
    opaque string and echo it into the id_token unchanged, and redemption looks the value up as
    issued. The SHA256(nonce) convention seen in Apple examples belongs to Firebase, which hashes
    on its own side before comparing; hashing here would make the lookup miss.

    Args:
        identity_provider_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RobloxAuthenticationApiModelsResponseExternalIdentityGatewayExternalIdentityNonceResponse]
    """

    kwargs = _get_kwargs(
        identity_provider_id=identity_provider_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    identity_provider_id: int,
    *,
    client: AuthenticatedClient,
) -> RobloxAuthenticationApiModelsResponseExternalIdentityGatewayExternalIdentityNonceResponse | None:
    """Reserves a nonce for a native SSO sign-in attempt.

     The web flow gets its nonce from M:Roblox.Authentication.Api.Controllers.V1.ExternalIdentitiesGatewa
    yController.OAuthInit(System.Int64,System.Threading.CancellationToken), which native clients never
    call
    because they have no authorization redirect. They call this instead, pass the nonce to the
    provider SDK, and post the resulting id_token to /access.

    The client must pass this value to the SDK verbatim. Both providers treat the nonce as an
    opaque string and echo it into the id_token unchanged, and redemption looks the value up as
    issued. The SHA256(nonce) convention seen in Apple examples belongs to Firebase, which hashes
    on its own side before comparing; hashing here would make the lookup miss.

    Args:
        identity_provider_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RobloxAuthenticationApiModelsResponseExternalIdentityGatewayExternalIdentityNonceResponse
    """

    return (
        await asyncio_detailed(
            identity_provider_id=identity_provider_id,
            client=client,
        )
    ).parsed
