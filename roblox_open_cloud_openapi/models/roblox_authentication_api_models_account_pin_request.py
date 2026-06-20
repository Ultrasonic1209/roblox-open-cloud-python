from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAuthenticationApiModelsAccountPinRequest")


@_attrs_define
class RobloxAuthenticationApiModelsAccountPinRequest:
    """
    Attributes:
        pin (str | Unset):
        reauthentication_token (str | Unset):
    """

    pin: str | Unset = UNSET
    reauthentication_token: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        pin = self.pin

        reauthentication_token = self.reauthentication_token

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if pin is not UNSET:
            field_dict["pin"] = pin
        if reauthentication_token is not UNSET:
            field_dict["reauthenticationToken"] = reauthentication_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        pin = d.pop("pin", UNSET)

        reauthentication_token = d.pop("reauthenticationToken", UNSET)

        roblox_authentication_api_models_account_pin_request = cls(
            pin=pin,
            reauthentication_token=reauthentication_token,
        )

        return roblox_authentication_api_models_account_pin_request
