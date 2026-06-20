from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxApiNotificationsModelsSuccessResponseModel")


@_attrs_define
class RobloxApiNotificationsModelsSuccessResponseModel:
    """
    Attributes:
        status_message (str | Unset): Message for the success response
    """

    status_message: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        status_message = self.status_message

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if status_message is not UNSET:
            field_dict["statusMessage"] = status_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        status_message = d.pop("statusMessage", UNSET)

        roblox_api_notifications_models_success_response_model = cls(
            status_message=status_message,
        )

        return roblox_api_notifications_models_success_response_model
