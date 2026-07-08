from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.data_status import DataStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="DataPoint")


@_attrs_define
class DataPoint:
    """A single data point in a metric query result.

    Attributes:
        time (datetime.datetime): The timestamp of the data point in UTC.
        value (float): The numeric value of the data point.
        string_values (list[str] | None | Unset): String values associated with the data point, when applicable.
        status (DataStatus | Unset): The status of a data point in a query result.
    """

    time: datetime.datetime
    value: float
    string_values: list[str] | None | Unset = UNSET
    status: DataStatus | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        time = self.time.isoformat()

        value = self.value

        string_values: list[str] | None | Unset
        if isinstance(self.string_values, Unset):
            string_values = UNSET
        elif isinstance(self.string_values, list):
            string_values = self.string_values

        else:
            string_values = self.string_values

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "time": time,
                "value": value,
            }
        )
        if string_values is not UNSET:
            field_dict["stringValues"] = string_values
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        time = datetime.datetime.fromisoformat(d.pop("time"))

        value = d.pop("value")

        def _parse_string_values(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                string_values_type_0 = cast(list[str], data)

                return string_values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        string_values = _parse_string_values(d.pop("stringValues", UNSET))

        _status = d.pop("status", UNSET)
        status: DataStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = DataStatus(_status)

        data_point = cls(
            time=time,
            value=value,
            string_values=string_values,
            status=status,
        )

        return data_point
