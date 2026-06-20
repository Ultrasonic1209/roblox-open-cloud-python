from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.revenue_summary_response import RevenueSummaryResponse
from ...models.revenue_summary_time_frame import RevenueSummaryTimeFrame
from ...types import Response


def _get_kwargs(
    group_id: int,
    time_frame: RevenueSummaryTimeFrame,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://economy.roblox.com/v1/groups/{group_id}/revenue/summary/{time_frame}".format(
            group_id=quote(str(group_id), safe=""),
            time_frame=quote(str(time_frame), safe=""),
        ),
        "extensions": {
            "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
            "openapi-id": "RevenueSummary_GetGroupRevenueSummary",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> RevenueSummaryResponse | None:
    if response.status_code == 200:
        response_200 = RevenueSummaryResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[RevenueSummaryResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    group_id: int,
    time_frame: RevenueSummaryTimeFrame,
    *,
    client: AuthenticatedClient,
) -> Response[RevenueSummaryResponse]:
    """
    Args:
        group_id (int):
        time_frame (RevenueSummaryTimeFrame):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RevenueSummaryResponse]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        time_frame=time_frame,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: int,
    time_frame: RevenueSummaryTimeFrame,
    *,
    client: AuthenticatedClient,
) -> RevenueSummaryResponse | None:
    """
    Args:
        group_id (int):
        time_frame (RevenueSummaryTimeFrame):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RevenueSummaryResponse
    """

    return sync_detailed(
        group_id=group_id,
        time_frame=time_frame,
        client=client,
    ).parsed


async def asyncio_detailed(
    group_id: int,
    time_frame: RevenueSummaryTimeFrame,
    *,
    client: AuthenticatedClient,
) -> Response[RevenueSummaryResponse]:
    """
    Args:
        group_id (int):
        time_frame (RevenueSummaryTimeFrame):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RevenueSummaryResponse]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        time_frame=time_frame,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: int,
    time_frame: RevenueSummaryTimeFrame,
    *,
    client: AuthenticatedClient,
) -> RevenueSummaryResponse | None:
    """
    Args:
        group_id (int):
        time_frame (RevenueSummaryTimeFrame):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RevenueSummaryResponse
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            time_frame=time_frame,
            client=client,
        )
    ).parsed
