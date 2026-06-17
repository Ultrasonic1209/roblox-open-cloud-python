from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.secret import Secret
from ...models.secrets_store_service_problem_details import SecretsStoreServiceProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    universe_id: int,
    *,
    body: Secret | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/cloud/v2/universes/{universe_id}/secrets".format(
            universe_id=quote(str(universe_id), safe=""),
        ),
        "openapi-extensions": {
            "x-roblox-scopes": [{"name": "universe.secret:write", "description": "Required"}],
            "x-roblox-stability": "BETA",
            "x-roblox-rate-limits": {
                "perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 120},
                "perOauth2Authorization": {"period": "MINUTE", "maxInPeriod": 120},
            },
            "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
        },
        "openapi-id": "post_cloud_v2_universes_universeId_secrets",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Secret | SecretsStoreServiceProblemDetails | None:
    if response.status_code == 201:
        response_201 = Secret.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = SecretsStoreServiceProblemDetails.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = SecretsStoreServiceProblemDetails.from_dict(response.json())

        return response_403

    if response.status_code == 409:
        response_409 = SecretsStoreServiceProblemDetails.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
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
    body: Secret | Unset = UNSET,
) -> Response[Secret | SecretsStoreServiceProblemDetails]:
    """Create Secret

     Creates a new secret. A maximum of 500 secrets per universe is allowed.

    Only the owner of the universe can create secrets. For group-owned universes, only the group owner
    or authorized
    members can create secrets.

    To encrypt the secret:
    1. Get the public key using the Get Public Key endpoint
    2. Encrypt your secret using LibSodium sealed box
    3. Base64 encode the encrypted content

    Include the key_id from the public key response in the request.

    For an example, see the [Secrets store guide](https://create.roblox.com/docs/cloud/guides/secrets-
    store).

    Args:
        universe_id (int):
        body (Secret | Unset): Universe-specific secret, identified by `id`, and belonging to a
            specific `environment`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Secret | SecretsStoreServiceProblemDetails]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        body=body,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    body: Secret | Unset = UNSET,
) -> Secret | SecretsStoreServiceProblemDetails | None:
    """Create Secret

     Creates a new secret. A maximum of 500 secrets per universe is allowed.

    Only the owner of the universe can create secrets. For group-owned universes, only the group owner
    or authorized
    members can create secrets.

    To encrypt the secret:
    1. Get the public key using the Get Public Key endpoint
    2. Encrypt your secret using LibSodium sealed box
    3. Base64 encode the encrypted content

    Include the key_id from the public key response in the request.

    For an example, see the [Secrets store guide](https://create.roblox.com/docs/cloud/guides/secrets-
    store).

    Args:
        universe_id (int):
        body (Secret | Unset): Universe-specific secret, identified by `id`, and belonging to a
            specific `environment`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Secret | SecretsStoreServiceProblemDetails
    """

    return sync_detailed(
        universe_id=universe_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    body: Secret | Unset = UNSET,
) -> Response[Secret | SecretsStoreServiceProblemDetails]:
    """Create Secret

     Creates a new secret. A maximum of 500 secrets per universe is allowed.

    Only the owner of the universe can create secrets. For group-owned universes, only the group owner
    or authorized
    members can create secrets.

    To encrypt the secret:
    1. Get the public key using the Get Public Key endpoint
    2. Encrypt your secret using LibSodium sealed box
    3. Base64 encode the encrypted content

    Include the key_id from the public key response in the request.

    For an example, see the [Secrets store guide](https://create.roblox.com/docs/cloud/guides/secrets-
    store).

    Args:
        universe_id (int):
        body (Secret | Unset): Universe-specific secret, identified by `id`, and belonging to a
            specific `environment`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Secret | SecretsStoreServiceProblemDetails]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    body: Secret | Unset = UNSET,
) -> Secret | SecretsStoreServiceProblemDetails | None:
    """Create Secret

     Creates a new secret. A maximum of 500 secrets per universe is allowed.

    Only the owner of the universe can create secrets. For group-owned universes, only the group owner
    or authorized
    members can create secrets.

    To encrypt the secret:
    1. Get the public key using the Get Public Key endpoint
    2. Encrypt your secret using LibSodium sealed box
    3. Base64 encode the encrypted content

    Include the key_id from the public key response in the request.

    For an example, see the [Secrets store guide](https://create.roblox.com/docs/cloud/guides/secrets-
    store).

    Args:
        universe_id (int):
        body (Secret | Unset): Universe-specific secret, identified by `id`, and belonging to a
            specific `environment`.

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
            body=body,
        )
    ).parsed
