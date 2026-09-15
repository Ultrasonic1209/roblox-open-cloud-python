from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="RobloxGroupsClientTierCapabilities")


@_attrs_define
class RobloxGroupsClientTierCapabilities:
    """
    Attributes:
        is_eligible_for_unrestricted_messages (bool):
    """

    is_eligible_for_unrestricted_messages: bool

    def to_dict(self) -> dict[str, Any]:
        is_eligible_for_unrestricted_messages = self.is_eligible_for_unrestricted_messages

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "isEligibleForUnrestrictedMessages": is_eligible_for_unrestricted_messages,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        is_eligible_for_unrestricted_messages = d.pop("isEligibleForUnrestrictedMessages")

        roblox_groups_client_tier_capabilities = cls(
            is_eligible_for_unrestricted_messages=is_eligible_for_unrestricted_messages,
        )

        return roblox_groups_client_tier_capabilities
