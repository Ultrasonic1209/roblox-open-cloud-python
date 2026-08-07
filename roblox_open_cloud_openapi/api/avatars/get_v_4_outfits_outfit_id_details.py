from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v4_outfits_outfit_id_details_selection_types_item import (
    GetV4OutfitsOutfitIdDetailsSelectionTypesItem,
)
from ...models.roblox_api_avatar_models_v4_outfit_definition import RobloxApiAvatarModelsV4OutfitDefinition
from ...types import UNSET, Response, Unset


def _get_kwargs(
    outfit_id: str,
    *,
    selection_types: list[GetV4OutfitsOutfitIdDetailsSelectionTypesItem] | Unset = UNSET,
    check_asset_availability: bool | Unset = False,
    roblox_place_id: int | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(roblox_place_id, Unset):
        headers["Roblox-Place-Id"] = str(roblox_place_id)

    params: dict[str, Any] = {}

    json_selection_types: list[int] | Unset = UNSET
    if not isinstance(selection_types, Unset):
        json_selection_types = []
        for selection_types_item_data in selection_types:
            selection_types_item = selection_types_item_data.value
            json_selection_types.append(selection_types_item)

    params["selectionTypes"] = json_selection_types

    params["checkAssetAvailability"] = check_asset_availability

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "https://avatar.roblox.com/v4/outfits/{outfit_id}/details".format(
            outfit_id=quote(str(outfit_id), safe=""),
        ),
        "params": params,
        "extensions": {
            "openapi-extensions": {"x-roblox-engine-usability": {"apiKeyWithHttpService": False}},
            "openapi-id": "get_v4_outfits_outfitId_details",
        },
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Any | RobloxApiAvatarModelsV4OutfitDefinition | None:
    if response.status_code == 200:
        response_200 = RobloxApiAvatarModelsV4OutfitDefinition.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx2.Response
) -> Response[Any | RobloxApiAvatarModelsV4OutfitDefinition]:
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
    selection_types: list[GetV4OutfitsOutfitIdDetailsSelectionTypesItem] | Unset = UNSET,
    check_asset_availability: bool | Unset = False,
    roblox_place_id: int | Unset = UNSET,
) -> Response[Any | RobloxApiAvatarModelsV4OutfitDefinition]:
    """Gets the definition for an outfit.

     Returns an Roblox.Api.Avatar.Models.V4.OutfitDefinition containing an
    Roblox.Api.Avatar.Models.V4.OutfitModelV4 and background
    Roblox.Api.Avatar.Models.V4.OutfitConfigurations.
    Behavior is aligned with the V1/V3 `GET v{1|3}/outfits/{userOutfitId}/details` endpoints
    (authentication optional).

    Args:
        outfit_id (str):
        selection_types (list[GetV4OutfitsOutfitIdDetailsSelectionTypesItem] | Unset):
        check_asset_availability (bool | Unset):  Default: False.
        roblox_place_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxApiAvatarModelsV4OutfitDefinition]
    """

    kwargs = _get_kwargs(
        outfit_id=outfit_id,
        selection_types=selection_types,
        check_asset_availability=check_asset_availability,
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
    selection_types: list[GetV4OutfitsOutfitIdDetailsSelectionTypesItem] | Unset = UNSET,
    check_asset_availability: bool | Unset = False,
    roblox_place_id: int | Unset = UNSET,
) -> Any | RobloxApiAvatarModelsV4OutfitDefinition | None:
    """Gets the definition for an outfit.

     Returns an Roblox.Api.Avatar.Models.V4.OutfitDefinition containing an
    Roblox.Api.Avatar.Models.V4.OutfitModelV4 and background
    Roblox.Api.Avatar.Models.V4.OutfitConfigurations.
    Behavior is aligned with the V1/V3 `GET v{1|3}/outfits/{userOutfitId}/details` endpoints
    (authentication optional).

    Args:
        outfit_id (str):
        selection_types (list[GetV4OutfitsOutfitIdDetailsSelectionTypesItem] | Unset):
        check_asset_availability (bool | Unset):  Default: False.
        roblox_place_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxApiAvatarModelsV4OutfitDefinition
    """

    return sync_detailed(
        outfit_id=outfit_id,
        client=client,
        selection_types=selection_types,
        check_asset_availability=check_asset_availability,
        roblox_place_id=roblox_place_id,
    ).parsed


async def asyncio_detailed(
    outfit_id: str,
    *,
    client: AuthenticatedClient,
    selection_types: list[GetV4OutfitsOutfitIdDetailsSelectionTypesItem] | Unset = UNSET,
    check_asset_availability: bool | Unset = False,
    roblox_place_id: int | Unset = UNSET,
) -> Response[Any | RobloxApiAvatarModelsV4OutfitDefinition]:
    """Gets the definition for an outfit.

     Returns an Roblox.Api.Avatar.Models.V4.OutfitDefinition containing an
    Roblox.Api.Avatar.Models.V4.OutfitModelV4 and background
    Roblox.Api.Avatar.Models.V4.OutfitConfigurations.
    Behavior is aligned with the V1/V3 `GET v{1|3}/outfits/{userOutfitId}/details` endpoints
    (authentication optional).

    Args:
        outfit_id (str):
        selection_types (list[GetV4OutfitsOutfitIdDetailsSelectionTypesItem] | Unset):
        check_asset_availability (bool | Unset):  Default: False.
        roblox_place_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RobloxApiAvatarModelsV4OutfitDefinition]
    """

    kwargs = _get_kwargs(
        outfit_id=outfit_id,
        selection_types=selection_types,
        check_asset_availability=check_asset_availability,
        roblox_place_id=roblox_place_id,
    )

    response = await client.get_async_httpx2_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    outfit_id: str,
    *,
    client: AuthenticatedClient,
    selection_types: list[GetV4OutfitsOutfitIdDetailsSelectionTypesItem] | Unset = UNSET,
    check_asset_availability: bool | Unset = False,
    roblox_place_id: int | Unset = UNSET,
) -> Any | RobloxApiAvatarModelsV4OutfitDefinition | None:
    """Gets the definition for an outfit.

     Returns an Roblox.Api.Avatar.Models.V4.OutfitDefinition containing an
    Roblox.Api.Avatar.Models.V4.OutfitModelV4 and background
    Roblox.Api.Avatar.Models.V4.OutfitConfigurations.
    Behavior is aligned with the V1/V3 `GET v{1|3}/outfits/{userOutfitId}/details` endpoints
    (authentication optional).

    Args:
        outfit_id (str):
        selection_types (list[GetV4OutfitsOutfitIdDetailsSelectionTypesItem] | Unset):
        check_asset_availability (bool | Unset):  Default: False.
        roblox_place_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RobloxApiAvatarModelsV4OutfitDefinition
    """

    return (
        await asyncio_detailed(
            outfit_id=outfit_id,
            client=client,
            selection_types=selection_types,
            check_asset_availability=check_asset_availability,
            roblox_place_id=roblox_place_id,
        )
    ).parsed
