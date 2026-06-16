from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_restriction_log_moderator import UserRestrictionLogModerator
    from ..models.user_restriction_log_restriction_type import UserRestrictionLogRestrictionType


T = TypeVar("T", bound="UserRestrictionLog")


@_attrs_define
class UserRestrictionLog:
    """An entity capturing a state change on a type of restriction.

    Attributes:
        user (str | Unset): The user to which this restriction update is applied. Example: users/156.
        place (str | Unset): The place in which a user restriction was explicitly updated.
            This field is empty if the log captures a state change applied on the
            universe level. Example: places/456.
        moderator (UserRestrictionLogModerator | Unset): An entity capturing the author of a state change.
        create_time (datetime.datetime | Unset): When the change happened. Example: 2023-07-05T12:34:56Z.
        active (bool | Unset): Whether the restriction was active after the action
            represented by this log. Example: True.
        start_time (datetime.datetime | Unset): The start time of the restriction. Example: 2023-07-05T12:34:56Z.
        duration (str | Unset): The duration of the restriction.

            If not specified, the restriction is permanent. Example: 3s.
        private_reason (str | Unset): The reason the restriction was created.

            This field *is not* displayed to the user. Example: some private reason.
        display_reason (str | Unset): The user-facing reason the restriction was created.

            This field *is* displayed to the user. Example: some display reason.
        restriction_type (UserRestrictionLogRestrictionType | Unset): The type of restriction.
        exclude_alt_accounts (bool | Unset): When true, the restriction will not be be propagated to alt accounts.

            Defaults to false. Example: True.
    """

    user: str | Unset = UNSET
    place: str | Unset = UNSET
    moderator: UserRestrictionLogModerator | Unset = UNSET
    create_time: datetime.datetime | Unset = UNSET
    active: bool | Unset = UNSET
    start_time: datetime.datetime | Unset = UNSET
    duration: str | Unset = UNSET
    private_reason: str | Unset = UNSET
    display_reason: str | Unset = UNSET
    restriction_type: UserRestrictionLogRestrictionType | Unset = UNSET
    exclude_alt_accounts: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user = self.user

        place = self.place

        moderator: dict[str, Any] | Unset = UNSET
        if not isinstance(self.moderator, Unset):
            moderator = self.moderator.to_dict()

        create_time: str | Unset = UNSET
        if not isinstance(self.create_time, Unset):
            create_time = self.create_time.isoformat()

        active = self.active

        start_time: str | Unset = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat()

        duration = self.duration

        private_reason = self.private_reason

        display_reason = self.display_reason

        restriction_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.restriction_type, Unset):
            restriction_type = self.restriction_type.to_dict()

        exclude_alt_accounts = self.exclude_alt_accounts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user is not UNSET:
            field_dict["user"] = user
        if place is not UNSET:
            field_dict["place"] = place
        if moderator is not UNSET:
            field_dict["moderator"] = moderator
        if create_time is not UNSET:
            field_dict["createTime"] = create_time
        if active is not UNSET:
            field_dict["active"] = active
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if duration is not UNSET:
            field_dict["duration"] = duration
        if private_reason is not UNSET:
            field_dict["privateReason"] = private_reason
        if display_reason is not UNSET:
            field_dict["displayReason"] = display_reason
        if restriction_type is not UNSET:
            field_dict["restrictionType"] = restriction_type
        if exclude_alt_accounts is not UNSET:
            field_dict["excludeAltAccounts"] = exclude_alt_accounts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_restriction_log_moderator import UserRestrictionLogModerator
        from ..models.user_restriction_log_restriction_type import UserRestrictionLogRestrictionType

        d = dict(src_dict)
        user = d.pop("user", UNSET)

        place = d.pop("place", UNSET)

        _moderator = d.pop("moderator", UNSET)
        moderator: UserRestrictionLogModerator | Unset
        if isinstance(_moderator, Unset):
            moderator = UNSET
        else:
            moderator = UserRestrictionLogModerator.from_dict(_moderator)

        _create_time = d.pop("createTime", UNSET)
        create_time: datetime.datetime | Unset
        if isinstance(_create_time, Unset):
            create_time = UNSET
        else:
            create_time = datetime.datetime.fromisoformat(_create_time)

        active = d.pop("active", UNSET)

        _start_time = d.pop("startTime", UNSET)
        start_time: datetime.datetime | Unset
        if isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = datetime.datetime.fromisoformat(_start_time)

        duration = d.pop("duration", UNSET)

        private_reason = d.pop("privateReason", UNSET)

        display_reason = d.pop("displayReason", UNSET)

        _restriction_type = d.pop("restrictionType", UNSET)
        restriction_type: UserRestrictionLogRestrictionType | Unset
        if isinstance(_restriction_type, Unset):
            restriction_type = UNSET
        else:
            restriction_type = UserRestrictionLogRestrictionType.from_dict(_restriction_type)

        exclude_alt_accounts = d.pop("excludeAltAccounts", UNSET)

        user_restriction_log = cls(
            user=user,
            place=place,
            moderator=moderator,
            create_time=create_time,
            active=active,
            start_time=start_time,
            duration=duration,
            private_reason=private_reason,
            display_reason=display_reason,
            restriction_type=restriction_type,
            exclude_alt_accounts=exclude_alt_accounts,
        )

        user_restriction_log.additional_properties = d
        return user_restriction_log

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
