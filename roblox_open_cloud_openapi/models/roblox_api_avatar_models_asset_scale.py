from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxApiAvatarModelsAssetScale")


@_attrs_define
class RobloxApiAvatarModelsAssetScale:
    """A model which contains accessory scale.

    Attributes:
        x (float | Unset): X scale multiplier of accessory.
        y (float | Unset): Y scale multiplier of accessory.
        z (float | Unset): Z scale multiplier of accessory.
    """

    x: float | Unset = UNSET
    y: float | Unset = UNSET
    z: float | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        x = self.x

        y = self.y

        z = self.z

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if x is not UNSET:
            field_dict["X"] = x
        if y is not UNSET:
            field_dict["Y"] = y
        if z is not UNSET:
            field_dict["Z"] = z

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        x = d.pop("X", UNSET)

        y = d.pop("Y", UNSET)

        z = d.pop("Z", UNSET)

        roblox_api_avatar_models_asset_scale = cls(
            x=x,
            y=y,
            z=z,
        )

        return roblox_api_avatar_models_asset_scale
