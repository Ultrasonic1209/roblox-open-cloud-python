from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_api_avatar_models_asset_meta_model_v1_head_shape import (
    RobloxApiAvatarModelsAssetMetaModelV1HeadShape,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_api_avatar_models_asset_position import RobloxApiAvatarModelsAssetPosition
    from ..models.roblox_api_avatar_models_asset_rotation import RobloxApiAvatarModelsAssetRotation
    from ..models.roblox_api_avatar_models_asset_scale import RobloxApiAvatarModelsAssetScale


T = TypeVar("T", bound="RobloxApiAvatarModelsAssetMetaModelV1")


@_attrs_define
class RobloxApiAvatarModelsAssetMetaModelV1:
    """Exhaustive model denoting all possible metadata fields of an asset

    Attributes:
        order (int | Unset): Layered-clothing order
        puffiness (float | Unset): Layered-clothing puffiness
        position (RobloxApiAvatarModelsAssetPosition | Unset): A model which contains accessory position coordinates.
        rotation (RobloxApiAvatarModelsAssetRotation | Unset): A model which contains accessory rotation coordinates.
        scale (RobloxApiAvatarModelsAssetScale | Unset): A model which contains accessory scale.
        head_shape (RobloxApiAvatarModelsAssetMetaModelV1HeadShape | Unset): Head Shape selected for the asset id.
            Applicable for dynamic head assets.
        static_facial_animation (bool | Unset): Indicates user choice for facial animation.
            staticFacialAnimation=false, implies the toggle as on and face will animate.
            Applicable for dynamic head assets.
        version (int | Unset): Client-authoritative meta model format version
            - default is always 1
    """

    order: int | Unset = UNSET
    puffiness: float | Unset = UNSET
    position: RobloxApiAvatarModelsAssetPosition | Unset = UNSET
    rotation: RobloxApiAvatarModelsAssetRotation | Unset = UNSET
    scale: RobloxApiAvatarModelsAssetScale | Unset = UNSET
    head_shape: RobloxApiAvatarModelsAssetMetaModelV1HeadShape | Unset = UNSET
    static_facial_animation: bool | Unset = UNSET
    version: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        order = self.order

        puffiness = self.puffiness

        position: dict[str, Any] | Unset = UNSET
        if not isinstance(self.position, Unset):
            position = self.position.to_dict()

        rotation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rotation, Unset):
            rotation = self.rotation.to_dict()

        scale: dict[str, Any] | Unset = UNSET
        if not isinstance(self.scale, Unset):
            scale = self.scale.to_dict()

        head_shape: int | Unset = UNSET
        if not isinstance(self.head_shape, Unset):
            head_shape = self.head_shape.value

        static_facial_animation = self.static_facial_animation

        version = self.version

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if order is not UNSET:
            field_dict["order"] = order
        if puffiness is not UNSET:
            field_dict["puffiness"] = puffiness
        if position is not UNSET:
            field_dict["position"] = position
        if rotation is not UNSET:
            field_dict["rotation"] = rotation
        if scale is not UNSET:
            field_dict["scale"] = scale
        if head_shape is not UNSET:
            field_dict["headShape"] = head_shape
        if static_facial_animation is not UNSET:
            field_dict["staticFacialAnimation"] = static_facial_animation
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_api_avatar_models_asset_position import RobloxApiAvatarModelsAssetPosition
        from ..models.roblox_api_avatar_models_asset_rotation import RobloxApiAvatarModelsAssetRotation
        from ..models.roblox_api_avatar_models_asset_scale import RobloxApiAvatarModelsAssetScale

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        order = d.pop("order", UNSET)

        puffiness = d.pop("puffiness", UNSET)

        _position = d.pop("position", UNSET)
        position: RobloxApiAvatarModelsAssetPosition | Unset
        if isinstance(_position, Unset):
            position = UNSET
        else:
            position = RobloxApiAvatarModelsAssetPosition.from_dict(_position)

        _rotation = d.pop("rotation", UNSET)
        rotation: RobloxApiAvatarModelsAssetRotation | Unset
        if isinstance(_rotation, Unset):
            rotation = UNSET
        else:
            rotation = RobloxApiAvatarModelsAssetRotation.from_dict(_rotation)

        _scale = d.pop("scale", UNSET)
        scale: RobloxApiAvatarModelsAssetScale | Unset
        if isinstance(_scale, Unset):
            scale = UNSET
        else:
            scale = RobloxApiAvatarModelsAssetScale.from_dict(_scale)

        _head_shape = d.pop("headShape", UNSET)
        head_shape: RobloxApiAvatarModelsAssetMetaModelV1HeadShape | Unset
        if isinstance(_head_shape, Unset):
            head_shape = UNSET
        else:
            head_shape = RobloxApiAvatarModelsAssetMetaModelV1HeadShape(_head_shape)

        static_facial_animation = d.pop("staticFacialAnimation", UNSET)

        version = d.pop("version", UNSET)

        roblox_api_avatar_models_asset_meta_model_v1 = cls(
            order=order,
            puffiness=puffiness,
            position=position,
            rotation=rotation,
            scale=scale,
            head_shape=head_shape,
            static_facial_animation=static_facial_animation,
            version=version,
        )

        return roblox_api_avatar_models_asset_meta_model_v1
