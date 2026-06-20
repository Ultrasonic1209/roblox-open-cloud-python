from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MatchmakingCustomizationFeatureFlags")


@_attrs_define
class MatchmakingCustomizationFeatureFlags:
    """Matchmaking object for universe feature flags controlling matchmaking customization.

    Attributes:
        is_matchmaking_customization_allowed (bool | Unset): If matchmaking customization is allowed for this universe
        is_matchmaking_customization_experiments_allowed (bool | Unset): If matchmaking customization experiments are
            allowed for this universe
        is_matchmaking_text_chat_signal_enabled (bool | Unset): Whether text chat signal is enabled for Custom
            Matchmaking.
    """

    is_matchmaking_customization_allowed: bool | Unset = UNSET
    is_matchmaking_customization_experiments_allowed: bool | Unset = UNSET
    is_matchmaking_text_chat_signal_enabled: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        is_matchmaking_customization_allowed = self.is_matchmaking_customization_allowed

        is_matchmaking_customization_experiments_allowed = self.is_matchmaking_customization_experiments_allowed

        is_matchmaking_text_chat_signal_enabled = self.is_matchmaking_text_chat_signal_enabled

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if is_matchmaking_customization_allowed is not UNSET:
            field_dict["isMatchmakingCustomizationAllowed"] = is_matchmaking_customization_allowed
        if is_matchmaking_customization_experiments_allowed is not UNSET:
            field_dict["isMatchmakingCustomizationExperimentsAllowed"] = (
                is_matchmaking_customization_experiments_allowed
            )
        if is_matchmaking_text_chat_signal_enabled is not UNSET:
            field_dict["isMatchmakingTextChatSignalEnabled"] = is_matchmaking_text_chat_signal_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        is_matchmaking_customization_allowed = d.pop("isMatchmakingCustomizationAllowed", UNSET)

        is_matchmaking_customization_experiments_allowed = d.pop("isMatchmakingCustomizationExperimentsAllowed", UNSET)

        is_matchmaking_text_chat_signal_enabled = d.pop("isMatchmakingTextChatSignalEnabled", UNSET)

        matchmaking_customization_feature_flags = cls(
            is_matchmaking_customization_allowed=is_matchmaking_customization_allowed,
            is_matchmaking_customization_experiments_allowed=is_matchmaking_customization_experiments_allowed,
            is_matchmaking_text_chat_signal_enabled=is_matchmaking_text_chat_signal_enabled,
        )

        return matchmaking_customization_feature_flags
