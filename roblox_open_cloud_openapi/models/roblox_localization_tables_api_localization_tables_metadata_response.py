from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxLocalizationTablesApiLocalizationTablesMetadataResponse")


@_attrs_define
class RobloxLocalizationTablesApiLocalizationTablesMetadataResponse:
    """
    Attributes:
        is_bulk_upload_feature_enabled (bool | Unset): Is bulk upload feature enabled
        is_csv_download_enabled (bool | Unset): Is CSV download feature enabled
        is_access_to_translation_meta_data_enabled (bool | Unset): Is access to translation metadata feature enabled
        is_translation_management_redirection_enabled (bool | Unset): Is access to translation metadata feature enabled
        is_untranslated_filter_enabled (bool | Unset): Is untranslated filter on UI is enabled
        is_automatic_translation_filter_enabled (bool | Unset): Is filter for automatic translations on UI is enabled
    """

    is_bulk_upload_feature_enabled: bool | Unset = UNSET
    is_csv_download_enabled: bool | Unset = UNSET
    is_access_to_translation_meta_data_enabled: bool | Unset = UNSET
    is_translation_management_redirection_enabled: bool | Unset = UNSET
    is_untranslated_filter_enabled: bool | Unset = UNSET
    is_automatic_translation_filter_enabled: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        is_bulk_upload_feature_enabled = self.is_bulk_upload_feature_enabled

        is_csv_download_enabled = self.is_csv_download_enabled

        is_access_to_translation_meta_data_enabled = self.is_access_to_translation_meta_data_enabled

        is_translation_management_redirection_enabled = self.is_translation_management_redirection_enabled

        is_untranslated_filter_enabled = self.is_untranslated_filter_enabled

        is_automatic_translation_filter_enabled = self.is_automatic_translation_filter_enabled

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if is_bulk_upload_feature_enabled is not UNSET:
            field_dict["isBulkUploadFeatureEnabled"] = is_bulk_upload_feature_enabled
        if is_csv_download_enabled is not UNSET:
            field_dict["isCsvDownloadEnabled"] = is_csv_download_enabled
        if is_access_to_translation_meta_data_enabled is not UNSET:
            field_dict["isAccessToTranslationMetaDataEnabled"] = is_access_to_translation_meta_data_enabled
        if is_translation_management_redirection_enabled is not UNSET:
            field_dict["isTranslationManagementRedirectionEnabled"] = is_translation_management_redirection_enabled
        if is_untranslated_filter_enabled is not UNSET:
            field_dict["isUntranslatedFilterEnabled"] = is_untranslated_filter_enabled
        if is_automatic_translation_filter_enabled is not UNSET:
            field_dict["isAutomaticTranslationFilterEnabled"] = is_automatic_translation_filter_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        is_bulk_upload_feature_enabled = d.pop("isBulkUploadFeatureEnabled", UNSET)

        is_csv_download_enabled = d.pop("isCsvDownloadEnabled", UNSET)

        is_access_to_translation_meta_data_enabled = d.pop("isAccessToTranslationMetaDataEnabled", UNSET)

        is_translation_management_redirection_enabled = d.pop("isTranslationManagementRedirectionEnabled", UNSET)

        is_untranslated_filter_enabled = d.pop("isUntranslatedFilterEnabled", UNSET)

        is_automatic_translation_filter_enabled = d.pop("isAutomaticTranslationFilterEnabled", UNSET)

        roblox_localization_tables_api_localization_tables_metadata_response = cls(
            is_bulk_upload_feature_enabled=is_bulk_upload_feature_enabled,
            is_csv_download_enabled=is_csv_download_enabled,
            is_access_to_translation_meta_data_enabled=is_access_to_translation_meta_data_enabled,
            is_translation_management_redirection_enabled=is_translation_management_redirection_enabled,
            is_untranslated_filter_enabled=is_untranslated_filter_enabled,
            is_automatic_translation_filter_enabled=is_automatic_translation_filter_enabled,
        )

        return roblox_localization_tables_api_localization_tables_metadata_response
