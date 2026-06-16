from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.matchmaking_customization_feature_flags import MatchmakingCustomizationFeatureFlags


T = TypeVar("T", bound="GetMatchmakingCustomizationFeatureFlagsResponse")


@_attrs_define
class GetMatchmakingCustomizationFeatureFlagsResponse:
    """Response to get matchmaking customization feature flags.

    Attributes:
        feature_flags (MatchmakingCustomizationFeatureFlags | Unset): Matchmaking object for universe feature flags
            controlling matchmaking customization.
    """

    feature_flags: MatchmakingCustomizationFeatureFlags | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        feature_flags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.feature_flags, Unset):
            feature_flags = self.feature_flags.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if feature_flags is not UNSET:
            field_dict["featureFlags"] = feature_flags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matchmaking_customization_feature_flags import MatchmakingCustomizationFeatureFlags

        d = dict(src_dict)
        _feature_flags = d.pop("featureFlags", UNSET)
        feature_flags: MatchmakingCustomizationFeatureFlags | Unset
        if isinstance(_feature_flags, Unset):
            feature_flags = UNSET
        else:
            feature_flags = MatchmakingCustomizationFeatureFlags.from_dict(_feature_flags)

        get_matchmaking_customization_feature_flags_response = cls(
            feature_flags=feature_flags,
        )

        return get_matchmaking_customization_feature_flags_response
