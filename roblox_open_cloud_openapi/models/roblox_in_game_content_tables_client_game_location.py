from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxInGameContentTablesClientGameLocation")


@_attrs_define
class RobloxInGameContentTablesClientGameLocation:
    """
    Attributes:
        path (str | Unset):
    """

    path: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        path = d.pop("path", UNSET)

        roblox_in_game_content_tables_client_game_location = cls(
            path=path,
        )

        return roblox_in_game_content_tables_client_game_location
