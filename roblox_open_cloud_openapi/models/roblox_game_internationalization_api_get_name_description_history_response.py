from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_game_internationalization_api_translation_history import (
        RobloxGameInternationalizationApiTranslationHistory,
    )


T = TypeVar("T", bound="RobloxGameInternationalizationApiGetNameDescriptionHistoryResponse")


@_attrs_define
class RobloxGameInternationalizationApiGetNameDescriptionHistoryResponse:
    """
    Attributes:
        history (list[RobloxGameInternationalizationApiTranslationHistory] | Unset):
        last_evaluated_id (str | Unset):
    """

    history: list[RobloxGameInternationalizationApiTranslationHistory] | Unset = UNSET
    last_evaluated_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        history: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.history, Unset):
            history = []
            for history_item_data in self.history:
                history_item = history_item_data.to_dict()
                history.append(history_item)

        last_evaluated_id = self.last_evaluated_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if history is not UNSET:
            field_dict["history"] = history
        if last_evaluated_id is not UNSET:
            field_dict["lastEvaluatedId"] = last_evaluated_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_game_internationalization_api_translation_history import (
            RobloxGameInternationalizationApiTranslationHistory,
        )

        d = dict(src_dict)
        _history = d.pop("history", UNSET)
        history: list[RobloxGameInternationalizationApiTranslationHistory] | Unset = UNSET
        if _history is not UNSET:
            history = []
            for history_item_data in _history:
                history_item = RobloxGameInternationalizationApiTranslationHistory.from_dict(history_item_data)

                history.append(history_item)

        last_evaluated_id = d.pop("lastEvaluatedId", UNSET)

        roblox_game_internationalization_api_get_name_description_history_response = cls(
            history=history,
            last_evaluated_id=last_evaluated_id,
        )

        return roblox_game_internationalization_api_get_name_description_history_response
