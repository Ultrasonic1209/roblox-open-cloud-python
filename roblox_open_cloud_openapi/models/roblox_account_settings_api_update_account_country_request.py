from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAccountSettingsApiUpdateAccountCountryRequest")


@_attrs_define
class RobloxAccountSettingsApiUpdateAccountCountryRequest:
    """Request Model for updating a user's account country

    Attributes:
        target_country_id (int | Unset): The targetCountryId
    """

    target_country_id: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        target_country_id = self.target_country_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if target_country_id is not UNSET:
            field_dict["targetCountryId"] = target_country_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        target_country_id = d.pop("targetCountryId", UNSET)

        roblox_account_settings_api_update_account_country_request = cls(
            target_country_id=target_country_id,
        )

        return roblox_account_settings_api_update_account_country_request
