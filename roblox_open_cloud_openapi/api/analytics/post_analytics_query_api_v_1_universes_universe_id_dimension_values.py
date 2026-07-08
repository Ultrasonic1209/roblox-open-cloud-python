from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dimension_values_operation_result import DimensionValuesOperationResult
from ...models.dimension_values_request import DimensionValuesRequest
from ...models.operation_error import OperationError
from ...models.operation_pending import OperationPending
from ...types import UNSET, Response, Unset


def _get_kwargs(
    universe_id: int,
    *,
    body: DimensionValuesRequest | DimensionValuesRequest | DimensionValuesRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/analytics-query-api/v1/universes/{universe_id}/dimension-values".format(
            universe_id=quote(str(universe_id), safe=""),
        ),
        "extensions": {
            "openapi-extensions": {
                "x-roblox-stability": "BETA",
                "x-roblox-rate-limits": {"perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 30}},
                "x-roblox-scopes": [{"name": "universe.analytics:read", "targetResourceSpecifier": "universes"}],
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            },
            "openapi-id": "post_analytics-query-api_v1_universes_universeId_dimension-values",
        },
    }

    if isinstance(body, DimensionValuesRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, DimensionValuesRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"
    if isinstance(body, DimensionValuesRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
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

    if response.status_code == 403:
        response_403 = OperationError.from_dict(response.json())

        return response_403

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
    *,
    client: AuthenticatedClient,
    body: DimensionValuesRequest | DimensionValuesRequest | DimensionValuesRequest | Unset = UNSET,
) -> Response[DimensionValuesOperationResult | OperationError | OperationPending]:
    r"""Queries dimension values for a universe.

     See the <a href=\"https://create.roblox.com/docs/cloud/guides/analytics\">Analytics guide</a> for
    more information.

    Args:
        universe_id (int):
        body (DimensionValuesRequest): A request to query dimension values.
        body (DimensionValuesRequest): A request to query dimension values.
        body (DimensionValuesRequest): A request to query dimension values.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DimensionValuesOperationResult | OperationError | OperationPending]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        body=body,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    body: DimensionValuesRequest | DimensionValuesRequest | DimensionValuesRequest | Unset = UNSET,
) -> DimensionValuesOperationResult | OperationError | OperationPending | None:
    r"""Queries dimension values for a universe.

     See the <a href=\"https://create.roblox.com/docs/cloud/guides/analytics\">Analytics guide</a> for
    more information.

    Args:
        universe_id (int):
        body (DimensionValuesRequest): A request to query dimension values.
        body (DimensionValuesRequest): A request to query dimension values.
        body (DimensionValuesRequest): A request to query dimension values.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DimensionValuesOperationResult | OperationError | OperationPending
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
    body: DimensionValuesRequest | DimensionValuesRequest | DimensionValuesRequest | Unset = UNSET,
) -> Response[DimensionValuesOperationResult | OperationError | OperationPending]:
    r"""Queries dimension values for a universe.

     See the <a href=\"https://create.roblox.com/docs/cloud/guides/analytics\">Analytics guide</a> for
    more information.

    Args:
        universe_id (int):
        body (DimensionValuesRequest): A request to query dimension values.
        body (DimensionValuesRequest): A request to query dimension values.
        body (DimensionValuesRequest): A request to query dimension values.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DimensionValuesOperationResult | OperationError | OperationPending]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: int,
    *,
    client: AuthenticatedClient,
    body: DimensionValuesRequest | DimensionValuesRequest | DimensionValuesRequest | Unset = UNSET,
) -> DimensionValuesOperationResult | OperationError | OperationPending | None:
    r"""Queries dimension values for a universe.

     See the <a href=\"https://create.roblox.com/docs/cloud/guides/analytics\">Analytics guide</a> for
    more information.

    Args:
        universe_id (int):
        body (DimensionValuesRequest): A request to query dimension values.
        body (DimensionValuesRequest): A request to query dimension values.
        body (DimensionValuesRequest): A request to query dimension values.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DimensionValuesOperationResult | OperationError | OperationPending
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            client=client,
            body=body,
        )
    ).parsed
