from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_game_internationalization_api_localization_table_game_association import (
        RobloxGameInternationalizationApiLocalizationTableGameAssociation,
    )


T = TypeVar("T", bound="RobloxGameInternationalizationApiAssociateLocalizationTablesToGameRequest")


@_attrs_define
class RobloxGameInternationalizationApiAssociateLocalizationTablesToGameRequest:
    """
    Attributes:
        tables (list[RobloxGameInternationalizationApiLocalizationTableGameAssociation] | Unset):
    """

    tables: list[RobloxGameInternationalizationApiLocalizationTableGameAssociation] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        tables: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tables, Unset):
            tables = []
            for tables_item_data in self.tables:
                tables_item = tables_item_data.to_dict()
                tables.append(tables_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if tables is not UNSET:
            field_dict["tables"] = tables

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_game_internationalization_api_localization_table_game_association import (
            RobloxGameInternationalizationApiLocalizationTableGameAssociation,
        )

        d = dict(src_dict)
        _tables = d.pop("tables", UNSET)
        tables: list[RobloxGameInternationalizationApiLocalizationTableGameAssociation] | Unset = UNSET
        if _tables is not UNSET:
            tables = []
            for tables_item_data in _tables:
                tables_item = RobloxGameInternationalizationApiLocalizationTableGameAssociation.from_dict(
                    tables_item_data
                )

                tables.append(tables_item)

        roblox_game_internationalization_api_associate_localization_tables_to_game_request = cls(
            tables=tables,
        )

        return roblox_game_internationalization_api_associate_localization_tables_to_game_request
