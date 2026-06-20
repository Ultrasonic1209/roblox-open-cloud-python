from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.forecast_restart_response_place_forecasts_type_0 import ForecastRestartResponsePlaceForecastsType0


T = TypeVar("T", bound="ForecastRestartResponse")


@_attrs_define
class ForecastRestartResponse:
    """Response model for the forecast restart endpoint.

    Attributes:
        place_forecasts (ForecastRestartResponsePlaceForecastsType0 | None | Unset): Per-place forecast data keyed by
            place ID.
            Empty if no active places.
    """

    place_forecasts: ForecastRestartResponsePlaceForecastsType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.forecast_restart_response_place_forecasts_type_0 import ForecastRestartResponsePlaceForecastsType0

        place_forecasts: dict[str, Any] | None | Unset
        if isinstance(self.place_forecasts, Unset):
            place_forecasts = UNSET
        elif isinstance(self.place_forecasts, ForecastRestartResponsePlaceForecastsType0):
            place_forecasts = self.place_forecasts.to_dict()
        else:
            place_forecasts = self.place_forecasts

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if place_forecasts is not UNSET:
            field_dict["placeForecasts"] = place_forecasts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.forecast_restart_response_place_forecasts_type_0 import ForecastRestartResponsePlaceForecastsType0

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_place_forecasts(data: object) -> ForecastRestartResponsePlaceForecastsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                place_forecasts_type_0 = ForecastRestartResponsePlaceForecastsType0.from_dict(data)

                return place_forecasts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ForecastRestartResponsePlaceForecastsType0 | None | Unset, data)

        place_forecasts = _parse_place_forecasts(d.pop("placeForecasts", UNSET))

        forecast_restart_response = cls(
            place_forecasts=place_forecasts,
        )

        return forecast_restart_response
