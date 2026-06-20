from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_private_messages_api_models_failed_message_response import (
        RobloxPrivateMessagesApiModelsFailedMessageResponse,
    )


T = TypeVar("T", bound="RobloxPrivateMessagesApiModelsBatchMessagesResponse")


@_attrs_define
class RobloxPrivateMessagesApiModelsBatchMessagesResponse:
    """
    Attributes:
        failed_messages (list[RobloxPrivateMessagesApiModelsFailedMessageResponse] | Unset):
    """

    failed_messages: list[RobloxPrivateMessagesApiModelsFailedMessageResponse] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        failed_messages: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.failed_messages, Unset):
            failed_messages = []
            for failed_messages_item_data in self.failed_messages:
                failed_messages_item = failed_messages_item_data.to_dict()
                failed_messages.append(failed_messages_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if failed_messages is not UNSET:
            field_dict["failedMessages"] = failed_messages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_private_messages_api_models_failed_message_response import (
            RobloxPrivateMessagesApiModelsFailedMessageResponse,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _failed_messages = d.pop("failedMessages", UNSET)
        failed_messages: list[RobloxPrivateMessagesApiModelsFailedMessageResponse] | Unset = UNSET
        if _failed_messages is not UNSET:
            failed_messages = []
            for failed_messages_item_data in _failed_messages:
                failed_messages_item = RobloxPrivateMessagesApiModelsFailedMessageResponse.from_dict(
                    failed_messages_item_data
                )

                failed_messages.append(failed_messages_item)

        roblox_private_messages_api_models_batch_messages_response = cls(
            failed_messages=failed_messages,
        )

        return roblox_private_messages_api_models_batch_messages_response
