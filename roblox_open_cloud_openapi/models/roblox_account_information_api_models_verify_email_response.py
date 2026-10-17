from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAccountInformationApiModelsVerifyEmailResponse")


@_attrs_define
class RobloxAccountInformationApiModelsVerifyEmailResponse:
    """The verify email response

    Attributes:
        verified_user_hat_asset_id (int | Unset): Free item id after email verification
    """

    verified_user_hat_asset_id: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        verified_user_hat_asset_id = self.verified_user_hat_asset_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if verified_user_hat_asset_id is not UNSET:
            field_dict["verifiedUserHatAssetId"] = verified_user_hat_asset_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        verified_user_hat_asset_id = d.pop("verifiedUserHatAssetId", UNSET)

        roblox_account_information_api_models_verify_email_response = cls(
            verified_user_hat_asset_id=verified_user_hat_asset_id,
        )

        return roblox_account_information_api_models_verify_email_response
