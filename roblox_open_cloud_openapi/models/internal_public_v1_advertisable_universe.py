from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InternalPublicV1AdvertisableUniverse")


@_attrs_define
class InternalPublicV1AdvertisableUniverse:
    """
    Attributes:
        universe_id (str | Unset): The identifier of an experience the caller can advertise, as a decimal string.
            Resolve its name via the Open Cloud Universe API.
    """

    universe_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        universe_id = self.universe_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if universe_id is not UNSET:
            field_dict["universeId"] = universe_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        universe_id = d.pop("universeId", UNSET)

        internal_public_v1_advertisable_universe = cls(
            universe_id=universe_id,
        )

        internal_public_v1_advertisable_universe.additional_properties = d
        return internal_public_v1_advertisable_universe

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
