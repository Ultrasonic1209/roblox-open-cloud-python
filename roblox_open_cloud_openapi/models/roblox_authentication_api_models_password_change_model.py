from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_authentication_api_models_request_secure_authentication_intent_model import (
        RobloxAuthenticationApiModelsRequestSecureAuthenticationIntentModel,
    )


T = TypeVar("T", bound="RobloxAuthenticationApiModelsPasswordChangeModel")


@_attrs_define
class RobloxAuthenticationApiModelsPasswordChangeModel:
    """
    Attributes:
        current_password (str | Unset):
        new_password (str | Unset):
        secure_authentication_intent (RobloxAuthenticationApiModelsRequestSecureAuthenticationIntentModel | Unset):
    """

    current_password: str | Unset = UNSET
    new_password: str | Unset = UNSET
    secure_authentication_intent: RobloxAuthenticationApiModelsRequestSecureAuthenticationIntentModel | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        current_password = self.current_password

        new_password = self.new_password

        secure_authentication_intent: dict[str, Any] | Unset = UNSET
        if not isinstance(self.secure_authentication_intent, Unset):
            secure_authentication_intent = self.secure_authentication_intent.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if current_password is not UNSET:
            field_dict["currentPassword"] = current_password
        if new_password is not UNSET:
            field_dict["newPassword"] = new_password
        if secure_authentication_intent is not UNSET:
            field_dict["secureAuthenticationIntent"] = secure_authentication_intent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_authentication_api_models_request_secure_authentication_intent_model import (
            RobloxAuthenticationApiModelsRequestSecureAuthenticationIntentModel,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        current_password = d.pop("currentPassword", UNSET)

        new_password = d.pop("newPassword", UNSET)

        _secure_authentication_intent = d.pop("secureAuthenticationIntent", UNSET)
        secure_authentication_intent: RobloxAuthenticationApiModelsRequestSecureAuthenticationIntentModel | Unset
        if isinstance(_secure_authentication_intent, Unset):
            secure_authentication_intent = UNSET
        else:
            secure_authentication_intent = (
                RobloxAuthenticationApiModelsRequestSecureAuthenticationIntentModel.from_dict(
                    _secure_authentication_intent
                )
            )

        roblox_authentication_api_models_password_change_model = cls(
            current_password=current_password,
            new_password=new_password,
            secure_authentication_intent=secure_authentication_intent,
        )

        return roblox_authentication_api_models_password_change_model
