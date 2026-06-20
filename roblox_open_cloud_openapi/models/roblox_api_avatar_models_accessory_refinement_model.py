from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_api_avatar_models_accessory_position_model import RobloxApiAvatarModelsAccessoryPositionModel
    from ..models.roblox_api_avatar_models_accessory_rotation_model import RobloxApiAvatarModelsAccessoryRotationModel
    from ..models.roblox_api_avatar_models_accessory_scale_model import RobloxApiAvatarModelsAccessoryScaleModel


T = TypeVar("T", bound="RobloxApiAvatarModelsAccessoryRefinementModel")


@_attrs_define
class RobloxApiAvatarModelsAccessoryRefinementModel:
    """A model containing details about accessory refinement data

    Attributes:
        position (RobloxApiAvatarModelsAccessoryPositionModel | Unset): A model which contains accessory position
            coordinates
        rotation (RobloxApiAvatarModelsAccessoryRotationModel | Unset): A model which contains accessory rotation
            coordinates
        scale (RobloxApiAvatarModelsAccessoryScaleModel | Unset): A model which contains accessory Scale, that is the
            multiplier
            with respect to the default size. For example, scale = 2 means
            twice the default size of an asset
    """

    position: RobloxApiAvatarModelsAccessoryPositionModel | Unset = UNSET
    rotation: RobloxApiAvatarModelsAccessoryRotationModel | Unset = UNSET
    scale: RobloxApiAvatarModelsAccessoryScaleModel | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        position: dict[str, Any] | Unset = UNSET
        if not isinstance(self.position, Unset):
            position = self.position.to_dict()

        rotation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rotation, Unset):
            rotation = self.rotation.to_dict()

        scale: dict[str, Any] | Unset = UNSET
        if not isinstance(self.scale, Unset):
            scale = self.scale.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if position is not UNSET:
            field_dict["position"] = position
        if rotation is not UNSET:
            field_dict["rotation"] = rotation
        if scale is not UNSET:
            field_dict["scale"] = scale

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_api_avatar_models_accessory_position_model import (
            RobloxApiAvatarModelsAccessoryPositionModel,
        )
        from ..models.roblox_api_avatar_models_accessory_rotation_model import (
            RobloxApiAvatarModelsAccessoryRotationModel,
        )
        from ..models.roblox_api_avatar_models_accessory_scale_model import RobloxApiAvatarModelsAccessoryScaleModel

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _position = d.pop("position", UNSET)
        position: RobloxApiAvatarModelsAccessoryPositionModel | Unset
        if isinstance(_position, Unset):
            position = UNSET
        else:
            position = RobloxApiAvatarModelsAccessoryPositionModel.from_dict(_position)

        _rotation = d.pop("rotation", UNSET)
        rotation: RobloxApiAvatarModelsAccessoryRotationModel | Unset
        if isinstance(_rotation, Unset):
            rotation = UNSET
        else:
            rotation = RobloxApiAvatarModelsAccessoryRotationModel.from_dict(_rotation)

        _scale = d.pop("scale", UNSET)
        scale: RobloxApiAvatarModelsAccessoryScaleModel | Unset
        if isinstance(_scale, Unset):
            scale = UNSET
        else:
            scale = RobloxApiAvatarModelsAccessoryScaleModel.from_dict(_scale)

        roblox_api_avatar_models_accessory_refinement_model = cls(
            position=position,
            rotation=rotation,
            scale=scale,
        )

        return roblox_api_avatar_models_accessory_refinement_model
