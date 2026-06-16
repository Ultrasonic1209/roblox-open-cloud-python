from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

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
        "method": "put",
        "url": "/creator-configs-public-api/v1/configs/universes/{universe_id}/repositories/{repository}/draft:overwrite".format(
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
    *, client: AuthenticatedClient | Client, response: httpx.Response
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
    *, client: AuthenticatedClient | Client, response: httpx.Response
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
    """Overwrites the entire draft with the request payload.

     Full overwrite of current draft. The payload is the expected final state after publish (not a merge
    with the draft or published config from the client’s perspective).
    The service aligns that intent with CMS validation by emitting explicit deletions for published keys
    and conditional branches omitted from the body.
    If a key is not included, it is interpreted as removed.
    When `conditionalRules` is included, `conditionalRules.rules` is authoritative for rule definitions:
    any conditional rule that exists on the latest published configuration but is omitted from `rules`
    is removed (same as sending an empty RPN rule).
    When `conditionalRules` is omitted, all published conditional rules are removed; entries must not
    use conditional branches or `.RBX.conditional.*` keys unless you send `conditionalRules`.
    If draftHash is provided, this call will fail if the hash doesn't match.
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

    response = client.get_httpx_client().request(
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
    """Overwrites the entire draft with the request payload.

     Full overwrite of current draft. The payload is the expected final state after publish (not a merge
    with the draft or published config from the client’s perspective).
    The service aligns that intent with CMS validation by emitting explicit deletions for published keys
    and conditional branches omitted from the body.
    If a key is not included, it is interpreted as removed.
    When `conditionalRules` is included, `conditionalRules.rules` is authoritative for rule definitions:
    any conditional rule that exists on the latest published configuration but is omitted from `rules`
    is removed (same as sending an empty RPN rule).
    When `conditionalRules` is omitted, all published conditional rules are removed; entries must not
    use conditional branches or `.RBX.conditional.*` keys unless you send `conditionalRules`.
    If draftHash is provided, this call will fail if the hash doesn't match.
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
    """Overwrites the entire draft with the request payload.

     Full overwrite of current draft. The payload is the expected final state after publish (not a merge
    with the draft or published config from the client’s perspective).
    The service aligns that intent with CMS validation by emitting explicit deletions for published keys
    and conditional branches omitted from the body.
    If a key is not included, it is interpreted as removed.
    When `conditionalRules` is included, `conditionalRules.rules` is authoritative for rule definitions:
    any conditional rule that exists on the latest published configuration but is omitted from `rules`
    is removed (same as sending an empty RPN rule).
    When `conditionalRules` is omitted, all published conditional rules are removed; entries must not
    use conditional branches or `.RBX.conditional.*` keys unless you send `conditionalRules`.
    If draftHash is provided, this call will fail if the hash doesn't match.
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

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    universe_id: str,
    repository: Repository,
    *,
    client: AuthenticatedClient,
    body: UpdateDraftRequest | UpdateDraftRequest | UpdateDraftRequest | UpdateDraftRequest | Unset = UNSET,
) -> ActionResult | DraftHashResponse | None:
    """Overwrites the entire draft with the request payload.

     Full overwrite of current draft. The payload is the expected final state after publish (not a merge
    with the draft or published config from the client’s perspective).
    The service aligns that intent with CMS validation by emitting explicit deletions for published keys
    and conditional branches omitted from the body.
    If a key is not included, it is interpreted as removed.
    When `conditionalRules` is included, `conditionalRules.rules` is authoritative for rule definitions:
    any conditional rule that exists on the latest published configuration but is omitted from `rules`
    is removed (same as sending an empty RPN rule).
    When `conditionalRules` is omitted, all published conditional rules are removed; entries must not
    use conditional branches or `.RBX.conditional.*` keys unless you send `conditionalRules`.
    If draftHash is provided, this call will fail if the hash doesn't match.
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
