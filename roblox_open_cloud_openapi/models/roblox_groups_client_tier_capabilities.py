from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGroupsClientTierCapabilities")


@_attrs_define
class RobloxGroupsClientTierCapabilities:
    """
    Attributes:
        is_eligible_for_unrestricted_messages (bool | Unset):
    """

    is_eligible_for_unrestricted_messages: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        is_eligible_for_unrestricted_messages = self.is_eligible_for_unrestricted_messages

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if is_eligible_for_unrestricted_messages is not UNSET:
            field_dict["isEligibleForUnrestrictedMessages"] = is_eligible_for_unrestricted_messages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        is_eligible_for_unrestricted_messages = d.pop("isEligibleForUnrestrictedMessages", UNSET)

        roblox_groups_client_tier_capabilities = cls(
            is_eligible_for_unrestricted_messages=is_eligible_for_unrestricted_messages,
        )

        return roblox_groups_client_tier_capabilities
