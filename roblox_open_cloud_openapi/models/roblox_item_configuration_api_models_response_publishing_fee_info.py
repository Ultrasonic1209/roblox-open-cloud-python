from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_item_configuration_api_models_response_publishing_fee_info_publishing_fee_type import (
    RobloxItemConfigurationApiModelsResponsePublishingFeeInfoPublishingFeeType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxItemConfigurationApiModelsResponsePublishingFeeInfo")


@_attrs_define
class RobloxItemConfigurationApiModelsResponsePublishingFeeInfo:
    """A publishing fee returned with the price floor.

    Attributes:
        publishing_fee_in_robux (int | Unset): The publishing fee in Robux. For
            Roblox.ItemConfiguration.Api.PublishingFeeType.PayPerInstance, this is the fee for each unit.
        publishing_fee_type (RobloxItemConfigurationApiModelsResponsePublishingFeeInfoPublishingFeeType | Unset):
            Whether the fee is charged once or for each unit. ['Invalid' = 0, 'PayPerInstance' = 1, 'PayInTotal' = 2]
        display_name (str | Unset): The user-facing name of the publishing fee.
    """

    publishing_fee_in_robux: int | Unset = UNSET
    publishing_fee_type: RobloxItemConfigurationApiModelsResponsePublishingFeeInfoPublishingFeeType | Unset = UNSET
    display_name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        publishing_fee_in_robux = self.publishing_fee_in_robux

        publishing_fee_type: int | Unset = UNSET
        if not isinstance(self.publishing_fee_type, Unset):
            publishing_fee_type = self.publishing_fee_type.value

        display_name = self.display_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if publishing_fee_in_robux is not UNSET:
            field_dict["publishingFeeInRobux"] = publishing_fee_in_robux
        if publishing_fee_type is not UNSET:
            field_dict["publishingFeeType"] = publishing_fee_type
        if display_name is not UNSET:
            field_dict["displayName"] = display_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        publishing_fee_in_robux = d.pop("publishingFeeInRobux", UNSET)

        _publishing_fee_type = d.pop("publishingFeeType", UNSET)
        publishing_fee_type: RobloxItemConfigurationApiModelsResponsePublishingFeeInfoPublishingFeeType | Unset
        if isinstance(_publishing_fee_type, Unset):
            publishing_fee_type = UNSET
        else:
            publishing_fee_type = RobloxItemConfigurationApiModelsResponsePublishingFeeInfoPublishingFeeType(
                _publishing_fee_type
            )

        display_name = d.pop("displayName", UNSET)

        roblox_item_configuration_api_models_response_publishing_fee_info = cls(
            publishing_fee_in_robux=publishing_fee_in_robux,
            publishing_fee_type=publishing_fee_type,
            display_name=display_name,
        )

        return roblox_item_configuration_api_models_response_publishing_fee_info
