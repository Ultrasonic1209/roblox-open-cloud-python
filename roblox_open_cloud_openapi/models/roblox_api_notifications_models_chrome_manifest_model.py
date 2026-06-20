from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxApiNotificationsModelsChromeManifestModel")


@_attrs_define
class RobloxApiNotificationsModelsChromeManifestModel:
    """Chrome Manifest to link GCM project to Chrome browser

    Attributes:
        name (str | Unset):
        gcm_sender_id (str | Unset):
    """

    name: str | Unset = UNSET
    gcm_sender_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        gcm_sender_id = self.gcm_sender_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if gcm_sender_id is not UNSET:
            field_dict["gcm_sender_id"] = gcm_sender_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        name = d.pop("name", UNSET)

        gcm_sender_id = d.pop("gcm_sender_id", UNSET)

        roblox_api_notifications_models_chrome_manifest_model = cls(
            name=name,
            gcm_sender_id=gcm_sender_id,
        )

        return roblox_api_notifications_models_chrome_manifest_model
