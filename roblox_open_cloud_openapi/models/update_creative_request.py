from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateCreativeRequest")


@_attrs_define
class UpdateCreativeRequest:
    """
    Attributes:
        is_archived (bool | Unset): Archive or unarchive the creative. Archiving must be the only field and requires no
            enabled ad to use the asset.
        universe_id (None | str | Unset): Set the associated experience, or use null to clear it. Omit to keep it
            unchanged.
    """

    is_archived: bool | Unset = UNSET
    universe_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_archived = self.is_archived

        universe_id: None | str | Unset
        if isinstance(self.universe_id, Unset):
            universe_id = UNSET
        else:
            universe_id = self.universe_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_archived is not UNSET:
            field_dict["isArchived"] = is_archived
        if universe_id is not UNSET:
            field_dict["universeId"] = universe_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_archived = d.pop("isArchived", UNSET)

        def _parse_universe_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        universe_id = _parse_universe_id(d.pop("universeId", UNSET))

        update_creative_request = cls(
            is_archived=is_archived,
            universe_id=universe_id,
        )

        update_creative_request.additional_properties = d
        return update_creative_request

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
