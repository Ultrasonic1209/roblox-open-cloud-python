from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PrivateServersEnabledInUniverseResponse")


@_attrs_define
class PrivateServersEnabledInUniverseResponse:
    """
    Attributes:
        private_servers_enabled (bool | Unset):
    """

    private_servers_enabled: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        private_servers_enabled = self.private_servers_enabled

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if private_servers_enabled is not UNSET:
            field_dict["privateServersEnabled"] = private_servers_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        private_servers_enabled = d.pop("privateServersEnabled", UNSET)

        private_servers_enabled_in_universe_response = cls(
            private_servers_enabled=private_servers_enabled,
        )

        return private_servers_enabled_in_universe_response
