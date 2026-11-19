from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_item_configuration_api_bundle_details_bundle_type import (
    RobloxItemConfigurationApiBundleDetailsBundleType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxItemConfigurationApiBundleDetails")


@_attrs_define
class RobloxItemConfigurationApiBundleDetails:
    """The bundle details.

    Attributes:
        bundle_type (RobloxItemConfigurationApiBundleDetailsBundleType | Unset): The bundle type. ['Invalid' = 0, 'Body'
            = 1, 'DynamicHead' = 2, 'Shoes' = 3, 'AvatarAnimations' = 4]
    """

    bundle_type: RobloxItemConfigurationApiBundleDetailsBundleType | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        bundle_type: int | Unset = UNSET
        if not isinstance(self.bundle_type, Unset):
            bundle_type = self.bundle_type.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if bundle_type is not UNSET:
            field_dict["bundleType"] = bundle_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _bundle_type = d.pop("bundleType", UNSET)
        bundle_type: RobloxItemConfigurationApiBundleDetailsBundleType | Unset
        if isinstance(_bundle_type, Unset):
            bundle_type = UNSET
        else:
            bundle_type = RobloxItemConfigurationApiBundleDetailsBundleType(_bundle_type)

        roblox_item_configuration_api_bundle_details = cls(
            bundle_type=bundle_type,
        )

        return roblox_item_configuration_api_bundle_details
