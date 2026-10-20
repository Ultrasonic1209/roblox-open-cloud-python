from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_authentication_api_models_request_start_authentication_by_user_request_ctype import (
    RobloxAuthenticationApiModelsRequestStartAuthenticationByUserRequestCtype,
)

T = TypeVar("T", bound="RobloxAuthenticationApiModelsRequestStartAuthenticationByUserRequest")


@_attrs_define
class RobloxAuthenticationApiModelsRequestStartAuthenticationByUserRequest:
    """
    Attributes:
        ctype (RobloxAuthenticationApiModelsRequestStartAuthenticationByUserRequestCtype):
        cvalue (str):
    """

    ctype: RobloxAuthenticationApiModelsRequestStartAuthenticationByUserRequestCtype
    cvalue: str

    def to_dict(self) -> dict[str, Any]:
        ctype = self.ctype.value

        cvalue = self.cvalue

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "ctype": ctype,
                "cvalue": cvalue,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ctype = RobloxAuthenticationApiModelsRequestStartAuthenticationByUserRequestCtype(d.pop("ctype"))

        cvalue = d.pop("cvalue")

        roblox_authentication_api_models_request_start_authentication_by_user_request = cls(
            ctype=ctype,
            cvalue=cvalue,
        )

        return roblox_authentication_api_models_request_start_authentication_by_user_request
