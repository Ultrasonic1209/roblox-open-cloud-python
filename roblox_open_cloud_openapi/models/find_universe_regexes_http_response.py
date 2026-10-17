from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.universe_regex_http_response import UniverseRegexHttpResponse


T = TypeVar("T", bound="FindUniverseRegexesHttpResponse")


@_attrs_define
class FindUniverseRegexesHttpResponse:
    """
    Attributes:
        universe_regexes (list[UniverseRegexHttpResponse] | None | Unset):
    """

    universe_regexes: list[UniverseRegexHttpResponse] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        universe_regexes: list[dict[str, Any]] | None | Unset
        if isinstance(self.universe_regexes, Unset):
            universe_regexes = UNSET
        elif isinstance(self.universe_regexes, list):
            universe_regexes = []
            for universe_regexes_type_0_item_data in self.universe_regexes:
                universe_regexes_type_0_item = universe_regexes_type_0_item_data.to_dict()
                universe_regexes.append(universe_regexes_type_0_item)

        else:
            universe_regexes = self.universe_regexes

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if universe_regexes is not UNSET:
            field_dict["universeRegexes"] = universe_regexes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.universe_regex_http_response import UniverseRegexHttpResponse

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_universe_regexes(data: object) -> list[UniverseRegexHttpResponse] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                universe_regexes_type_0 = []
                _universe_regexes_type_0 = data
                for universe_regexes_type_0_item_data in _universe_regexes_type_0:
                    universe_regexes_type_0_item = UniverseRegexHttpResponse.from_dict(
                        universe_regexes_type_0_item_data
                    )

                    universe_regexes_type_0.append(universe_regexes_type_0_item)

                return universe_regexes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UniverseRegexHttpResponse] | None | Unset, data)

        universe_regexes = _parse_universe_regexes(d.pop("universeRegexes", UNSET))

        find_universe_regexes_http_response = cls(
            universe_regexes=universe_regexes,
        )

        return find_universe_regexes_http_response
