from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxApiNotificationsModelsNotificationUser")


@_attrs_define
class RobloxApiNotificationsModelsNotificationUser:
    """
    Attributes:
        name (str | Unset): Name of the user
        user_id (int | Unset): Id of the user
    """

    name: str | Unset = UNSET
    user_id: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        user_id = self.user_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        name = d.pop("name", UNSET)

        user_id = d.pop("userId", UNSET)

        roblox_api_notifications_models_notification_user = cls(
            name=name,
            user_id=user_id,
        )

        return roblox_api_notifications_models_notification_user
