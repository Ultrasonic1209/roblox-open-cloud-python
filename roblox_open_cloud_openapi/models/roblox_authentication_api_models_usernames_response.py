from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAuthenticationApiModelsUsernamesResponse")


@_attrs_define
class RobloxAuthenticationApiModelsUsernamesResponse:
    """
    Attributes:
        usernames (list[str] | Unset):
    """

    usernames: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        usernames: list[str] | Unset = UNSET
        if not isinstance(self.usernames, Unset):
            usernames = self.usernames

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if usernames is not UNSET:
            field_dict["usernames"] = usernames

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        usernames = cast(list[str], d.pop("usernames", UNSET))

        roblox_authentication_api_models_usernames_response = cls(
            usernames=usernames,
        )

        return roblox_authentication_api_models_usernames_response
