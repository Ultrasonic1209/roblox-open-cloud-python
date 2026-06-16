from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxLocalizationTablesApiAutoLocalizationMetadataResponse")


@_attrs_define
class RobloxLocalizationTablesApiAutoLocalizationMetadataResponse:
    """
    Attributes:
        is_react_version_enabled_for_auto_localization_settings (bool | Unset): Is React Implementation of
            AutoLocalization Settings Enabled
        is_tabbed_ui_enabled_for_configure_localization_page (bool | Unset): Is Tabbed UI Enabled for Configure
            Localization Page
        is_automatic_translation_toggle_ui_enabled (bool | Unset): Is Toggle UI Enabled for Automatic Translations
        is_automatic_translation_quota_ui_enabled (bool | Unset): Is Quota UI Enabled for Automatic Translations
    """

    is_react_version_enabled_for_auto_localization_settings: bool | Unset = UNSET
    is_tabbed_ui_enabled_for_configure_localization_page: bool | Unset = UNSET
    is_automatic_translation_toggle_ui_enabled: bool | Unset = UNSET
    is_automatic_translation_quota_ui_enabled: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        is_react_version_enabled_for_auto_localization_settings = (
            self.is_react_version_enabled_for_auto_localization_settings
        )

        is_tabbed_ui_enabled_for_configure_localization_page = self.is_tabbed_ui_enabled_for_configure_localization_page

        is_automatic_translation_toggle_ui_enabled = self.is_automatic_translation_toggle_ui_enabled

        is_automatic_translation_quota_ui_enabled = self.is_automatic_translation_quota_ui_enabled

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if is_react_version_enabled_for_auto_localization_settings is not UNSET:
            field_dict["isReactVersionEnabledForAutoLocalizationSettings"] = (
                is_react_version_enabled_for_auto_localization_settings
            )
        if is_tabbed_ui_enabled_for_configure_localization_page is not UNSET:
            field_dict["isTabbedUIEnabledForConfigureLocalizationPage"] = (
                is_tabbed_ui_enabled_for_configure_localization_page
            )
        if is_automatic_translation_toggle_ui_enabled is not UNSET:
            field_dict["isAutomaticTranslationToggleUIEnabled"] = is_automatic_translation_toggle_ui_enabled
        if is_automatic_translation_quota_ui_enabled is not UNSET:
            field_dict["isAutomaticTranslationQuotaUIEnabled"] = is_automatic_translation_quota_ui_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_react_version_enabled_for_auto_localization_settings = d.pop(
            "isReactVersionEnabledForAutoLocalizationSettings", UNSET
        )

        is_tabbed_ui_enabled_for_configure_localization_page = d.pop(
            "isTabbedUIEnabledForConfigureLocalizationPage", UNSET
        )

        is_automatic_translation_toggle_ui_enabled = d.pop("isAutomaticTranslationToggleUIEnabled", UNSET)

        is_automatic_translation_quota_ui_enabled = d.pop("isAutomaticTranslationQuotaUIEnabled", UNSET)

        roblox_localization_tables_api_auto_localization_metadata_response = cls(
            is_react_version_enabled_for_auto_localization_settings=is_react_version_enabled_for_auto_localization_settings,
            is_tabbed_ui_enabled_for_configure_localization_page=is_tabbed_ui_enabled_for_configure_localization_page,
            is_automatic_translation_toggle_ui_enabled=is_automatic_translation_toggle_ui_enabled,
            is_automatic_translation_quota_ui_enabled=is_automatic_translation_quota_ui_enabled,
        )

        return roblox_localization_tables_api_auto_localization_metadata_response
