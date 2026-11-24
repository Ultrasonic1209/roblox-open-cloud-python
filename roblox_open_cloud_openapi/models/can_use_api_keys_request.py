from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CanUseApiKeysRequest")


@_attrs_define
class CanUseApiKeysRequest:
    """
    Attributes:
        group_id (int | Unset): Owner group of the potential API keys.
    """

    group_id: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        group_id = self.group_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if group_id is not UNSET:
            field_dict["groupId"] = group_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        group_id = d.pop("groupId", UNSET)

        can_use_api_keys_request = cls(
            group_id=group_id,
        )

        return can_use_api_keys_request
