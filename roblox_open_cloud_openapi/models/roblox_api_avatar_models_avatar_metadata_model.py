from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxApiAvatarModelsAvatarMetadataModel")


@_attrs_define
class RobloxApiAvatarModelsAvatarMetadataModel:
    """A model containing website metadata for avatars

    Attributes:
        enable_default_clothing_message (bool | Unset): Whether or not to show the Default Clothing message
        is_avatar_scale_embedded_in_tab (bool | Unset): Whether or not the Scales is embedded in the tab
        is_body_type_scale_out_of_tab (bool | Unset): Whether or not the Boby Type scale is embedded in the tab
        scale_height_increment (float | Unset): How much the height scaler should increment by
        scale_width_increment (float | Unset): How much the width scaler should increment by
        scale_head_increment (float | Unset): How much the head scaler should increment by
        scale_proportion_increment (float | Unset): How much the proportion scaler should increment by
        scale_body_type_increment (float | Unset): How much the body type scaler should increment by
        support_proportion_and_body_type (bool | Unset): Whether or not to support proportion and body type
        show_default_clothing_message_on_page_load (bool | Unset): Whether or not to show the default clothing message
            when the page loads
        are_three_dee_thumbs_enabled (bool | Unset): Whether or not 3D thumbnails are shown
        is_avatar_wearing_api_calls_locking_on_frontend_enabled (bool | Unset): Does the frontend lock avatar editor
            input until the wearing call returns
        is_outfit_handling_on_frontend_enabled (bool | Unset): Does the frontend lock avatar editor input until the
            wearing call returns
        is_justin_ui_changes_enabled (bool | Unset): Determines whether a bunch of UI improvements are released
        is_category_reorg_enabled (bool | Unset): Determines whether Category Reorg is released
        lc_enabled_in_editor_and_catalog (bool | Unset): Flag for both web UI and App, name is fixed due to sharing, do
            not change
        is_lc_completely_enabled (bool | Unset): Useful for the time between enabling Jackets for most users and
            all LC types for everyone, meanwhile Soothsayers need all types
            at all times
    """

    enable_default_clothing_message: bool | Unset = UNSET
    is_avatar_scale_embedded_in_tab: bool | Unset = UNSET
    is_body_type_scale_out_of_tab: bool | Unset = UNSET
    scale_height_increment: float | Unset = UNSET
    scale_width_increment: float | Unset = UNSET
    scale_head_increment: float | Unset = UNSET
    scale_proportion_increment: float | Unset = UNSET
    scale_body_type_increment: float | Unset = UNSET
    support_proportion_and_body_type: bool | Unset = UNSET
    show_default_clothing_message_on_page_load: bool | Unset = UNSET
    are_three_dee_thumbs_enabled: bool | Unset = UNSET
    is_avatar_wearing_api_calls_locking_on_frontend_enabled: bool | Unset = UNSET
    is_outfit_handling_on_frontend_enabled: bool | Unset = UNSET
    is_justin_ui_changes_enabled: bool | Unset = UNSET
    is_category_reorg_enabled: bool | Unset = UNSET
    lc_enabled_in_editor_and_catalog: bool | Unset = UNSET
    is_lc_completely_enabled: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        enable_default_clothing_message = self.enable_default_clothing_message

        is_avatar_scale_embedded_in_tab = self.is_avatar_scale_embedded_in_tab

        is_body_type_scale_out_of_tab = self.is_body_type_scale_out_of_tab

        scale_height_increment = self.scale_height_increment

        scale_width_increment = self.scale_width_increment

        scale_head_increment = self.scale_head_increment

        scale_proportion_increment = self.scale_proportion_increment

        scale_body_type_increment = self.scale_body_type_increment

        support_proportion_and_body_type = self.support_proportion_and_body_type

        show_default_clothing_message_on_page_load = self.show_default_clothing_message_on_page_load

        are_three_dee_thumbs_enabled = self.are_three_dee_thumbs_enabled

        is_avatar_wearing_api_calls_locking_on_frontend_enabled = (
            self.is_avatar_wearing_api_calls_locking_on_frontend_enabled
        )

        is_outfit_handling_on_frontend_enabled = self.is_outfit_handling_on_frontend_enabled

        is_justin_ui_changes_enabled = self.is_justin_ui_changes_enabled

        is_category_reorg_enabled = self.is_category_reorg_enabled

        lc_enabled_in_editor_and_catalog = self.lc_enabled_in_editor_and_catalog

        is_lc_completely_enabled = self.is_lc_completely_enabled

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if enable_default_clothing_message is not UNSET:
            field_dict["enableDefaultClothingMessage"] = enable_default_clothing_message
        if is_avatar_scale_embedded_in_tab is not UNSET:
            field_dict["isAvatarScaleEmbeddedInTab"] = is_avatar_scale_embedded_in_tab
        if is_body_type_scale_out_of_tab is not UNSET:
            field_dict["isBodyTypeScaleOutOfTab"] = is_body_type_scale_out_of_tab
        if scale_height_increment is not UNSET:
            field_dict["scaleHeightIncrement"] = scale_height_increment
        if scale_width_increment is not UNSET:
            field_dict["scaleWidthIncrement"] = scale_width_increment
        if scale_head_increment is not UNSET:
            field_dict["scaleHeadIncrement"] = scale_head_increment
        if scale_proportion_increment is not UNSET:
            field_dict["scaleProportionIncrement"] = scale_proportion_increment
        if scale_body_type_increment is not UNSET:
            field_dict["scaleBodyTypeIncrement"] = scale_body_type_increment
        if support_proportion_and_body_type is not UNSET:
            field_dict["supportProportionAndBodyType"] = support_proportion_and_body_type
        if show_default_clothing_message_on_page_load is not UNSET:
            field_dict["showDefaultClothingMessageOnPageLoad"] = show_default_clothing_message_on_page_load
        if are_three_dee_thumbs_enabled is not UNSET:
            field_dict["areThreeDeeThumbsEnabled"] = are_three_dee_thumbs_enabled
        if is_avatar_wearing_api_calls_locking_on_frontend_enabled is not UNSET:
            field_dict["isAvatarWearingApiCallsLockingOnFrontendEnabled"] = (
                is_avatar_wearing_api_calls_locking_on_frontend_enabled
            )
        if is_outfit_handling_on_frontend_enabled is not UNSET:
            field_dict["isOutfitHandlingOnFrontendEnabled"] = is_outfit_handling_on_frontend_enabled
        if is_justin_ui_changes_enabled is not UNSET:
            field_dict["isJustinUiChangesEnabled"] = is_justin_ui_changes_enabled
        if is_category_reorg_enabled is not UNSET:
            field_dict["isCategoryReorgEnabled"] = is_category_reorg_enabled
        if lc_enabled_in_editor_and_catalog is not UNSET:
            field_dict["LCEnabledInEditorAndCatalog"] = lc_enabled_in_editor_and_catalog
        if is_lc_completely_enabled is not UNSET:
            field_dict["isLCCompletelyEnabled"] = is_lc_completely_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enable_default_clothing_message = d.pop("enableDefaultClothingMessage", UNSET)

        is_avatar_scale_embedded_in_tab = d.pop("isAvatarScaleEmbeddedInTab", UNSET)

        is_body_type_scale_out_of_tab = d.pop("isBodyTypeScaleOutOfTab", UNSET)

        scale_height_increment = d.pop("scaleHeightIncrement", UNSET)

        scale_width_increment = d.pop("scaleWidthIncrement", UNSET)

        scale_head_increment = d.pop("scaleHeadIncrement", UNSET)

        scale_proportion_increment = d.pop("scaleProportionIncrement", UNSET)

        scale_body_type_increment = d.pop("scaleBodyTypeIncrement", UNSET)

        support_proportion_and_body_type = d.pop("supportProportionAndBodyType", UNSET)

        show_default_clothing_message_on_page_load = d.pop("showDefaultClothingMessageOnPageLoad", UNSET)

        are_three_dee_thumbs_enabled = d.pop("areThreeDeeThumbsEnabled", UNSET)

        is_avatar_wearing_api_calls_locking_on_frontend_enabled = d.pop(
            "isAvatarWearingApiCallsLockingOnFrontendEnabled", UNSET
        )

        is_outfit_handling_on_frontend_enabled = d.pop("isOutfitHandlingOnFrontendEnabled", UNSET)

        is_justin_ui_changes_enabled = d.pop("isJustinUiChangesEnabled", UNSET)

        is_category_reorg_enabled = d.pop("isCategoryReorgEnabled", UNSET)

        lc_enabled_in_editor_and_catalog = d.pop("LCEnabledInEditorAndCatalog", UNSET)

        is_lc_completely_enabled = d.pop("isLCCompletelyEnabled", UNSET)

        roblox_api_avatar_models_avatar_metadata_model = cls(
            enable_default_clothing_message=enable_default_clothing_message,
            is_avatar_scale_embedded_in_tab=is_avatar_scale_embedded_in_tab,
            is_body_type_scale_out_of_tab=is_body_type_scale_out_of_tab,
            scale_height_increment=scale_height_increment,
            scale_width_increment=scale_width_increment,
            scale_head_increment=scale_head_increment,
            scale_proportion_increment=scale_proportion_increment,
            scale_body_type_increment=scale_body_type_increment,
            support_proportion_and_body_type=support_proportion_and_body_type,
            show_default_clothing_message_on_page_load=show_default_clothing_message_on_page_load,
            are_three_dee_thumbs_enabled=are_three_dee_thumbs_enabled,
            is_avatar_wearing_api_calls_locking_on_frontend_enabled=is_avatar_wearing_api_calls_locking_on_frontend_enabled,
            is_outfit_handling_on_frontend_enabled=is_outfit_handling_on_frontend_enabled,
            is_justin_ui_changes_enabled=is_justin_ui_changes_enabled,
            is_category_reorg_enabled=is_category_reorg_enabled,
            lc_enabled_in_editor_and_catalog=lc_enabled_in_editor_and_catalog,
            is_lc_completely_enabled=is_lc_completely_enabled,
        )

        return roblox_api_avatar_models_avatar_metadata_model
