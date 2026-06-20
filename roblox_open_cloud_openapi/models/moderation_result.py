from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModerationResult")


@_attrs_define
class ModerationResult:
    """The moderation result of the asset.

    Attributes:
        moderation_state (str | Unset): The moderation state of the asset. Can be `Reviewing`, `Rejected`, or
            `Approved`.
    """

    moderation_state: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        moderation_state = self.moderation_state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if moderation_state is not UNSET:
            field_dict["moderationState"] = moderation_state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        moderation_state = d.pop("moderationState", UNSET)

        moderation_result = cls(
            moderation_state=moderation_state,
        )

        moderation_result.additional_properties = d
        return moderation_result

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
