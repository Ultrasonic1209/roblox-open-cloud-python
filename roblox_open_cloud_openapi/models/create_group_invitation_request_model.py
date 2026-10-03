from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateGroupInvitationRequestModel")


@_attrs_define
class CreateGroupInvitationRequestModel:
    """Request for inviting a user to a group.

    Attributes:
        recipient_user_id (int): The user to invite.
        role_ids (list[int] | None | Unset): Group role ids to grant when the invitation is accepted.
    """

    recipient_user_id: int
    role_ids: list[int] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        recipient_user_id = self.recipient_user_id

        role_ids: list[int] | None | Unset
        if isinstance(self.role_ids, Unset):
            role_ids = UNSET
        elif isinstance(self.role_ids, list):
            role_ids = self.role_ids

        else:
            role_ids = self.role_ids

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "recipientUserId": recipient_user_id,
            }
        )
        if role_ids is not UNSET:
            field_dict["roleIds"] = role_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        recipient_user_id = d.pop("recipientUserId")

        def _parse_role_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                role_ids_type_0 = cast(list[int], data)

                return role_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        role_ids = _parse_role_ids(d.pop("roleIds", UNSET))

        create_group_invitation_request_model = cls(
            recipient_user_id=recipient_user_id,
            role_ids=role_ids,
        )

        return create_group_invitation_request_model
