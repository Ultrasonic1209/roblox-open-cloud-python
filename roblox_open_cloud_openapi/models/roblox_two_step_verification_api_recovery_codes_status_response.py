from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxTwoStepVerificationApiRecoveryCodesStatusResponse")


@_attrs_define
class RobloxTwoStepVerificationApiRecoveryCodesStatusResponse:
    """The response for getting the status of recovery codes for a user.

    Attributes:
        active_count (int | Unset): The number of unused recovery codes the user has available.
        created (datetime.datetime | Unset): The date time the recovery codes were generated at.
    """

    active_count: int | Unset = UNSET
    created: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        active_count = self.active_count

        created: str | Unset = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if active_count is not UNSET:
            field_dict["activeCount"] = active_count
        if created is not UNSET:
            field_dict["created"] = created

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        active_count = d.pop("activeCount", UNSET)

        _created = d.pop("created", UNSET)
        created: datetime.datetime | Unset
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = datetime.datetime.fromisoformat(_created)

        roblox_two_step_verification_api_recovery_codes_status_response = cls(
            active_count=active_count,
            created=created,
        )

        return roblox_two_step_verification_api_recovery_codes_status_response
