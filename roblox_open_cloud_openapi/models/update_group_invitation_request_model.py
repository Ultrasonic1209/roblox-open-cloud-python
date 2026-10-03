from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.group_invitation_status import GroupInvitationStatus

T = TypeVar("T", bound="UpdateGroupInvitationRequestModel")


@_attrs_define
class UpdateGroupInvitationRequestModel:
    """Request for accepting or declining a group invitation.

    Attributes:
        status (GroupInvitationStatus): Status of a group invitation, serialized as its name.
    """

    status: GroupInvitationStatus

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        status = GroupInvitationStatus(d.pop("status"))

        update_group_invitation_request_model = cls(
            status=status,
        )

        return update_group_invitation_request_model
