from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.internal_public_v1_advertisable_universe import InternalPublicV1AdvertisableUniverse


T = TypeVar("T", bound="InternalPublicV1ListAdvertisableUniversesResponse")


@_attrs_define
class InternalPublicV1ListAdvertisableUniversesResponse:
    """
    Attributes:
        advertisable_universes (list[InternalPublicV1AdvertisableUniverse] | Unset): The complete set of experiences the
            caller can advertise. This endpoint is not
            paginated; the full list is returned in one response.
    """

    advertisable_universes: list[InternalPublicV1AdvertisableUniverse] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        advertisable_universes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.advertisable_universes, Unset):
            advertisable_universes = []
            for advertisable_universes_item_data in self.advertisable_universes:
                advertisable_universes_item = advertisable_universes_item_data.to_dict()
                advertisable_universes.append(advertisable_universes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if advertisable_universes is not UNSET:
            field_dict["advertisableUniverses"] = advertisable_universes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.internal_public_v1_advertisable_universe import InternalPublicV1AdvertisableUniverse

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _advertisable_universes = d.pop("advertisableUniverses", UNSET)
        advertisable_universes: list[InternalPublicV1AdvertisableUniverse] | Unset = UNSET
        if _advertisable_universes is not UNSET:
            advertisable_universes = []
            for advertisable_universes_item_data in _advertisable_universes:
                advertisable_universes_item = InternalPublicV1AdvertisableUniverse.from_dict(
                    advertisable_universes_item_data
                )

                advertisable_universes.append(advertisable_universes_item)

        internal_public_v1_list_advertisable_universes_response = cls(
            advertisable_universes=advertisable_universes,
        )

        internal_public_v1_list_advertisable_universes_response.additional_properties = d
        return internal_public_v1_list_advertisable_universes_response

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
