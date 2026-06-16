from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_authentication_api_models_request_secure_authentication_intent_model import (
        RobloxAuthenticationApiModelsRequestSecureAuthenticationIntentModel,
    )


T = TypeVar("T", bound="RobloxAuthenticationApiModelsRequestLogoutFromAllSessionsAndReauthenticateRequest")


@_attrs_define
class RobloxAuthenticationApiModelsRequestLogoutFromAllSessionsAndReauthenticateRequest:
    """
    Attributes:
        secure_authentication_intent (RobloxAuthenticationApiModelsRequestSecureAuthenticationIntentModel | Unset):
    """

    secure_authentication_intent: RobloxAuthenticationApiModelsRequestSecureAuthenticationIntentModel | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        secure_authentication_intent: dict[str, Any] | Unset = UNSET
        if not isinstance(self.secure_authentication_intent, Unset):
            secure_authentication_intent = self.secure_authentication_intent.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if secure_authentication_intent is not UNSET:
            field_dict["SecureAuthenticationIntent"] = secure_authentication_intent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_authentication_api_models_request_secure_authentication_intent_model import (
            RobloxAuthenticationApiModelsRequestSecureAuthenticationIntentModel,
        )

        d = dict(src_dict)
        _secure_authentication_intent = d.pop("SecureAuthenticationIntent", UNSET)
        secure_authentication_intent: RobloxAuthenticationApiModelsRequestSecureAuthenticationIntentModel | Unset
        if isinstance(_secure_authentication_intent, Unset):
            secure_authentication_intent = UNSET
        else:
            secure_authentication_intent = (
                RobloxAuthenticationApiModelsRequestSecureAuthenticationIntentModel.from_dict(
                    _secure_authentication_intent
                )
            )

        roblox_authentication_api_models_request_logout_from_all_sessions_and_reauthenticate_request = cls(
            secure_authentication_intent=secure_authentication_intent,
        )

        return roblox_authentication_api_models_request_logout_from_all_sessions_and_reauthenticate_request
