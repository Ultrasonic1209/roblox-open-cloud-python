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
{'x-roblox-stability': 'BETA', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'MINUTE', 'maxInPeriod': 100}, 'perOauth2Authorization': {'period': 'MINUTE', 'maxInPeriod': 100}}, 'x-roblox-scopes': [{'name': 'universe.analytics.dashboard:read', 'targetResourceSpecifier': 'universes'}], 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.list_dashboards_response import ListDashboardsResponse
from ...models.open_cloud_error_response_of_custom_dashboard_error import OpenCloudErrorResponseOfCustomDashboardError
from ...types import Unset


def _get_kwargs(
    universe_id: int,
    *,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["pageSize"] = page_size

    params["pageToken"] = page_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/analytics-custom-dashboards/v1/universes/{universe_id}/custom-dashboards".format(
            universe_id=quote(str(universe_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListDashboardsResponse | OpenCloudErrorResponseOfCustomDashboardError | None:
    if response.status_code == 200:
        response_200 = ListDashboardsResponse.from_dict(response.json())

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
) -> Response[ListDashboardsResponse | OpenCloudErrorResponseOfCustomDashboardError]:
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
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> Response[ListDashboardsResponse | OpenCloudErrorResponseOfCustomDashboardError]:
    """Lists dashboard metadata for a universe.

    Args:
        universe_id (int):
        page_size (int | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListDashboardsResponse | OpenCloudErrorResponseOfCustomDashboardError]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        page_size=page_size,
        page_token=page_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> ListDashboardsResponse | OpenCloudErrorResponseOfCustomDashboardError | None:
    """Lists dashboard metadata for a universe.

    Args:
        universe_id (int):
        page_size (int | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListDashboardsResponse | OpenCloudErrorResponseOfCustomDashboardError
    """

    return sync_detailed(
        universe_id=universe_id,
        client=client,
        page_size=page_size,
        page_token=page_token,
    ).parsed


async def asyncio_detailed(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> Response[ListDashboardsResponse | OpenCloudErrorResponseOfCustomDashboardError]:
    """Lists dashboard metadata for a universe.

    Args:
        universe_id (int):
        page_size (int | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListDashboardsResponse | OpenCloudErrorResponseOfCustomDashboardError]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        page_size=page_size,
        page_token=page_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    page_size: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> ListDashboardsResponse | OpenCloudErrorResponseOfCustomDashboardError | None:
    """Lists dashboard metadata for a universe.

    Args:
        universe_id (int):
        page_size (int | Unset):
        page_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListDashboardsResponse | OpenCloudErrorResponseOfCustomDashboardError
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            client=client,
            page_size=page_size,
            page_token=page_token,
        )
    ).parsed
