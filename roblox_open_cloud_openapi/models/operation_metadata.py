from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="OperationMetadata")


@_attrs_define
class OperationMetadata:
    """The metadata associated with a long-running operation.

    Attributes:
        created_time (datetime.datetime | None | Unset): The time the operation was created.
    """

    created_time: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        created_time: None | str | Unset
        if isinstance(self.created_time, Unset):
            created_time = UNSET
        elif isinstance(self.created_time, datetime.datetime):
            created_time = self.created_time.isoformat()
        else:
            created_time = self.created_time

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if created_time is not UNSET:
            field_dict["createdTime"] = created_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_created_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_time_type_0 = datetime.datetime.fromisoformat(data)

                return created_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created_time = _parse_created_time(d.pop("createdTime", UNSET))

        operation_metadata = cls(
            created_time=created_time,
        )

        return operation_metadata
