from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.secret_paginated_list import SecretPaginatedList
from ...models.secrets_store_service_problem_details import SecretsStoreServiceProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    universe_id: int,
    *,
    limit: int | Unset = 10,
    cursor: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/cloud/v2/universes/{universe_id}/secrets".format(
            universe_id=quote(str(universe_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> SecretPaginatedList | SecretsStoreServiceProblemDetails | None:
    if response.status_code == 200:
        response_200 = SecretPaginatedList.from_dict(response.json())

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
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[SecretPaginatedList | SecretsStoreServiceProblemDetails]:
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
    limit: int | Unset = 10,
    cursor: str | Unset = UNSET,
) -> Response[SecretPaginatedList | SecretsStoreServiceProblemDetails]:
    """List Secrets

     Lists all secrets defined for a universe.
    Secret content is not returned for security reasons - only metadata such as ID, domain, creation and
    update timestamps are included.

    Only the owner of the universe can list secrets. For group-owned universes, only the group owner or
    authorized
    members can list secrets.

    Args:
        universe_id (int):
        limit (int | Unset):  Default: 10.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SecretPaginatedList | SecretsStoreServiceProblemDetails]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        limit=limit,
        cursor=cursor,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 10,
    cursor: str | Unset = UNSET,
) -> SecretPaginatedList | SecretsStoreServiceProblemDetails | None:
    """List Secrets

     Lists all secrets defined for a universe.
    Secret content is not returned for security reasons - only metadata such as ID, domain, creation and
    update timestamps are included.

    Only the owner of the universe can list secrets. For group-owned universes, only the group owner or
    authorized
    members can list secrets.

    Args:
        universe_id (int):
        limit (int | Unset):  Default: 10.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SecretPaginatedList | SecretsStoreServiceProblemDetails
    """

    return sync_detailed(
        universe_id=universe_id,
        client=client,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 10,
    cursor: str | Unset = UNSET,
) -> Response[SecretPaginatedList | SecretsStoreServiceProblemDetails]:
    """List Secrets

     Lists all secrets defined for a universe.
    Secret content is not returned for security reasons - only metadata such as ID, domain, creation and
    update timestamps are included.

    Only the owner of the universe can list secrets. For group-owned universes, only the group owner or
    authorized
    members can list secrets.

    Args:
        universe_id (int):
        limit (int | Unset):  Default: 10.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SecretPaginatedList | SecretsStoreServiceProblemDetails]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 10,
    cursor: str | Unset = UNSET,
) -> SecretPaginatedList | SecretsStoreServiceProblemDetails | None:
    """List Secrets

     Lists all secrets defined for a universe.
    Secret content is not returned for security reasons - only metadata such as ID, domain, creation and
    update timestamps are included.

    Only the owner of the universe can list secrets. For group-owned universes, only the group owner or
    authorized
    members can list secrets.

    Args:
        universe_id (int):
        limit (int | Unset):  Default: 10.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SecretPaginatedList | SecretsStoreServiceProblemDetails
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            client=client,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
