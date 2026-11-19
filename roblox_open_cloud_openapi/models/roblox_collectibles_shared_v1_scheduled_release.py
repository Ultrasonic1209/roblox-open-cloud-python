from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.google_protobuf_well_known_types_timestamp import GoogleProtobufWellKnownTypesTimestamp


T = TypeVar("T", bound="RobloxCollectiblesSharedV1ScheduledRelease")


@_attrs_define
class RobloxCollectiblesSharedV1ScheduledRelease:
    """
    Attributes:
        on_sale_time (GoogleProtobufWellKnownTypesTimestamp | Unset):
        off_sale_time (GoogleProtobufWellKnownTypesTimestamp | Unset):
    """

    on_sale_time: GoogleProtobufWellKnownTypesTimestamp | Unset = UNSET
    off_sale_time: GoogleProtobufWellKnownTypesTimestamp | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        on_sale_time: dict[str, Any] | Unset = UNSET
        if not isinstance(self.on_sale_time, Unset):
            on_sale_time = self.on_sale_time.to_dict()

        off_sale_time: dict[str, Any] | Unset = UNSET
        if not isinstance(self.off_sale_time, Unset):
            off_sale_time = self.off_sale_time.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if on_sale_time is not UNSET:
            field_dict["OnSaleTime"] = on_sale_time
        if off_sale_time is not UNSET:
            field_dict["OffSaleTime"] = off_sale_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.google_protobuf_well_known_types_timestamp import GoogleProtobufWellKnownTypesTimestamp  # noqa: PLC0415

        d = dict(src_dict)
        _on_sale_time = d.pop("OnSaleTime", UNSET)
        on_sale_time: GoogleProtobufWellKnownTypesTimestamp | Unset
        if isinstance(_on_sale_time, Unset):
            on_sale_time = UNSET
        else:
            on_sale_time = GoogleProtobufWellKnownTypesTimestamp.from_dict(_on_sale_time)

        _off_sale_time = d.pop("OffSaleTime", UNSET)
        off_sale_time: GoogleProtobufWellKnownTypesTimestamp | Unset
        if isinstance(_off_sale_time, Unset):
            off_sale_time = UNSET
        else:
            off_sale_time = GoogleProtobufWellKnownTypesTimestamp.from_dict(_off_sale_time)

        roblox_collectibles_shared_v1_scheduled_release = cls(
            on_sale_time=on_sale_time,
            off_sale_time=off_sale_time,
        )

        return roblox_collectibles_shared_v1_scheduled_release
