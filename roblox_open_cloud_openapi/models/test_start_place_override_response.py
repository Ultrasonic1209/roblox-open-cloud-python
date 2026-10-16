from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.start_place_override_test_result import StartPlaceOverrideTestResult
from ..types import UNSET, Unset

T = TypeVar("T", bound="TestStartPlaceOverrideResponse")


@_attrs_define
class TestStartPlaceOverrideResponse:
    """Response for testing a user's saved start place in a universe.

    Attributes:
        result (StartPlaceOverrideTestResult | Unset): Whether a user's saved start place passed every check, and if
            not, why.
        place_id (int | None | Unset): The place id read from the user's data store entry.
            Null when no place id could be read.
    """

    result: StartPlaceOverrideTestResult | Unset = UNSET
    place_id: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        result: str | Unset = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.value

        place_id: int | None | Unset
        if isinstance(self.place_id, Unset):
            place_id = UNSET
        else:
            place_id = self.place_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if result is not UNSET:
            field_dict["result"] = result
        if place_id is not UNSET:
            field_dict["placeId"] = place_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _result = d.pop("result", UNSET)
        result: StartPlaceOverrideTestResult | Unset
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = StartPlaceOverrideTestResult(_result)

        def _parse_place_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        place_id = _parse_place_id(d.pop("placeId", UNSET))

        test_start_place_override_response = cls(
            result=result,
            place_id=place_id,
        )

        return test_start_place_override_response
