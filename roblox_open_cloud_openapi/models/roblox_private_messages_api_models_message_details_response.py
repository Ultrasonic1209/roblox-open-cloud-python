from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_private_messages_api_models_verified_skinny_user_response import (
        RobloxPrivateMessagesApiModelsVerifiedSkinnyUserResponse,
    )


T = TypeVar("T", bound="RobloxPrivateMessagesApiModelsMessageDetailsResponse")


@_attrs_define
class RobloxPrivateMessagesApiModelsMessageDetailsResponse:
    """A message details response.

    Attributes:
        id (int | Unset): The message's ID.
        sender (RobloxPrivateMessagesApiModelsVerifiedSkinnyUserResponse | Unset): A response model representing user
            basic information and the user's verified badge status.
        recipient (RobloxPrivateMessagesApiModelsVerifiedSkinnyUserResponse | Unset): A response model representing user
            basic information and the user's verified badge status.
        subject (str | Unset): The subject of the message.
        body (str | Unset): The body of the message.
        created (datetime.datetime | Unset): When the message was created.
        updated (datetime.datetime | Unset): When the message was last updated.
        is_read (bool | Unset): Whether or not the message has been read.
        is_system_message (bool | Unset): Whether or not the message is a system message.
        is_report_abuse_displayed (bool | Unset): Whether or not the abuse report link is displayed for the message.
    """

    id: int | Unset = UNSET
    sender: RobloxPrivateMessagesApiModelsVerifiedSkinnyUserResponse | Unset = UNSET
    recipient: RobloxPrivateMessagesApiModelsVerifiedSkinnyUserResponse | Unset = UNSET
    subject: str | Unset = UNSET
    body: str | Unset = UNSET
    created: datetime.datetime | Unset = UNSET
    updated: datetime.datetime | Unset = UNSET
    is_read: bool | Unset = UNSET
    is_system_message: bool | Unset = UNSET
    is_report_abuse_displayed: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        sender: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sender, Unset):
            sender = self.sender.to_dict()

        recipient: dict[str, Any] | Unset = UNSET
        if not isinstance(self.recipient, Unset):
            recipient = self.recipient.to_dict()

        subject = self.subject

        body = self.body

        created: str | Unset = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        updated: str | Unset = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        is_read = self.is_read

        is_system_message = self.is_system_message

        is_report_abuse_displayed = self.is_report_abuse_displayed

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if sender is not UNSET:
            field_dict["sender"] = sender
        if recipient is not UNSET:
            field_dict["recipient"] = recipient
        if subject is not UNSET:
            field_dict["subject"] = subject
        if body is not UNSET:
            field_dict["body"] = body
        if created is not UNSET:
            field_dict["created"] = created
        if updated is not UNSET:
            field_dict["updated"] = updated
        if is_read is not UNSET:
            field_dict["isRead"] = is_read
        if is_system_message is not UNSET:
            field_dict["isSystemMessage"] = is_system_message
        if is_report_abuse_displayed is not UNSET:
            field_dict["isReportAbuseDisplayed"] = is_report_abuse_displayed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_private_messages_api_models_verified_skinny_user_response import (
            RobloxPrivateMessagesApiModelsVerifiedSkinnyUserResponse,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _sender = d.pop("sender", UNSET)
        sender: RobloxPrivateMessagesApiModelsVerifiedSkinnyUserResponse | Unset
        if isinstance(_sender, Unset):
            sender = UNSET
        else:
            sender = RobloxPrivateMessagesApiModelsVerifiedSkinnyUserResponse.from_dict(_sender)

        _recipient = d.pop("recipient", UNSET)
        recipient: RobloxPrivateMessagesApiModelsVerifiedSkinnyUserResponse | Unset
        if isinstance(_recipient, Unset):
            recipient = UNSET
        else:
            recipient = RobloxPrivateMessagesApiModelsVerifiedSkinnyUserResponse.from_dict(_recipient)

        subject = d.pop("subject", UNSET)

        body = d.pop("body", UNSET)

        _created = d.pop("created", UNSET)
        created: datetime.datetime | Unset
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = datetime.datetime.fromisoformat(_created)

        _updated = d.pop("updated", UNSET)
        updated: datetime.datetime | Unset
        if isinstance(_updated, Unset):
            updated = UNSET
        else:
            updated = datetime.datetime.fromisoformat(_updated)

        is_read = d.pop("isRead", UNSET)

        is_system_message = d.pop("isSystemMessage", UNSET)

        is_report_abuse_displayed = d.pop("isReportAbuseDisplayed", UNSET)

        roblox_private_messages_api_models_message_details_response = cls(
            id=id,
            sender=sender,
            recipient=recipient,
            subject=subject,
            body=body,
            created=created,
            updated=updated,
            is_read=is_read,
            is_system_message=is_system_message,
            is_report_abuse_displayed=is_report_abuse_displayed,
        )

        return roblox_private_messages_api_models_message_details_response
