from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_two_step_verification_api_user_configuration_method_media_type import (
    RobloxTwoStepVerificationApiUserConfigurationMethodMediaType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxTwoStepVerificationApiUserConfigurationMethod")


@_attrs_define
class RobloxTwoStepVerificationApiUserConfigurationMethod:
    """A user configuration method option.

    Attributes:
        media_type (RobloxTwoStepVerificationApiUserConfigurationMethodMediaType | Unset): The
            Roblox.TwoStepVerification.Client.TwoStepVerificationMediaType for the method. ['Email' = 0, 'SMS' = 1,
            'Authenticator' = 2, 'RecoveryCode' = 3, 'SecurityKey' = 4, 'CrossDevice' = 5, 'Password' = 6, 'Passkey' = 7]
        enabled (bool | Unset): Whether or not the method is enabled.
        updated (datetime.datetime | Unset): The last time this method was updated for the user.
    """

    media_type: RobloxTwoStepVerificationApiUserConfigurationMethodMediaType | Unset = UNSET
    enabled: bool | Unset = UNSET
    updated: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        media_type: int | Unset = UNSET
        if not isinstance(self.media_type, Unset):
            media_type = self.media_type.value

        enabled = self.enabled

        updated: str | Unset = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if media_type is not UNSET:
            field_dict["mediaType"] = media_type
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if updated is not UNSET:
            field_dict["updated"] = updated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _media_type = d.pop("mediaType", UNSET)
        media_type: RobloxTwoStepVerificationApiUserConfigurationMethodMediaType | Unset
        if isinstance(_media_type, Unset):
            media_type = UNSET
        else:
            media_type = RobloxTwoStepVerificationApiUserConfigurationMethodMediaType(_media_type)

        enabled = d.pop("enabled", UNSET)

        _updated = d.pop("updated", UNSET)
        updated: datetime.datetime | Unset
        if isinstance(_updated, Unset):
            updated = UNSET
        else:
            updated = datetime.datetime.fromisoformat(_updated)

        roblox_two_step_verification_api_user_configuration_method = cls(
            media_type=media_type,
            enabled=enabled,
            updated=updated,
        )

        return roblox_two_step_verification_api_user_configuration_method
