from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_two_step_verification_api_user_configuration_primary_media_type import (
    RobloxTwoStepVerificationApiUserConfigurationPrimaryMediaType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_two_step_verification_api_user_configuration_method import (
        RobloxTwoStepVerificationApiUserConfigurationMethod,
    )


T = TypeVar("T", bound="RobloxTwoStepVerificationApiUserConfiguration")


@_attrs_define
class RobloxTwoStepVerificationApiUserConfiguration:
    """The users two step verification configuration.

    Attributes:
        primary_media_type (RobloxTwoStepVerificationApiUserConfigurationPrimaryMediaType | Unset): The preferred two
            step verification method for the user.
        methods (list[RobloxTwoStepVerificationApiUserConfigurationMethod] | Unset): The two step verification methods
            associated with the user.
    """

    primary_media_type: RobloxTwoStepVerificationApiUserConfigurationPrimaryMediaType | Unset = UNSET
    methods: list[RobloxTwoStepVerificationApiUserConfigurationMethod] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        primary_media_type: int | Unset = UNSET
        if not isinstance(self.primary_media_type, Unset):
            primary_media_type = self.primary_media_type.value

        methods: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.methods, Unset):
            methods = []
            for methods_item_data in self.methods:
                methods_item = methods_item_data.to_dict()
                methods.append(methods_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if primary_media_type is not UNSET:
            field_dict["primaryMediaType"] = primary_media_type
        if methods is not UNSET:
            field_dict["methods"] = methods

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_two_step_verification_api_user_configuration_method import (
            RobloxTwoStepVerificationApiUserConfigurationMethod,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _primary_media_type = d.pop("primaryMediaType", UNSET)
        primary_media_type: RobloxTwoStepVerificationApiUserConfigurationPrimaryMediaType | Unset
        if isinstance(_primary_media_type, Unset):
            primary_media_type = UNSET
        else:
            primary_media_type = RobloxTwoStepVerificationApiUserConfigurationPrimaryMediaType(_primary_media_type)

        _methods = d.pop("methods", UNSET)
        methods: list[RobloxTwoStepVerificationApiUserConfigurationMethod] | Unset = UNSET
        if _methods is not UNSET:
            methods = []
            for methods_item_data in _methods:
                methods_item = RobloxTwoStepVerificationApiUserConfigurationMethod.from_dict(methods_item_data)

                methods.append(methods_item)

        roblox_two_step_verification_api_user_configuration = cls(
            primary_media_type=primary_media_type,
            methods=methods,
        )

        return roblox_two_step_verification_api_user_configuration
