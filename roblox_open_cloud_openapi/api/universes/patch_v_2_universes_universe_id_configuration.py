from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_api_develop_models_universe_settings_request_v2 import (
    RobloxApiDevelopModelsUniverseSettingsRequestV2,
)
from ...models.roblox_api_develop_models_universe_settings_response_v2 import (
    RobloxApiDevelopModelsUniverseSettingsResponseV2,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    universe_id: int,
    *,
    body: RobloxApiDevelopModelsUniverseSettingsRequestV2
    | RobloxApiDevelopModelsUniverseSettingsRequestV2
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "https://develop.roblox.com/v2/universes/{universe_id}/configuration".format(
            universe_id=quote(str(universe_id), safe=""),
        ),
        "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
        "openapi-id": "patch_v2_universes_universeId_configuration",
    }

    if isinstance(body, RobloxApiDevelopModelsUniverseSettingsRequestV2):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxApiDevelopModelsUniverseSettingsRequestV2):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxApiDevelopModelsUniverseSettingsResponseV2 | None:
    if response.status_code == 200:
        response_200 = RobloxApiDevelopModelsUniverseSettingsResponseV2.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxApiDevelopModelsUniverseSettingsResponseV2]:
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
    body: RobloxApiDevelopModelsUniverseSettingsRequestV2
    | RobloxApiDevelopModelsUniverseSettingsRequestV2
    | Unset = UNSET,
) -> Response[Any | RobloxApiDevelopModelsUniverseSettingsResponseV2]:
    """Update universe settings for an owned universe.
    V2 Contains data for avatar scale and asset override.

    Args:
        universe_id (int):
        body (RobloxApiDevelopModelsUniverseSettingsRequestV2): Model for UniverseSettings patch
            requests
        body (RobloxApiDevelopModelsUniverseSettingsRequestV2): Model for UniverseSettings patch
            requests

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxApiDevelopModelsUniverseSettingsResponseV2]
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
    body: RobloxApiDevelopModelsUniverseSettingsRequestV2
    | RobloxApiDevelopModelsUniverseSettingsRequestV2
    | Unset = UNSET,
) -> Any | RobloxApiDevelopModelsUniverseSettingsResponseV2 | None:
    """Update universe settings for an owned universe.
    V2 Contains data for avatar scale and asset override.

    Args:
        universe_id (int):
        body (RobloxApiDevelopModelsUniverseSettingsRequestV2): Model for UniverseSettings patch
            requests
        body (RobloxApiDevelopModelsUniverseSettingsRequestV2): Model for UniverseSettings patch
            requests

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxApiDevelopModelsUniverseSettingsResponseV2
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
    body: RobloxApiDevelopModelsUniverseSettingsRequestV2
    | RobloxApiDevelopModelsUniverseSettingsRequestV2
    | Unset = UNSET,
) -> Response[Any | RobloxApiDevelopModelsUniverseSettingsResponseV2]:
    """Update universe settings for an owned universe.
    V2 Contains data for avatar scale and asset override.

    Args:
        universe_id (int):
        body (RobloxApiDevelopModelsUniverseSettingsRequestV2): Model for UniverseSettings patch
            requests
        body (RobloxApiDevelopModelsUniverseSettingsRequestV2): Model for UniverseSettings patch
            requests

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxApiDevelopModelsUniverseSettingsResponseV2]
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
    body: RobloxApiDevelopModelsUniverseSettingsRequestV2
    | RobloxApiDevelopModelsUniverseSettingsRequestV2
    | Unset = UNSET,
) -> Any | RobloxApiDevelopModelsUniverseSettingsResponseV2 | None:
    """Update universe settings for an owned universe.
    V2 Contains data for avatar scale and asset override.

    Args:
        universe_id (int):
        body (RobloxApiDevelopModelsUniverseSettingsRequestV2): Model for UniverseSettings patch
            requests
        body (RobloxApiDevelopModelsUniverseSettingsRequestV2): Model for UniverseSettings patch
            requests

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxApiDevelopModelsUniverseSettingsResponseV2
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            client=client,
            body=body,
        )
    ).parsed
