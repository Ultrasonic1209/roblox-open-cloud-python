from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxApiAvatarModelsAccessoryScaleModel")


@_attrs_define
class RobloxApiAvatarModelsAccessoryScaleModel:
    """A model which contains accessory Scale, that is the multiplier
    with respect to the default size. For example, scale = 2 means
    twice the default size of an asset

        Attributes:
            x_scale (float | Unset): Float that determines the scale refinement that
                this accessory is resized in the x-direction
                Default size is 1
            y_scale (float | Unset): Float that determines the scale refinement that
                this accessory is resized in the y-direction
                Default size is 1
            z_scale (float | Unset): Float that determines the scale refinement that
                this accessory is resized in the z-direction
                Default size is 1
    """

    x_scale: float | Unset = UNSET
    y_scale: float | Unset = UNSET
    z_scale: float | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        x_scale = self.x_scale

        y_scale = self.y_scale

        z_scale = self.z_scale

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if x_scale is not UNSET:
            field_dict["xScale"] = x_scale
        if y_scale is not UNSET:
            field_dict["yScale"] = y_scale
        if z_scale is not UNSET:
            field_dict["zScale"] = z_scale

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        x_scale = d.pop("xScale", UNSET)

        y_scale = d.pop("yScale", UNSET)

        z_scale = d.pop("zScale", UNSET)

        roblox_api_avatar_models_accessory_scale_model = cls(
            x_scale=x_scale,
            y_scale=y_scale,
            z_scale=z_scale,
        )

        return roblox_api_avatar_models_accessory_scale_model
