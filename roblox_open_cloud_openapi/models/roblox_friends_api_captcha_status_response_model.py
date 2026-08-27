from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxFriendsApiCaptchaStatusResponseModel")


@_attrs_define
class RobloxFriendsApiCaptchaStatusResponseModel:
    """This is response model to notify when action succeeded, failed, or captcha is required

    Attributes:
        success (bool | Unset):
        is_captcha_required (bool | Unset): Captcha is set to true if captcha is required from user to perform action
        notification_muted (bool | Unset):
    """

    success: bool | Unset = UNSET
    is_captcha_required: bool | Unset = UNSET
    notification_muted: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        is_captcha_required = self.is_captcha_required

        notification_muted = self.notification_muted

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success
        if is_captcha_required is not UNSET:
            field_dict["isCaptchaRequired"] = is_captcha_required
        if notification_muted is not UNSET:
            field_dict["notificationMuted"] = notification_muted

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        success = d.pop("success", UNSET)

        is_captcha_required = d.pop("isCaptchaRequired", UNSET)

        notification_muted = d.pop("notificationMuted", UNSET)

        roblox_friends_api_captcha_status_response_model = cls(
            success=success,
            is_captcha_required=is_captcha_required,
            notification_muted=notification_muted,
        )

        return roblox_friends_api_captcha_status_response_model
