from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_api_avatar_models_v4_response_outfit_validation_result_v4 import (
        RobloxApiAvatarModelsV4ResponseOutfitValidationResultV4,
    )


T = TypeVar("T", bound="RobloxApiAvatarModelsV4ResponseUpdateOutfitDefinitionResponseV4")


@_attrs_define
class RobloxApiAvatarModelsV4ResponseUpdateOutfitDefinitionResponseV4:
    """Response model for update outfit (V4).

    Attributes:
        success (bool | Unset): Whether all requested changes were successfully applied.
        validation (RobloxApiAvatarModelsV4ResponseOutfitValidationResultV4 | Unset): Validation details for outfit
            mutation responses when one or more inputs could not be applied.
    """

    success: bool | Unset = UNSET
    validation: RobloxApiAvatarModelsV4ResponseOutfitValidationResultV4 | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        validation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.validation, Unset):
            validation = self.validation.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success
        if validation is not UNSET:
            field_dict["validation"] = validation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_api_avatar_models_v4_response_outfit_validation_result_v4 import (
            RobloxApiAvatarModelsV4ResponseOutfitValidationResultV4,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        success = d.pop("success", UNSET)

        _validation = d.pop("validation", UNSET)
        validation: RobloxApiAvatarModelsV4ResponseOutfitValidationResultV4 | Unset
        if isinstance(_validation, Unset):
            validation = UNSET
        else:
            validation = RobloxApiAvatarModelsV4ResponseOutfitValidationResultV4.from_dict(_validation)

        roblox_api_avatar_models_v4_response_update_outfit_definition_response_v4 = cls(
            success=success,
            validation=validation,
        )

        return roblox_api_avatar_models_v4_response_update_outfit_definition_response_v4
