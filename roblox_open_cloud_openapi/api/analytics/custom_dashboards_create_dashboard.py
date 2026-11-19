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
{'x-roblox-stability': 'BETA', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'MINUTE', 'maxInPeriod': 50}, 'perOauth2Authorization': {'period': 'MINUTE', 'maxInPeriod': 50}}, 'x-roblox-scopes': [{'name': 'universe.analytics.dashboard:write', 'targetResourceSpecifier': 'universes'}], 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.create_dashboard_response import CreateDashboardResponse
from ...models.custom_dashboards_create_dashboard_json_body import CustomDashboardsCreateDashboardJsonBody
from ...models.open_cloud_error_response_of_custom_dashboard_error import OpenCloudErrorResponseOfCustomDashboardError
from ...types import Unset


def _get_kwargs(
    universe_id: int,
    *,
    body: CustomDashboardsCreateDashboardJsonBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/analytics-custom-dashboards/v1/universes/{universe_id}/custom-dashboards".format(
            universe_id=quote(str(universe_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateDashboardResponse | OpenCloudErrorResponseOfCustomDashboardError | None:
    if response.status_code == 200:
        response_200 = CreateDashboardResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = OpenCloudErrorResponseOfCustomDashboardError.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = OpenCloudErrorResponseOfCustomDashboardError.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = OpenCloudErrorResponseOfCustomDashboardError.from_dict(response.json())

        return response_403

    if response.status_code == 409:
        response_409 = OpenCloudErrorResponseOfCustomDashboardError.from_dict(response.json())

        return response_409

    if response.status_code == 429:
        response_429 = OpenCloudErrorResponseOfCustomDashboardError.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = OpenCloudErrorResponseOfCustomDashboardError.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = OpenCloudErrorResponseOfCustomDashboardError.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateDashboardResponse | OpenCloudErrorResponseOfCustomDashboardError]:
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
    body: CustomDashboardsCreateDashboardJsonBody | Unset = UNSET,
) -> Response[CreateDashboardResponse | OpenCloudErrorResponseOfCustomDashboardError]:
    """Creates a dashboard.

    Args:
        universe_id (int):
        body (CustomDashboardsCreateDashboardJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateDashboardResponse | OpenCloudErrorResponseOfCustomDashboardError]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    body: CustomDashboardsCreateDashboardJsonBody | Unset = UNSET,
) -> CreateDashboardResponse | OpenCloudErrorResponseOfCustomDashboardError | None:
    """Creates a dashboard.

    Args:
        universe_id (int):
        body (CustomDashboardsCreateDashboardJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateDashboardResponse | OpenCloudErrorResponseOfCustomDashboardError
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
    body: CustomDashboardsCreateDashboardJsonBody | Unset = UNSET,
) -> Response[CreateDashboardResponse | OpenCloudErrorResponseOfCustomDashboardError]:
    """Creates a dashboard.

    Args:
        universe_id (int):
        body (CustomDashboardsCreateDashboardJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateDashboardResponse | OpenCloudErrorResponseOfCustomDashboardError]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    body: CustomDashboardsCreateDashboardJsonBody | Unset = UNSET,
) -> CreateDashboardResponse | OpenCloudErrorResponseOfCustomDashboardError | None:
    """Creates a dashboard.

    Args:
        universe_id (int):
        body (CustomDashboardsCreateDashboardJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateDashboardResponse | OpenCloudErrorResponseOfCustomDashboardError
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            client=client,
            body=body,
        )
    ).parsed
