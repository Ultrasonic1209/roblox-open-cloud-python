from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="RobloxGroupsApiSetFeaturesResponseModel")


@_attrs_define
class RobloxGroupsApiSetFeaturesResponseModel:
    """Response model for setting the desired status of group features.

    Attributes:
        updated (bool): Whether any features were updated.
    """

    updated: bool

    def to_dict(self) -> dict[str, Any]:
        updated = self.updated

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "Updated": updated,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        updated = d.pop("Updated")

        roblox_groups_api_set_features_response_model = cls(
            updated=updated,
        )

        return roblox_groups_api_set_features_response_model
