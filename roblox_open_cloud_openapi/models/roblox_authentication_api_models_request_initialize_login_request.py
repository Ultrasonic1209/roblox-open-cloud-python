from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_authentication_api_models_request_initialize_login_request_ctype import (
    RobloxAuthenticationApiModelsRequestInitializeLoginRequestCtype,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAuthenticationApiModelsRequestInitializeLoginRequest")


@_attrs_define
class RobloxAuthenticationApiModelsRequestInitializeLoginRequest:
    """
    Attributes:
        ctype (RobloxAuthenticationApiModelsRequestInitializeLoginRequestCtype):
        cvalue (str):
        captcha_id (str | Unset):
        captcha_token (str | Unset):
        captcha_provider (str | Unset):
        challenge_id (str | Unset):
    """

    ctype: RobloxAuthenticationApiModelsRequestInitializeLoginRequestCtype
    cvalue: str
    captcha_id: str | Unset = UNSET
    captcha_token: str | Unset = UNSET
    captcha_provider: str | Unset = UNSET
    challenge_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        ctype = self.ctype.value

        cvalue = self.cvalue

        captcha_id = self.captcha_id

        captcha_token = self.captcha_token

        captcha_provider = self.captcha_provider

        challenge_id = self.challenge_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "ctype": ctype,
                "cvalue": cvalue,
            }
        )
        if captcha_id is not UNSET:
            field_dict["captchaId"] = captcha_id
        if captcha_token is not UNSET:
            field_dict["captchaToken"] = captcha_token
        if captcha_provider is not UNSET:
            field_dict["captchaProvider"] = captcha_provider
        if challenge_id is not UNSET:
            field_dict["challengeId"] = challenge_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ctype = RobloxAuthenticationApiModelsRequestInitializeLoginRequestCtype(d.pop("ctype"))

        cvalue = d.pop("cvalue")

        captcha_id = d.pop("captchaId", UNSET)

        captcha_token = d.pop("captchaToken", UNSET)

        captcha_provider = d.pop("captchaProvider", UNSET)

        challenge_id = d.pop("challengeId", UNSET)

        roblox_authentication_api_models_request_initialize_login_request = cls(
            ctype=ctype,
            cvalue=cvalue,
            captcha_id=captcha_id,
            captcha_token=captcha_token,
            captcha_provider=captcha_provider,
            challenge_id=challenge_id,
        )

        return roblox_authentication_api_models_request_initialize_login_request
