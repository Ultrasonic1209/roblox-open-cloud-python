from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAuthenticationApiModelsRequestListPasskeysRequest")


@_attrs_define
class RobloxAuthenticationApiModelsRequestListPasskeysRequest:
    """
    Attributes:
        all_ (bool | Unset):
    """

    all_: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        all_ = self.all_

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if all_ is not UNSET:
            field_dict["all"] = all_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        all_ = d.pop("all", UNSET)

        roblox_authentication_api_models_request_list_passkeys_request = cls(
            all_=all_,
        )

        return roblox_authentication_api_models_request_list_passkeys_request
