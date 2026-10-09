from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.alert_storage_resource_type import AlertStorageResourceType
from ...models.analytics_alert_control_plane_models_error_response import AnalyticsAlertControlPlaneModelsErrorResponse
from ...types import Response


def _get_kwargs(
    resource_type: AlertStorageResourceType,
    resource_id: str,
    alert_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/analytics-alert-control-plane/v1/resource/{resource_type}/id/{resource_id}/alerts/{alert_id}".format(
            resource_type=quote(str(resource_type), safe=""),
            resource_id=quote(str(resource_id), safe=""),
            alert_id=quote(str(alert_id), safe=""),
        ),
        "extensions": {
            "openapi-extensions": {
                "x-roblox-stability": "EXPERIMENTAL",
                "x-roblox-rate-limits": {
                    "perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 30},
                    "perOauth2Authorization": {"period": "MINUTE", "maxInPeriod": 30},
                },
                "x-roblox-scopes": [{"name": "universe.analytics.alert:write", "targetResourceSpecifier": "id"}],
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            },
            "openapi-id": "delete_analytics-alert-control-plane_v1_resource_resourceType_id_resourceId_alerts_alertId",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> AnalyticsAlertControlPlaneModelsErrorResponse | Any | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = AnalyticsAlertControlPlaneModelsErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = AnalyticsAlertControlPlaneModelsErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = AnalyticsAlertControlPlaneModelsErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = AnalyticsAlertControlPlaneModelsErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 503:
        response_503 = AnalyticsAlertControlPlaneModelsErrorResponse.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[AnalyticsAlertControlPlaneModelsErrorResponse | Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    resource_type: AlertStorageResourceType,
    resource_id: str,
    alert_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[AnalyticsAlertControlPlaneModelsErrorResponse | Any]:
    """Deletes an alert configuration. This action is irreversible.

    Args:
        resource_type (AlertStorageResourceType): The type of resource an alert is attached to.

            Universe
        resource_id (str):
        alert_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsAlertControlPlaneModelsErrorResponse | Any]
    """

    kwargs = _get_kwargs(
        resource_type=resource_type,
        resource_id=resource_id,
        alert_id=alert_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    resource_type: AlertStorageResourceType,
    resource_id: str,
    alert_id: str,
    *,
    client: AuthenticatedClient,
) -> AnalyticsAlertControlPlaneModelsErrorResponse | Any | None:
    """Deletes an alert configuration. This action is irreversible.

    Args:
        resource_type (AlertStorageResourceType): The type of resource an alert is attached to.

            Universe
        resource_id (str):
        alert_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsAlertControlPlaneModelsErrorResponse | Any
    """

    return sync_detailed(
        resource_type=resource_type,
        resource_id=resource_id,
        alert_id=alert_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    resource_type: AlertStorageResourceType,
    resource_id: str,
    alert_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[AnalyticsAlertControlPlaneModelsErrorResponse | Any]:
    """Deletes an alert configuration. This action is irreversible.

    Args:
        resource_type (AlertStorageResourceType): The type of resource an alert is attached to.

            Universe
        resource_id (str):
        alert_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsAlertControlPlaneModelsErrorResponse | Any]
    """

    kwargs = _get_kwargs(
        resource_type=resource_type,
        resource_id=resource_id,
        alert_id=alert_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    resource_type: AlertStorageResourceType,
    resource_id: str,
    alert_id: str,
    *,
    client: AuthenticatedClient,
) -> AnalyticsAlertControlPlaneModelsErrorResponse | Any | None:
    """Deletes an alert configuration. This action is irreversible.

    Args:
        resource_type (AlertStorageResourceType): The type of resource an alert is attached to.

            Universe
        resource_id (str):
        alert_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsAlertControlPlaneModelsErrorResponse | Any
    """

    return (
        await asyncio_detailed(
            resource_type=resource_type,
            resource_id=resource_id,
            alert_id=alert_id,
            client=client,
        )
    ).parsed
