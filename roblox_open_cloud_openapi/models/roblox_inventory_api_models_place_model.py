from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_inventory_api_models_creator_model import RobloxInventoryApiModelsCreatorModel


T = TypeVar("T", bound="RobloxInventoryApiModelsPlaceModel")


@_attrs_define
class RobloxInventoryApiModelsPlaceModel:
    """
    Attributes:
        universe_id (int | Unset):
        place_id (int | Unset):
        name (str | Unset):
        creator (RobloxInventoryApiModelsCreatorModel | Unset):
        price_in_robux (int | Unset):
    """

    universe_id: int | Unset = UNSET
    place_id: int | Unset = UNSET
    name: str | Unset = UNSET
    creator: RobloxInventoryApiModelsCreatorModel | Unset = UNSET
    price_in_robux: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        universe_id = self.universe_id

        place_id = self.place_id

        name = self.name

        creator: dict[str, Any] | Unset = UNSET
        if not isinstance(self.creator, Unset):
            creator = self.creator.to_dict()

        price_in_robux = self.price_in_robux

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if universe_id is not UNSET:
            field_dict["universeId"] = universe_id
        if place_id is not UNSET:
            field_dict["placeId"] = place_id
        if name is not UNSET:
            field_dict["name"] = name
        if creator is not UNSET:
            field_dict["creator"] = creator
        if price_in_robux is not UNSET:
            field_dict["priceInRobux"] = price_in_robux

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_inventory_api_models_creator_model import RobloxInventoryApiModelsCreatorModel

        d = dict(src_dict)
        universe_id = d.pop("universeId", UNSET)

        place_id = d.pop("placeId", UNSET)

        name = d.pop("name", UNSET)

        _creator = d.pop("creator", UNSET)
        creator: RobloxInventoryApiModelsCreatorModel | Unset
        if isinstance(_creator, Unset):
            creator = UNSET
        else:
            creator = RobloxInventoryApiModelsCreatorModel.from_dict(_creator)

        price_in_robux = d.pop("priceInRobux", UNSET)

        roblox_inventory_api_models_place_model = cls(
            universe_id=universe_id,
            place_id=place_id,
            name=name,
            creator=creator,
            price_in_robux=price_in_robux,
        )

        return roblox_inventory_api_models_place_model
