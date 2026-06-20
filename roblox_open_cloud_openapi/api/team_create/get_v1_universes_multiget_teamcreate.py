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

from ...models.roblox_web_web_api_models_api_array_response_roblox_api_develop_models_universe_team_create_settings_model import (
    RobloxWebWebAPIModelsApiArrayResponseRobloxApiDevelopModelsUniverseTeamCreateSettingsModel,
)


def _get_kwargs(
    *,
    ids: list[int],
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_ids = ids

    params["ids"] = json_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://develop.roblox.com/v1/universes/multiget/teamcreate",
        "params": params,
        "extensions": {
            "openapi-extensions": {
                "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
                "x-roblox-recommended-alternatives": [
                    {
                        "url": "https://apis.roblox.com/legacy-develop/v1/universes/multiget/teamcreate",
                        "httpMethod": "GET",
                        "documentationUrl": "https://create.roblox.com/docs/cloud/reference/features/team-create#get_legacy_develop_v1_universes_multiget_teamcreate",
                    }
                ],
            },
            "openapi-id": "get_v1_universes_multiget_teamcreate",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxApiDevelopModelsUniverseTeamCreateSettingsModel | None:
    if response.status_code == 200:
        response_200 = (
            RobloxWebWebAPIModelsApiArrayResponseRobloxApiDevelopModelsUniverseTeamCreateSettingsModel.from_dict(
                response.json()
            )
        )

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
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxApiDevelopModelsUniverseTeamCreateSettingsModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/team-create#develop_get_v1_universes_multiget_teamcreate"
)
def sync_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[int],
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxApiDevelopModelsUniverseTeamCreateSettingsModel]:
    """Gets TeamCreate settings for multiple universes specified by Ids

    Args:
        ids (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxApiDevelopModelsUniverseTeamCreateSettingsModel]
    """

    kwargs = _get_kwargs(
        ids=ids,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/team-create#develop_get_v1_universes_multiget_teamcreate"
)
def sync(
    *,
    client: AuthenticatedClient,
    ids: list[int],
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxApiDevelopModelsUniverseTeamCreateSettingsModel | None:
    """Gets TeamCreate settings for multiple universes specified by Ids

    Args:
        ids (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiArrayResponseRobloxApiDevelopModelsUniverseTeamCreateSettingsModel
    """

    return sync_detailed(
        client=client,
        ids=ids,
    ).parsed


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/team-create#develop_get_v1_universes_multiget_teamcreate"
)
async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: list[int],
) -> Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxApiDevelopModelsUniverseTeamCreateSettingsModel]:
    """Gets TeamCreate settings for multiple universes specified by Ids

    Args:
        ids (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxWebWebAPIModelsApiArrayResponseRobloxApiDevelopModelsUniverseTeamCreateSettingsModel]
    """

    kwargs = _get_kwargs(
        ids=ids,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/team-create#develop_get_v1_universes_multiget_teamcreate"
)
async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: list[int],
) -> Any | RobloxWebWebAPIModelsApiArrayResponseRobloxApiDevelopModelsUniverseTeamCreateSettingsModel | None:
    """Gets TeamCreate settings for multiple universes specified by Ids

    Args:
        ids (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxWebWebAPIModelsApiArrayResponseRobloxApiDevelopModelsUniverseTeamCreateSettingsModel
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
        )
    ).parsed
