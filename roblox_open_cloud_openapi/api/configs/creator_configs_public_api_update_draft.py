from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.action_result import ActionResult
from ...models.draft_hash_response import DraftHashResponse
from ...models.repository import Repository
from ...models.update_draft_request import UpdateDraftRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    universe_id: str,
    repository: Repository,
    *,
    body: UpdateDraftRequest | UpdateDraftRequest | UpdateDraftRequest | UpdateDraftRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/creator-configs-public-api/v1/configs/universes/{universe_id}/repositories/{repository}/draft".format(
            universe_id=quote(str(universe_id), safe=""),
            repository=quote(str(repository), safe=""),
        ),
    }

    if isinstance(body, UpdateDraftRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, UpdateDraftRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, UpdateDraftRequest):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"
    if isinstance(body, UpdateDraftRequest):
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
    body: UpdateDraftRequest | UpdateDraftRequest | UpdateDraftRequest | UpdateDraftRequest | Unset = UNSET,
) -> Response[ActionResult | DraftHashResponse]:
    """Partially updates the draft.

     Updates the draft treating the payload as a partial changeset.
    If draftHash is provided, this call will fail if the hash doesn't match.
    A key not included will not be changed. To indicate deletion, set key to null.
    To discard a change, set key to its currently published value.
    When `conditionalRules` is omitted or empty (`{}`), the CMS update omits the conditional-rules field
    so existing published rules remain at publish time;
    send a non-empty `conditionalRules` object to merge rule changes.
    Entry count and per-value size limits are enforced here via
    CreatorConfigsPublicApi.Utils.DraftValidationHelper; further schema validation is performed by
    Config Management.

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
        body (UpdateDraftRequest | Unset): Request model for draft updates: PATCH uses a partial
            merge; PUT `draft:overwrite` treats the body as the full intended configuration after
            publish.
        body (UpdateDraftRequest | Unset): Request model for draft updates: PATCH uses a partial
            merge; PUT `draft:overwrite` treats the body as the full intended configuration after
            publish.
        body (UpdateDraftRequest | Unset): Request model for draft updates: PATCH uses a partial
            merge; PUT `draft:overwrite` treats the body as the full intended configuration after
            publish.
        body (UpdateDraftRequest | Unset): Request model for draft updates: PATCH uses a partial
            merge; PUT `draft:overwrite` treats the body as the full intended configuration after
            publish.

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
    body: UpdateDraftRequest | UpdateDraftRequest | UpdateDraftRequest | UpdateDraftRequest | Unset = UNSET,
) -> ActionResult | DraftHashResponse | None:
    """Partially updates the draft.

     Updates the draft treating the payload as a partial changeset.
    If draftHash is provided, this call will fail if the hash doesn't match.
    A key not included will not be changed. To indicate deletion, set key to null.
    To discard a change, set key to its currently published value.
    When `conditionalRules` is omitted or empty (`{}`), the CMS update omits the conditional-rules field
    so existing published rules remain at publish time;
    send a non-empty `conditionalRules` object to merge rule changes.
    Entry count and per-value size limits are enforced here via
    CreatorConfigsPublicApi.Utils.DraftValidationHelper; further schema validation is performed by
    Config Management.

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
        body (UpdateDraftRequest | Unset): Request model for draft updates: PATCH uses a partial
            merge; PUT `draft:overwrite` treats the body as the full intended configuration after
            publish.
        body (UpdateDraftRequest | Unset): Request model for draft updates: PATCH uses a partial
            merge; PUT `draft:overwrite` treats the body as the full intended configuration after
            publish.
        body (UpdateDraftRequest | Unset): Request model for draft updates: PATCH uses a partial
            merge; PUT `draft:overwrite` treats the body as the full intended configuration after
            publish.
        body (UpdateDraftRequest | Unset): Request model for draft updates: PATCH uses a partial
            merge; PUT `draft:overwrite` treats the body as the full intended configuration after
            publish.

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
    body: UpdateDraftRequest | UpdateDraftRequest | UpdateDraftRequest | UpdateDraftRequest | Unset = UNSET,
) -> Response[ActionResult | DraftHashResponse]:
    """Partially updates the draft.

     Updates the draft treating the payload as a partial changeset.
    If draftHash is provided, this call will fail if the hash doesn't match.
    A key not included will not be changed. To indicate deletion, set key to null.
    To discard a change, set key to its currently published value.
    When `conditionalRules` is omitted or empty (`{}`), the CMS update omits the conditional-rules field
    so existing published rules remain at publish time;
    send a non-empty `conditionalRules` object to merge rule changes.
    Entry count and per-value size limits are enforced here via
    CreatorConfigsPublicApi.Utils.DraftValidationHelper; further schema validation is performed by
    Config Management.

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
        body (UpdateDraftRequest | Unset): Request model for draft updates: PATCH uses a partial
            merge; PUT `draft:overwrite` treats the body as the full intended configuration after
            publish.
        body (UpdateDraftRequest | Unset): Request model for draft updates: PATCH uses a partial
            merge; PUT `draft:overwrite` treats the body as the full intended configuration after
            publish.
        body (UpdateDraftRequest | Unset): Request model for draft updates: PATCH uses a partial
            merge; PUT `draft:overwrite` treats the body as the full intended configuration after
            publish.
        body (UpdateDraftRequest | Unset): Request model for draft updates: PATCH uses a partial
            merge; PUT `draft:overwrite` treats the body as the full intended configuration after
            publish.

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
    body: UpdateDraftRequest | UpdateDraftRequest | UpdateDraftRequest | UpdateDraftRequest | Unset = UNSET,
) -> ActionResult | DraftHashResponse | None:
    """Partially updates the draft.

     Updates the draft treating the payload as a partial changeset.
    If draftHash is provided, this call will fail if the hash doesn't match.
    A key not included will not be changed. To indicate deletion, set key to null.
    To discard a change, set key to its currently published value.
    When `conditionalRules` is omitted or empty (`{}`), the CMS update omits the conditional-rules field
    so existing published rules remain at publish time;
    send a non-empty `conditionalRules` object to merge rule changes.
    Entry count and per-value size limits are enforced here via
    CreatorConfigsPublicApi.Utils.DraftValidationHelper; further schema validation is performed by
    Config Management.

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
        body (UpdateDraftRequest | Unset): Request model for draft updates: PATCH uses a partial
            merge; PUT `draft:overwrite` treats the body as the full intended configuration after
            publish.
        body (UpdateDraftRequest | Unset): Request model for draft updates: PATCH uses a partial
            merge; PUT `draft:overwrite` treats the body as the full intended configuration after
            publish.
        body (UpdateDraftRequest | Unset): Request model for draft updates: PATCH uses a partial
            merge; PUT `draft:overwrite` treats the body as the full intended configuration after
            publish.
        body (UpdateDraftRequest | Unset): Request model for draft updates: PATCH uses a partial
            merge; PUT `draft:overwrite` treats the body as the full intended configuration after
            publish.

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
