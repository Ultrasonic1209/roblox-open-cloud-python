from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAuthenticationApiModelsSignupResponse")


@_attrs_define
class RobloxAuthenticationApiModelsSignupResponse:
    """
    Attributes:
        user_id (int | Unset):
        starter_place_id (int | Unset):
        return_url (str | Unset):
        account_blob (str | Unset):
    """

    user_id: int | Unset = UNSET
    starter_place_id: int | Unset = UNSET
    return_url: str | Unset = UNSET
    account_blob: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        starter_place_id = self.starter_place_id

        return_url = self.return_url

        account_blob = self.account_blob

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if starter_place_id is not UNSET:
            field_dict["starterPlaceId"] = starter_place_id
        if return_url is not UNSET:
            field_dict["returnUrl"] = return_url
        if account_blob is not UNSET:
            field_dict["accountBlob"] = account_blob

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        user_id = d.pop("userId", UNSET)

        starter_place_id = d.pop("starterPlaceId", UNSET)

        return_url = d.pop("returnUrl", UNSET)

        account_blob = d.pop("accountBlob", UNSET)

        roblox_authentication_api_models_signup_response = cls(
            user_id=user_id,
            starter_place_id=starter_place_id,
            return_url=return_url,
            account_blob=account_blob,
        )

        return roblox_authentication_api_models_signup_response
