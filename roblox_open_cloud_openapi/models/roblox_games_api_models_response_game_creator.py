from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGamesApiModelsResponseGameCreator")


@_attrs_define
class RobloxGamesApiModelsResponseGameCreator:
    """Response model for getting the game creator

    Attributes:
        id (int | Unset): The game creator id
        name (str | Unset): The game creator name
        type_ (str | Unset): The game creator type
        is_rnv_account (bool | Unset): The game creator account is Luobu Real Name Verified
        has_verified_badge (bool | Unset): Builder verified badge status.
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    type_: str | Unset = UNSET
    is_rnv_account: bool | Unset = UNSET
    has_verified_badge: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        type_ = self.type_

        is_rnv_account = self.is_rnv_account

        has_verified_badge = self.has_verified_badge

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if is_rnv_account is not UNSET:
            field_dict["isRNVAccount"] = is_rnv_account
        if has_verified_badge is not UNSET:
            field_dict["hasVerifiedBadge"] = has_verified_badge

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        is_rnv_account = d.pop("isRNVAccount", UNSET)

        has_verified_badge = d.pop("hasVerifiedBadge", UNSET)

        roblox_games_api_models_response_game_creator = cls(
            id=id,
            name=name,
            type_=type_,
            is_rnv_account=is_rnv_account,
            has_verified_badge=has_verified_badge,
        )

        return roblox_games_api_models_response_game_creator
