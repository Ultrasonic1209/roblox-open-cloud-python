from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="QueryCorrectionType0")


@_attrs_define
class QueryCorrectionType0:
    """Contains query correction information for a search query.

    Attributes:
        suggested_query (None | str | Unset): The suggested spelling correction for the original search query.
    """

    suggested_query: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        suggested_query: None | str | Unset
        if isinstance(self.suggested_query, Unset):
            suggested_query = UNSET
        else:
            suggested_query = self.suggested_query

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if suggested_query is not UNSET:
            field_dict["suggestedQuery"] = suggested_query

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_suggested_query(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        suggested_query = _parse_suggested_query(d.pop("suggestedQuery", UNSET))

        query_correction_type_0 = cls(
            suggested_query=suggested_query,
        )

        return query_correction_type_0
