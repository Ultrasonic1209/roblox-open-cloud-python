from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_web_assets_i_asset_item_error_custom_error_code import (
    RobloxWebAssetsIAssetItemErrorCustomErrorCode,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxWebAssetsIAssetItemError")


@_attrs_define
class RobloxWebAssetsIAssetItemError:
    """
    Attributes:
        code (int | Unset):
        message (str | Unset):
        custom_error_code (RobloxWebAssetsIAssetItemErrorCustomErrorCode | Unset): Custom error code for
            Roblox.Web.Assets.IAssetItemError ['UnknownError' = 0, 'NoPermissionToAsset' = 1, 'AssetPermissionCheckFailed' =
            2, 'NotAuthorizedForAgeRecommendation' = 3, 'AgeRecommendationCheckFailed' = 4,
            'InvalidPlaceRequestFromGameServer' = 5, 'BlockedAssetTypeRequestedFromInsertService' = 6,
            'BlockedAssetTypeRequestedFromGameServer' = 7, 'AssetTypeMismatch' = 8, 'MissingAssetTypeInRequestHeader' = 9,
            'AssetNotTrustedForPlace' = 10, 'NoAuthentication' = 11, 'AssetContentRepresentationBlockedDueToModeration' =
            12, 'AssetNotFound' = 13, 'AssetVersionNotFound' = 14, 'AssetContentRepresentationNotFound' = 15,
            'BlockedByAgeGeoRestriction' = 16, 'BlockedAssetTypeRequestedFromNonGameServer' = 17, 'AssetPendingReview' = 18,
            'NotApprovedForRequestor' = 19, 'NotApprovedByContentCompliance' = 20, 'AssetContentRepresentationGenerating' =
            21, 'AssetArchived' = 22, 'AssetUsageNotAllowed' = 23]
    """

    code: int | Unset = UNSET
    message: str | Unset = UNSET
    custom_error_code: RobloxWebAssetsIAssetItemErrorCustomErrorCode | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        custom_error_code: int | Unset = UNSET
        if not isinstance(self.custom_error_code, Unset):
            custom_error_code = self.custom_error_code.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if code is not UNSET:
            field_dict["Code"] = code
        if message is not UNSET:
            field_dict["Message"] = message
        if custom_error_code is not UNSET:
            field_dict["CustomErrorCode"] = custom_error_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("Code", UNSET)

        message = d.pop("Message", UNSET)

        _custom_error_code = d.pop("CustomErrorCode", UNSET)
        custom_error_code: RobloxWebAssetsIAssetItemErrorCustomErrorCode | Unset
        if isinstance(_custom_error_code, Unset):
            custom_error_code = UNSET
        else:
            custom_error_code = RobloxWebAssetsIAssetItemErrorCustomErrorCode(_custom_error_code)

        roblox_web_assets_i_asset_item_error = cls(
            code=code,
            message=message,
            custom_error_code=custom_error_code,
        )

        return roblox_web_assets_i_asset_item_error
