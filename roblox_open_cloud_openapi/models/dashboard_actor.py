from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DashboardActor")


@_attrs_define
class DashboardActor:
    """DashboardActor identifies a user responsible for creating or mutating dashboard state.

    Attributes:
        user_id (None | str | Unset): Signed 64-bit integer encoded as a decimal string. Default: '0'.
    """

    user_id: None | str | Unset = "0"

    def to_dict(self) -> dict[str, Any]:
        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_id = _parse_user_id(d.pop("userId", UNSET))

        dashboard_actor = cls(
            user_id=user_id,
        )

        return dashboard_actor
