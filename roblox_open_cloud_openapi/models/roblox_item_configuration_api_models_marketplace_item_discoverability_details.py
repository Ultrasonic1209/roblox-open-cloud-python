from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxItemConfigurationApiModelsMarketplaceItemDiscoverabilityDetails")


@_attrs_define
class RobloxItemConfigurationApiModelsMarketplaceItemDiscoverabilityDetails:
    """The discoverability-related details of an item.

    Attributes:
        is_discoverability_reduced (bool | Unset):
        is_core_content_gated (bool | Unset):
    """

    is_discoverability_reduced: bool | Unset = UNSET
    is_core_content_gated: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        is_discoverability_reduced = self.is_discoverability_reduced

        is_core_content_gated = self.is_core_content_gated

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if is_discoverability_reduced is not UNSET:
            field_dict["isDiscoverabilityReduced"] = is_discoverability_reduced
        if is_core_content_gated is not UNSET:
            field_dict["isCoreContentGated"] = is_core_content_gated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_discoverability_reduced = d.pop("isDiscoverabilityReduced", UNSET)

        is_core_content_gated = d.pop("isCoreContentGated", UNSET)

        roblox_item_configuration_api_models_marketplace_item_discoverability_details = cls(
            is_discoverability_reduced=is_discoverability_reduced,
            is_core_content_gated=is_core_content_gated,
        )

        return roblox_item_configuration_api_models_marketplace_item_discoverability_details
