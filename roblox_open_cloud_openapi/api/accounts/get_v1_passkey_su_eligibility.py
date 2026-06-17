from http import HTTPStatus
from typing import Any, cast

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_authentication_api_models_response_silent_upgrade_eligibility_response import (
    RobloxAuthenticationApiModelsResponseSilentUpgradeEligibilityResponse,
)
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://auth.roblox.com/v1/passkey/su-eligibility",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxAuthenticationApiModelsResponseSilentUpgradeEligibilityResponse | None:
    if response.status_code == 200:
        response_200 = RobloxAuthenticationApiModelsResponseSilentUpgradeEligibilityResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxAuthenticationApiModelsResponseSilentUpgradeEligibilityResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxAuthenticationApiModelsResponseSilentUpgradeEligibilityResponse]:
    r"""Checks whether the authenticated user is eligible for silent passkey upgrade.
    Route and response are intentionally obfuscated (\"su-eligibility\" = \"silent-upgrade-
    eligibility\").

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxAuthenticationApiModelsResponseSilentUpgradeEligibilityResponse]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Any | RobloxAuthenticationApiModelsResponseSilentUpgradeEligibilityResponse | None:
    r"""Checks whether the authenticated user is eligible for silent passkey upgrade.
    Route and response are intentionally obfuscated (\"su-eligibility\" = \"silent-upgrade-
    eligibility\").

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxAuthenticationApiModelsResponseSilentUpgradeEligibilityResponse
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxAuthenticationApiModelsResponseSilentUpgradeEligibilityResponse]:
    r"""Checks whether the authenticated user is eligible for silent passkey upgrade.
    Route and response are intentionally obfuscated (\"su-eligibility\" = \"silent-upgrade-
    eligibility\").

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxAuthenticationApiModelsResponseSilentUpgradeEligibilityResponse]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Any | RobloxAuthenticationApiModelsResponseSilentUpgradeEligibilityResponse | None:
    r"""Checks whether the authenticated user is eligible for silent passkey upgrade.
    Route and response are intentionally obfuscated (\"su-eligibility\" = \"silent-upgrade-
    eligibility\").

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxAuthenticationApiModelsResponseSilentUpgradeEligibilityResponse
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
