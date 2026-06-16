from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.place_response import PlaceResponse


T = TypeVar("T", bound="GameResponse")


@_attrs_define
class GameResponse:
    """
    Attributes:
        id (int | Unset):
        name (None | str | Unset):
        root_place (None | PlaceResponse | Unset):
    """

    id: int | Unset = UNSET
    name: None | str | Unset = UNSET
    root_place: None | PlaceResponse | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.place_response import PlaceResponse

        id = self.id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        root_place: dict[str, Any] | None | Unset
        if isinstance(self.root_place, Unset):
            root_place = UNSET
        elif isinstance(self.root_place, PlaceResponse):
            root_place = self.root_place.to_dict()
        else:
            root_place = self.root_place

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if root_place is not UNSET:
            field_dict["rootPlace"] = root_place

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.place_response import PlaceResponse

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_root_place(data: object) -> None | PlaceResponse | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                root_place_type_1 = PlaceResponse.from_dict(data)

                return root_place_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PlaceResponse | Unset, data)

        root_place = _parse_root_place(d.pop("rootPlace", UNSET))

        game_response = cls(
            id=id,
            name=name,
            root_place=root_place,
        )

        return game_response
