from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGameInternationalizationApiLocalizationTableGameAssociation")


@_attrs_define
class RobloxGameInternationalizationApiLocalizationTableGameAssociation:
    """
    Attributes:
        id (UUID | Unset):
        dissociate (bool | Unset):
    """

    id: UUID | Unset = UNSET
    dissociate: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        dissociate = self.dissociate

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if dissociate is not UNSET:
            field_dict["dissociate"] = dissociate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        dissociate = d.pop("dissociate", UNSET)

        roblox_game_internationalization_api_localization_table_game_association = cls(
            id=id,
            dissociate=dissociate,
        )

        return roblox_game_internationalization_api_localization_table_game_association
