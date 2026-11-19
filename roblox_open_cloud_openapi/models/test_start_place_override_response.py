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
        saved_value (None | str | Unset): The value read at the configured value path of the user's data store entry, as
            JSON text,
            so a place id saved as text keeps its quotes. Cut to at most 100 characters.
            Null when no value could be read.
    """

    result: StartPlaceOverrideTestResult | Unset = UNSET
    place_id: int | None | Unset = UNSET
    saved_value: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        result: str | Unset = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.value

        place_id: int | None | Unset
        if isinstance(self.place_id, Unset):
            place_id = UNSET
        else:
            place_id = self.place_id

        saved_value: None | str | Unset
        if isinstance(self.saved_value, Unset):
            saved_value = UNSET
        else:
            saved_value = self.saved_value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if result is not UNSET:
            field_dict["result"] = result
        if place_id is not UNSET:
            field_dict["placeId"] = place_id
        if saved_value is not UNSET:
            field_dict["savedValue"] = saved_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
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

        def _parse_saved_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        saved_value = _parse_saved_value(d.pop("savedValue", UNSET))

        test_start_place_override_response = cls(
            result=result,
            place_id=place_id,
            saved_value=saved_value,
        )

        return test_start_place_override_response
