from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxItemConfigurationApiModelsResponseAvatarItemUpdateCreateAvatarItemUpdateContextResponse")


@_attrs_define
class RobloxItemConfigurationApiModelsResponseAvatarItemUpdateCreateAvatarItemUpdateContextResponse:
    """Response DTO for the create avatar item update context endpoint.

    Attributes:
        operation_id (str | Unset): The minted parent operation id. Studio threads this as the ParentOperationId of the
            staging
            asset upload so the backend can tie the new content back to the original item.
    """

    operation_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        operation_id = self.operation_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if operation_id is not UNSET:
            field_dict["operationId"] = operation_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        operation_id = d.pop("operationId", UNSET)

        roblox_item_configuration_api_models_response_avatar_item_update_create_avatar_item_update_context_response = (
            cls(
                operation_id=operation_id,
            )
        )

        return (
            roblox_item_configuration_api_models_response_avatar_item_update_create_avatar_item_update_context_response
        )
