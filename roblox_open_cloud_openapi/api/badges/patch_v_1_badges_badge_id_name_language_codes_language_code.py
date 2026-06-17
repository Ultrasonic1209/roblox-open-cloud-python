import sys
from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset

if sys.version_info >= (3, 13):
    from warnings import deprecated
else:
    from typing_extensions import deprecated

from ...models.roblox_game_internationalization_api_update_badge_name_request import (
    RobloxGameInternationalizationApiUpdateBadgeNameRequest,
)
from ...models.roblox_game_internationalization_api_update_badge_name_response import (
    RobloxGameInternationalizationApiUpdateBadgeNameResponse,
)


def _get_kwargs(
    badge_id: int,
    language_code: str,
    *,
    body: RobloxGameInternationalizationApiUpdateBadgeNameRequest
    | RobloxGameInternationalizationApiUpdateBadgeNameRequest
    | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "https://gameinternationalization.roblox.com/v1/badges/{badge_id}/name/language-codes/{language_code}".format(
            badge_id=quote(str(badge_id), safe=""),
            language_code=quote(str(language_code), safe=""),
        ),
        "openapi-extensions": {
            "x-roblox-engine-usability": {"apiKeyWithHttpService": False},
            "x-roblox-recommended-alternatives": [
                {
                    "url": "https://apis.roblox.com/legacy-game-internationalization/v1/badges/{badgeId}/name/language-codes/{languageCode}",
                    "httpMethod": "PATCH",
                    "documentationUrl": "https://create.roblox.com/docs/cloud/reference/features/badges#patch_legacy_game_internationalization_v1_badges__badgeId__name_language_codes__languageCode_",
                }
            ],
        },
        "openapi-id": "patch_v1_badges_badgeId_name_language-codes_languageCode",
    }

    if isinstance(body, RobloxGameInternationalizationApiUpdateBadgeNameRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxGameInternationalizationApiUpdateBadgeNameRequest):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxGameInternationalizationApiUpdateBadgeNameResponse | None:
    if response.status_code == 200:
        response_200 = RobloxGameInternationalizationApiUpdateBadgeNameResponse.from_dict(response.json())

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
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxGameInternationalizationApiUpdateBadgeNameResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/badges#gameinternationalization_patch_v1_badges__badgeId__name_language_codes__languageCode_"
)
def sync_detailed(
    badge_id: int,
    language_code: str,
    *,
    client: AuthenticatedClient,
    body: RobloxGameInternationalizationApiUpdateBadgeNameRequest
    | RobloxGameInternationalizationApiUpdateBadgeNameRequest
    | Unset = UNSET,
) -> Response[Any | RobloxGameInternationalizationApiUpdateBadgeNameResponse]:
    """Update localized name of a badge

    Args:
        badge_id (int):
        language_code (str):
        body (RobloxGameInternationalizationApiUpdateBadgeNameRequest): A request model for
            updating badge name
        body (RobloxGameInternationalizationApiUpdateBadgeNameRequest): A request model for
            updating badge name

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxGameInternationalizationApiUpdateBadgeNameResponse]
    """

    kwargs = _get_kwargs(
        badge_id=badge_id,
        language_code=language_code,
        body=body,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/badges#gameinternationalization_patch_v1_badges__badgeId__name_language_codes__languageCode_"
)
def sync(
    badge_id: int,
    language_code: str,
    *,
    client: AuthenticatedClient,
    body: RobloxGameInternationalizationApiUpdateBadgeNameRequest
    | RobloxGameInternationalizationApiUpdateBadgeNameRequest
    | Unset = UNSET,
) -> Any | RobloxGameInternationalizationApiUpdateBadgeNameResponse | None:
    """Update localized name of a badge

    Args:
        badge_id (int):
        language_code (str):
        body (RobloxGameInternationalizationApiUpdateBadgeNameRequest): A request model for
            updating badge name
        body (RobloxGameInternationalizationApiUpdateBadgeNameRequest): A request model for
            updating badge name

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxGameInternationalizationApiUpdateBadgeNameResponse
    """

    return sync_detailed(
        badge_id=badge_id,
        language_code=language_code,
        client=client,
        body=body,
    ).parsed


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/badges#gameinternationalization_patch_v1_badges__badgeId__name_language_codes__languageCode_"
)
async def asyncio_detailed(
    badge_id: int,
    language_code: str,
    *,
    client: AuthenticatedClient,
    body: RobloxGameInternationalizationApiUpdateBadgeNameRequest
    | RobloxGameInternationalizationApiUpdateBadgeNameRequest
    | Unset = UNSET,
) -> Response[Any | RobloxGameInternationalizationApiUpdateBadgeNameResponse]:
    """Update localized name of a badge

    Args:
        badge_id (int):
        language_code (str):
        body (RobloxGameInternationalizationApiUpdateBadgeNameRequest): A request model for
            updating badge name
        body (RobloxGameInternationalizationApiUpdateBadgeNameRequest): A request model for
            updating badge name

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxGameInternationalizationApiUpdateBadgeNameResponse]
    """

    kwargs = _get_kwargs(
        badge_id=badge_id,
        language_code=language_code,
        body=body,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated(
    "Roblox has deprecated this endpoint. See documentation: https://create.roblox.com/docs/cloud/reference/features/badges#gameinternationalization_patch_v1_badges__badgeId__name_language_codes__languageCode_"
)
async def asyncio(
    badge_id: int,
    language_code: str,
    *,
    client: AuthenticatedClient,
    body: RobloxGameInternationalizationApiUpdateBadgeNameRequest
    | RobloxGameInternationalizationApiUpdateBadgeNameRequest
    | Unset = UNSET,
) -> Any | RobloxGameInternationalizationApiUpdateBadgeNameResponse | None:
    """Update localized name of a badge

    Args:
        badge_id (int):
        language_code (str):
        body (RobloxGameInternationalizationApiUpdateBadgeNameRequest): A request model for
            updating badge name
        body (RobloxGameInternationalizationApiUpdateBadgeNameRequest): A request model for
            updating badge name

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxGameInternationalizationApiUpdateBadgeNameResponse
    """

    return (
        await asyncio_detailed(
            badge_id=badge_id,
            language_code=language_code,
            client=client,
            body=body,
        )
    ).parsed
