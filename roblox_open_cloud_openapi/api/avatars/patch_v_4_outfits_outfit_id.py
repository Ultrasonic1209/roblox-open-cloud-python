from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roblox_api_avatar_models_v4_request_update_outfit_definition_request_v4 import (
    RobloxApiAvatarModelsV4RequestUpdateOutfitDefinitionRequestV4,
)
from ...models.roblox_api_avatar_models_v4_response_update_outfit_definition_response_v4 import (
    RobloxApiAvatarModelsV4ResponseUpdateOutfitDefinitionResponseV4,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    outfit_id: str,
    *,
    body: RobloxApiAvatarModelsV4RequestUpdateOutfitDefinitionRequestV4
    | RobloxApiAvatarModelsV4RequestUpdateOutfitDefinitionRequestV4
    | Unset = UNSET,
    roblox_place_id: int | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(roblox_place_id, Unset):
        headers["Roblox-Place-Id"] = str(roblox_place_id)

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "https://avatar.roblox.com/v4/outfits/{outfit_id}".format(
            outfit_id=quote(str(outfit_id), safe=""),
        ),
        "extensions": {
            "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
            "openapi-id": "patch_v4_outfits_outfitId",
        },
    }

    if isinstance(body, RobloxApiAvatarModelsV4RequestUpdateOutfitDefinitionRequestV4):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, RobloxApiAvatarModelsV4RequestUpdateOutfitDefinitionRequestV4):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "text/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxApiAvatarModelsV4ResponseUpdateOutfitDefinitionResponseV4 | None:
    if response.status_code == 200:
        response_200 = RobloxApiAvatarModelsV4ResponseUpdateOutfitDefinitionResponseV4.from_dict(response.json())

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

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxApiAvatarModelsV4ResponseUpdateOutfitDefinitionResponseV4]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    outfit_id: str,
    *,
    client: AuthenticatedClient,
    body: RobloxApiAvatarModelsV4RequestUpdateOutfitDefinitionRequestV4
    | RobloxApiAvatarModelsV4RequestUpdateOutfitDefinitionRequestV4
    | Unset = UNSET,
    roblox_place_id: int | Unset = UNSET,
) -> Response[Any | RobloxApiAvatarModelsV4ResponseUpdateOutfitDefinitionResponseV4]:
    """Updates the contents of an outfit.

     Fails if the user does not own any of the assetIds or if they are not wearable asset types.
    Accepts partial updates via update types.

    Args:
        outfit_id (str):
        roblox_place_id (int | Unset):
        body (RobloxApiAvatarModelsV4RequestUpdateOutfitDefinitionRequestV4): Request model for
            updating an outfit (V4).
        body (RobloxApiAvatarModelsV4RequestUpdateOutfitDefinitionRequestV4): Request model for
            updating an outfit (V4).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxApiAvatarModelsV4ResponseUpdateOutfitDefinitionResponseV4]
    """

    kwargs = _get_kwargs(
        outfit_id=outfit_id,
        body=body,
        roblox_place_id=roblox_place_id,
    )

    response = client.get_httpx2_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    outfit_id: str,
    *,
    client: AuthenticatedClient,
    body: RobloxApiAvatarModelsV4RequestUpdateOutfitDefinitionRequestV4
    | RobloxApiAvatarModelsV4RequestUpdateOutfitDefinitionRequestV4
    | Unset = UNSET,
    roblox_place_id: int | Unset = UNSET,
) -> Any | RobloxApiAvatarModelsV4ResponseUpdateOutfitDefinitionResponseV4 | None:
    """Updates the contents of an outfit.

     Fails if the user does not own any of the assetIds or if they are not wearable asset types.
    Accepts partial updates via update types.

    Args:
        outfit_id (str):
        roblox_place_id (int | Unset):
        body (RobloxApiAvatarModelsV4RequestUpdateOutfitDefinitionRequestV4): Request model for
            updating an outfit (V4).
        body (RobloxApiAvatarModelsV4RequestUpdateOutfitDefinitionRequestV4): Request model for
            updating an outfit (V4).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxApiAvatarModelsV4ResponseUpdateOutfitDefinitionResponseV4
    """

    return sync_detailed(
        outfit_id=outfit_id,
        client=client,
        body=body,
        roblox_place_id=roblox_place_id,
    ).parsed


async def asyncio_detailed(
    outfit_id: str,
    *,
    client: AuthenticatedClient,
    body: RobloxApiAvatarModelsV4RequestUpdateOutfitDefinitionRequestV4
    | RobloxApiAvatarModelsV4RequestUpdateOutfitDefinitionRequestV4
    | Unset = UNSET,
    roblox_place_id: int | Unset = UNSET,
) -> Response[Any | RobloxApiAvatarModelsV4ResponseUpdateOutfitDefinitionResponseV4]:
    """Updates the contents of an outfit.

     Fails if the user does not own any of the assetIds or if they are not wearable asset types.
    Accepts partial updates via update types.

    Args:
        outfit_id (str):
        roblox_place_id (int | Unset):
        body (RobloxApiAvatarModelsV4RequestUpdateOutfitDefinitionRequestV4): Request model for
            updating an outfit (V4).
        body (RobloxApiAvatarModelsV4RequestUpdateOutfitDefinitionRequestV4): Request model for
            updating an outfit (V4).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxApiAvatarModelsV4ResponseUpdateOutfitDefinitionResponseV4]
    """

    kwargs = _get_kwargs(
        outfit_id=outfit_id,
        body=body,
        roblox_place_id=roblox_place_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    outfit_id: str,
    *,
    client: AuthenticatedClient,
    body: RobloxApiAvatarModelsV4RequestUpdateOutfitDefinitionRequestV4
    | RobloxApiAvatarModelsV4RequestUpdateOutfitDefinitionRequestV4
    | Unset = UNSET,
    roblox_place_id: int | Unset = UNSET,
) -> Any | RobloxApiAvatarModelsV4ResponseUpdateOutfitDefinitionResponseV4 | None:
    """Updates the contents of an outfit.

     Fails if the user does not own any of the assetIds or if they are not wearable asset types.
    Accepts partial updates via update types.

    Args:
        outfit_id (str):
        roblox_place_id (int | Unset):
        body (RobloxApiAvatarModelsV4RequestUpdateOutfitDefinitionRequestV4): Request model for
            updating an outfit (V4).
        body (RobloxApiAvatarModelsV4RequestUpdateOutfitDefinitionRequestV4): Request model for
            updating an outfit (V4).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxApiAvatarModelsV4ResponseUpdateOutfitDefinitionResponseV4
    """

    return (
        await asyncio_detailed(
            outfit_id=outfit_id,
            client=client,
            body=body,
            roblox_place_id=roblox_place_id,
        )
    ).parsed
