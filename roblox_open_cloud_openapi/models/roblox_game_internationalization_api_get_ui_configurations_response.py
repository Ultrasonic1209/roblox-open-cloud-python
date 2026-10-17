from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGameInternationalizationApiGetUiConfigurationsResponse")


@_attrs_define
class RobloxGameInternationalizationApiGetUiConfigurationsResponse:
    """
    Attributes:
        is_game_products_enabled (bool | Unset): Game products translation management page is enabled or not.
        is_badge_icon_enabled (bool | Unset): Badge Icon translation management is enabled or not.
        is_game_pass_enabled (bool | Unset): Game pass translation management is enabled or not.
        is_developer_product_enabled (bool | Unset): Developer product translation management is enabled or not.
    """

    is_game_products_enabled: bool | Unset = UNSET
    is_badge_icon_enabled: bool | Unset = UNSET
    is_game_pass_enabled: bool | Unset = UNSET
    is_developer_product_enabled: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        is_game_products_enabled = self.is_game_products_enabled

        is_badge_icon_enabled = self.is_badge_icon_enabled

        is_game_pass_enabled = self.is_game_pass_enabled

        is_developer_product_enabled = self.is_developer_product_enabled

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if is_game_products_enabled is not UNSET:
            field_dict["isGameProductsEnabled"] = is_game_products_enabled
        if is_badge_icon_enabled is not UNSET:
            field_dict["isBadgeIconEnabled"] = is_badge_icon_enabled
        if is_game_pass_enabled is not UNSET:
            field_dict["isGamePassEnabled"] = is_game_pass_enabled
        if is_developer_product_enabled is not UNSET:
            field_dict["isDeveloperProductEnabled"] = is_developer_product_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_game_products_enabled = d.pop("isGameProductsEnabled", UNSET)

        is_badge_icon_enabled = d.pop("isBadgeIconEnabled", UNSET)

        is_game_pass_enabled = d.pop("isGamePassEnabled", UNSET)

        is_developer_product_enabled = d.pop("isDeveloperProductEnabled", UNSET)

        roblox_game_internationalization_api_get_ui_configurations_response = cls(
            is_game_products_enabled=is_game_products_enabled,
            is_badge_icon_enabled=is_badge_icon_enabled,
            is_game_pass_enabled=is_game_pass_enabled,
            is_developer_product_enabled=is_developer_product_enabled,
        )

        return roblox_game_internationalization_api_get_ui_configurations_response
