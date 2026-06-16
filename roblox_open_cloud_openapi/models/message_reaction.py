from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MessageReaction")


@_attrs_define
class MessageReaction:
    """Represents the reaction to a message.

    Attributes:
        emote_id (str | Unset): The id of the emote.
        count (int | Unset): The count of reactions for this emote.
    """

    emote_id: str | Unset = UNSET
    count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        emote_id = self.emote_id

        count = self.count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if emote_id is not UNSET:
            field_dict["emoteId"] = emote_id
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        emote_id = d.pop("emoteId", UNSET)

        count = d.pop("count", UNSET)

        message_reaction = cls(
            emote_id=emote_id,
            count=count,
        )

        message_reaction.additional_properties = d
        return message_reaction

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
