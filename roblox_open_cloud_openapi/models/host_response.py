from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.host_type import HostType
from ..types import UNSET, Unset

T = TypeVar("T", bound="HostResponse")


@_attrs_define
class HostResponse:
    """Host block. VirtualEventsApi.Models.V3.Response.HostResponse.HostName and
    VirtualEventsApi.Models.V3.Response.HostResponse.HasVerifiedBadge are omitted when host-details resolution failed.

        Attributes:
            host_type (HostType | Unset): The type of host of a virtual event.
            host_id (int | Unset):
            host_name (None | str | Unset):
            has_verified_badge (bool | None | Unset):
    """

    host_type: HostType | Unset = UNSET
    host_id: int | Unset = UNSET
    host_name: None | str | Unset = UNSET
    has_verified_badge: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        host_type: str | Unset = UNSET
        if not isinstance(self.host_type, Unset):
            host_type = self.host_type.value

        host_id = self.host_id

        host_name: None | str | Unset
        if isinstance(self.host_name, Unset):
            host_name = UNSET
        else:
            host_name = self.host_name

        has_verified_badge: bool | None | Unset
        if isinstance(self.has_verified_badge, Unset):
            has_verified_badge = UNSET
        else:
            has_verified_badge = self.has_verified_badge

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if host_type is not UNSET:
            field_dict["hostType"] = host_type
        if host_id is not UNSET:
            field_dict["hostId"] = host_id
        if host_name is not UNSET:
            field_dict["hostName"] = host_name
        if has_verified_badge is not UNSET:
            field_dict["hasVerifiedBadge"] = has_verified_badge

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _host_type = d.pop("hostType", UNSET)
        host_type: HostType | Unset
        if isinstance(_host_type, Unset):
            host_type = UNSET
        else:
            host_type = HostType(_host_type)

        host_id = d.pop("hostId", UNSET)

        def _parse_host_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        host_name = _parse_host_name(d.pop("hostName", UNSET))

        def _parse_has_verified_badge(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        has_verified_badge = _parse_has_verified_badge(d.pop("hasVerifiedBadge", UNSET))

        host_response = cls(
            host_type=host_type,
            host_id=host_id,
            host_name=host_name,
            has_verified_badge=has_verified_badge,
        )

        return host_response
