from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_api_avatar_models_v4_request_update_avatar_definition_request_v4_update_types_item import (
    RobloxApiAvatarModelsV4RequestUpdateAvatarDefinitionRequestV4UpdateTypesItem,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_api_avatar_models_v4_update_avatar_definition import (
        RobloxApiAvatarModelsV4UpdateAvatarDefinition,
    )


T = TypeVar("T", bound="RobloxApiAvatarModelsV4RequestUpdateAvatarDefinitionRequestV4")


@_attrs_define
class RobloxApiAvatarModelsV4RequestUpdateAvatarDefinitionRequestV4:
    """Request model for updating an avatar definition (V4).

    Attributes:
        update_types (list[RobloxApiAvatarModelsV4RequestUpdateAvatarDefinitionRequestV4UpdateTypesItem] | Unset): The
            list of data needed to be updated.
        avatar_definition (RobloxApiAvatarModelsV4UpdateAvatarDefinition | Unset): A model containing details about an
            avatar update.
    """

    update_types: list[RobloxApiAvatarModelsV4RequestUpdateAvatarDefinitionRequestV4UpdateTypesItem] | Unset = UNSET
    avatar_definition: RobloxApiAvatarModelsV4UpdateAvatarDefinition | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        update_types: list[int] | Unset = UNSET
        if not isinstance(self.update_types, Unset):
            update_types = []
            for update_types_item_data in self.update_types:
                update_types_item = update_types_item_data.value
                update_types.append(update_types_item)

        avatar_definition: dict[str, Any] | Unset = UNSET
        if not isinstance(self.avatar_definition, Unset):
            avatar_definition = self.avatar_definition.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if update_types is not UNSET:
            field_dict["updateTypes"] = update_types
        if avatar_definition is not UNSET:
            field_dict["avatarDefinition"] = avatar_definition

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_api_avatar_models_v4_update_avatar_definition import (
            RobloxApiAvatarModelsV4UpdateAvatarDefinition,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _update_types = d.pop("updateTypes", UNSET)
        update_types: list[RobloxApiAvatarModelsV4RequestUpdateAvatarDefinitionRequestV4UpdateTypesItem] | Unset = UNSET
        if _update_types is not UNSET:
            update_types = []
            for update_types_item_data in _update_types:
                update_types_item = RobloxApiAvatarModelsV4RequestUpdateAvatarDefinitionRequestV4UpdateTypesItem(
                    update_types_item_data
                )

                update_types.append(update_types_item)

        _avatar_definition = d.pop("avatarDefinition", UNSET)
        avatar_definition: RobloxApiAvatarModelsV4UpdateAvatarDefinition | Unset
        if isinstance(_avatar_definition, Unset):
            avatar_definition = UNSET
        else:
            avatar_definition = RobloxApiAvatarModelsV4UpdateAvatarDefinition.from_dict(_avatar_definition)

        roblox_api_avatar_models_v4_request_update_avatar_definition_request_v4 = cls(
            update_types=update_types,
            avatar_definition=avatar_definition,
        )

        return roblox_api_avatar_models_v4_request_update_avatar_definition_request_v4
