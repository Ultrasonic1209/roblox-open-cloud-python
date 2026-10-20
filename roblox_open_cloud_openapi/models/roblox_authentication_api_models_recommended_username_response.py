from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAuthenticationApiModelsRecommendedUsernameResponse")


@_attrs_define
class RobloxAuthenticationApiModelsRecommendedUsernameResponse:
    """
    Attributes:
        did_generate_new_username (bool | Unset):
        suggested_usernames (list[str] | Unset):
    """

    did_generate_new_username: bool | Unset = UNSET
    suggested_usernames: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        did_generate_new_username = self.did_generate_new_username

        suggested_usernames: list[str] | Unset = UNSET
        if not isinstance(self.suggested_usernames, Unset):
            suggested_usernames = self.suggested_usernames

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if did_generate_new_username is not UNSET:
            field_dict["didGenerateNewUsername"] = did_generate_new_username
        if suggested_usernames is not UNSET:
            field_dict["suggestedUsernames"] = suggested_usernames

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        did_generate_new_username = d.pop("didGenerateNewUsername", UNSET)

        suggested_usernames = cast(list[str], d.pop("suggestedUsernames", UNSET))

        roblox_authentication_api_models_recommended_username_response = cls(
            did_generate_new_username=did_generate_new_username,
            suggested_usernames=suggested_usernames,
        )

        return roblox_authentication_api_models_recommended_username_response
