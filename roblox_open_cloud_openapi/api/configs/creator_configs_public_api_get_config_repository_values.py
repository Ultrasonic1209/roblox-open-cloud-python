from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.action_result import ActionResult
from ...models.config_repository_values import ConfigRepositoryValues
from ...models.repository import Repository
from ...types import Response


def _get_kwargs(
    universe_id: str,
    repository: Repository,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/creator-configs-public-api/v1/configs/universes/{universe_id}/repositories/{repository}".format(
            universe_id=quote(str(universe_id), safe=""),
            repository=quote(str(repository), safe=""),
        ),
        "extensions": {
            "openapi-extensions": {
                "x-roblox-stability": "BETA",
                "x-roblox-rate-limits": {
                    "perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 100},
                    "perOauth2Authorization": {"period": "MINUTE", "maxInPeriod": 100},
                },
                "x-roblox-scopes": [{"name": "universe:read", "targetResourceSpecifier": "universes"}],
                "x-roblox-engine-usability": {"apiKeyWithHttpService": True},
            },
            "openapi-id": "CreatorConfigsPublicApi_GetConfigRepositoryValues",
        },
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ActionResult | ConfigRepositoryValues | None:
    if response.status_code == 200:
        response_200 = ConfigRepositoryValues.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ActionResult.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ActionResult.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ActionResult.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[ActionResult | ConfigRepositoryValues]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    universe_id: str,
    repository: Repository,
    *,
    client: AuthenticatedClient,
) -> Response[ActionResult | ConfigRepositoryValues]:
    """Gets published config values without metadata.

     Returns the latest published config values without metadata and decorators.
    This response can be used as a direct copy-and-paste to the draft update endpoints.

    Args:
        universe_id (str):
        repository (Repository): Public API repository identifier. Only values exposed by the
            public API are included;
            internal repository types are not exposed to allow development and testing before
            enabling.

            InExperienceConfig

            RecommendationServicesConfig

            DataStoresConfig

            ExtendedServicesConfig

            LeaderboardsConfig

            ExperienceUserConfig

            JourneysConfig

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionResult | ConfigRepositoryValues]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        repository=repository,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    universe_id: str,
    repository: Repository,
    *,
    client: AuthenticatedClient,
) -> ActionResult | ConfigRepositoryValues | None:
    """Gets published config values without metadata.

     Returns the latest published config values without metadata and decorators.
    This response can be used as a direct copy-and-paste to the draft update endpoints.

    Args:
        universe_id (str):
        repository (Repository): Public API repository identifier. Only values exposed by the
            public API are included;
            internal repository types are not exposed to allow development and testing before
            enabling.

            InExperienceConfig

            RecommendationServicesConfig

            DataStoresConfig

            ExtendedServicesConfig

            LeaderboardsConfig

            ExperienceUserConfig

            JourneysConfig

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionResult | ConfigRepositoryValues
    """

    return sync_detailed(
        universe_id=universe_id,
        repository=repository,
        client=client,
    ).parsed


async def asyncio_detailed(
    universe_id: str,
    repository: Repository,
    *,
    client: AuthenticatedClient,
) -> Response[ActionResult | ConfigRepositoryValues]:
    """Gets published config values without metadata.

     Returns the latest published config values without metadata and decorators.
    This response can be used as a direct copy-and-paste to the draft update endpoints.

    Args:
        universe_id (str):
        repository (Repository): Public API repository identifier. Only values exposed by the
            public API are included;
            internal repository types are not exposed to allow development and testing before
            enabling.

            InExperienceConfig

            RecommendationServicesConfig

            DataStoresConfig

            ExtendedServicesConfig

            LeaderboardsConfig

            ExperienceUserConfig

            JourneysConfig

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionResult | ConfigRepositoryValues]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        repository=repository,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: str,
    repository: Repository,
    *,
    client: AuthenticatedClient,
) -> ActionResult | ConfigRepositoryValues | None:
    """Gets published config values without metadata.

     Returns the latest published config values without metadata and decorators.
    This response can be used as a direct copy-and-paste to the draft update endpoints.

    Args:
        universe_id (str):
        repository (Repository): Public API repository identifier. Only values exposed by the
            public API are included;
            internal repository types are not exposed to allow development and testing before
            enabling.

            InExperienceConfig

            RecommendationServicesConfig

            DataStoresConfig

            ExtendedServicesConfig

            LeaderboardsConfig

            ExperienceUserConfig

            JourneysConfig

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionResult | ConfigRepositoryValues
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            repository=repository,
            client=client,
        )
    ).parsed
