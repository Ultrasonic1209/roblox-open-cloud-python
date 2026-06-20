from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.roblox_api_avatar_models_accessory_refinement_model import (
        RobloxApiAvatarModelsAccessoryRefinementModel,
    )


T = TypeVar("T", bound="RobloxApiAvatarModelsAvatarRulesModelAccessoryRefinementUpperBounds")


@_attrs_define
class RobloxApiAvatarModelsAvatarRulesModelAccessoryRefinementUpperBounds:
    """The lower bounds for accessory refinement settings."""

    additional_properties: dict[str, RobloxApiAvatarModelsAccessoryRefinementModel] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_api_avatar_models_accessory_refinement_model import (
            RobloxApiAvatarModelsAccessoryRefinementModel,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        roblox_api_avatar_models_avatar_rules_model_accessory_refinement_upper_bounds = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = RobloxApiAvatarModelsAccessoryRefinementModel.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        roblox_api_avatar_models_avatar_rules_model_accessory_refinement_upper_bounds.additional_properties = (
            additional_properties
        )
        return roblox_api_avatar_models_avatar_rules_model_accessory_refinement_upper_bounds

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> RobloxApiAvatarModelsAccessoryRefinementModel:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: RobloxApiAvatarModelsAccessoryRefinementModel) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
