from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.action_result import ActionResult
from ...models.delete_draft_request import DeleteDraftRequest
from ...models.draft_hash_response import DraftHashResponse
from ...models.repository import Repository
from ...types import UNSET, Response, Unset


def _get_kwargs(
    universe_id: str,
    repository: Repository,
    *,
    body: DeleteDraftRequest | DeleteDraftRequest | DeleteDraftRequest | DeleteDraftRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/creator-configs-public-api/v1/configs/universes/{universe_id}/repositories/{repository}/draft".format(
            universe_id=quote(str(universe_id), safe=""),
            repository=quote(str(repository), safe=""),
        ),
        "extensions": {
            "openapi-extensions": {
                "x-roblox-stability": "BETA",
                "x-roblox-rate-limits": {
                    "perApiKeyOwner": {"period": "MINUTE", "maxInPeriod": 50},
                    "perOauth2Authorization": {"period": "MINUTE", "maxInPeriod": 50},
                },
                "x-roblox-scopes": [{"name": "universe:write", "targetResourceSpecifier": "universes"}],
                "x-roblox-engine-usability": {"apiKeyWithHttpService": True},
            },
            "openapi-id": "CreatorConfigsPublicApi_DeleteDraft",
        },
    }

    if isinstance(body, DeleteDraftRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, DeleteDraftRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, DeleteDraftRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"
    if isinstance(body, DeleteDraftRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> ActionResult | DraftHashResponse | None:
    if response.status_code == 200:
        response_200 = DraftHashResponse.from_dict(response.json())

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
) -> Response[ActionResult | DraftHashResponse]:
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
    body: DeleteDraftRequest | DeleteDraftRequest | DeleteDraftRequest | DeleteDraftRequest | Unset = UNSET,
) -> Response[ActionResult | DraftHashResponse]:
    """Resets (deletes) the current draft.

     Resets the current draft area. If draftHash is provided, this call will fail if the hash doesn't
    match.

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
        body (DeleteDraftRequest | Unset): Request model for deleting/resetting a draft.
        body (DeleteDraftRequest | Unset): Request model for deleting/resetting a draft.
        body (DeleteDraftRequest | Unset): Request model for deleting/resetting a draft.
        body (DeleteDraftRequest | Unset): Request model for deleting/resetting a draft.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionResult | DraftHashResponse]
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
    body: DeleteDraftRequest | DeleteDraftRequest | DeleteDraftRequest | DeleteDraftRequest | Unset = UNSET,
) -> ActionResult | DraftHashResponse | None:
    """Resets (deletes) the current draft.

     Resets the current draft area. If draftHash is provided, this call will fail if the hash doesn't
    match.

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
        body (DeleteDraftRequest | Unset): Request model for deleting/resetting a draft.
        body (DeleteDraftRequest | Unset): Request model for deleting/resetting a draft.
        body (DeleteDraftRequest | Unset): Request model for deleting/resetting a draft.
        body (DeleteDraftRequest | Unset): Request model for deleting/resetting a draft.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionResult | DraftHashResponse
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
    body: DeleteDraftRequest | DeleteDraftRequest | DeleteDraftRequest | DeleteDraftRequest | Unset = UNSET,
) -> Response[ActionResult | DraftHashResponse]:
    """Resets (deletes) the current draft.

     Resets the current draft area. If draftHash is provided, this call will fail if the hash doesn't
    match.

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
        body (DeleteDraftRequest | Unset): Request model for deleting/resetting a draft.
        body (DeleteDraftRequest | Unset): Request model for deleting/resetting a draft.
        body (DeleteDraftRequest | Unset): Request model for deleting/resetting a draft.
        body (DeleteDraftRequest | Unset): Request model for deleting/resetting a draft.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActionResult | DraftHashResponse]
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
    body: DeleteDraftRequest | DeleteDraftRequest | DeleteDraftRequest | DeleteDraftRequest | Unset = UNSET,
) -> ActionResult | DraftHashResponse | None:
    """Resets (deletes) the current draft.

     Resets the current draft area. If draftHash is provided, this call will fail if the hash doesn't
    match.

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
        body (DeleteDraftRequest | Unset): Request model for deleting/resetting a draft.
        body (DeleteDraftRequest | Unset): Request model for deleting/resetting a draft.
        body (DeleteDraftRequest | Unset): Request model for deleting/resetting a draft.
        body (DeleteDraftRequest | Unset): Request model for deleting/resetting a draft.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActionResult | DraftHashResponse
    """

    return (
        await asyncio_detailed(
            universe_id=universe_id,
            repository=repository,
            client=client,
            body=body,
        )
    ).parsed
