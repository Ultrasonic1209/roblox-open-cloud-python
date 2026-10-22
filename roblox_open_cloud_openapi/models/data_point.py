from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_point_metadata import DataPointMetadata


T = TypeVar("T", bound="DataPoint")


@_attrs_define
class DataPoint:
    """DataPoint dataPoints in the resulting query.

    Attributes:
        time (str | Unset): The date of the benchmark value.
        value (float | Unset): The benchmark value, in the metric's units.
        metadata (DataPointMetadata | Unset): DataPointMetadata metadata for a data point.
    """

    time: str | Unset = UNSET
    value: float | Unset = UNSET
    metadata: DataPointMetadata | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        time = self.time

        value = self.value

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if time is not UNSET:
            field_dict["time"] = time
        if value is not UNSET:
            field_dict["value"] = value
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_point_metadata import DataPointMetadata  # noqa: PLC0415

        d = dict(src_dict)
        time = d.pop("time", UNSET)

        value = d.pop("value", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: DataPointMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = DataPointMetadata.from_dict(_metadata)

        data_point = cls(
            time=time,
            value=value,
            metadata=metadata,
        )

        return data_point
