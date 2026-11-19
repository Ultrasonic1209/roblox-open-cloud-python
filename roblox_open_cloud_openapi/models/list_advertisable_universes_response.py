from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.advertisable_universe import AdvertisableUniverse


T = TypeVar("T", bound="ListAdvertisableUniversesResponse")


@_attrs_define
class ListAdvertisableUniversesResponse:
    """
    Attributes:
        advertisable_universes (list[AdvertisableUniverse]): The complete set of experiences the caller can advertise.
            This endpoint is not
            paginated; the full list is returned in one response.
    """

    advertisable_universes: list[AdvertisableUniverse]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        advertisable_universes = []
        for advertisable_universes_item_data in self.advertisable_universes:
            advertisable_universes_item = advertisable_universes_item_data.to_dict()
            advertisable_universes.append(advertisable_universes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "advertisableUniverses": advertisable_universes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.advertisable_universe import AdvertisableUniverse  # noqa: PLC0415

        d = dict(src_dict)
        advertisable_universes = []
        _advertisable_universes = d.pop("advertisableUniverses")
        for advertisable_universes_item_data in _advertisable_universes:
            advertisable_universes_item = AdvertisableUniverse.from_dict(advertisable_universes_item_data)

            advertisable_universes.append(advertisable_universes_item)

        list_advertisable_universes_response = cls(
            advertisable_universes=advertisable_universes,
        )

        list_advertisable_universes_response.additional_properties = d
        return list_advertisable_universes_response

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
