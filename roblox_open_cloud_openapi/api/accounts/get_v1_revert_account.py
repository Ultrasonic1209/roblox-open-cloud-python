import sys
from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response

if sys.version_info >= (3, 13):
    from warnings import deprecated
else:
    from typing_extensions import deprecated

from ...models.roblox_authentication_api_models_revert_account_info_response import (
    RobloxAuthenticationApiModelsRevertAccountInfoResponse,
)


def _get_kwargs(
    *,
    ticket: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["ticket"] = ticket

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://auth.roblox.com/v1/revert/account",
        "params": params,
        "openapi-extensions": {
            "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            "x-roblox-recommended-alternatives": [
                {
                    "url": "https://auth.roblox.com/v2/revert/account",
                    "httpMethod": "GET",
                    "documentationUrl": "https://create.roblox.com/docs/cloud/reference/features/accounts#auth_get_v2_revert_account",
                }
            ],
        },
        "openapi-id": "get_v1_revert_account",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxAuthenticationApiModelsRevertAccountInfoResponse | None:
    if response.status_code == 200:
        response_200 = RobloxAuthenticationApiModelsRevertAccountInfoResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxAuthenticationApiModelsRevertAccountInfoResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/accounts#auth_get_v1_revert_account"
)
def sync_detailed(
    *,
    client: AuthenticatedClient,
    ticket: str,
) -> Response[Any | RobloxAuthenticationApiModelsRevertAccountInfoResponse]:
    """Get Revert Account ticket info

    Args:
        ticket (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxAuthenticationApiModelsRevertAccountInfoResponse]
    """

    kwargs = _get_kwargs(
        ticket=ticket,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/accounts#auth_get_v1_revert_account"
)
def sync(
    *,
    client: AuthenticatedClient,
    ticket: str,
) -> Any | RobloxAuthenticationApiModelsRevertAccountInfoResponse | None:
    """Get Revert Account ticket info

    Args:
        ticket (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxAuthenticationApiModelsRevertAccountInfoResponse
    """

    return sync_detailed(
        client=client,
        ticket=ticket,
    ).parsed


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/accounts#auth_get_v1_revert_account"
)
async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ticket: str,
) -> Response[Any | RobloxAuthenticationApiModelsRevertAccountInfoResponse]:
    """Get Revert Account ticket info

    Args:
        ticket (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxAuthenticationApiModelsRevertAccountInfoResponse]
    """

    kwargs = _get_kwargs(
        ticket=ticket,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/accounts#auth_get_v1_revert_account"
)
async def asyncio(
    *,
    client: AuthenticatedClient,
    ticket: str,
) -> Any | RobloxAuthenticationApiModelsRevertAccountInfoResponse | None:
    """Get Revert Account ticket info

    Args:
        ticket (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxAuthenticationApiModelsRevertAccountInfoResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            ticket=ticket,
        )
    ).parsed
