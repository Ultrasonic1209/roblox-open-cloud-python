from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetPlaceContributorsResponse")


@_attrs_define
class GetPlaceContributorsResponse:
    """
    Attributes:
        next_cursor (None | str | Unset):
        has_more (bool | Unset):
        contributors (list[int] | None | Unset):
    """

    next_cursor: None | str | Unset = UNSET
    has_more: bool | Unset = UNSET
    contributors: list[int] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        next_cursor: None | str | Unset
        if isinstance(self.next_cursor, Unset):
            next_cursor = UNSET
        else:
            next_cursor = self.next_cursor

        has_more = self.has_more

        contributors: list[int] | None | Unset
        if isinstance(self.contributors, Unset):
            contributors = UNSET
        elif isinstance(self.contributors, list):
            contributors = self.contributors

        else:
            contributors = self.contributors

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if next_cursor is not UNSET:
            field_dict["nextCursor"] = next_cursor
        if has_more is not UNSET:
            field_dict["hasMore"] = has_more
        if contributors is not UNSET:
            field_dict["contributors"] = contributors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_next_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_cursor = _parse_next_cursor(d.pop("nextCursor", UNSET))

        has_more = d.pop("hasMore", UNSET)

        def _parse_contributors(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                contributors_type_0 = cast(list[int], data)

                return contributors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        contributors = _parse_contributors(d.pop("contributors", UNSET))

        get_place_contributors_response = cls(
            next_cursor=next_cursor,
            has_more=has_more,
            contributors=contributors,
        )

        return get_place_contributors_response
