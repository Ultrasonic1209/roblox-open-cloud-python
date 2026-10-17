from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxUsersApiUserAgeBracketResponse")


@_attrs_define
class RobloxUsersApiUserAgeBracketResponse:
    """A user age bracket response model.

    Attributes:
        age_bracket (int | Unset): The age bracket of the user.
    """

    age_bracket: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        age_bracket = self.age_bracket

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if age_bracket is not UNSET:
            field_dict["ageBracket"] = age_bracket

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        age_bracket = d.pop("ageBracket", UNSET)

        roblox_users_api_user_age_bracket_response = cls(
            age_bracket=age_bracket,
        )

        return roblox_users_api_user_age_bracket_response
