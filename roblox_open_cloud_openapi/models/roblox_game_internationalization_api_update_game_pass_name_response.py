from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGameInternationalizationApiUpdateGamePassNameResponse")


@_attrs_define
class RobloxGameInternationalizationApiUpdateGamePassNameResponse:
    """A response model for updating game pass name

    Attributes:
        name (str | Unset): Game pass name saved
    """

    name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        roblox_game_internationalization_api_update_game_pass_name_response = cls(
            name=name,
        )

        return roblox_game_internationalization_api_update_game_pass_name_response
