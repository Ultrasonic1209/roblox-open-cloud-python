from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_item_configuration_api_target_model_target_type import (
    RobloxItemConfigurationApiTargetModelTargetType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxItemConfigurationApiTargetModel")


@_attrs_define
class RobloxItemConfigurationApiTargetModel:
    """An item target model.

    Attributes:
        target_type (RobloxItemConfigurationApiTargetModelTargetType | Unset): The asset type of the target. ['Asset' =
            0, 'Bundle' = 1, 'IecToken' = 2, 'Look' = 3]
        target_id (str | Unset): The id of the target.
    """

    target_type: RobloxItemConfigurationApiTargetModelTargetType | Unset = UNSET
    target_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        target_type: int | Unset = UNSET
        if not isinstance(self.target_type, Unset):
            target_type = self.target_type.value

        target_id = self.target_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if target_type is not UNSET:
            field_dict["targetType"] = target_type
        if target_id is not UNSET:
            field_dict["targetId"] = target_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _target_type = d.pop("targetType", UNSET)
        target_type: RobloxItemConfigurationApiTargetModelTargetType | Unset
        if isinstance(_target_type, Unset):
            target_type = UNSET
        else:
            target_type = RobloxItemConfigurationApiTargetModelTargetType(_target_type)

        target_id = d.pop("targetId", UNSET)

        roblox_item_configuration_api_target_model = cls(
            target_type=target_type,
            target_id=target_id,
        )

        return roblox_item_configuration_api_target_model
