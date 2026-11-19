from http import HTTPStatus
from typing import TYPE_CHECKING, Any

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
{'x-roblox-recommended-alternatives': [{'url': 'https://apis.roblox.com/server-management/v1/universes/{universeId}/restarts:forecast', 'httpMethod': 'GET', 'description': 'Forecast a server restart using the universe ID in the URL instead of the request body.', 'documentationUrl': 'https://create.roblox.com/docs/cloud/reference/features/observability#Restarts_ForecastRestart'}], 'x-roblox-stability': 'BETA', 'x-roblox-engine-usability': {'apiKeyWithHttpService': False}}
"""

import sys

if sys.version_info >= (3, 13):
    from warnings import deprecated
else:
    from typing_extensions import deprecated

from ...models.forecast_update_request import ForecastUpdateRequest
from ...models.forecast_update_response import ForecastUpdateResponse
from ...types import Unset


def _get_kwargs(
    *,
    body: ForecastUpdateRequest | ForecastUpdateRequest | ForecastUpdateRequest | ForecastUpdateRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/matchmaking-api/v1/game-instances/forecast-update",
    }

    if isinstance(body, ForecastUpdateRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, ForecastUpdateRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, ForecastUpdateRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"
    if isinstance(body, ForecastUpdateRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ForecastUpdateResponse | None:
    if response.status_code == 200:
        response_200 = ForecastUpdateResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ForecastUpdateResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/matchmaking#post_matchmaking_api_v1_game_instances_forecast_update"
)
def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ForecastUpdateRequest | ForecastUpdateRequest | ForecastUpdateRequest | ForecastUpdateRequest | Unset = UNSET,
) -> Response[ForecastUpdateResponse]:
    """Forecast the outcome of launching an update

    Args:
        body (ForecastUpdateRequest | Unset): ForecastUpdateRequest is used to request an update
            to the forecast of a Place in a Universe.
        body (ForecastUpdateRequest | Unset): ForecastUpdateRequest is used to request an update
            to the forecast of a Place in a Universe.
        body (ForecastUpdateRequest | Unset): ForecastUpdateRequest is used to request an update
            to the forecast of a Place in a Universe.
        body (ForecastUpdateRequest | Unset): ForecastUpdateRequest is used to request an update
            to the forecast of a Place in a Universe.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ForecastUpdateResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/matchmaking#post_matchmaking_api_v1_game_instances_forecast_update"
)
def sync(
    *,
    client: AuthenticatedClient,
    body: ForecastUpdateRequest | ForecastUpdateRequest | ForecastUpdateRequest | ForecastUpdateRequest | Unset = UNSET,
) -> ForecastUpdateResponse | None:
    """Forecast the outcome of launching an update

    Args:
        body (ForecastUpdateRequest | Unset): ForecastUpdateRequest is used to request an update
            to the forecast of a Place in a Universe.
        body (ForecastUpdateRequest | Unset): ForecastUpdateRequest is used to request an update
            to the forecast of a Place in a Universe.
        body (ForecastUpdateRequest | Unset): ForecastUpdateRequest is used to request an update
            to the forecast of a Place in a Universe.
        body (ForecastUpdateRequest | Unset): ForecastUpdateRequest is used to request an update
            to the forecast of a Place in a Universe.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ForecastUpdateResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/matchmaking#post_matchmaking_api_v1_game_instances_forecast_update"
)
async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ForecastUpdateRequest | ForecastUpdateRequest | ForecastUpdateRequest | ForecastUpdateRequest | Unset = UNSET,
) -> Response[ForecastUpdateResponse]:
    """Forecast the outcome of launching an update

    Args:
        body (ForecastUpdateRequest | Unset): ForecastUpdateRequest is used to request an update
            to the forecast of a Place in a Universe.
        body (ForecastUpdateRequest | Unset): ForecastUpdateRequest is used to request an update
            to the forecast of a Place in a Universe.
        body (ForecastUpdateRequest | Unset): ForecastUpdateRequest is used to request an update
            to the forecast of a Place in a Universe.
        body (ForecastUpdateRequest | Unset): ForecastUpdateRequest is used to request an update
            to the forecast of a Place in a Universe.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ForecastUpdateResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/matchmaking#post_matchmaking_api_v1_game_instances_forecast_update"
)
async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ForecastUpdateRequest | ForecastUpdateRequest | ForecastUpdateRequest | ForecastUpdateRequest | Unset = UNSET,
) -> ForecastUpdateResponse | None:
    """Forecast the outcome of launching an update

    Args:
        body (ForecastUpdateRequest | Unset): ForecastUpdateRequest is used to request an update
            to the forecast of a Place in a Universe.
        body (ForecastUpdateRequest | Unset): ForecastUpdateRequest is used to request an update
            to the forecast of a Place in a Universe.
        body (ForecastUpdateRequest | Unset): ForecastUpdateRequest is used to request an update
            to the forecast of a Place in a Universe.
        body (ForecastUpdateRequest | Unset): ForecastUpdateRequest is used to request an update
            to the forecast of a Place in a Universe.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ForecastUpdateResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
