from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_api_avatar_models_v4_request_update_outfit_definition_request_v4_update_types_item import (
    RobloxApiAvatarModelsV4RequestUpdateOutfitDefinitionRequestV4UpdateTypesItem,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_api_avatar_models_v4_update_outfit_definition import (
        RobloxApiAvatarModelsV4UpdateOutfitDefinition,
    )


T = TypeVar("T", bound="RobloxApiAvatarModelsV4RequestUpdateOutfitDefinitionRequestV4")


@_attrs_define
class RobloxApiAvatarModelsV4RequestUpdateOutfitDefinitionRequestV4:
    """Request model for updating an outfit (V4).

    Attributes:
        update_types (list[RobloxApiAvatarModelsV4RequestUpdateOutfitDefinitionRequestV4UpdateTypesItem] | Unset): The
            list of data needed to be updated.
        outfit_definition (RobloxApiAvatarModelsV4UpdateOutfitDefinition | Unset): A model containing outfit fields to
            create or update.
    """

    update_types: list[RobloxApiAvatarModelsV4RequestUpdateOutfitDefinitionRequestV4UpdateTypesItem] | Unset = UNSET
    outfit_definition: RobloxApiAvatarModelsV4UpdateOutfitDefinition | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        update_types: list[int] | Unset = UNSET
        if not isinstance(self.update_types, Unset):
            update_types = []
            for update_types_item_data in self.update_types:
                update_types_item = update_types_item_data.value
                update_types.append(update_types_item)

        outfit_definition: dict[str, Any] | Unset = UNSET
        if not isinstance(self.outfit_definition, Unset):
            outfit_definition = self.outfit_definition.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if update_types is not UNSET:
            field_dict["updateTypes"] = update_types
        if outfit_definition is not UNSET:
            field_dict["outfitDefinition"] = outfit_definition

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_api_avatar_models_v4_update_outfit_definition import (
            RobloxApiAvatarModelsV4UpdateOutfitDefinition,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _update_types = d.pop("updateTypes", UNSET)
        update_types: list[RobloxApiAvatarModelsV4RequestUpdateOutfitDefinitionRequestV4UpdateTypesItem] | Unset = UNSET
        if _update_types is not UNSET:
            update_types = []
            for update_types_item_data in _update_types:
                update_types_item = RobloxApiAvatarModelsV4RequestUpdateOutfitDefinitionRequestV4UpdateTypesItem(
                    update_types_item_data
                )

                update_types.append(update_types_item)

        _outfit_definition = d.pop("outfitDefinition", UNSET)
        outfit_definition: RobloxApiAvatarModelsV4UpdateOutfitDefinition | Unset
        if isinstance(_outfit_definition, Unset):
            outfit_definition = UNSET
        else:
            outfit_definition = RobloxApiAvatarModelsV4UpdateOutfitDefinition.from_dict(_outfit_definition)

        roblox_api_avatar_models_v4_request_update_outfit_definition_request_v4 = cls(
            update_types=update_types,
            outfit_definition=outfit_definition,
        )

        return roblox_api_avatar_models_v4_request_update_outfit_definition_request_v4
