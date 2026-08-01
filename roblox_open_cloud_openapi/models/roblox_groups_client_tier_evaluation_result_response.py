from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_groups_client_community_tier_info_response import RobloxGroupsClientCommunityTierInfoResponse


T = TypeVar("T", bound="RobloxGroupsClientTierEvaluationResultResponse")


@_attrs_define
class RobloxGroupsClientTierEvaluationResultResponse:
    """
    Attributes:
        tier_info (RobloxGroupsClientCommunityTierInfoResponse | Unset):
        passed_signals (list[str] | Unset):
    """

    tier_info: RobloxGroupsClientCommunityTierInfoResponse | Unset = UNSET
    passed_signals: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        tier_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tier_info, Unset):
            tier_info = self.tier_info.to_dict()

        passed_signals: list[str] | Unset = UNSET
        if not isinstance(self.passed_signals, Unset):
            passed_signals = self.passed_signals

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if tier_info is not UNSET:
            field_dict["tierInfo"] = tier_info
        if passed_signals is not UNSET:
            field_dict["passedSignals"] = passed_signals

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_groups_client_community_tier_info_response import (
            RobloxGroupsClientCommunityTierInfoResponse,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _tier_info = d.pop("tierInfo", UNSET)
        tier_info: RobloxGroupsClientCommunityTierInfoResponse | Unset
        if isinstance(_tier_info, Unset):
            tier_info = UNSET
        else:
            tier_info = RobloxGroupsClientCommunityTierInfoResponse.from_dict(_tier_info)

        passed_signals = cast(list[str], d.pop("passedSignals", UNSET))

        roblox_groups_client_tier_evaluation_result_response = cls(
            tier_info=tier_info,
            passed_signals=passed_signals,
        )

        return roblox_groups_client_tier_evaluation_result_response
