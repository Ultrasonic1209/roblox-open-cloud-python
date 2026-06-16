from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_groups_client_emote_set_model import RobloxGroupsClientEmoteSetModel


T = TypeVar("T", bound="RobloxGroupsClientGetGroupEmoteSetsResponse")


@_attrs_define
class RobloxGroupsClientGetGroupEmoteSetsResponse:
    """
    Attributes:
        emote_sets (list[RobloxGroupsClientEmoteSetModel] | Unset):
    """

    emote_sets: list[RobloxGroupsClientEmoteSetModel] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        emote_sets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.emote_sets, Unset):
            emote_sets = []
            for emote_sets_item_data in self.emote_sets:
                emote_sets_item = emote_sets_item_data.to_dict()
                emote_sets.append(emote_sets_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if emote_sets is not UNSET:
            field_dict["emoteSets"] = emote_sets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_groups_client_emote_set_model import RobloxGroupsClientEmoteSetModel

        d = dict(src_dict)
        _emote_sets = d.pop("emoteSets", UNSET)
        emote_sets: list[RobloxGroupsClientEmoteSetModel] | Unset = UNSET
        if _emote_sets is not UNSET:
            emote_sets = []
            for emote_sets_item_data in _emote_sets:
                emote_sets_item = RobloxGroupsClientEmoteSetModel.from_dict(emote_sets_item_data)

                emote_sets.append(emote_sets_item)

        roblox_groups_client_get_group_emote_sets_response = cls(
            emote_sets=emote_sets,
        )

        return roblox_groups_client_get_group_emote_sets_response
