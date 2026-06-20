from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_two_step_verification_api_security_key_credential import (
        RobloxTwoStepVerificationApiSecurityKeyCredential,
    )


T = TypeVar("T", bound="RobloxTwoStepVerificationApiListSecurityKeyResponse")


@_attrs_define
class RobloxTwoStepVerificationApiListSecurityKeyResponse:
    """Response parameters for listing all credentials under a user.

    Attributes:
        credentials (list[RobloxTwoStepVerificationApiSecurityKeyCredential] | Unset): An array of credentials for a
            user.
    """

    credentials: list[RobloxTwoStepVerificationApiSecurityKeyCredential] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        credentials: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.credentials, Unset):
            credentials = []
            for credentials_item_data in self.credentials:
                credentials_item = credentials_item_data.to_dict()
                credentials.append(credentials_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if credentials is not UNSET:
            field_dict["credentials"] = credentials

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_two_step_verification_api_security_key_credential import (
            RobloxTwoStepVerificationApiSecurityKeyCredential,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _credentials = d.pop("credentials", UNSET)
        credentials: list[RobloxTwoStepVerificationApiSecurityKeyCredential] | Unset = UNSET
        if _credentials is not UNSET:
            credentials = []
            for credentials_item_data in _credentials:
                credentials_item = RobloxTwoStepVerificationApiSecurityKeyCredential.from_dict(credentials_item_data)

                credentials.append(credentials_item)

        roblox_two_step_verification_api_list_security_key_response = cls(
            credentials=credentials,
        )

        return roblox_two_step_verification_api_list_security_key_response
