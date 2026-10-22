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


from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response

"""
{'x-roblox-stability': 'EXPERIMENTAL', 'x-roblox-rate-limits': {'perApiKeyOwner': {'period': 'MINUTE', 'maxInPeriod': 300}, 'perOauth2Authorization': {'period': 'MINUTE', 'maxInPeriod': 300}}, 'x-roblox-scopes': [{'name': 'universe.analytics:read', 'targetResourceSpecifier': 'universes'}], 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""


from ...models.analytics_benchmark_api_status import AnalyticsBenchmarkApiStatus
from ...models.benchmark_query import BenchmarkQuery
from ...models.query_universe_benchmark_response import QueryUniverseBenchmarkResponse
from ...types import Unset


def _get_kwargs(
    universe_id: int,
    *,
    body: BenchmarkQuery | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/analytics-benchmark/v1/universes/{universe_id}/benchmarks".format(
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
) -> AnalyticsBenchmarkApiStatus | QueryUniverseBenchmarkResponse:
    if response.status_code == 200:
        response_200 = QueryUniverseBenchmarkResponse.from_dict(response.json())

        return response_200

    response_default = AnalyticsBenchmarkApiStatus.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AnalyticsBenchmarkApiStatus | QueryUniverseBenchmarkResponse]:
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
    body: BenchmarkQuery | Unset = UNSET,
) -> Response[AnalyticsBenchmarkApiStatus | QueryUniverseBenchmarkResponse]:
    """Returns daily benchmark percentiles for a metric, comparing a universe against other experiences on
    Roblox.

     See [Analytics Guide](https://create.roblox.com/docs/cloud/guides/analytics) for more information.

    Args:
        universe_id (int):
        body (BenchmarkQuery | Unset): BenchmarkQuery is the request object for the benchmark
            query.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsBenchmarkApiStatus | QueryUniverseBenchmarkResponse]
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
    body: BenchmarkQuery | Unset = UNSET,
) -> AnalyticsBenchmarkApiStatus | QueryUniverseBenchmarkResponse | None:
    """Returns daily benchmark percentiles for a metric, comparing a universe against other experiences on
    Roblox.

     See [Analytics Guide](https://create.roblox.com/docs/cloud/guides/analytics) for more information.

    Args:
        universe_id (int):
        body (BenchmarkQuery | Unset): BenchmarkQuery is the request object for the benchmark
            query.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsBenchmarkApiStatus | QueryUniverseBenchmarkResponse
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
    body: BenchmarkQuery | Unset = UNSET,
) -> Response[AnalyticsBenchmarkApiStatus | QueryUniverseBenchmarkResponse]:
    """Returns daily benchmark percentiles for a metric, comparing a universe against other experiences on
    Roblox.

     See [Analytics Guide](https://create.roblox.com/docs/cloud/guides/analytics) for more information.

    Args:
        universe_id (int):
        body (BenchmarkQuery | Unset): BenchmarkQuery is the request object for the benchmark
            query.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsBenchmarkApiStatus | QueryUniverseBenchmarkResponse]
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
    body: BenchmarkQuery | Unset = UNSET,
) -> AnalyticsBenchmarkApiStatus | QueryUniverseBenchmarkResponse | None:
    """Returns daily benchmark percentiles for a metric, comparing a universe against other experiences on
    Roblox.

     See [Analytics Guide](https://create.roblox.com/docs/cloud/guides/analytics) for more information.

    Args:
        universe_id (int):
        body (BenchmarkQuery | Unset): BenchmarkQuery is the request object for the benchmark
            query.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsBenchmarkApiStatus | QueryUniverseBenchmarkResponse
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            client=client,
            body=body,
        )
    ).parsed
