from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxApiAvatarModelsAccessoryRotationModel")


@_attrs_define
class RobloxApiAvatarModelsAccessoryRotationModel:
    """A model which contains accessory rotation coordinates

    Attributes:
        x_rotation (float | Unset): Float from -180 to 180 that determines the absolute
            rotation refinement that this accessory is rotated in the
            x-direction
        y_rotation (float | Unset): Float from -180 to 180 that determines the absolute
            rotation refinement that this accessory is rotated in the
            y-direction
        z_rotation (float | Unset): Float from -180 to 180 that determines the absolute
            rotation refinement that this accessory is rotated in the
            z-direction
    """

    x_rotation: float | Unset = UNSET
    y_rotation: float | Unset = UNSET
    z_rotation: float | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        x_rotation = self.x_rotation

        y_rotation = self.y_rotation

        z_rotation = self.z_rotation

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if x_rotation is not UNSET:
            field_dict["xRotation"] = x_rotation
        if y_rotation is not UNSET:
            field_dict["yRotation"] = y_rotation
        if z_rotation is not UNSET:
            field_dict["zRotation"] = z_rotation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        x_rotation = d.pop("xRotation", UNSET)

        y_rotation = d.pop("yRotation", UNSET)

        z_rotation = d.pop("zRotation", UNSET)

        roblox_api_avatar_models_accessory_rotation_model = cls(
            x_rotation=x_rotation,
            y_rotation=y_rotation,
            z_rotation=z_rotation,
        )

        return roblox_api_avatar_models_accessory_rotation_model
