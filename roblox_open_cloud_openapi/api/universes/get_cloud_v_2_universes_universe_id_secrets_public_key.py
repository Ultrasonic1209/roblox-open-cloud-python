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
{'x-roblox-scopes': [{'name': 'universe.secret:read', 'description': 'Required'}], 'x-roblox-stability': 'BETA', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'MINUTE', 'maxInPeriod': 120}, 'perOauth2Authorization': {'period': 'MINUTE', 'maxInPeriod': 120}}, 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.secret import Secret
from ...models.secrets_store_service_problem_details import SecretsStoreServiceProblemDetails


def _get_kwargs(
    universe_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/cloud/v2/universes/{universe_id}/secrets/public-key".format(
            universe_id=quote(str(universe_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Secret | SecretsStoreServiceProblemDetails | None:
    if response.status_code == 200:
        response_200 = Secret.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = SecretsStoreServiceProblemDetails.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = SecretsStoreServiceProblemDetails.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Secret | SecretsStoreServiceProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    universe_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Secret | SecretsStoreServiceProblemDetails]:
    """Get Public Key

     Retrieves the public key for a universe. You need this key to encrypt secret content
    before sending it to Roblox.

    Only the owner of the universe can retrieve the public key. For group-owned universes, only the
    group owner or
    authorized members can retrieve the public key.

    The secret id field is static and always returns "public-key".

    The returned public key in the secret field is universe-specific and derived from a master key using
    the universe ID.
    Use this key with LibSodium sealed box encryption to encrypt your secret content before
    creating or updating secrets.

    Include the key_id from the public key response in the request to create or update a secret.

    Args:
        universe_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Secret | SecretsStoreServiceProblemDetails]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: int,
    *,
    client: AuthenticatedClient,
) -> Secret | SecretsStoreServiceProblemDetails | None:
    """Get Public Key

     Retrieves the public key for a universe. You need this key to encrypt secret content
    before sending it to Roblox.

    Only the owner of the universe can retrieve the public key. For group-owned universes, only the
    group owner or
    authorized members can retrieve the public key.

    The secret id field is static and always returns "public-key".

    The returned public key in the secret field is universe-specific and derived from a master key using
    the universe ID.
    Use this key with LibSodium sealed box encryption to encrypt your secret content before
    creating or updating secrets.

    Include the key_id from the public key response in the request to create or update a secret.

    Args:
        universe_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Secret | SecretsStoreServiceProblemDetails
    """

    return sync_detailed(
        universe_id=universe_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    universe_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Secret | SecretsStoreServiceProblemDetails]:
    """Get Public Key

     Retrieves the public key for a universe. You need this key to encrypt secret content
    before sending it to Roblox.

    Only the owner of the universe can retrieve the public key. For group-owned universes, only the
    group owner or
    authorized members can retrieve the public key.

    The secret id field is static and always returns "public-key".

    The returned public key in the secret field is universe-specific and derived from a master key using
    the universe ID.
    Use this key with LibSodium sealed box encryption to encrypt your secret content before
    creating or updating secrets.

    Include the key_id from the public key response in the request to create or update a secret.

    Args:
        universe_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Secret | SecretsStoreServiceProblemDetails]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: int,
    *,
    client: AuthenticatedClient,
) -> Secret | SecretsStoreServiceProblemDetails | None:
    """Get Public Key

     Retrieves the public key for a universe. You need this key to encrypt secret content
    before sending it to Roblox.

    Only the owner of the universe can retrieve the public key. For group-owned universes, only the
    group owner or
    authorized members can retrieve the public key.

    The secret id field is static and always returns "public-key".

    The returned public key in the secret field is universe-specific and derived from a master key using
    the universe ID.
    Use this key with LibSodium sealed box encryption to encrypt your secret content before
    creating or updating secrets.

    Include the key_id from the public key response in the request to create or update a secret.

    Args:
        universe_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Secret | SecretsStoreServiceProblemDetails
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            client=client,
        )
    ).parsed
