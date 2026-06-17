import sys
from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response

if sys.version_info >= (3, 13):
    from warnings import deprecated
else:
    from typing_extensions import deprecated

from ...models.roblox_api_develop_models_response_team_create_settings_response import (
    RobloxApiDevelopModelsResponseTeamCreateSettingsResponse,
)


def _get_kwargs(
    universe_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://develop.roblox.com/v1/universes/{universe_id}/teamcreate".format(
            universe_id=quote(str(universe_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxApiDevelopModelsResponseTeamCreateSettingsResponse | None:
    if response.status_code == 200:
        response_200 = RobloxApiDevelopModelsResponseTeamCreateSettingsResponse.from_dict(response.json())

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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxApiDevelopModelsResponseTeamCreateSettingsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/team-create#develop_get_v1_universes__universeId__teamcreate"
)
def sync_detailed(
    universe_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxApiDevelopModelsResponseTeamCreateSettingsResponse]:
    """Gets TeamCreate settings for an Roblox.Platform.Universes.IUniverse.

    Args:
        universe_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxApiDevelopModelsResponseTeamCreateSettingsResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/team-create#develop_get_v1_universes__universeId__teamcreate"
)
def sync(
    universe_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxApiDevelopModelsResponseTeamCreateSettingsResponse | None:
    """Gets TeamCreate settings for an Roblox.Platform.Universes.IUniverse.

    Args:
        universe_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxApiDevelopModelsResponseTeamCreateSettingsResponse
    """

    return sync_detailed(
        universe_id=universe_id,
        client=client,
    ).parsed


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/team-create#develop_get_v1_universes__universeId__teamcreate"
)
async def asyncio_detailed(
    universe_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | RobloxApiDevelopModelsResponseTeamCreateSettingsResponse]:
    """Gets TeamCreate settings for an Roblox.Platform.Universes.IUniverse.

    Args:
        universe_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxApiDevelopModelsResponseTeamCreateSettingsResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/team-create#develop_get_v1_universes__universeId__teamcreate"
)
async def asyncio(
    universe_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | RobloxApiDevelopModelsResponseTeamCreateSettingsResponse | None:
    """Gets TeamCreate settings for an Roblox.Platform.Universes.IUniverse.

    Args:
        universe_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxApiDevelopModelsResponseTeamCreateSettingsResponse
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            client=client,
        )
    ).parsed
