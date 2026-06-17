import sys
from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response

if sys.version_info >= (3, 13):
    from warnings import deprecated
else:
    from typing_extensions import deprecated

from ...models.roblox_localization_tables_api_get_limits_response import RobloxLocalizationTablesApiGetLimitsResponse


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://localizationtables.roblox.com/v1/localization-table/limits",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxLocalizationTablesApiGetLimitsResponse | None:
    if response.status_code == 200:
        response_200 = RobloxLocalizationTablesApiGetLimitsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxLocalizationTablesApiGetLimitsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/localization#localizationtables_get_v1_localization_table_limits"
)
def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxLocalizationTablesApiGetLimitsResponse]:
    """Get limits for translation table entries operations

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxLocalizationTablesApiGetLimitsResponse]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/localization#localizationtables_get_v1_localization_table_limits"
)
def sync(
    *,
    client: AuthenticatedClient,
) -> Any | RobloxLocalizationTablesApiGetLimitsResponse | None:
    """Get limits for translation table entries operations

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxLocalizationTablesApiGetLimitsResponse
    """

    return sync_detailed(
        client=client,
    ).parsed


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/localization#localizationtables_get_v1_localization_table_limits"
)
async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxLocalizationTablesApiGetLimitsResponse]:
    """Get limits for translation table entries operations

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxLocalizationTablesApiGetLimitsResponse]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/localization#localizationtables_get_v1_localization_table_limits"
)
async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Any | RobloxLocalizationTablesApiGetLimitsResponse | None:
    """Get limits for translation table entries operations

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxLocalizationTablesApiGetLimitsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
