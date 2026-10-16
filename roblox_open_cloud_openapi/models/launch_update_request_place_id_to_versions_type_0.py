from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LaunchUpdateRequestPlaceIdToVersionsType0")


@_attrs_define
class LaunchUpdateRequestPlaceIdToVersionsType0:
    """Optional. A mapping of PlaceId to the specific versions to restart/bleed off for that place.
    When set for a place, only servers running those exact versions will be affected.
    If a place is not in this dictionary or has an empty set, behavior falls back to CloseOldVersionsOnly logic.

    """

    additional_properties: dict[str, list[int] | None] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            if isinstance(prop, list):
                field_dict[prop_name] = prop

            else:
                field_dict[prop_name] = prop

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        launch_update_request_place_id_to_versions_type_0 = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():

            def _parse_additional_property(data: object) -> list[int] | None:
                if data is None:
                    return data
                try:
                    if not isinstance(data, list):
                        raise TypeError()
                    additional_property_type_0 = cast(list[int], data)

                    return additional_property_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                return cast(list[int] | None, data)

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        launch_update_request_place_id_to_versions_type_0.additional_properties = additional_properties
        return launch_update_request_place_id_to_versions_type_0

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> list[int] | None:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: list[int] | None) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
