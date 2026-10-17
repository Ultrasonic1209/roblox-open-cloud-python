from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxUsersApiUserCountryCodeResponse")


@_attrs_define
class RobloxUsersApiUserCountryCodeResponse:
    """A user country code response model.

    Attributes:
        country_code (str | Unset): The country code of the user.
    """

    country_code: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        country_code = self.country_code

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        country_code = d.pop("countryCode", UNSET)

        roblox_users_api_user_country_code_response = cls(
            country_code=country_code,
        )

        return roblox_users_api_user_country_code_response
