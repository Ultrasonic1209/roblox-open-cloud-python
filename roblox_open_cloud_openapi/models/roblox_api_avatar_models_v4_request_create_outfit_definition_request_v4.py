from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_api_avatar_models_v4_update_outfit_definition import (
        RobloxApiAvatarModelsV4UpdateOutfitDefinition,
    )


T = TypeVar("T", bound="RobloxApiAvatarModelsV4RequestCreateOutfitDefinitionRequestV4")


@_attrs_define
class RobloxApiAvatarModelsV4RequestCreateOutfitDefinitionRequestV4:
    """Request model for creating an outfit (V4).

    Attributes:
        outfit_definition (RobloxApiAvatarModelsV4UpdateOutfitDefinition | Unset): A model containing outfit fields to
            create or update.
    """

    outfit_definition: RobloxApiAvatarModelsV4UpdateOutfitDefinition | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        outfit_definition: dict[str, Any] | Unset = UNSET
        if not isinstance(self.outfit_definition, Unset):
            outfit_definition = self.outfit_definition.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if outfit_definition is not UNSET:
            field_dict["outfitDefinition"] = outfit_definition

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_api_avatar_models_v4_update_outfit_definition import (
            RobloxApiAvatarModelsV4UpdateOutfitDefinition,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _outfit_definition = d.pop("outfitDefinition", UNSET)
        outfit_definition: RobloxApiAvatarModelsV4UpdateOutfitDefinition | Unset
        if isinstance(_outfit_definition, Unset):
            outfit_definition = UNSET
        else:
            outfit_definition = RobloxApiAvatarModelsV4UpdateOutfitDefinition.from_dict(_outfit_definition)

        roblox_api_avatar_models_v4_request_create_outfit_definition_request_v4 = cls(
            outfit_definition=outfit_definition,
        )

        return roblox_api_avatar_models_v4_request_create_outfit_definition_request_v4
