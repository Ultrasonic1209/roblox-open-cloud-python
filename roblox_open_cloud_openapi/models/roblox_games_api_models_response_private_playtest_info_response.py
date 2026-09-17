from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_games_api_models_response_private_playtest_info_response_playability_status import (
    RobloxGamesApiModelsResponsePrivatePlaytestInfoResponsePlayabilityStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxGamesApiModelsResponsePrivatePlaytestInfoResponse")


@_attrs_define
class RobloxGamesApiModelsResponsePrivatePlaytestInfoResponse:
    """Private playtest eligibility for the authenticated user.

    Attributes:
        is_playable (bool | Unset): Whether the user is eligible to play as a private playtester.
        playability_status (RobloxGamesApiModelsResponsePrivatePlaytestInfoResponsePlayabilityStatus | Unset): The
            private playtest eligibility status. ['UnplayableOtherReason' = 0, 'Playable' = 1, 'GuestProhibited' = 2,
            'GameUnapproved' = 3, 'IncorrectConfiguration' = 4, 'UniverseRootPlaceIsPrivate' = 5,
            'InsufficientPermissionFriendsOnly' = 6, 'InsufficientPermissionGroupOnly' = 7, 'DeviceRestricted' = 8,
            'UnderReview' = 9, 'PurchaseRequired' = 10, 'AccountRestricted' = 11, 'TemporarilyUnavailable' = 12,
            'PlaceHasNoPublishedVersion' = 13, 'ComplianceBlocked' = 14, 'ContextualPlayabilityRegionalAvailability' = 15,
            'ContextualPlayabilityRegionalCompliance' = 16, 'ContextualPlayabilityAgeRecommendationParentalControls' = 17,
            'ContextualPlayabilityExperienceBlockedParentalControls' = 18, 'ContextualPlayabilityAgeGated' = 19,
            'ContextualPlayabilityUnverifiedSeventeenPlusUser' = 20, 'FiatPurchaseRequired' = 21,
            'FiatPurchaseDeviceRestricted' = 22, 'ContextualPlayabilityUnrated' = 23,
            'ContextualPlayabilityAgeGatedByDescriptor' = 24, 'ContextualPlayabilityGeneral' = 25,
            'ContextualPlayabilityAgeCheckRequired' = 26, 'ContextualPlayabilityRequireParentApproval' = 27,
            'ContextualPlayabilityCoreGated' = 28, 'ContextualPlayabilityTrustedFriendRequired' = 29,
            'PlusSubscriptionRequired' = 30, 'ContextualPlayabilityPlaytestDisabled' = 31,
            'InsufficientPermissionEditorsOnly' = 32]
    """

    is_playable: bool | Unset = UNSET
    playability_status: RobloxGamesApiModelsResponsePrivatePlaytestInfoResponsePlayabilityStatus | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        is_playable = self.is_playable

        playability_status: int | Unset = UNSET
        if not isinstance(self.playability_status, Unset):
            playability_status = self.playability_status.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if is_playable is not UNSET:
            field_dict["isPlayable"] = is_playable
        if playability_status is not UNSET:
            field_dict["playabilityStatus"] = playability_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        is_playable = d.pop("isPlayable", UNSET)

        _playability_status = d.pop("playabilityStatus", UNSET)
        playability_status: RobloxGamesApiModelsResponsePrivatePlaytestInfoResponsePlayabilityStatus | Unset
        if isinstance(_playability_status, Unset):
            playability_status = UNSET
        else:
            playability_status = RobloxGamesApiModelsResponsePrivatePlaytestInfoResponsePlayabilityStatus(
                _playability_status
            )

        roblox_games_api_models_response_private_playtest_info_response = cls(
            is_playable=is_playable,
            playability_status=playability_status,
        )

        return roblox_games_api_models_response_private_playtest_info_response
