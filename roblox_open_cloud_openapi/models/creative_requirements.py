from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.creative_requirements_accepted_asset_types_item import CreativeRequirementsAcceptedAssetTypesItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreativeRequirements")


@_attrs_define
class CreativeRequirements:
    """
    Attributes:
        accepted_asset_types (list[CreativeRequirementsAcceptedAssetTypesItem] | Unset): The creative asset types
            accepted. Values can be `IMAGE`.
        maximum_count (int | Unset): The most creatives a campaign can have.
        minimum_count (int | Unset): The fewest creatives a campaign can have.
    """

    accepted_asset_types: list[CreativeRequirementsAcceptedAssetTypesItem] | Unset = UNSET
    maximum_count: int | Unset = UNSET
    minimum_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accepted_asset_types: list[str] | Unset = UNSET
        if not isinstance(self.accepted_asset_types, Unset):
            accepted_asset_types = []
            for accepted_asset_types_item_data in self.accepted_asset_types:
                accepted_asset_types_item = accepted_asset_types_item_data.value
                accepted_asset_types.append(accepted_asset_types_item)

        maximum_count = self.maximum_count

        minimum_count = self.minimum_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accepted_asset_types is not UNSET:
            field_dict["acceptedAssetTypes"] = accepted_asset_types
        if maximum_count is not UNSET:
            field_dict["maximumCount"] = maximum_count
        if minimum_count is not UNSET:
            field_dict["minimumCount"] = minimum_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _accepted_asset_types = d.pop("acceptedAssetTypes", UNSET)
        accepted_asset_types: list[CreativeRequirementsAcceptedAssetTypesItem] | Unset = UNSET
        if _accepted_asset_types is not UNSET:
            accepted_asset_types = []
            for accepted_asset_types_item_data in _accepted_asset_types:
                accepted_asset_types_item = CreativeRequirementsAcceptedAssetTypesItem(accepted_asset_types_item_data)

                accepted_asset_types.append(accepted_asset_types_item)

        maximum_count = d.pop("maximumCount", UNSET)

        minimum_count = d.pop("minimumCount", UNSET)

        creative_requirements = cls(
            accepted_asset_types=accepted_asset_types,
            maximum_count=maximum_count,
            minimum_count=minimum_count,
        )

        creative_requirements.additional_properties = d
        return creative_requirements

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
