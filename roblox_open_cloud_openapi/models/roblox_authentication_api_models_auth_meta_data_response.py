from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAuthenticationApiModelsAuthMetaDataResponse")


@_attrs_define
class RobloxAuthenticationApiModelsAuthMetaDataResponse:
    """
    Attributes:
        cookie_law_notice_timeout (int | Unset):
    """

    cookie_law_notice_timeout: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        cookie_law_notice_timeout = self.cookie_law_notice_timeout

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if cookie_law_notice_timeout is not UNSET:
            field_dict["cookieLawNoticeTimeout"] = cookie_law_notice_timeout

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        cookie_law_notice_timeout = d.pop("cookieLawNoticeTimeout", UNSET)

        roblox_authentication_api_models_auth_meta_data_response = cls(
            cookie_law_notice_timeout=cookie_law_notice_timeout,
        )

        return roblox_authentication_api_models_auth_meta_data_response
