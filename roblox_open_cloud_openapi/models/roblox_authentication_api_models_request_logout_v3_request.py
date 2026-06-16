from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAuthenticationApiModelsRequestLogoutV3Request")


@_attrs_define
class RobloxAuthenticationApiModelsRequestLogoutV3Request:
    """
    Attributes:
        logout_reason (str | Unset):
        url (str | Unset):
        user_id (str | Unset):
    """

    logout_reason: str | Unset = UNSET
    url: str | Unset = UNSET
    user_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        logout_reason = self.logout_reason

        url = self.url

        user_id = self.user_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if logout_reason is not UNSET:
            field_dict["logoutReason"] = logout_reason
        if url is not UNSET:
            field_dict["url"] = url
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        logout_reason = d.pop("logoutReason", UNSET)

        url = d.pop("url", UNSET)

        user_id = d.pop("userId", UNSET)

        roblox_authentication_api_models_request_logout_v3_request = cls(
            logout_reason=logout_reason,
            url=url,
            user_id=user_id,
        )

        return roblox_authentication_api_models_request_logout_v3_request
