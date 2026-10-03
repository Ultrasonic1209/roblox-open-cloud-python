from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.group_invitation_status import GroupInvitationStatus

T = TypeVar("T", bound="GroupInvitation")


@_attrs_define
class GroupInvitation:
    """An invitation to join a group.

    Attributes:
        id (str): The invitation id. Stringified because it can exceed the 2^53-1 JSON number limit.
        group_id (int): The group the invitation is for.
        recipient_user_id (int): The invited user.
        sender_user_id (int): The user who sent the invitation.
        status (GroupInvitationStatus): Status of a group invitation, serialized as its name.
        role_ids (list[int]): Every group role id attached to the invitation.
        updated_at (datetime.datetime): When the invitation was last updated (UTC).
    """

    id: str
    group_id: int
    recipient_user_id: int
    sender_user_id: int
    status: GroupInvitationStatus
    role_ids: list[int]
    updated_at: datetime.datetime

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        group_id = self.group_id

        recipient_user_id = self.recipient_user_id

        sender_user_id = self.sender_user_id

        status = self.status.value

        role_ids = self.role_ids

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "groupId": group_id,
                "recipientUserId": recipient_user_id,
                "senderUserId": sender_user_id,
                "status": status,
                "roleIds": role_ids,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        id = d.pop("id")

        group_id = d.pop("groupId")

        recipient_user_id = d.pop("recipientUserId")

        sender_user_id = d.pop("senderUserId")

        status = GroupInvitationStatus(d.pop("status"))

        role_ids = cast(list[int], d.pop("roleIds"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updatedAt"))

        group_invitation = cls(
            id=id,
            group_id=group_id,
            recipient_user_id=recipient_user_id,
            sender_user_id=sender_user_id,
            status=status,
            role_ids=role_ids,
            updated_at=updated_at,
        )

        return group_invitation
