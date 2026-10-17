from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxPrivateMessagesApiModelsFailedMessageResponse")


@_attrs_define
class RobloxPrivateMessagesApiModelsFailedMessageResponse:
    """
    Attributes:
        message_id (int | Unset):
        error_message (str | Unset):
    """

    message_id: int | Unset = UNSET
    error_message: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        message_id = self.message_id

        error_message = self.error_message

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if message_id is not UNSET:
            field_dict["messageId"] = message_id
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message_id = d.pop("messageId", UNSET)

        error_message = d.pop("errorMessage", UNSET)

        roblox_private_messages_api_models_failed_message_response = cls(
            message_id=message_id,
            error_message=error_message,
        )

        return roblox_private_messages_api_models_failed_message_response
