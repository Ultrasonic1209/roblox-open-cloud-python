from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxTradesApiModelsV2CurrencyTransferEligibilityResponse")


@_attrs_define
class RobloxTradesApiModelsV2CurrencyTransferEligibilityResponse:
    """
    Attributes:
        can_send (bool | Unset):
        can_request (bool | Unset):
    """

    can_send: bool | Unset = UNSET
    can_request: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        can_send = self.can_send

        can_request = self.can_request

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if can_send is not UNSET:
            field_dict["canSend"] = can_send
        if can_request is not UNSET:
            field_dict["canRequest"] = can_request

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        can_send = d.pop("canSend", UNSET)

        can_request = d.pop("canRequest", UNSET)

        roblox_trades_api_models_v2_currency_transfer_eligibility_response = cls(
            can_send=can_send,
            can_request=can_request,
        )

        return roblox_trades_api_models_v2_currency_transfer_eligibility_response
