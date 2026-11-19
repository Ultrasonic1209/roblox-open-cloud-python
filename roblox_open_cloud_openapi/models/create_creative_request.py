from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateCreativeRequest")


@_attrs_define
class CreateCreativeRequest:
    """
    Attributes:
        asset_id (str): The Roblox image asset ID to save to the selected ads account, as a decimal string.
            groupId selects the group ads account; absent groupId selects the personal ads account.
        universe_id (str | Unset): Optional experience to associate the creative with, as a decimal string.
    """

    asset_id: str
    universe_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_id = self.asset_id

        universe_id = self.universe_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assetId": asset_id,
            }
        )
        if universe_id is not UNSET:
            field_dict["universeId"] = universe_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        asset_id = d.pop("assetId")

        universe_id = d.pop("universeId", UNSET)

        create_creative_request = cls(
            asset_id=asset_id,
            universe_id=universe_id,
        )

        create_creative_request.additional_properties = d
        return create_creative_request

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
