from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.roblox_localization_tables_api_entry_translation_feedback_reasons_item import (
    RobloxLocalizationTablesApiEntryTranslationFeedbackReasonsItem,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_localization_tables_api_entry_identifier_with_translation import (
        RobloxLocalizationTablesApiEntryIdentifierWithTranslation,
    )


T = TypeVar("T", bound="RobloxLocalizationTablesApiEntryTranslationFeedback")


@_attrs_define
class RobloxLocalizationTablesApiEntryTranslationFeedback:
    """
    Attributes:
        identifier (RobloxLocalizationTablesApiEntryIdentifierWithTranslation | Unset):
        feedback_count (int | Unset): The number of unique reporters that send feedback to the given entry identifier.
        player_suggestion_text (list[str] | Unset): A set of player translation suggestion in text for the given entry
            identifier.
        reasons (list[RobloxLocalizationTablesApiEntryTranslationFeedbackReasonsItem] | Unset): A set of translation
            feedback reasons for the given entry identifier.
        roblox_suggestion_text (str | Unset): Roblox translation suggestion in text for the given entry identifier.
    """

    identifier: RobloxLocalizationTablesApiEntryIdentifierWithTranslation | Unset = UNSET
    feedback_count: int | Unset = UNSET
    player_suggestion_text: list[str] | Unset = UNSET
    reasons: list[RobloxLocalizationTablesApiEntryTranslationFeedbackReasonsItem] | Unset = UNSET
    roblox_suggestion_text: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        identifier: dict[str, Any] | Unset = UNSET
        if not isinstance(self.identifier, Unset):
            identifier = self.identifier.to_dict()

        feedback_count = self.feedback_count

        player_suggestion_text: list[str] | Unset = UNSET
        if not isinstance(self.player_suggestion_text, Unset):
            player_suggestion_text = self.player_suggestion_text

        reasons: list[str] | Unset = UNSET
        if not isinstance(self.reasons, Unset):
            reasons = []
            for reasons_item_data in self.reasons:
                reasons_item = reasons_item_data.value
                reasons.append(reasons_item)

        roblox_suggestion_text = self.roblox_suggestion_text

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if feedback_count is not UNSET:
            field_dict["feedbackCount"] = feedback_count
        if player_suggestion_text is not UNSET:
            field_dict["playerSuggestionText"] = player_suggestion_text
        if reasons is not UNSET:
            field_dict["reasons"] = reasons
        if roblox_suggestion_text is not UNSET:
            field_dict["robloxSuggestionText"] = roblox_suggestion_text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_localization_tables_api_entry_identifier_with_translation import (
            RobloxLocalizationTablesApiEntryIdentifierWithTranslation,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _identifier = d.pop("identifier", UNSET)
        identifier: RobloxLocalizationTablesApiEntryIdentifierWithTranslation | Unset
        if isinstance(_identifier, Unset):
            identifier = UNSET
        else:
            identifier = RobloxLocalizationTablesApiEntryIdentifierWithTranslation.from_dict(_identifier)

        feedback_count = d.pop("feedbackCount", UNSET)

        player_suggestion_text = cast(list[str], d.pop("playerSuggestionText", UNSET))

        _reasons = d.pop("reasons", UNSET)
        reasons: list[RobloxLocalizationTablesApiEntryTranslationFeedbackReasonsItem] | Unset = UNSET
        if _reasons is not UNSET:
            reasons = []
            for reasons_item_data in _reasons:
                reasons_item = RobloxLocalizationTablesApiEntryTranslationFeedbackReasonsItem(reasons_item_data)

                reasons.append(reasons_item)

        roblox_suggestion_text = d.pop("robloxSuggestionText", UNSET)

        roblox_localization_tables_api_entry_translation_feedback = cls(
            identifier=identifier,
            feedback_count=feedback_count,
            player_suggestion_text=player_suggestion_text,
            reasons=reasons,
            roblox_suggestion_text=roblox_suggestion_text,
        )

        return roblox_localization_tables_api_entry_translation_feedback
