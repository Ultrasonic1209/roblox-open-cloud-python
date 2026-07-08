from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dimension_values_operation_result import DimensionValuesOperationResult
from ...models.operation_error import OperationError
from ...models.operation_pending import OperationPending
from ...types import Response


def _get_kwargs(
    universe_id: int,
    operation_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/analytics-query-api/v1/universes/{universe_id}/operations/dimension-values/{operation_id}".format(
            universe_id=quote(str(universe_id), safe=""),
            operation_id=quote(str(operation_id), safe=""),
        ),
        "extensions": {
            "openapi-extensions": {
                "x-roblox-stability": "BETA",
                "x-roblox-rate-limits": {"perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 3000}},
                "x-roblox-scopes": [{"name": "universe.analytics:read", "targetResourceSpecifier": "universes"}],
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            },
            "openapi-id": "get_analytics-query-api_v1_universes_universeId_operations_dimension-values_operationId",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> DimensionValuesOperationResult | OperationError | OperationPending | None:
    if response.status_code == 200:
        response_200 = DimensionValuesOperationResult.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = OperationPending.from_dict(response.json())

        return response_202

    if response.status_code == 400:
        response_400 = OperationError.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = OperationError.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = OperationError.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = OperationError.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = OperationError.from_dict(response.json())

        return response_503

    if response.status_code == 504:
        response_504 = OperationError.from_dict(response.json())

        return response_504

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[DimensionValuesOperationResult | OperationError | OperationPending]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    universe_id: int,
    operation_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[DimensionValuesOperationResult | OperationError | OperationPending]:
    r"""Retrieves the result of a long-running dimension values operation.

     See the <a href=\"https://create.roblox.com/docs/cloud/guides/analytics\">Analytics guide</a> for
    more information.

    Args:
        universe_id (int):
        operation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DimensionValuesOperationResult | OperationError | OperationPending]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        operation_id=operation_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: int,
    operation_id: str,
    *,
    client: AuthenticatedClient,
) -> DimensionValuesOperationResult | OperationError | OperationPending | None:
    r"""Retrieves the result of a long-running dimension values operation.

     See the <a href=\"https://create.roblox.com/docs/cloud/guides/analytics\">Analytics guide</a> for
    more information.

    Args:
        universe_id (int):
        operation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DimensionValuesOperationResult | OperationError | OperationPending
    """

    return sync_detailed(
        universe_id=universe_id,
        operation_id=operation_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    universe_id: int,
    operation_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[DimensionValuesOperationResult | OperationError | OperationPending]:
    r"""Retrieves the result of a long-running dimension values operation.

     See the <a href=\"https://create.roblox.com/docs/cloud/guides/analytics\">Analytics guide</a> for
    more information.

    Args:
        universe_id (int):
        operation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DimensionValuesOperationResult | OperationError | OperationPending]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        operation_id=operation_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: int,
    operation_id: str,
    *,
    client: AuthenticatedClient,
) -> DimensionValuesOperationResult | OperationError | OperationPending | None:
    r"""Retrieves the result of a long-running dimension values operation.

     See the <a href=\"https://create.roblox.com/docs/cloud/guides/analytics\">Analytics guide</a> for
    more information.

    Args:
        universe_id (int):
        operation_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DimensionValuesOperationResult | OperationError | OperationPending
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            operation_id=operation_id,
            client=client,
        )
    ).parsed
