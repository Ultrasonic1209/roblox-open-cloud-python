from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.private_server_invite_response_type import PrivateServerInviteResponseType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CanInviteUserResponse")


@_attrs_define
class CanInviteUserResponse:
    """
    Attributes:
        can_invite (bool | Unset):
        does_owner_privacy_restrict_joins (bool | Unset):
        invite_response_type (PrivateServerInviteResponseType | Unset):
    """

    can_invite: bool | Unset = UNSET
    does_owner_privacy_restrict_joins: bool | Unset = UNSET
    invite_response_type: PrivateServerInviteResponseType | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        can_invite = self.can_invite

        does_owner_privacy_restrict_joins = self.does_owner_privacy_restrict_joins

        invite_response_type: str | Unset = UNSET
        if not isinstance(self.invite_response_type, Unset):
            invite_response_type = self.invite_response_type.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if can_invite is not UNSET:
            field_dict["canInvite"] = can_invite
        if does_owner_privacy_restrict_joins is not UNSET:
            field_dict["doesOwnerPrivacyRestrictJoins"] = does_owner_privacy_restrict_joins
        if invite_response_type is not UNSET:
            field_dict["inviteResponseType"] = invite_response_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        can_invite = d.pop("canInvite", UNSET)

        does_owner_privacy_restrict_joins = d.pop("doesOwnerPrivacyRestrictJoins", UNSET)

        _invite_response_type = d.pop("inviteResponseType", UNSET)
        invite_response_type: PrivateServerInviteResponseType | Unset
        if isinstance(_invite_response_type, Unset):
            invite_response_type = UNSET
        else:
            invite_response_type = PrivateServerInviteResponseType(_invite_response_type)

        can_invite_user_response = cls(
            can_invite=can_invite,
            does_owner_privacy_restrict_joins=does_owner_privacy_restrict_joins,
            invite_response_type=invite_response_type,
        )

        return can_invite_user_response
