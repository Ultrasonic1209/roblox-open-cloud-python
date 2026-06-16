from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_authentication_api_models_recover_username_request_target_type import (
    RobloxAuthenticationApiModelsRecoverUsernameRequestTargetType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAuthenticationApiModelsRecoverUsernameRequest")


@_attrs_define
class RobloxAuthenticationApiModelsRecoverUsernameRequest:
    """
    Attributes:
        target_type (RobloxAuthenticationApiModelsRecoverUsernameRequestTargetType | Unset):  ['Email' = 0,
            'PhoneNumber' = 1, 'RecoverySessionID' = 2]
        target (str | Unset):
    """

    target_type: RobloxAuthenticationApiModelsRecoverUsernameRequestTargetType | Unset = UNSET
    target: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        target_type: int | Unset = UNSET
        if not isinstance(self.target_type, Unset):
            target_type = self.target_type.value

        target = self.target

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if target_type is not UNSET:
            field_dict["targetType"] = target_type
        if target is not UNSET:
            field_dict["target"] = target

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _target_type = d.pop("targetType", UNSET)
        target_type: RobloxAuthenticationApiModelsRecoverUsernameRequestTargetType | Unset
        if isinstance(_target_type, Unset):
            target_type = UNSET
        else:
            target_type = RobloxAuthenticationApiModelsRecoverUsernameRequestTargetType(_target_type)

        target = d.pop("target", UNSET)

        roblox_authentication_api_models_recover_username_request = cls(
            target_type=target_type,
            target=target,
        )

        return roblox_authentication_api_models_recover_username_request
