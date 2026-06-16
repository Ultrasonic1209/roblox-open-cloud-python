from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_trades_api_models_v2_can_trade_with_response_mutual_trade_eligibility import (
    RobloxTradesApiModelsV2CanTradeWithResponseMutualTradeEligibility,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxTradesApiModelsV2CanTradeWithResponse")


@_attrs_define
class RobloxTradesApiModelsV2CanTradeWithResponse:
    """The response for the CanTradeWith endpoint.

    Attributes:
        user_id (int | Unset): The ID of the user.
        target_user_id (int | Unset): The ID of the target user.
        can_trade (bool | Unset): Whether the user can trade with the target user or not.
        mutual_trade_eligibility (RobloxTradesApiModelsV2CanTradeWithResponseMutualTradeEligibility | Unset): The mutual
            trade eligibility status between the two users. ['Unknown' = 0, 'Eligible' = 1, 'CallingUserIneligible' = 2,
            'TargetUserIneligible' = 3, 'CannotTradeWithSelf' = 4, 'CallingUserPrivacySettingsRestricted' = 5]
    """

    user_id: int | Unset = UNSET
    target_user_id: int | Unset = UNSET
    can_trade: bool | Unset = UNSET
    mutual_trade_eligibility: RobloxTradesApiModelsV2CanTradeWithResponseMutualTradeEligibility | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        target_user_id = self.target_user_id

        can_trade = self.can_trade

        mutual_trade_eligibility: str | Unset = UNSET
        if not isinstance(self.mutual_trade_eligibility, Unset):
            mutual_trade_eligibility = self.mutual_trade_eligibility.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if target_user_id is not UNSET:
            field_dict["targetUserId"] = target_user_id
        if can_trade is not UNSET:
            field_dict["canTrade"] = can_trade
        if mutual_trade_eligibility is not UNSET:
            field_dict["mutualTradeEligibility"] = mutual_trade_eligibility

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id = d.pop("userId", UNSET)

        target_user_id = d.pop("targetUserId", UNSET)

        can_trade = d.pop("canTrade", UNSET)

        _mutual_trade_eligibility = d.pop("mutualTradeEligibility", UNSET)
        mutual_trade_eligibility: RobloxTradesApiModelsV2CanTradeWithResponseMutualTradeEligibility | Unset
        if isinstance(_mutual_trade_eligibility, Unset):
            mutual_trade_eligibility = UNSET
        else:
            mutual_trade_eligibility = RobloxTradesApiModelsV2CanTradeWithResponseMutualTradeEligibility(
                _mutual_trade_eligibility
            )

        roblox_trades_api_models_v2_can_trade_with_response = cls(
            user_id=user_id,
            target_user_id=target_user_id,
            can_trade=can_trade,
            mutual_trade_eligibility=mutual_trade_eligibility,
        )

        return roblox_trades_api_models_v2_can_trade_with_response
