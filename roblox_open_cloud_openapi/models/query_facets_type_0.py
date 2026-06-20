from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="QueryFacetsType0")


@_attrs_define
class QueryFacetsType0:
    """The facets of a query.

    Attributes:
        applied_facets (list[str] | None | Unset): Facets that are already applied to the search.
        available_facets (list[str] | None | Unset): The unused and still available facets.
    """

    applied_facets: list[str] | None | Unset = UNSET
    available_facets: list[str] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        applied_facets: list[str] | None | Unset
        if isinstance(self.applied_facets, Unset):
            applied_facets = UNSET
        elif isinstance(self.applied_facets, list):
            applied_facets = self.applied_facets

        else:
            applied_facets = self.applied_facets

        available_facets: list[str] | None | Unset
        if isinstance(self.available_facets, Unset):
            available_facets = UNSET
        elif isinstance(self.available_facets, list):
            available_facets = self.available_facets

        else:
            available_facets = self.available_facets

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if applied_facets is not UNSET:
            field_dict["appliedFacets"] = applied_facets
        if available_facets is not UNSET:
            field_dict["availableFacets"] = available_facets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_applied_facets(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                applied_facets_type_0 = cast(list[str], data)

                return applied_facets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        applied_facets = _parse_applied_facets(d.pop("appliedFacets", UNSET))

        def _parse_available_facets(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                available_facets_type_0 = cast(list[str], data)

                return available_facets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        available_facets = _parse_available_facets(d.pop("availableFacets", UNSET))

        query_facets_type_0 = cls(
            applied_facets=applied_facets,
            available_facets=available_facets,
        )

        return query_facets_type_0
