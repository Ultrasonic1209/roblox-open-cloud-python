from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PrivateServerVoiceSettingsResponse")


@_attrs_define
class PrivateServerVoiceSettingsResponse:
    """
    Attributes:
        enabled (bool | Unset):
    """

    enabled: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        enabled = d.pop("enabled", UNSET)

        private_server_voice_settings_response = cls(
            enabled=enabled,
        )

        return private_server_voice_settings_response
