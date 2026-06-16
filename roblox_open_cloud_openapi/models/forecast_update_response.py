from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.place_summary_for_game_update import PlaceSummaryForGameUpdate


T = TypeVar("T", bound="ForecastUpdateResponse")


@_attrs_define
class ForecastUpdateResponse:
    """ForecastUpdateResponse is used to return information about the forecasted update of a place.

    Attributes:
        place_summaries (list[PlaceSummaryForGameUpdate] | None | Unset):
    """

    place_summaries: list[PlaceSummaryForGameUpdate] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        place_summaries: list[dict[str, Any]] | None | Unset
        if isinstance(self.place_summaries, Unset):
            place_summaries = UNSET
        elif isinstance(self.place_summaries, list):
            place_summaries = []
            for place_summaries_type_0_item_data in self.place_summaries:
                place_summaries_type_0_item = place_summaries_type_0_item_data.to_dict()
                place_summaries.append(place_summaries_type_0_item)

        else:
            place_summaries = self.place_summaries

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if place_summaries is not UNSET:
            field_dict["placeSummaries"] = place_summaries

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.place_summary_for_game_update import PlaceSummaryForGameUpdate

        d = dict(src_dict)

        def _parse_place_summaries(data: object) -> list[PlaceSummaryForGameUpdate] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                place_summaries_type_0 = []
                _place_summaries_type_0 = data
                for place_summaries_type_0_item_data in _place_summaries_type_0:
                    place_summaries_type_0_item = PlaceSummaryForGameUpdate.from_dict(place_summaries_type_0_item_data)

                    place_summaries_type_0.append(place_summaries_type_0_item)

                return place_summaries_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PlaceSummaryForGameUpdate] | None | Unset, data)

        place_summaries = _parse_place_summaries(d.pop("placeSummaries", UNSET))

        forecast_update_response = cls(
            place_summaries=place_summaries,
        )

        return forecast_update_response
