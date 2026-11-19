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
{'x-roblox-stability': 'BETA', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'MINUTE', 'maxInPeriod': 100}, 'perOauth2Authorization': {'period': 'MINUTE', 'maxInPeriod': 100}}, 'x-roblox-scopes': [{'name': 'universe.analytics.dashboard:read', 'targetResourceSpecifier': 'universes'}], 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.get_dashboard_response import GetDashboardResponse
from ...models.open_cloud_error_response_of_custom_dashboard_error import OpenCloudErrorResponseOfCustomDashboardError


def _get_kwargs(
    universe_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/analytics-custom-dashboards/v1/universes/{universe_id}/custom-dashboards/pinned".format(
            universe_id=quote(str(universe_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetDashboardResponse | OpenCloudErrorResponseOfCustomDashboardError | None:
    if response.status_code == 200:
        response_200 = GetDashboardResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = OpenCloudErrorResponseOfCustomDashboardError.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = OpenCloudErrorResponseOfCustomDashboardError.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = OpenCloudErrorResponseOfCustomDashboardError.from_dict(response.json())

        return response_404

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
) -> Response[GetDashboardResponse | OpenCloudErrorResponseOfCustomDashboardError]:
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
) -> Response[GetDashboardResponse | OpenCloudErrorResponseOfCustomDashboardError]:
    """Gets the latest published dashboard snapshot.

    Args:
        universe_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetDashboardResponse | OpenCloudErrorResponseOfCustomDashboardError]
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
) -> GetDashboardResponse | OpenCloudErrorResponseOfCustomDashboardError | None:
    """Gets the latest published dashboard snapshot.

    Args:
        universe_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetDashboardResponse | OpenCloudErrorResponseOfCustomDashboardError
    """

    return sync_detailed(
        universe_id=universe_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    universe_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[GetDashboardResponse | OpenCloudErrorResponseOfCustomDashboardError]:
    """Gets the latest published dashboard snapshot.

    Args:
        universe_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetDashboardResponse | OpenCloudErrorResponseOfCustomDashboardError]
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
) -> GetDashboardResponse | OpenCloudErrorResponseOfCustomDashboardError | None:
    """Gets the latest published dashboard snapshot.

    Args:
        universe_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetDashboardResponse | OpenCloudErrorResponseOfCustomDashboardError
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            client=client,
        )
    ).parsed
