from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PrivateServerUpdateRequest")


@_attrs_define
class PrivateServerUpdateRequest:
    """
    Attributes:
        name (None | str | Unset):
        new_join_code (bool | None | Unset):
        active (bool | None | Unset):
    """

    name: None | str | Unset = UNSET
    new_join_code: bool | None | Unset = UNSET
    active: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        new_join_code: bool | None | Unset
        if isinstance(self.new_join_code, Unset):
            new_join_code = UNSET
        else:
            new_join_code = self.new_join_code

        active: bool | None | Unset
        if isinstance(self.active, Unset):
            active = UNSET
        else:
            active = self.active

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if new_join_code is not UNSET:
            field_dict["newJoinCode"] = new_join_code
        if active is not UNSET:
            field_dict["active"] = active

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_new_join_code(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        new_join_code = _parse_new_join_code(d.pop("newJoinCode", UNSET))

        def _parse_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        active = _parse_active(d.pop("active", UNSET))

        private_server_update_request = cls(
            name=name,
            new_join_code=new_join_code,
            active=active,
        )

        return private_server_update_request
