from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_item_configuration_api_models_request_update_item_display_information_request_target_type import (
    RobloxItemConfigurationApiModelsRequestUpdateItemDisplayInformationRequestTargetType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxItemConfigurationApiModelsRequestUpdateItemDisplayInformationRequest")


@_attrs_define
class RobloxItemConfigurationApiModelsRequestUpdateItemDisplayInformationRequest:
    """Api request to update the display information of an item.

    Attributes:
        target_type (RobloxItemConfigurationApiModelsRequestUpdateItemDisplayInformationRequestTargetType | Unset): The
            type of the item. ['Asset' = 0, 'Bundle' = 1, 'IecToken' = 2, 'Look' = 3]
        target_id (str | Unset): The id of the item.
        name (str | Unset): The name of the item. Null means no update.
        description (str | Unset): The description for the item. Null means no update.
    """

    target_type: RobloxItemConfigurationApiModelsRequestUpdateItemDisplayInformationRequestTargetType | Unset = UNSET
    target_id: str | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        target_type: int | Unset = UNSET
        if not isinstance(self.target_type, Unset):
            target_type = self.target_type.value

        target_id = self.target_id

        name = self.name

        description = self.description

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if target_type is not UNSET:
            field_dict["targetType"] = target_type
        if target_id is not UNSET:
            field_dict["targetId"] = target_id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _target_type = d.pop("targetType", UNSET)
        target_type: RobloxItemConfigurationApiModelsRequestUpdateItemDisplayInformationRequestTargetType | Unset
        if isinstance(_target_type, Unset):
            target_type = UNSET
        else:
            target_type = RobloxItemConfigurationApiModelsRequestUpdateItemDisplayInformationRequestTargetType(
                _target_type
            )

        target_id = d.pop("targetId", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        roblox_item_configuration_api_models_request_update_item_display_information_request = cls(
            target_type=target_type,
            target_id=target_id,
            name=name,
            description=description,
        )

        return roblox_item_configuration_api_models_request_update_item_display_information_request
