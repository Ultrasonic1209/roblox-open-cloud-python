from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_item_configuration_api_publishing_fee_response_publishing_fee_type import (
    RobloxItemConfigurationApiPublishingFeeResponsePublishingFeeType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxItemConfigurationApiPublishingFeeResponse")


@_attrs_define
class RobloxItemConfigurationApiPublishingFeeResponse:
    """Response Model for Collectibles Publishing Fee request.

    Attributes:
        publishing_fee_in_robux (int | Unset): Publishing fee in Robux for a Collectible.
        unit_publishing_fee_in_robux (int | Unset): Publishing fee per-unit in Robux for a Collectible.
        is_dynamic_fee_enabled (bool | Unset): Whether the publishing fee is using a dynamically set value.
        publishing_fee_type (RobloxItemConfigurationApiPublishingFeeResponsePublishingFeeType | Unset): The type of the
            publishing fee. ['Invalid' = 0, 'PayPerInstance' = 1, 'PayInTotal' = 2]
    """

    publishing_fee_in_robux: int | Unset = UNSET
    unit_publishing_fee_in_robux: int | Unset = UNSET
    is_dynamic_fee_enabled: bool | Unset = UNSET
    publishing_fee_type: RobloxItemConfigurationApiPublishingFeeResponsePublishingFeeType | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        publishing_fee_in_robux = self.publishing_fee_in_robux

        unit_publishing_fee_in_robux = self.unit_publishing_fee_in_robux

        is_dynamic_fee_enabled = self.is_dynamic_fee_enabled

        publishing_fee_type: int | Unset = UNSET
        if not isinstance(self.publishing_fee_type, Unset):
            publishing_fee_type = self.publishing_fee_type.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if publishing_fee_in_robux is not UNSET:
            field_dict["publishingFeeInRobux"] = publishing_fee_in_robux
        if unit_publishing_fee_in_robux is not UNSET:
            field_dict["unitPublishingFeeInRobux"] = unit_publishing_fee_in_robux
        if is_dynamic_fee_enabled is not UNSET:
            field_dict["isDynamicFeeEnabled"] = is_dynamic_fee_enabled
        if publishing_fee_type is not UNSET:
            field_dict["publishingFeeType"] = publishing_fee_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        publishing_fee_in_robux = d.pop("publishingFeeInRobux", UNSET)

        unit_publishing_fee_in_robux = d.pop("unitPublishingFeeInRobux", UNSET)

        is_dynamic_fee_enabled = d.pop("isDynamicFeeEnabled", UNSET)

        _publishing_fee_type = d.pop("publishingFeeType", UNSET)
        publishing_fee_type: RobloxItemConfigurationApiPublishingFeeResponsePublishingFeeType | Unset
        if isinstance(_publishing_fee_type, Unset):
            publishing_fee_type = UNSET
        else:
            publishing_fee_type = RobloxItemConfigurationApiPublishingFeeResponsePublishingFeeType(_publishing_fee_type)

        roblox_item_configuration_api_publishing_fee_response = cls(
            publishing_fee_in_robux=publishing_fee_in_robux,
            unit_publishing_fee_in_robux=unit_publishing_fee_in_robux,
            is_dynamic_fee_enabled=is_dynamic_fee_enabled,
            publishing_fee_type=publishing_fee_type,
        )

        return roblox_item_configuration_api_publishing_fee_response
