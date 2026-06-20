from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_game_internationalization_api_language_or_locale import (
        RobloxGameInternationalizationApiLanguageOrLocale,
    )


T = TypeVar("T", bound="RobloxWebWebAPIModelsApiArrayResponseRobloxGameInternationalizationApiLanguageOrLocale")


@_attrs_define
class RobloxWebWebAPIModelsApiArrayResponseRobloxGameInternationalizationApiLanguageOrLocale:
    """
    Attributes:
        data (list[RobloxGameInternationalizationApiLanguageOrLocale] | Unset):
    """

    data: list[RobloxGameInternationalizationApiLanguageOrLocale] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_game_internationalization_api_language_or_locale import (
            RobloxGameInternationalizationApiLanguageOrLocale,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _data = d.pop("data", UNSET)
        data: list[RobloxGameInternationalizationApiLanguageOrLocale] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = RobloxGameInternationalizationApiLanguageOrLocale.from_dict(data_item_data)

                data.append(data_item)

        roblox_web_web_api_models_api_array_response_roblox_game_internationalization_api_language_or_locale = cls(
            data=data,
        )

        return roblox_web_web_api_models_api_array_response_roblox_game_internationalization_api_language_or_locale
