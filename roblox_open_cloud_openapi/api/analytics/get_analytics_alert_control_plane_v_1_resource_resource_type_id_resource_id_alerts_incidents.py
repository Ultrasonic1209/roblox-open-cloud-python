import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.alert_storage_resource_type import AlertStorageResourceType
from ...models.alert_storage_severity import AlertStorageSeverity
from ...models.analytics_alert_control_plane_models_error_response import AnalyticsAlertControlPlaneModelsErrorResponse
from ...models.analytics_alert_control_plane_models_incident_detail_response import (
    AnalyticsAlertControlPlaneModelsIncidentDetailResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    resource_type: AlertStorageResourceType,
    resource_id: str,
    *,
    start_time: datetime.datetime,
    end_time: datetime.datetime,
    metric: str | Unset = UNSET,
    alert_ids: list[str] | Unset = UNSET,
    severities: list[AlertStorageSeverity] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_start_time = start_time.isoformat()
    params["startTime"] = json_start_time

    json_end_time = end_time.isoformat()
    params["endTime"] = json_end_time

    params["metric"] = metric

    json_alert_ids: list[str] | Unset = UNSET
    if not isinstance(alert_ids, Unset):
        json_alert_ids = alert_ids

    params["alertIds"] = json_alert_ids

    json_severities: list[str] | Unset = UNSET
    if not isinstance(severities, Unset):
        json_severities = []
        for severities_item_data in severities:
            severities_item = severities_item_data.value
            json_severities.append(severities_item)

    params["severities"] = json_severities

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/analytics-alert-control-plane/v1/resource/{resource_type}/id/{resource_id}/alerts/incidents".format(
            resource_type=quote(str(resource_type), safe=""),
            resource_id=quote(str(resource_id), safe=""),
        ),
        "params": params,
        "extensions": {
            "openapi-extensions": {
                "x-roblox-stability": "EXPERIMENTAL",
                "x-roblox-rate-limits": {
                    "perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 120},
                    "perOauth2Authorization": {"period": "MINUTE", "maxInPeriod": 120},
                },
                "x-roblox-scopes": [{"name": "universe.analytics.alert:read", "targetResourceSpecifier": "id"}],
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            },
            "openapi-id": "get_analytics-alert-control-plane_v1_resource_resourceType_id_resourceId_alerts_incidents",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> (
    AnalyticsAlertControlPlaneModelsErrorResponse | list[AnalyticsAlertControlPlaneModelsIncidentDetailResponse] | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AnalyticsAlertControlPlaneModelsIncidentDetailResponse.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = AnalyticsAlertControlPlaneModelsErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = AnalyticsAlertControlPlaneModelsErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = AnalyticsAlertControlPlaneModelsErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 503:
        response_503 = AnalyticsAlertControlPlaneModelsErrorResponse.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[
    AnalyticsAlertControlPlaneModelsErrorResponse | list[AnalyticsAlertControlPlaneModelsIncidentDetailResponse]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    resource_type: AlertStorageResourceType,
    resource_id: str,
    *,
    client: AuthenticatedClient,
    start_time: datetime.datetime,
    end_time: datetime.datetime,
    metric: str | Unset = UNSET,
    alert_ids: list[str] | Unset = UNSET,
    severities: list[AlertStorageSeverity] | Unset = UNSET,
) -> Response[
    AnalyticsAlertControlPlaneModelsErrorResponse | list[AnalyticsAlertControlPlaneModelsIncidentDetailResponse]
]:
    """Returns alert incidents for a resource whose active window overlaps the specified time
    range. An incident is included if it was open at any point between `startTime` and
    `endTime`.

    Args:
        resource_type (AlertStorageResourceType): The type of resource an alert is attached to.

            Universe
        resource_id (str):
        start_time (datetime.datetime):
        end_time (datetime.datetime):
        metric (str | Unset):
        alert_ids (list[str] | Unset):
        severities (list[AlertStorageSeverity] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsAlertControlPlaneModelsErrorResponse | list[AnalyticsAlertControlPlaneModelsIncidentDetailResponse]]
    """

    kwargs = _get_kwargs(
        resource_type=resource_type,
        resource_id=resource_id,
        start_time=start_time,
        end_time=end_time,
        metric=metric,
        alert_ids=alert_ids,
        severities=severities,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    resource_type: AlertStorageResourceType,
    resource_id: str,
    *,
    client: AuthenticatedClient,
    start_time: datetime.datetime,
    end_time: datetime.datetime,
    metric: str | Unset = UNSET,
    alert_ids: list[str] | Unset = UNSET,
    severities: list[AlertStorageSeverity] | Unset = UNSET,
) -> (
    AnalyticsAlertControlPlaneModelsErrorResponse | list[AnalyticsAlertControlPlaneModelsIncidentDetailResponse] | None
):
    """Returns alert incidents for a resource whose active window overlaps the specified time
    range. An incident is included if it was open at any point between `startTime` and
    `endTime`.

    Args:
        resource_type (AlertStorageResourceType): The type of resource an alert is attached to.

            Universe
        resource_id (str):
        start_time (datetime.datetime):
        end_time (datetime.datetime):
        metric (str | Unset):
        alert_ids (list[str] | Unset):
        severities (list[AlertStorageSeverity] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsAlertControlPlaneModelsErrorResponse | list[AnalyticsAlertControlPlaneModelsIncidentDetailResponse]
    """

    return sync_detailed(
        resource_type=resource_type,
        resource_id=resource_id,
        client=client,
        start_time=start_time,
        end_time=end_time,
        metric=metric,
        alert_ids=alert_ids,
        severities=severities,
    ).parsed


async def asyncio_detailed(
    resource_type: AlertStorageResourceType,
    resource_id: str,
    *,
    client: AuthenticatedClient,
    start_time: datetime.datetime,
    end_time: datetime.datetime,
    metric: str | Unset = UNSET,
    alert_ids: list[str] | Unset = UNSET,
    severities: list[AlertStorageSeverity] | Unset = UNSET,
) -> Response[
    AnalyticsAlertControlPlaneModelsErrorResponse | list[AnalyticsAlertControlPlaneModelsIncidentDetailResponse]
]:
    """Returns alert incidents for a resource whose active window overlaps the specified time
    range. An incident is included if it was open at any point between `startTime` and
    `endTime`.

    Args:
        resource_type (AlertStorageResourceType): The type of resource an alert is attached to.

            Universe
        resource_id (str):
        start_time (datetime.datetime):
        end_time (datetime.datetime):
        metric (str | Unset):
        alert_ids (list[str] | Unset):
        severities (list[AlertStorageSeverity] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsAlertControlPlaneModelsErrorResponse | list[AnalyticsAlertControlPlaneModelsIncidentDetailResponse]]
    """

    kwargs = _get_kwargs(
        resource_type=resource_type,
        resource_id=resource_id,
        start_time=start_time,
        end_time=end_time,
        metric=metric,
        alert_ids=alert_ids,
        severities=severities,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    resource_type: AlertStorageResourceType,
    resource_id: str,
    *,
    client: AuthenticatedClient,
    start_time: datetime.datetime,
    end_time: datetime.datetime,
    metric: str | Unset = UNSET,
    alert_ids: list[str] | Unset = UNSET,
    severities: list[AlertStorageSeverity] | Unset = UNSET,
) -> (
    AnalyticsAlertControlPlaneModelsErrorResponse | list[AnalyticsAlertControlPlaneModelsIncidentDetailResponse] | None
):
    """Returns alert incidents for a resource whose active window overlaps the specified time
    range. An incident is included if it was open at any point between `startTime` and
    `endTime`.

    Args:
        resource_type (AlertStorageResourceType): The type of resource an alert is attached to.

            Universe
        resource_id (str):
        start_time (datetime.datetime):
        end_time (datetime.datetime):
        metric (str | Unset):
        alert_ids (list[str] | Unset):
        severities (list[AlertStorageSeverity] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsAlertControlPlaneModelsErrorResponse | list[AnalyticsAlertControlPlaneModelsIncidentDetailResponse]
    """

    return (
        await asyncio_detailed(
            resource_type=resource_type,
            resource_id=resource_id,
            client=client,
            start_time=start_time,
            end_time=end_time,
            metric=metric,
            alert_ids=alert_ids,
            severities=severities,
        )
    ).parsed
