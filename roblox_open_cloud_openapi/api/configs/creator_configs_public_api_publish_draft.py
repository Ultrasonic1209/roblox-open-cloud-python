from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.action_result import ActionResult
from ...models.publish_draft_request import PublishDraftRequest
from ...models.publish_draft_response import PublishDraftResponse
from ...models.repository import Repository
from ...types import UNSET, Response, Unset


def _get_kwargs(
    universe_id: str,
    repository: Repository,
    *,
    body: PublishDraftRequest | PublishDraftRequest | PublishDraftRequest | PublishDraftRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/creator-configs-public-api/v1/configs/universes/{universe_id}/repositories/{repository}/publish".format(
            universe_id=quote(str(universe_id), safe=""),
            repository=quote(str(repository), safe=""),
        ),
        "extensions": {
            "openapi-extensions": {
                "x-roblox-stability": "BETA",
                "x-roblox-rate-limits": {
                    "perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 10},
                    "perOauth2Authorization": {"period": "MINUTE", "maxInPeriod": 10},
                },
                "x-roblox-scopes": [{"name": "universe:write", "targetResourceSpecifier": "universes"}],
                "x-roblox-engine-usability": {"apiKeyWithHttpService": True},
            },
            "openapi-id": "CreatorConfigsPublicApi_PublishDraft",
        },
    }

    if isinstance(body, PublishDraftRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, PublishDraftRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PublishDraftRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"
    if isinstance(body, PublishDraftRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ActionResult | PublishDraftResponse | None:
    if response.status_code == 200:
        response_200 = PublishDraftResponse.from_dict(response.json())

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
) -> Response[ActionResult | PublishDraftResponse]:
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
    body: PublishDraftRequest | PublishDraftRequest | PublishDraftRequest | PublishDraftRequest | Unset = UNSET,
) -> Response[ActionResult | PublishDraftResponse]:
    """Publishes draft changes.

     Applies the current draft to the published config. Requires a draft hash and optional message and
    deployment strategy.

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
        body (PublishDraftRequest | Unset): Request model for publishing a draft.
        body (PublishDraftRequest | Unset): Request model for publishing a draft.
        body (PublishDraftRequest | Unset): Request model for publishing a draft.
        body (PublishDraftRequest | Unset): Request model for publishing a draft.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionResult | PublishDraftResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        repository=repository,
        body=body,
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
    body: PublishDraftRequest | PublishDraftRequest | PublishDraftRequest | PublishDraftRequest | Unset = UNSET,
) -> ActionResult | PublishDraftResponse | None:
    """Publishes draft changes.

     Applies the current draft to the published config. Requires a draft hash and optional message and
    deployment strategy.

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
        body (PublishDraftRequest | Unset): Request model for publishing a draft.
        body (PublishDraftRequest | Unset): Request model for publishing a draft.
        body (PublishDraftRequest | Unset): Request model for publishing a draft.
        body (PublishDraftRequest | Unset): Request model for publishing a draft.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionResult | PublishDraftResponse
    """

    return sync_detailed(
        universe_id=universe_id,
        repository=repository,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    universe_id: str,
    repository: Repository,
    *,
    client: AuthenticatedClient,
    body: PublishDraftRequest | PublishDraftRequest | PublishDraftRequest | PublishDraftRequest | Unset = UNSET,
) -> Response[ActionResult | PublishDraftResponse]:
    """Publishes draft changes.

     Applies the current draft to the published config. Requires a draft hash and optional message and
    deployment strategy.

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
        body (PublishDraftRequest | Unset): Request model for publishing a draft.
        body (PublishDraftRequest | Unset): Request model for publishing a draft.
        body (PublishDraftRequest | Unset): Request model for publishing a draft.
        body (PublishDraftRequest | Unset): Request model for publishing a draft.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionResult | PublishDraftResponse]
    """

    kwargs = _get_kwargs(
        universe_id=universe_id,
        repository=repository,
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: str,
    repository: Repository,
    *,
    client: AuthenticatedClient,
    body: PublishDraftRequest | PublishDraftRequest | PublishDraftRequest | PublishDraftRequest | Unset = UNSET,
) -> ActionResult | PublishDraftResponse | None:
    """Publishes draft changes.

     Applies the current draft to the published config. Requires a draft hash and optional message and
    deployment strategy.

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
        body (PublishDraftRequest | Unset): Request model for publishing a draft.
        body (PublishDraftRequest | Unset): Request model for publishing a draft.
        body (PublishDraftRequest | Unset): Request model for publishing a draft.
        body (PublishDraftRequest | Unset): Request model for publishing a draft.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionResult | PublishDraftResponse
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            repository=repository,
            client=client,
            body=body,
        )
    ).parsed
