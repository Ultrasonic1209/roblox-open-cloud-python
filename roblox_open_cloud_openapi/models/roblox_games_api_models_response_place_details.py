from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_games_api_models_response_purchase_data import RobloxGamesApiModelsResponsePurchaseData


T = TypeVar("T", bound="RobloxGamesApiModelsResponsePlaceDetails")


@_attrs_define
class RobloxGamesApiModelsResponsePlaceDetails:
    """Response model for a place.

    Attributes:
        place_id (int | Unset): Place Id
        name (str | Unset): Place name
        description (str | Unset): Place description
        source_name (str | Unset): Place name in source language
        source_description (str | Unset): Place description in source language
        url (str | Unset): Url
        builder (str | Unset): Creator name
        builder_id (int | Unset): Creator Id
        has_verified_badge (bool | Unset): Builder verified badge status.
        is_playable (bool | Unset): Is playable
        reason_prohibited (str | Unset): Reason prohibited
        universe_id (int | Unset): Universe id
        universe_root_place_id (int | Unset): UniverseRootPlaceId
        price (int | Unset): Price
        image_token (str | Unset): Place image token
        fiat_purchase_data (RobloxGamesApiModelsResponsePurchaseData | Unset):
    """

    place_id: int | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    source_name: str | Unset = UNSET
    source_description: str | Unset = UNSET
    url: str | Unset = UNSET
    builder: str | Unset = UNSET
    builder_id: int | Unset = UNSET
    has_verified_badge: bool | Unset = UNSET
    is_playable: bool | Unset = UNSET
    reason_prohibited: str | Unset = UNSET
    universe_id: int | Unset = UNSET
    universe_root_place_id: int | Unset = UNSET
    price: int | Unset = UNSET
    image_token: str | Unset = UNSET
    fiat_purchase_data: RobloxGamesApiModelsResponsePurchaseData | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        place_id = self.place_id

        name = self.name

        description = self.description

        source_name = self.source_name

        source_description = self.source_description

        url = self.url

        builder = self.builder

        builder_id = self.builder_id

        has_verified_badge = self.has_verified_badge

        is_playable = self.is_playable

        reason_prohibited = self.reason_prohibited

        universe_id = self.universe_id

        universe_root_place_id = self.universe_root_place_id

        price = self.price

        image_token = self.image_token

        fiat_purchase_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fiat_purchase_data, Unset):
            fiat_purchase_data = self.fiat_purchase_data.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if place_id is not UNSET:
            field_dict["placeId"] = place_id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if source_name is not UNSET:
            field_dict["sourceName"] = source_name
        if source_description is not UNSET:
            field_dict["sourceDescription"] = source_description
        if url is not UNSET:
            field_dict["url"] = url
        if builder is not UNSET:
            field_dict["builder"] = builder
        if builder_id is not UNSET:
            field_dict["builderId"] = builder_id
        if has_verified_badge is not UNSET:
            field_dict["hasVerifiedBadge"] = has_verified_badge
        if is_playable is not UNSET:
            field_dict["isPlayable"] = is_playable
        if reason_prohibited is not UNSET:
            field_dict["reasonProhibited"] = reason_prohibited
        if universe_id is not UNSET:
            field_dict["universeId"] = universe_id
        if universe_root_place_id is not UNSET:
            field_dict["universeRootPlaceId"] = universe_root_place_id
        if price is not UNSET:
            field_dict["price"] = price
        if image_token is not UNSET:
            field_dict["imageToken"] = image_token
        if fiat_purchase_data is not UNSET:
            field_dict["fiatPurchaseData"] = fiat_purchase_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_games_api_models_response_purchase_data import RobloxGamesApiModelsResponsePurchaseData

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        place_id = d.pop("placeId", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        source_name = d.pop("sourceName", UNSET)

        source_description = d.pop("sourceDescription", UNSET)

        url = d.pop("url", UNSET)

        builder = d.pop("builder", UNSET)

        builder_id = d.pop("builderId", UNSET)

        has_verified_badge = d.pop("hasVerifiedBadge", UNSET)

        is_playable = d.pop("isPlayable", UNSET)

        reason_prohibited = d.pop("reasonProhibited", UNSET)

        universe_id = d.pop("universeId", UNSET)

        universe_root_place_id = d.pop("universeRootPlaceId", UNSET)

        price = d.pop("price", UNSET)

        image_token = d.pop("imageToken", UNSET)

        _fiat_purchase_data = d.pop("fiatPurchaseData", UNSET)
        fiat_purchase_data: RobloxGamesApiModelsResponsePurchaseData | Unset
        if isinstance(_fiat_purchase_data, Unset):
            fiat_purchase_data = UNSET
        else:
            fiat_purchase_data = RobloxGamesApiModelsResponsePurchaseData.from_dict(_fiat_purchase_data)

        roblox_games_api_models_response_place_details = cls(
            place_id=place_id,
            name=name,
            description=description,
            source_name=source_name,
            source_description=source_description,
            url=url,
            builder=builder,
            builder_id=builder_id,
            has_verified_badge=has_verified_badge,
            is_playable=is_playable,
            reason_prohibited=reason_prohibited,
            universe_id=universe_id,
            universe_root_place_id=universe_root_place_id,
            price=price,
            image_token=image_token,
            fiat_purchase_data=fiat_purchase_data,
        )

        return roblox_games_api_models_response_place_details
