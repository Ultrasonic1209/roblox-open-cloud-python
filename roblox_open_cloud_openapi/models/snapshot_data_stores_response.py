from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnapshotDataStoresResponse")


@_attrs_define
class SnapshotDataStoresResponse:
    """Returns whether a new snapshot was taken and the time of the latest snapshot
    after the operation (regardless of whether a new snapshot was taken).

        Attributes:
            new_snapshot_taken (bool | Unset): Whether a new snapshot was taken by this operation.
                (Only one snapshot can be taken per experience per UTC day.) Example: True.
            latest_snapshot_time (datetime.datetime | Unset): The time of the latest snapshot after the operation
                (regardless of
                whether a new snapshot was created). This time is always returned in UTC. Example: 2023-07-05T12:34:56Z.
    """

    new_snapshot_taken: bool | Unset = UNSET
    latest_snapshot_time: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        new_snapshot_taken = self.new_snapshot_taken

        latest_snapshot_time: str | Unset = UNSET
        if not isinstance(self.latest_snapshot_time, Unset):
            latest_snapshot_time = self.latest_snapshot_time.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if new_snapshot_taken is not UNSET:
            field_dict["newSnapshotTaken"] = new_snapshot_taken
        if latest_snapshot_time is not UNSET:
            field_dict["latestSnapshotTime"] = latest_snapshot_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        new_snapshot_taken = d.pop("newSnapshotTaken", UNSET)

        _latest_snapshot_time = d.pop("latestSnapshotTime", UNSET)
        latest_snapshot_time: datetime.datetime | Unset
        if isinstance(_latest_snapshot_time, Unset):
            latest_snapshot_time = UNSET
        else:
            latest_snapshot_time = datetime.datetime.fromisoformat(_latest_snapshot_time)

        snapshot_data_stores_response = cls(
            new_snapshot_taken=new_snapshot_taken,
            latest_snapshot_time=latest_snapshot_time,
        )

        snapshot_data_stores_response.additional_properties = d
        return snapshot_data_stores_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
