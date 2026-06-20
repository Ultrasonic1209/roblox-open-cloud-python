from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserRestrictionGameJoinRestriction")


@_attrs_define
class UserRestrictionGameJoinRestriction:
    """A restriction means the affected user will not be able to join the parent
    universe or place, and will be kicked if currently joined.

        Attributes:
            active (bool | Unset): By default, this is false since a user's access to an experience
                is not restricted to begin with.

                If this is set to true at the experience level, this becomes true
                automatically at the place level for all places in the experience. Example: True.
            start_time (datetime.datetime | Unset): The start time of the restriction. Example: 2023-07-05T12:34:56Z.
            duration (str | Unset): The duration of the restriction.

                If not specified, the restriction is permanent. If specified, the range
                must be from 1 second to 315,576,000,000 seconds, inclusive. Durations
                with sub-second precision are not permitted. Example: 3s.
            private_reason (str | Unset): The reason the restriction was created.

                This field *is not* displayed to the user. 1,000 character maximum. Example: some private reason.
            display_reason (str | Unset): The user-facing reason the restriction was created.

                This field *is* displayed to the user. 400 character maximum. Example: some display reason.
            exclude_alt_accounts (bool | Unset): When true, the restriction will not be be propagated to alt accounts.

                Defaults to false. Example: True.
            inherited (bool | Unset): This is true when the restriction doesn't directly apply to the parent
                resource, but to some other ancestor resource.

                For example, if a user restriction exists on universes/123, then any
                places within that universe from which the user was not explicitly
                restricted will have an inherited restriction and this field will be
                `true`. Example: True.
    """

    active: bool | Unset = UNSET
    start_time: datetime.datetime | Unset = UNSET
    duration: str | Unset = UNSET
    private_reason: str | Unset = UNSET
    display_reason: str | Unset = UNSET
    exclude_alt_accounts: bool | Unset = UNSET
    inherited: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active = self.active

        start_time: str | Unset = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat()

        duration = self.duration

        private_reason = self.private_reason

        display_reason = self.display_reason

        exclude_alt_accounts = self.exclude_alt_accounts

        inherited = self.inherited

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        if exclude_alt_accounts is not UNSET:
            field_dict["excludeAltAccounts"] = exclude_alt_accounts
        if inherited is not UNSET:
            field_dict["inherited"] = inherited

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
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

        exclude_alt_accounts = d.pop("excludeAltAccounts", UNSET)

        inherited = d.pop("inherited", UNSET)

        user_restriction_game_join_restriction = cls(
            active=active,
            start_time=start_time,
            duration=duration,
            private_reason=private_reason,
            display_reason=display_reason,
            exclude_alt_accounts=exclude_alt_accounts,
            inherited=inherited,
        )

        user_restriction_game_join_restriction.additional_properties = d
        return user_restriction_game_join_restriction

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
