from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxCatalogApiTopicModel")


@_attrs_define
class RobloxCatalogApiTopicModel:
    """Response model for avatar topics.

    Attributes:
        display_name (str | Unset): The display topic name.
        original_topic_name (str | Unset): The original topic name stored in the table.
    """

    display_name: str | Unset = UNSET
    original_topic_name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        original_topic_name = self.original_topic_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if original_topic_name is not UNSET:
            field_dict["originalTopicName"] = original_topic_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        display_name = d.pop("displayName", UNSET)

        original_topic_name = d.pop("originalTopicName", UNSET)

        roblox_catalog_api_topic_model = cls(
            display_name=display_name,
            original_topic_name=original_topic_name,
        )

        return roblox_catalog_api_topic_model
