from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CanUseApiKeysResponse")


@_attrs_define
class CanUseApiKeysResponse:
    """
    Attributes:
        can_use_api_keys (bool | Unset): Whether the current user can create and use API keys under the group.
    """

    can_use_api_keys: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        can_use_api_keys = self.can_use_api_keys

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if can_use_api_keys is not UNSET:
            field_dict["canUseApiKeys"] = can_use_api_keys

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        can_use_api_keys = d.pop("canUseApiKeys", UNSET)

        can_use_api_keys_response = cls(
            can_use_api_keys=can_use_api_keys,
        )

        return can_use_api_keys_response
