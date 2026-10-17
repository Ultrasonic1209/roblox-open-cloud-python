from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxApiAvatarModelsScaleRulesModel")


@_attrs_define
class RobloxApiAvatarModelsScaleRulesModel:
    """A model that contains information about the max/mins for each scale

    Attributes:
        min_ (float | Unset): The min scale
        max_ (float | Unset): The max scale
        increment (float | Unset): The increment of the scale
    """

    min_: float | Unset = UNSET
    max_: float | Unset = UNSET
    increment: float | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        min_ = self.min_

        max_ = self.max_

        increment = self.increment

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if min_ is not UNSET:
            field_dict["min"] = min_
        if max_ is not UNSET:
            field_dict["max"] = max_
        if increment is not UNSET:
            field_dict["increment"] = increment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        min_ = d.pop("min", UNSET)

        max_ = d.pop("max", UNSET)

        increment = d.pop("increment", UNSET)

        roblox_api_avatar_models_scale_rules_model = cls(
            min_=min_,
            max_=max_,
            increment=increment,
        )

        return roblox_api_avatar_models_scale_rules_model
