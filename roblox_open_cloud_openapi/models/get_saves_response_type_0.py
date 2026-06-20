from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.hydrated_save_type_0 import HydratedSaveType0


T = TypeVar("T", bound="GetSavesResponseType0")


@_attrs_define
class GetSavesResponseType0:
    """Response model for getting saves

    Attributes:
        total_count (int): The total number of saves that match the query.
        saves (list[HydratedSaveType0 | None] | None): Gets or sets the saves.
    """

    total_count: int
    saves: list[HydratedSaveType0 | None] | None

    def to_dict(self) -> dict[str, Any]:
        from ..models.hydrated_save_type_0 import HydratedSaveType0

        total_count = self.total_count

        saves: list[dict[str, Any] | None] | None
        if isinstance(self.saves, list):
            saves = []
            for saves_type_0_item_data in self.saves:
                saves_type_0_item: dict[str, Any] | None
                if isinstance(saves_type_0_item_data, HydratedSaveType0):
                    saves_type_0_item = saves_type_0_item_data.to_dict()
                else:
                    saves_type_0_item = saves_type_0_item_data
                saves.append(saves_type_0_item)

        else:
            saves = self.saves

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "totalCount": total_count,
                "saves": saves,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hydrated_save_type_0 import HydratedSaveType0

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        total_count = d.pop("totalCount")

        def _parse_saves(data: object) -> list[HydratedSaveType0 | None] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                saves_type_0 = []
                _saves_type_0 = data
                for saves_type_0_item_data in _saves_type_0:

                    def _parse_saves_type_0_item(data: object) -> HydratedSaveType0 | None:
                        if data is None:
                            return data
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_hydrated_save_type_0 = HydratedSaveType0.from_dict(data)

                            return componentsschemas_hydrated_save_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(HydratedSaveType0 | None, data)

                    saves_type_0_item = _parse_saves_type_0_item(saves_type_0_item_data)

                    saves_type_0.append(saves_type_0_item)

                return saves_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[HydratedSaveType0 | None] | None, data)

        saves = _parse_saves(d.pop("saves"))

        get_saves_response_type_0 = cls(
            total_count=total_count,
            saves=saves,
        )

        return get_saves_response_type_0
