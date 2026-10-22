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
from ...types import UNSET, Response

"""
{'x-roblox-stability': 'EXPERIMENTAL', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'MINUTE', 'maxInPeriod': 30}, 'perOauth2Authorization': {'period': 'MINUTE', 'maxInPeriod': 30}}, 'x-roblox-scopes': [{'name': 'universe.analytics.alert:write', 'targetResourceSpecifier': 'id'}], 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.alert_storage_resource_type import AlertStorageResourceType
from ...models.analytics_alert_control_plane_models_alert_detail_response import (
    AnalyticsAlertControlPlaneModelsAlertDetailResponse,
)
from ...models.analytics_alert_control_plane_models_create_alert_config_request import (
    AnalyticsAlertControlPlaneModelsCreateAlertConfigRequest,
)
from ...models.analytics_alert_control_plane_models_error_response import AnalyticsAlertControlPlaneModelsErrorResponse
from ...types import Unset


def _get_kwargs(
    resource_type: AlertStorageResourceType,
    resource_id: str,
    *,
    body: AnalyticsAlertControlPlaneModelsCreateAlertConfigRequest
    | AnalyticsAlertControlPlaneModelsCreateAlertConfigRequest
    | AnalyticsAlertControlPlaneModelsCreateAlertConfigRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/analytics-alert-control-plane/v1/resource/{resource_type}/id/{resource_id}/alerts".format(
            resource_type=quote(str(resource_type), safe=""),
            resource_id=quote(str(resource_id), safe=""),
        ),
    }

    if isinstance(body, AnalyticsAlertControlPlaneModelsCreateAlertConfigRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, AnalyticsAlertControlPlaneModelsCreateAlertConfigRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"
    if isinstance(body, AnalyticsAlertControlPlaneModelsCreateAlertConfigRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AnalyticsAlertControlPlaneModelsAlertDetailResponse | AnalyticsAlertControlPlaneModelsErrorResponse | None:
    if response.status_code == 201:
        response_201 = AnalyticsAlertControlPlaneModelsAlertDetailResponse.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = AnalyticsAlertControlPlaneModelsErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = AnalyticsAlertControlPlaneModelsErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = AnalyticsAlertControlPlaneModelsErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 409:
        response_409 = AnalyticsAlertControlPlaneModelsErrorResponse.from_dict(response.json())

        return response_409

    if response.status_code == 503:
        response_503 = AnalyticsAlertControlPlaneModelsErrorResponse.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AnalyticsAlertControlPlaneModelsAlertDetailResponse | AnalyticsAlertControlPlaneModelsErrorResponse]:
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
    body: AnalyticsAlertControlPlaneModelsCreateAlertConfigRequest
    | AnalyticsAlertControlPlaneModelsCreateAlertConfigRequest
    | AnalyticsAlertControlPlaneModelsCreateAlertConfigRequest
    | Unset = UNSET,
) -> Response[AnalyticsAlertControlPlaneModelsAlertDetailResponse | AnalyticsAlertControlPlaneModelsErrorResponse]:
    """Creates a new alert configuration for a resource.

     See the <a href="https://create.roblox.com/docs/cloud/guides/alerts/metrics">alerts guide</a> for
    supported metrics and dimensions.

    Args:
        resource_type (AlertStorageResourceType): The type of resource an alert is attached to.

            Universe
        resource_id (str):
        body (AnalyticsAlertControlPlaneModelsCreateAlertConfigRequest | Unset): Request body for
            creating a new alert configuration.
        body (AnalyticsAlertControlPlaneModelsCreateAlertConfigRequest | Unset): Request body for
            creating a new alert configuration.
        body (AnalyticsAlertControlPlaneModelsCreateAlertConfigRequest | Unset): Request body for
            creating a new alert configuration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsAlertControlPlaneModelsAlertDetailResponse | AnalyticsAlertControlPlaneModelsErrorResponse]
    """

    kwargs = _get_kwargs(
        resource_type=resource_type,
        resource_id=resource_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    resource_type: AlertStorageResourceType,
    resource_id: str,
    *,
    client: AuthenticatedClient,
    body: AnalyticsAlertControlPlaneModelsCreateAlertConfigRequest
    | AnalyticsAlertControlPlaneModelsCreateAlertConfigRequest
    | AnalyticsAlertControlPlaneModelsCreateAlertConfigRequest
    | Unset = UNSET,
) -> AnalyticsAlertControlPlaneModelsAlertDetailResponse | AnalyticsAlertControlPlaneModelsErrorResponse | None:
    """Creates a new alert configuration for a resource.

     See the <a href="https://create.roblox.com/docs/cloud/guides/alerts/metrics">alerts guide</a> for
    supported metrics and dimensions.

    Args:
        resource_type (AlertStorageResourceType): The type of resource an alert is attached to.

            Universe
        resource_id (str):
        body (AnalyticsAlertControlPlaneModelsCreateAlertConfigRequest | Unset): Request body for
            creating a new alert configuration.
        body (AnalyticsAlertControlPlaneModelsCreateAlertConfigRequest | Unset): Request body for
            creating a new alert configuration.
        body (AnalyticsAlertControlPlaneModelsCreateAlertConfigRequest | Unset): Request body for
            creating a new alert configuration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsAlertControlPlaneModelsAlertDetailResponse | AnalyticsAlertControlPlaneModelsErrorResponse
    """

    return sync_detailed(
        resource_type=resource_type,
        resource_id=resource_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    resource_type: AlertStorageResourceType,
    resource_id: str,
    *,
    client: AuthenticatedClient,
    body: AnalyticsAlertControlPlaneModelsCreateAlertConfigRequest
    | AnalyticsAlertControlPlaneModelsCreateAlertConfigRequest
    | AnalyticsAlertControlPlaneModelsCreateAlertConfigRequest
    | Unset = UNSET,
) -> Response[AnalyticsAlertControlPlaneModelsAlertDetailResponse | AnalyticsAlertControlPlaneModelsErrorResponse]:
    """Creates a new alert configuration for a resource.

     See the <a href="https://create.roblox.com/docs/cloud/guides/alerts/metrics">alerts guide</a> for
    supported metrics and dimensions.

    Args:
        resource_type (AlertStorageResourceType): The type of resource an alert is attached to.

            Universe
        resource_id (str):
        body (AnalyticsAlertControlPlaneModelsCreateAlertConfigRequest | Unset): Request body for
            creating a new alert configuration.
        body (AnalyticsAlertControlPlaneModelsCreateAlertConfigRequest | Unset): Request body for
            creating a new alert configuration.
        body (AnalyticsAlertControlPlaneModelsCreateAlertConfigRequest | Unset): Request body for
            creating a new alert configuration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsAlertControlPlaneModelsAlertDetailResponse | AnalyticsAlertControlPlaneModelsErrorResponse]
    """

    kwargs = _get_kwargs(
        resource_type=resource_type,
        resource_id=resource_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    resource_type: AlertStorageResourceType,
    resource_id: str,
    *,
    client: AuthenticatedClient,
    body: AnalyticsAlertControlPlaneModelsCreateAlertConfigRequest
    | AnalyticsAlertControlPlaneModelsCreateAlertConfigRequest
    | AnalyticsAlertControlPlaneModelsCreateAlertConfigRequest
    | Unset = UNSET,
) -> AnalyticsAlertControlPlaneModelsAlertDetailResponse | AnalyticsAlertControlPlaneModelsErrorResponse | None:
    """Creates a new alert configuration for a resource.

     See the <a href="https://create.roblox.com/docs/cloud/guides/alerts/metrics">alerts guide</a> for
    supported metrics and dimensions.

    Args:
        resource_type (AlertStorageResourceType): The type of resource an alert is attached to.

            Universe
        resource_id (str):
        body (AnalyticsAlertControlPlaneModelsCreateAlertConfigRequest | Unset): Request body for
            creating a new alert configuration.
        body (AnalyticsAlertControlPlaneModelsCreateAlertConfigRequest | Unset): Request body for
            creating a new alert configuration.
        body (AnalyticsAlertControlPlaneModelsCreateAlertConfigRequest | Unset): Request body for
            creating a new alert configuration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsAlertControlPlaneModelsAlertDetailResponse | AnalyticsAlertControlPlaneModelsErrorResponse
    """

    return (
        await asyncio_detailed(
            resource_type=resource_type,
            resource_id=resource_id,
            client=client,
            body=body,
        )
    ).parsed
