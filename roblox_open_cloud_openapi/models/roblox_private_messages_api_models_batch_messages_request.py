from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxPrivateMessagesApiModelsBatchMessagesRequest")


@_attrs_define
class RobloxPrivateMessagesApiModelsBatchMessagesRequest:
    """
    Attributes:
        message_ids (list[int] | Unset):
    """

    message_ids: list[int] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        message_ids: list[int] | Unset = UNSET
        if not isinstance(self.message_ids, Unset):
            message_ids = self.message_ids

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if message_ids is not UNSET:
            field_dict["messageIds"] = message_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        message_ids = cast(list[int], d.pop("messageIds", UNSET))

        roblox_private_messages_api_models_batch_messages_request = cls(
            message_ids=message_ids,
        )

        return roblox_private_messages_api_models_batch_messages_request
