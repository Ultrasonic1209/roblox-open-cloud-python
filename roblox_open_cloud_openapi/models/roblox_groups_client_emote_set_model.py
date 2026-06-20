from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_groups_client_emote_model import RobloxGroupsClientEmoteModel


T = TypeVar("T", bound="RobloxGroupsClientEmoteSetModel")


@_attrs_define
class RobloxGroupsClientEmoteSetModel:
    """
    Attributes:
        id (str | Unset):
        name (str | Unset):
        emotes (list[RobloxGroupsClientEmoteModel] | Unset):
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    emotes: list[RobloxGroupsClientEmoteModel] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        emotes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.emotes, Unset):
            emotes = []
            for emotes_item_data in self.emotes:
                emotes_item = emotes_item_data.to_dict()
                emotes.append(emotes_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if emotes is not UNSET:
            field_dict["emotes"] = emotes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_groups_client_emote_model import RobloxGroupsClientEmoteModel

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _emotes = d.pop("emotes", UNSET)
        emotes: list[RobloxGroupsClientEmoteModel] | Unset = UNSET
        if _emotes is not UNSET:
            emotes = []
            for emotes_item_data in _emotes:
                emotes_item = RobloxGroupsClientEmoteModel.from_dict(emotes_item_data)

                emotes.append(emotes_item)

        roblox_groups_client_emote_set_model = cls(
            id=id,
            name=name,
            emotes=emotes,
        )

        return roblox_groups_client_emote_set_model
