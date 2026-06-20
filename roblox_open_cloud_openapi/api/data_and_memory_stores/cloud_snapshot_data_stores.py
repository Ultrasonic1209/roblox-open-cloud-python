from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.snapshot_data_stores_request import SnapshotDataStoresRequest
from ...models.snapshot_data_stores_response import SnapshotDataStoresResponse
from ...types import Response


def _get_kwargs(
    universe_id: str,
    *,
    body: SnapshotDataStoresRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/cloud/v2/universes/{universe_id}/data-stores:snapshot".format(
            universe_id=quote(str(universe_id), safe=""),
        ),
        "extensions": {
            "openapi-extensions": {
                "x-roblox-engine-usability": {"apiKeyWithHttpService": True},
                "x-roblox-rate-limits": {
                    "description": "Data stores requests are subject to additional throttling limits described in the [Open Cloud guide for data stores](https://create.roblox.com/docs/cloud/guides/data-stores/throttling).",
                    "perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 60},
                },
                "x-roblox-scopes": [{"name": "universe-datastores.control:snapshot"}],
                "x-roblox-docs": {
                    "category": "Data and memory stores",
                    "methodProperties": {"scopes": ["universe-datastores.control:snapshot"]},
                    "resource": {"$ref": "#/components/schemas/DataStore", "name": "DataStore"},
                },
                "x-roblox-stability": "STABLE",
            },
            "openapi-id": "Cloud_SnapshotDataStores",
        },
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> SnapshotDataStoresResponse | None:
    if response.status_code == 200:
        response_200 = SnapshotDataStoresResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[SnapshotDataStoresResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    universe_id: str,
    *,
    client: AuthenticatedClient,
    body: SnapshotDataStoresRequest,
) -> Response[SnapshotDataStoresResponse]:
    """Snapshot Data Stores

     Takes a new snapshot of the data stores in an experience.

    After a snapshot, the next write to every key in the experience will
    create a versioned backup of the previous data, regardless of the time of
    the last write.

    In effect, all data current at the time of the snapshot is guaranteed to be
    available as a versioned backup for at least 30 days.

    Snapshots can be taken once per UTC day, per experience. If the latest
    snapshot was taken within the same UTC day, this operation is a no-op and
    the time of the latest snapshot will be returned.

    For more information on using snapshots, see the [Data
    stores](https://create.roblox.com/docs/cloud-services/data-stores#snapshots)
    Engine guide.

    Args:
        universe_id (str):
        body (SnapshotDataStoresRequest): Takes a new snapshot for the given experience.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SnapshotDataStoresResponse]
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
    universe_id: str,
    *,
    client: AuthenticatedClient,
    body: SnapshotDataStoresRequest,
) -> SnapshotDataStoresResponse | None:
    """Snapshot Data Stores

     Takes a new snapshot of the data stores in an experience.

    After a snapshot, the next write to every key in the experience will
    create a versioned backup of the previous data, regardless of the time of
    the last write.

    In effect, all data current at the time of the snapshot is guaranteed to be
    available as a versioned backup for at least 30 days.

    Snapshots can be taken once per UTC day, per experience. If the latest
    snapshot was taken within the same UTC day, this operation is a no-op and
    the time of the latest snapshot will be returned.

    For more information on using snapshots, see the [Data
    stores](https://create.roblox.com/docs/cloud-services/data-stores#snapshots)
    Engine guide.

    Args:
        universe_id (str):
        body (SnapshotDataStoresRequest): Takes a new snapshot for the given experience.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SnapshotDataStoresResponse
    """

    return sync_detailed(
        universe_id=universe_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    universe_id: str,
    *,
    client: AuthenticatedClient,
    body: SnapshotDataStoresRequest,
) -> Response[SnapshotDataStoresResponse]:
    """Snapshot Data Stores

     Takes a new snapshot of the data stores in an experience.

    After a snapshot, the next write to every key in the experience will
    create a versioned backup of the previous data, regardless of the time of
    the last write.

    In effect, all data current at the time of the snapshot is guaranteed to be
    available as a versioned backup for at least 30 days.

    Snapshots can be taken once per UTC day, per experience. If the latest
    snapshot was taken within the same UTC day, this operation is a no-op and
    the time of the latest snapshot will be returned.

    For more information on using snapshots, see the [Data
    stores](https://create.roblox.com/docs/cloud-services/data-stores#snapshots)
    Engine guide.

    Args:
        universe_id (str):
        body (SnapshotDataStoresRequest): Takes a new snapshot for the given experience.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SnapshotDataStoresResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: str,
    *,
    client: AuthenticatedClient,
    body: SnapshotDataStoresRequest,
) -> SnapshotDataStoresResponse | None:
    """Snapshot Data Stores

     Takes a new snapshot of the data stores in an experience.

    After a snapshot, the next write to every key in the experience will
    create a versioned backup of the previous data, regardless of the time of
    the last write.

    In effect, all data current at the time of the snapshot is guaranteed to be
    available as a versioned backup for at least 30 days.

    Snapshots can be taken once per UTC day, per experience. If the latest
    snapshot was taken within the same UTC day, this operation is a no-op and
    the time of the latest snapshot will be returned.

    For more information on using snapshots, see the [Data
    stores](https://create.roblox.com/docs/cloud-services/data-stores#snapshots)
    Engine guide.

    Args:
        universe_id (str):
        body (SnapshotDataStoresRequest): Takes a new snapshot for the given experience.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SnapshotDataStoresResponse
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            client=client,
            body=body,
        )
    ).parsed
