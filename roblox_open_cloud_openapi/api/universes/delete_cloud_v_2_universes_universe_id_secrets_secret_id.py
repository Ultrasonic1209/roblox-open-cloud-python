from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.secrets_store_service_problem_details import SecretsStoreServiceProblemDetails
from ...types import Response


def _get_kwargs(
    universe_id: int,
    secret_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/cloud/v2/universes/{universe_id}/secrets/{secret_id}".format(
            universe_id=quote(str(universe_id), safe=""),
            secret_id=quote(str(secret_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | SecretsStoreServiceProblemDetails | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 400:
        response_400 = SecretsStoreServiceProblemDetails.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = SecretsStoreServiceProblemDetails.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = SecretsStoreServiceProblemDetails.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | SecretsStoreServiceProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    universe_id: int,
    secret_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | SecretsStoreServiceProblemDetails]:
    """Delete Secret

     Permanently deletes a secret from a universe.

    Only the owner of the universe can delete secrets. For group-owned universes, only the group owner
    or authorized
    members can delete secrets.

    This operation is irreversible. Make sure you no longer need the secret before deleting it.

    Args:
        universe_id (int):
        secret_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SecretsStoreServiceProblemDetails]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        secret_id=secret_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: int,
    secret_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | SecretsStoreServiceProblemDetails | None:
    """Delete Secret

     Permanently deletes a secret from a universe.

    Only the owner of the universe can delete secrets. For group-owned universes, only the group owner
    or authorized
    members can delete secrets.

    This operation is irreversible. Make sure you no longer need the secret before deleting it.

    Args:
        universe_id (int):
        secret_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SecretsStoreServiceProblemDetails
    """

    return sync_detailed(
        universe_id=universe_id,
        secret_id=secret_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    universe_id: int,
    secret_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | SecretsStoreServiceProblemDetails]:
    """Delete Secret

     Permanently deletes a secret from a universe.

    Only the owner of the universe can delete secrets. For group-owned universes, only the group owner
    or authorized
    members can delete secrets.

    This operation is irreversible. Make sure you no longer need the secret before deleting it.

    Args:
        universe_id (int):
        secret_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | SecretsStoreServiceProblemDetails]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        secret_id=secret_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: int,
    secret_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | SecretsStoreServiceProblemDetails | None:
    """Delete Secret

     Permanently deletes a secret from a universe.

    Only the owner of the universe can delete secrets. For group-owned universes, only the group owner
    or authorized
    members can delete secrets.

    This operation is irreversible. Make sure you no longer need the secret before deleting it.

    Args:
        universe_id (int):
        secret_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | SecretsStoreServiceProblemDetails
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            secret_id=secret_id,
            client=client,
        )
    ).parsed
