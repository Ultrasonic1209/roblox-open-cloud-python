from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="GoogleProtobufWellKnownTypesTimestamp")


@_attrs_define
class GoogleProtobufWellKnownTypesTimestamp:
    """
    Attributes:
        seconds (int | Unset):
        nanos (int | Unset):
    """

    seconds: int | Unset = UNSET
    nanos: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        seconds = self.seconds

        nanos = self.nanos

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if seconds is not UNSET:
            field_dict["Seconds"] = seconds
        if nanos is not UNSET:
            field_dict["Nanos"] = nanos

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        seconds = d.pop("Seconds", UNSET)

        nanos = d.pop("Nanos", UNSET)

        google_protobuf_well_known_types_timestamp = cls(
            seconds=seconds,
            nanos=nanos,
        )

        return google_protobuf_well_known_types_timestamp
