from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.message_reaction import MessageReaction


T = TypeVar("T", bound="ContentMessage")


@_attrs_define
class ContentMessage:
    """Represents the content of a message.

    Attributes:
        create_time (datetime.datetime | Unset): The timestamp when the message was created. Example:
            2023-07-05T12:34:56Z.
        update_time (datetime.datetime | Unset): The timestamp when the message was last updated. Example:
            2023-07-05T12:34:56Z.
        plain_text (str | Unset): The plain text content of the message.
        author (str | Unset): The resource path of the user who created the message. Example: users/156.
        message_reaction (list[MessageReaction] | Unset): The reactions to the message, if this feature is enabled for
            this message.
    """

    create_time: datetime.datetime | Unset = UNSET
    update_time: datetime.datetime | Unset = UNSET
    plain_text: str | Unset = UNSET
    author: str | Unset = UNSET
    message_reaction: list[MessageReaction] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        create_time: str | Unset = UNSET
        if not isinstance(self.create_time, Unset):
            create_time = self.create_time.isoformat()

        update_time: str | Unset = UNSET
        if not isinstance(self.update_time, Unset):
            update_time = self.update_time.isoformat()

        plain_text = self.plain_text

        author = self.author

        message_reaction: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.message_reaction, Unset):
            message_reaction = []
            for message_reaction_item_data in self.message_reaction:
                message_reaction_item = message_reaction_item_data.to_dict()
                message_reaction.append(message_reaction_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if create_time is not UNSET:
            field_dict["createTime"] = create_time
        if update_time is not UNSET:
            field_dict["updateTime"] = update_time
        if plain_text is not UNSET:
            field_dict["plainText"] = plain_text
        if author is not UNSET:
            field_dict["author"] = author
        if message_reaction is not UNSET:
            field_dict["messageReaction"] = message_reaction

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.message_reaction import MessageReaction

        d = dict(src_dict)
        _create_time = d.pop("createTime", UNSET)
        create_time: datetime.datetime | Unset
        if isinstance(_create_time, Unset):
            create_time = UNSET
        else:
            create_time = datetime.datetime.fromisoformat(_create_time)

        _update_time = d.pop("updateTime", UNSET)
        update_time: datetime.datetime | Unset
        if isinstance(_update_time, Unset):
            update_time = UNSET
        else:
            update_time = datetime.datetime.fromisoformat(_update_time)

        plain_text = d.pop("plainText", UNSET)

        author = d.pop("author", UNSET)

        _message_reaction = d.pop("messageReaction", UNSET)
        message_reaction: list[MessageReaction] | Unset = UNSET
        if _message_reaction is not UNSET:
            message_reaction = []
            for message_reaction_item_data in _message_reaction:
                message_reaction_item = MessageReaction.from_dict(message_reaction_item_data)

                message_reaction.append(message_reaction_item)

        content_message = cls(
            create_time=create_time,
            update_time=update_time,
            plain_text=plain_text,
            author=author,
            message_reaction=message_reaction,
        )

        content_message.additional_properties = d
        return content_message

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
