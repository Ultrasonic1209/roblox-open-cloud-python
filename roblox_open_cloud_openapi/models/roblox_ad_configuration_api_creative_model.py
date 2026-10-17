from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_ad_configuration_api_creative_model_creative_type import (
    RobloxAdConfigurationApiCreativeModelCreativeType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAdConfigurationApiCreativeModel")


@_attrs_define
class RobloxAdConfigurationApiCreativeModel:
    """A model representing an Ad Creative (for example, an ad thumbnail).

    Attributes:
        creative_id (int | Unset): The ID of the creative. Typically, a thumbnail's imageId. Example: 1.
        creative_type (RobloxAdConfigurationApiCreativeModelCreativeType | Unset): The type of the ad creative.
            Typically, CreativeType.Image. ['Undefined' = 0, 'Image' = 1, 'Video' = 2] Example: 1.
    """

    creative_id: int | Unset = UNSET
    creative_type: RobloxAdConfigurationApiCreativeModelCreativeType | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        creative_id = self.creative_id

        creative_type: int | Unset = UNSET
        if not isinstance(self.creative_type, Unset):
            creative_type = self.creative_type.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if creative_id is not UNSET:
            field_dict["creativeId"] = creative_id
        if creative_type is not UNSET:
            field_dict["creativeType"] = creative_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        creative_id = d.pop("creativeId", UNSET)

        _creative_type = d.pop("creativeType", UNSET)
        creative_type: RobloxAdConfigurationApiCreativeModelCreativeType | Unset
        if isinstance(_creative_type, Unset):
            creative_type = UNSET
        else:
            creative_type = RobloxAdConfigurationApiCreativeModelCreativeType(_creative_type)

        roblox_ad_configuration_api_creative_model = cls(
            creative_id=creative_id,
            creative_type=creative_type,
        )

        return roblox_ad_configuration_api_creative_model
