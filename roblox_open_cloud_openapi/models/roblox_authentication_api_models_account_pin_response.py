from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAuthenticationApiModelsAccountPinResponse")


@_attrs_define
class RobloxAuthenticationApiModelsAccountPinResponse:
    """
    Attributes:
        unlocked_until (float | Unset):
    """

    unlocked_until: float | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        unlocked_until = self.unlocked_until

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if unlocked_until is not UNSET:
            field_dict["unlockedUntil"] = unlocked_until

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        unlocked_until = d.pop("unlockedUntil", UNSET)

        roblox_authentication_api_models_account_pin_response = cls(
            unlocked_until=unlocked_until,
        )

        return roblox_authentication_api_models_account_pin_response
