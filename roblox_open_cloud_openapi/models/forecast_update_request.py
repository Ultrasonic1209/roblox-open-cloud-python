from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ForecastUpdateRequest")


@_attrs_define
class ForecastUpdateRequest:
    """ForecastUpdateRequest is used to request an update to the forecast of a Place in a Universe.

    Attributes:
        universe_id (int | Unset): The Universe ID to update.
    """

    universe_id: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        universe_id = self.universe_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if universe_id is not UNSET:
            field_dict["universeId"] = universe_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        universe_id = d.pop("universeId", UNSET)

        forecast_update_request = cls(
            universe_id=universe_id,
        )

        return forecast_update_request
