from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxApiAvatarModelsAccessoryPositionModel")


@_attrs_define
class RobloxApiAvatarModelsAccessoryPositionModel:
    """A model which contains accessory position coordinates

    Attributes:
        x_position (float | Unset): Float that determines the absolute
            position refinement in studs that this accessory
            is relocated in the x-direction
        y_position (float | Unset): Float that determines the absolute
            position refinement in studs that this accessory
            is relocated in the y-direction
        z_position (float | Unset): Float that determines the absolute
            position refinement in studs that this accessory
            is relocated in the z-direction
    """

    x_position: float | Unset = UNSET
    y_position: float | Unset = UNSET
    z_position: float | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        x_position = self.x_position

        y_position = self.y_position

        z_position = self.z_position

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if x_position is not UNSET:
            field_dict["xPosition"] = x_position
        if y_position is not UNSET:
            field_dict["yPosition"] = y_position
        if z_position is not UNSET:
            field_dict["zPosition"] = z_position

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        x_position = d.pop("xPosition", UNSET)

        y_position = d.pop("yPosition", UNSET)

        z_position = d.pop("zPosition", UNSET)

        roblox_api_avatar_models_accessory_position_model = cls(
            x_position=x_position,
            y_position=y_position,
            z_position=z_position,
        )

        return roblox_api_avatar_models_accessory_position_model
