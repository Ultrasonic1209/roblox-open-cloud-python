import sys
from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response

if sys.version_info >= (3, 13):
    from warnings import deprecated
else:
    from typing_extensions import deprecated

from ...models.roblox_game_internationalization_api_update_badge_name_description_request import (
    RobloxGameInternationalizationApiUpdateBadgeNameDescriptionRequest,
)
from ...models.roblox_game_internationalization_api_update_badge_name_description_response import (
    RobloxGameInternationalizationApiUpdateBadgeNameDescriptionResponse,
)


def _get_kwargs(
    badge_id: int,
    language_code: str,
    *,
    body: RobloxGameInternationalizationApiUpdateBadgeNameDescriptionRequest
    | RobloxGameInternationalizationApiUpdateBadgeNameDescriptionRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/badges/{badge_id}/name-description/language-codes/{language_code}".format(
            badge_id=quote(str(badge_id), safe=""),
            language_code=quote(str(language_code), safe=""),
        ),
    }

    if isinstance(body, RobloxGameInternationalizationApiUpdateBadgeNameDescriptionRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxGameInternationalizationApiUpdateBadgeNameDescriptionRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RobloxGameInternationalizationApiUpdateBadgeNameDescriptionResponse | None:
    if response.status_code == 200:
        response_200 = RobloxGameInternationalizationApiUpdateBadgeNameDescriptionResponse.from_dict(response.json())

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

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RobloxGameInternationalizationApiUpdateBadgeNameDescriptionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/badges#gameinternationalization_patch_v1_badges__badgeId__name_description_language_codes__languageCode_"
)
def sync_detailed(
    badge_id: int,
    language_code: str,
    *,
    client: AuthenticatedClient,
    body: RobloxGameInternationalizationApiUpdateBadgeNameDescriptionRequest
    | RobloxGameInternationalizationApiUpdateBadgeNameDescriptionRequest
    | Unset = UNSET,
) -> Response[Any | RobloxGameInternationalizationApiUpdateBadgeNameDescriptionResponse]:
    """Update localized name and description of a badge

    Args:
        badge_id (int):
        language_code (str):
        body (RobloxGameInternationalizationApiUpdateBadgeNameDescriptionRequest): A request model
            for updating badge name and description
        body (RobloxGameInternationalizationApiUpdateBadgeNameDescriptionRequest): A request model
            for updating badge name and description

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxGameInternationalizationApiUpdateBadgeNameDescriptionResponse]
    """

    kwargs = _get_kwargs(
        badge_id=badge_id,
        language_code=language_code,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/badges#gameinternationalization_patch_v1_badges__badgeId__name_description_language_codes__languageCode_"
)
def sync(
    badge_id: int,
    language_code: str,
    *,
    client: AuthenticatedClient,
    body: RobloxGameInternationalizationApiUpdateBadgeNameDescriptionRequest
    | RobloxGameInternationalizationApiUpdateBadgeNameDescriptionRequest
    | Unset = UNSET,
) -> Any | RobloxGameInternationalizationApiUpdateBadgeNameDescriptionResponse | None:
    """Update localized name and description of a badge

    Args:
        badge_id (int):
        language_code (str):
        body (RobloxGameInternationalizationApiUpdateBadgeNameDescriptionRequest): A request model
            for updating badge name and description
        body (RobloxGameInternationalizationApiUpdateBadgeNameDescriptionRequest): A request model
            for updating badge name and description

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxGameInternationalizationApiUpdateBadgeNameDescriptionResponse
    """

    return sync_detailed(
        badge_id=badge_id,
        language_code=language_code,
        client=client,
        body=body,
    ).parsed


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/badges#gameinternationalization_patch_v1_badges__badgeId__name_description_language_codes__languageCode_"
)
async def asyncio_detailed(
    badge_id: int,
    language_code: str,
    *,
    client: AuthenticatedClient,
    body: RobloxGameInternationalizationApiUpdateBadgeNameDescriptionRequest
    | RobloxGameInternationalizationApiUpdateBadgeNameDescriptionRequest
    | Unset = UNSET,
) -> Response[Any | RobloxGameInternationalizationApiUpdateBadgeNameDescriptionResponse]:
    """Update localized name and description of a badge

    Args:
        badge_id (int):
        language_code (str):
        body (RobloxGameInternationalizationApiUpdateBadgeNameDescriptionRequest): A request model
            for updating badge name and description
        body (RobloxGameInternationalizationApiUpdateBadgeNameDescriptionRequest): A request model
            for updating badge name and description

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxGameInternationalizationApiUpdateBadgeNameDescriptionResponse]
    """

    kwargs = _get_kwargs(
        badge_id=badge_id,
        language_code=language_code,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/badges#gameinternationalization_patch_v1_badges__badgeId__name_description_language_codes__languageCode_"
)
async def asyncio(
    badge_id: int,
    language_code: str,
    *,
    client: AuthenticatedClient,
    body: RobloxGameInternationalizationApiUpdateBadgeNameDescriptionRequest
    | RobloxGameInternationalizationApiUpdateBadgeNameDescriptionRequest
    | Unset = UNSET,
) -> Any | RobloxGameInternationalizationApiUpdateBadgeNameDescriptionResponse | None:
    """Update localized name and description of a badge

    Args:
        badge_id (int):
        language_code (str):
        body (RobloxGameInternationalizationApiUpdateBadgeNameDescriptionRequest): A request model
            for updating badge name and description
        body (RobloxGameInternationalizationApiUpdateBadgeNameDescriptionRequest): A request model
            for updating badge name and description

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxGameInternationalizationApiUpdateBadgeNameDescriptionResponse
    """

    return (
        await asyncio_detailed(
            badge_id=badge_id,
            language_code=language_code,
            client=client,
            body=body,
        )
    ).parsed
