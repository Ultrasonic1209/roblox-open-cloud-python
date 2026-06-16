from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGroupsApiRecurringPayoutsConfigurationResponse")


@_attrs_define
class RobloxGroupsApiRecurringPayoutsConfigurationResponse:
    """A response model for recurring payout configuration

    Attributes:
        max_payout_partners (int | Unset): The maximum number of recurring payout partners
    """

    max_payout_partners: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        max_payout_partners = self.max_payout_partners

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if max_payout_partners is not UNSET:
            field_dict["maxPayoutPartners"] = max_payout_partners

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        max_payout_partners = d.pop("maxPayoutPartners", UNSET)

        roblox_groups_api_recurring_payouts_configuration_response = cls(
            max_payout_partners=max_payout_partners,
        )

        return roblox_groups_api_recurring_payouts_configuration_response
