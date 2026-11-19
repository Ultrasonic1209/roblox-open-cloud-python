from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_item_configuration_api_check_item_upload_access_response_denied_reason import (
    RobloxItemConfigurationApiCheckItemUploadAccessResponseDeniedReason,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxItemConfigurationApiCheckItemUploadAccessResponse")


@_attrs_define
class RobloxItemConfigurationApiCheckItemUploadAccessResponse:
    """Defines the response model for the GET v1/collectibles/check-item-upload-access.

    Attributes:
        is_allowed (bool | Unset): Whether or not the access is allowed.
        denied_reason (RobloxItemConfigurationApiCheckItemUploadAccessResponseDeniedReason | Unset): Denied reason when
            the access is rejected.
            Can return the following denied reasons
            (MissingIdVerification, MissingTwoStepVerification, CreationAccessBlocked, MissingPremiumSubscriptionTier,
            MissingCicRoleset). ['Unknown' = 0, 'InvalidTargetType' = 1, 'FailedToFetchPublishingFee' = 2,
            'ServiceUnavailable' = 3, 'InvalidArgument' = 4, 'NotFound' = 5, 'FailedToGetCollectibleItemId' = 6,
            'FailedToGetCommissionRates' = 7, 'NullParameterRequest' = 8, 'PublishLimitExceeded' = 9,
            'AssetIsPendingValidation' = 10, 'AssetContainsInvalidContent' = 11, 'UserDoesNotHavePermissionsForGroupAsset' =
            12, 'AssetTypeCannotBeReleased' = 13, 'AssetIsPendingReview' = 14, 'AssetIsModerated' = 15, 'ItemIsReleased' =
            16, 'UserDoesNotHavePermissionToRelease' = 17, 'UserDoesNotOwnTheItem' = 18, 'ItemPriceTooLow' = 19,
            'ItemPriceTooHigh' = 20, 'InvalidAssetId' = 21, 'InvalidAgent' = 22, 'NoExperiencesListed' = 23,
            'NameIsModerated' = 24, 'DescriptionIsModerated' = 25, 'TextIsModerated' = 26, 'FailedToFilterText' = 27,
            'AssetAlreadyReleasedAsUnlimited' = 28, 'AssetInDelayedRelease' = 29, 'InvalidIdempotencyToken' = 30,
            'InvalidAgreedPublishingFee' = 31, 'GatewayCouldNotPublishItem' = 32, 'GroupAssetNotSupported' = 33,
            'CouldNotFindInitialUserAsset' = 34, 'InvalidQuantity' = 35, 'SaleLocationCurrentlyNotSupported' = 36,
            'InvalidCollectibleItemId' = 37, 'FailedToGetCollectibleItemInformation' = 38, 'GroupItemsNotSupported' = 39,
            'FailedToUpdateCollectibleItem' = 40, 'PublishQuotaUnavailable' = 41, 'FailedToFetchMarketplaceFee' = 42,
            'QuantityLimitCurrentlyNotSupported' = 43, 'InvalidQuantityLimit' = 44, 'ExactCopyOfAssetHasBeenPublished' = 45,
            'ItemIsInBundle' = 46, 'ResaleRestrictionCurrentlyNotSupported' = 47, 'InvalidResaleRestriction' = 48,
            'FailedToUpdateCollectibleDescription' = 49, 'InvalidBundleId' = 50, 'BundleTypeCannotBeReleased' = 51,
            'BundleIsModerated' = 52, 'BundleAlreadyReleasedAsUnlimited' = 53, 'BundlesGatewayUnexpectedErrorCode' = 54,
            'CissUnexpectedException' = 55, 'PublishingGatewayUnexpectedException' = 56, 'NonLimitedPublishingNotSupported'
            = 57, 'InvalidPublishingType' = 58, 'InvalidPriceOffset' = 59, 'InvalidMinimumPrice' = 60, 'InvalidSaleStatus' =
            61, 'InvalidPriceConfiguration' = 62, 'FailedToGetPriceConfiguration' = 63, 'CannotBeFree' = 64,
            'UnexpectedPlaceIds' = 65, 'MissingAuthenticatedUser' = 66, 'InvalidCreatorType' = 67,
            'PermissionProviderNotEnabled' = 68, 'InvalidGroupId' = 69, 'InsufficientRobux' = 70, 'ItemNotFound' = 71,
            'ItemIsModerated' = 72, 'ItemModerationUnknown' = 73, 'InvalidItemType' = 74, 'ItemHasArchivedDependencies' =
            75, 'ItemIsDelisted' = 76, 'ResellableCreationNotAllowed' = 77, 'PolicyError' = 78, 'InvalidSaleLocationUpdate'
            = 79, 'InExperienceCreationPublishingBlocked' = 80, 'TokenServiceUnexpectedException' = 81,
            'InvalidScheduledSaleStatus' = 82, 'InvalidCancelScheduledSaleStatus' = 83, 'ScheduledPublishingNotEnabled' =
            84, 'OnSaleTimeInThePast' = 85, 'OffSaleTimeInThePast' = 86, 'OnSaleTimeTooFarInTheFuture' = 87,
            'OffSaleTimeTooFarInTheFuture' = 88, 'OffSaleTimeBeforeOnSaleTime' = 89, 'ScheduledTimeOnSaleTooShort' = 90,
            'ScheduledTimeAlreadySet' = 91, 'ScheduledTimeCannotSetItemOnSaleAgain' = 92,
            'ScheduledTimeCannotSetItemOffSaleAgain' = 93, 'ActorIsModerated' = 94, 'CalendarQuotaExceeded' = 101,
            'CalendarQuotaUnavailable' = 102, 'PublishingGatewayMissingReason' = 103, 'PublishingGatewayUnexpectedReason' =
            104, 'PublishingGatewayUnexpectedAccessStatus' = 105, 'MissingIdVerification' = 106, 'CreationAccessBlocked' =
            107, 'MissingPremiumSubscriptionTier' = 108, 'GroupOwnerMissingPremiumSubscriptionTier' = 109,
            'MissingCicRoleset' = 110, 'AssetRestrictedByCommerce' = 111, 'DisallowedItemType' = 112, 'InvalidTargetId' =
            113, 'PriceFloorNotFound' = 114, 'UserNotAuthorizedForAction' = 115, 'FailedToGetRevenueSplit' = 116,
            'InvalidTransactionType' = 117, 'GrantedItemCannotBePublished' = 118, 'InvalidRentableType' = 119,
            'LimitedItemsCannotBeRentable' = 120, 'TooManyPurchaseAttempts' = 121, 'InvalidName' = 122, 'InvalidDescription'
            = 123, 'RequestCancelled' = 124, 'MissingTwoStepVerification' = 125, 'FreeAvatarSystemNotEnabled' = 126,
            'LookNotLinkedToUniverse' = 127, 'FreeAvatarMaxUniversesExceeded' = 128, 'LookItemCreatorMismatch' = 130,
            'LookContainsLimitedItem' = 131, 'LookItemCollectibleDelisted' = 133, 'BundleNotFound' = 134,
            'RestockingNotEnabled' = 135, 'ItemNotEligibleForRestocking' = 136, 'InvalidAgreedRestockingFee' = 137,
            'FailedToRestockCollectibleItem' = 138, 'InvalidRestockQuantity' = 139, 'FailedToFetchRestockingFee' = 140,
            'FailedToGetRestockEligibility' = 141, 'ResaleLockedAfterRestock' = 142, 'AiGeneratedItemPublishingBlocked' =
            143, 'FailedToGetAgreement' = 144, 'FailedToGetLicense' = 145, 'AgreementNotPublishable' = 146,
            'ResaleNotAllowedByLicense' = 147, 'ImmediateOnSaleNotAllowedForPendingAgreement' = 148,
            'OnSaleTimeOutsideAgreementWindow' = 149, 'OffSaleTimeOutsideAgreementWindow' = 150,
            'OffSaleTimeRequiredForAgreement' = 151]
    """

    is_allowed: bool | Unset = UNSET
    denied_reason: RobloxItemConfigurationApiCheckItemUploadAccessResponseDeniedReason | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        is_allowed = self.is_allowed

        denied_reason: int | Unset = UNSET
        if not isinstance(self.denied_reason, Unset):
            denied_reason = self.denied_reason.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if is_allowed is not UNSET:
            field_dict["isAllowed"] = is_allowed
        if denied_reason is not UNSET:
            field_dict["deniedReason"] = denied_reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_allowed = d.pop("isAllowed", UNSET)

        _denied_reason = d.pop("deniedReason", UNSET)
        denied_reason: RobloxItemConfigurationApiCheckItemUploadAccessResponseDeniedReason | Unset
        if isinstance(_denied_reason, Unset):
            denied_reason = UNSET
        else:
            denied_reason = RobloxItemConfigurationApiCheckItemUploadAccessResponseDeniedReason(_denied_reason)

        roblox_item_configuration_api_check_item_upload_access_response = cls(
            is_allowed=is_allowed,
            denied_reason=denied_reason,
        )

        return roblox_item_configuration_api_check_item_upload_access_response
