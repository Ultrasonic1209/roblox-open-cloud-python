from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v1_universe_payout_history_response_200 import GetV1UniversePayoutHistoryResponse200
from ...types import UNSET, Response


def _get_kwargs(
    *,
    universe_id: int,
    start_date: str,
    end_date: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["universeId"] = universe_id

    params["startDate"] = start_date

    params["endDate"] = end_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://engagementpayouts.roblox.com/v1/universe-payout-history",
        "params": params,
        "extensions": {
            "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
            "openapi-id": "get_v1_universe-payout-history",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | GetV1UniversePayoutHistoryResponse200 | None:
    if response.status_code == 200:
        response_200 = GetV1UniversePayoutHistoryResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | GetV1UniversePayoutHistoryResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    universe_id: int,
    start_date: str,
    end_date: str,
) -> Response[Any | GetV1UniversePayoutHistoryResponse200]:
    """Gets the engagement payout history for a specific universe and a given date range, specified by
    start and end dates.

    Args:
        universe_id (int):
        start_date (str):
        end_date (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetV1UniversePayoutHistoryResponse200]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        start_date=start_date,
        end_date=end_date,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    universe_id: int,
    start_date: str,
    end_date: str,
) -> Any | GetV1UniversePayoutHistoryResponse200 | None:
    """Gets the engagement payout history for a specific universe and a given date range, specified by
    start and end dates.

    Args:
        universe_id (int):
        start_date (str):
        end_date (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetV1UniversePayoutHistoryResponse200
    """

    return sync_detailed(
        client=client,
        universe_id=universe_id,
        start_date=start_date,
        end_date=end_date,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    universe_id: int,
    start_date: str,
    end_date: str,
) -> Response[Any | GetV1UniversePayoutHistoryResponse200]:
    """Gets the engagement payout history for a specific universe and a given date range, specified by
    start and end dates.

    Args:
        universe_id (int):
        start_date (str):
        end_date (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetV1UniversePayoutHistoryResponse200]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        start_date=start_date,
        end_date=end_date,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    universe_id: int,
    start_date: str,
    end_date: str,
) -> Any | GetV1UniversePayoutHistoryResponse200 | None:
    """Gets the engagement payout history for a specific universe and a given date range, specified by
    start and end dates.

    Args:
        universe_id (int):
        start_date (str):
        end_date (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetV1UniversePayoutHistoryResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            universe_id=universe_id,
            start_date=start_date,
            end_date=end_date,
        )
    ).parsed
