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


T = TypeVar("T", bound="RobloxPrivateMessagesApiModelsAnnouncementsDetailsResponse")


@_attrs_define
class RobloxPrivateMessagesApiModelsAnnouncementsDetailsResponse:
    """A message details response.

    Attributes:
        id (int | Unset): The message's ID.
        sender (RobloxPrivateMessagesApiModelsVerifiedSkinnyUserResponse | Unset): A response model representing user
            basic information and the user's verified badge status.
        subject (str | Unset): The subject of the message.
        body (str | Unset): The body of the message.
        created (datetime.datetime | Unset): When the message was created.
        updated (datetime.datetime | Unset): When the message was last updated.
    """

    id: int | Unset = UNSET
    sender: RobloxPrivateMessagesApiModelsVerifiedSkinnyUserResponse | Unset = UNSET
    subject: str | Unset = UNSET
    body: str | Unset = UNSET
    created: datetime.datetime | Unset = UNSET
    updated: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        sender: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sender, Unset):
            sender = self.sender.to_dict()

        subject = self.subject

        body = self.body

        created: str | Unset = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        updated: str | Unset = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if sender is not UNSET:
            field_dict["sender"] = sender
        if subject is not UNSET:
            field_dict["subject"] = subject
        if body is not UNSET:
            field_dict["body"] = body
        if created is not UNSET:
            field_dict["created"] = created
        if updated is not UNSET:
            field_dict["updated"] = updated

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

        roblox_private_messages_api_models_announcements_details_response = cls(
            id=id,
            sender=sender,
            subject=subject,
            body=body,
            created=created,
            updated=updated,
        )

        return roblox_private_messages_api_models_announcements_details_response
