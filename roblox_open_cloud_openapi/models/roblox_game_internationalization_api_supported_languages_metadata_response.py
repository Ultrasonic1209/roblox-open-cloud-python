from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGameInternationalizationApiSupportedLanguagesMetadataResponse")


@_attrs_define
class RobloxGameInternationalizationApiSupportedLanguagesMetadataResponse:
    """
    Attributes:
        is_feature_enabled (bool | Unset):
        are_all_languages_enabled (bool | Unset):
        minimum_universe_id_for_feature (int | Unset):
        is_human_translation_progress_ui_enabled (bool | Unset): Is translation progress for human translations enabled
            on UI
        is_automatic_translation_progress_ui_enabled (bool | Unset): Is translation progress for automatic translations
            enabled on UI
        is_supported_languages_child_locales_ui_enabled (bool | Unset): Is Language Locales UI Enabled for Supported
            Languages
    """

    is_feature_enabled: bool | Unset = UNSET
    are_all_languages_enabled: bool | Unset = UNSET
    minimum_universe_id_for_feature: int | Unset = UNSET
    is_human_translation_progress_ui_enabled: bool | Unset = UNSET
    is_automatic_translation_progress_ui_enabled: bool | Unset = UNSET
    is_supported_languages_child_locales_ui_enabled: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        is_feature_enabled = self.is_feature_enabled

        are_all_languages_enabled = self.are_all_languages_enabled

        minimum_universe_id_for_feature = self.minimum_universe_id_for_feature

        is_human_translation_progress_ui_enabled = self.is_human_translation_progress_ui_enabled

        is_automatic_translation_progress_ui_enabled = self.is_automatic_translation_progress_ui_enabled

        is_supported_languages_child_locales_ui_enabled = self.is_supported_languages_child_locales_ui_enabled

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if is_feature_enabled is not UNSET:
            field_dict["isFeatureEnabled"] = is_feature_enabled
        if are_all_languages_enabled is not UNSET:
            field_dict["areAllLanguagesEnabled"] = are_all_languages_enabled
        if minimum_universe_id_for_feature is not UNSET:
            field_dict["minimumUniverseIdForFeature"] = minimum_universe_id_for_feature
        if is_human_translation_progress_ui_enabled is not UNSET:
            field_dict["isHumanTranslationProgressUIEnabled"] = is_human_translation_progress_ui_enabled
        if is_automatic_translation_progress_ui_enabled is not UNSET:
            field_dict["isAutomaticTranslationProgressUIEnabled"] = is_automatic_translation_progress_ui_enabled
        if is_supported_languages_child_locales_ui_enabled is not UNSET:
            field_dict["isSupportedLanguagesChildLocalesUIEnabled"] = is_supported_languages_child_locales_ui_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        is_feature_enabled = d.pop("isFeatureEnabled", UNSET)

        are_all_languages_enabled = d.pop("areAllLanguagesEnabled", UNSET)

        minimum_universe_id_for_feature = d.pop("minimumUniverseIdForFeature", UNSET)

        is_human_translation_progress_ui_enabled = d.pop("isHumanTranslationProgressUIEnabled", UNSET)

        is_automatic_translation_progress_ui_enabled = d.pop("isAutomaticTranslationProgressUIEnabled", UNSET)

        is_supported_languages_child_locales_ui_enabled = d.pop("isSupportedLanguagesChildLocalesUIEnabled", UNSET)

        roblox_game_internationalization_api_supported_languages_metadata_response = cls(
            is_feature_enabled=is_feature_enabled,
            are_all_languages_enabled=are_all_languages_enabled,
            minimum_universe_id_for_feature=minimum_universe_id_for_feature,
            is_human_translation_progress_ui_enabled=is_human_translation_progress_ui_enabled,
            is_automatic_translation_progress_ui_enabled=is_automatic_translation_progress_ui_enabled,
            is_supported_languages_child_locales_ui_enabled=is_supported_languages_child_locales_ui_enabled,
        )

        return roblox_game_internationalization_api_supported_languages_metadata_response
