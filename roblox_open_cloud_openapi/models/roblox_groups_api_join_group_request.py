from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGroupsApiJoinGroupRequest")


@_attrs_define
class RobloxGroupsApiJoinGroupRequest:
    """A request model for joining group.

    Attributes:
        session_id (str | Unset):
        redemption_token (str | Unset):
        captcha_id (str | Unset):
        captcha_token (str | Unset):
        captcha_provider (str | Unset):
        challenge_id (str | Unset):
    """

    session_id: str | Unset = UNSET
    redemption_token: str | Unset = UNSET
    captcha_id: str | Unset = UNSET
    captcha_token: str | Unset = UNSET
    captcha_provider: str | Unset = UNSET
    challenge_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        session_id = self.session_id

        redemption_token = self.redemption_token

        captcha_id = self.captcha_id

        captcha_token = self.captcha_token

        captcha_provider = self.captcha_provider

        challenge_id = self.challenge_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if session_id is not UNSET:
            field_dict["sessionId"] = session_id
        if redemption_token is not UNSET:
            field_dict["redemptionToken"] = redemption_token
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
        session_id = d.pop("sessionId", UNSET)

        redemption_token = d.pop("redemptionToken", UNSET)

        captcha_id = d.pop("captchaId", UNSET)

        captcha_token = d.pop("captchaToken", UNSET)

        captcha_provider = d.pop("captchaProvider", UNSET)

        challenge_id = d.pop("challengeId", UNSET)

        roblox_groups_api_join_group_request = cls(
            session_id=session_id,
            redemption_token=redemption_token,
            captcha_id=captcha_id,
            captcha_token=captcha_token,
            captcha_provider=captcha_provider,
            challenge_id=challenge_id,
        )

        return roblox_groups_api_join_group_request
