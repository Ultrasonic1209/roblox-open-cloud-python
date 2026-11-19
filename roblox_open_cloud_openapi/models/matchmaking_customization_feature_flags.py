from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="MatchmakingCustomizationFeatureFlags")


@_attrs_define
class MatchmakingCustomizationFeatureFlags:
    """Matchmaking object for universe feature flags controlling matchmaking customization.

    Attributes:
        is_matchmaking_customization_allowed (bool): If matchmaking customization is allowed for this universe
        is_matchmaking_customization_experiments_allowed (bool): If matchmaking customization experiments are allowed
            for this universe
        is_matchmaking_text_chat_signal_enabled (bool): Whether text chat signal is enabled for Custom Matchmaking.
    """

    is_matchmaking_customization_allowed: bool
    is_matchmaking_customization_experiments_allowed: bool
    is_matchmaking_text_chat_signal_enabled: bool

    def to_dict(self) -> dict[str, Any]:
        is_matchmaking_customization_allowed = self.is_matchmaking_customization_allowed

        is_matchmaking_customization_experiments_allowed = self.is_matchmaking_customization_experiments_allowed

        is_matchmaking_text_chat_signal_enabled = self.is_matchmaking_text_chat_signal_enabled

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "isMatchmakingCustomizationAllowed": is_matchmaking_customization_allowed,
                "isMatchmakingCustomizationExperimentsAllowed": is_matchmaking_customization_experiments_allowed,
                "isMatchmakingTextChatSignalEnabled": is_matchmaking_text_chat_signal_enabled,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_matchmaking_customization_allowed = d.pop("isMatchmakingCustomizationAllowed")

        is_matchmaking_customization_experiments_allowed = d.pop("isMatchmakingCustomizationExperimentsAllowed")

        is_matchmaking_text_chat_signal_enabled = d.pop("isMatchmakingTextChatSignalEnabled")

        matchmaking_customization_feature_flags = cls(
            is_matchmaking_customization_allowed=is_matchmaking_customization_allowed,
            is_matchmaking_customization_experiments_allowed=is_matchmaking_customization_experiments_allowed,
            is_matchmaking_text_chat_signal_enabled=is_matchmaking_text_chat_signal_enabled,
        )

        return matchmaking_customization_feature_flags
