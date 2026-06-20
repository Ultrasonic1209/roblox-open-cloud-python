from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_games_api_models_response_playability_status_response_playability_status import (
    RobloxGamesApiModelsResponsePlayabilityStatusResponsePlayabilityStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_games_api_models_response_playable_ux_treatment import (
        RobloxGamesApiModelsResponsePlayableUxTreatment,
    )
    from ..models.roblox_games_api_models_response_upsell_ux_treatment import (
        RobloxGamesApiModelsResponseUpsellUxTreatment,
    )


T = TypeVar("T", bound="RobloxGamesApiModelsResponsePlayabilityStatusResponse")


@_attrs_define
class RobloxGamesApiModelsResponsePlayabilityStatusResponse:
    """Response model for getting a universe's playability status for a user

    Attributes:
        playability_status (RobloxGamesApiModelsResponsePlayabilityStatusResponsePlayabilityStatus | Unset): The actual
            playability status of the universe including the reason if unplayable ['UnplayableOtherReason' = 0, 'Playable' =
            1, 'GuestProhibited' = 2, 'GameUnapproved' = 3, 'IncorrectConfiguration' = 4, 'UniverseRootPlaceIsPrivate' = 5,
            'InsufficientPermissionFriendsOnly' = 6, 'InsufficientPermissionGroupOnly' = 7, 'DeviceRestricted' = 8,
            'UnderReview' = 9, 'PurchaseRequired' = 10, 'AccountRestricted' = 11, 'TemporarilyUnavailable' = 12,
            'PlaceHasNoPublishedVersion' = 13, 'ComplianceBlocked' = 14, 'ContextualPlayabilityRegionalAvailability' = 15,
            'ContextualPlayabilityRegionalCompliance' = 16, 'ContextualPlayabilityAgeRecommendationParentalControls' = 17,
            'ContextualPlayabilityExperienceBlockedParentalControls' = 18, 'ContextualPlayabilityAgeGated' = 19,
            'ContextualPlayabilityUnverifiedSeventeenPlusUser' = 20, 'FiatPurchaseRequired' = 21,
            'FiatPurchaseDeviceRestricted' = 22, 'ContextualPlayabilityUnrated' = 23,
            'ContextualPlayabilityAgeGatedByDescriptor' = 24, 'ContextualPlayabilityGeneral' = 25,
            'ContextualPlayabilityAgeCheckRequired' = 26, 'ContextualPlayabilityRequireParentApproval' = 27,
            'ContextualPlayabilityCoreGated' = 28]
        is_playable (bool | Unset): Whether or not the universe is playable for the user
        universe_id (int | Unset): The universeId of the requested universe to help with batching requests
        unplayable_display_text (str | Unset): Localized display text explaining why unplayable
        playable_ux_treatment (RobloxGamesApiModelsResponsePlayableUxTreatment | Unset):
        upsell_ux_treatment (RobloxGamesApiModelsResponseUpsellUxTreatment | Unset): Upsell UX treatment metadata
            appended to a playability response when an experience is
            currently playable but will be restricted under upcoming Roblox-Core content rules.
            Mirrors the existing Roblox.Games.Api.Models.Response.PlayableUxTreatment contract intentionally so client
            rendering can be unified.
    """

    playability_status: RobloxGamesApiModelsResponsePlayabilityStatusResponsePlayabilityStatus | Unset = UNSET
    is_playable: bool | Unset = UNSET
    universe_id: int | Unset = UNSET
    unplayable_display_text: str | Unset = UNSET
    playable_ux_treatment: RobloxGamesApiModelsResponsePlayableUxTreatment | Unset = UNSET
    upsell_ux_treatment: RobloxGamesApiModelsResponseUpsellUxTreatment | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        playability_status: int | Unset = UNSET
        if not isinstance(self.playability_status, Unset):
            playability_status = self.playability_status.value

        is_playable = self.is_playable

        universe_id = self.universe_id

        unplayable_display_text = self.unplayable_display_text

        playable_ux_treatment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.playable_ux_treatment, Unset):
            playable_ux_treatment = self.playable_ux_treatment.to_dict()

        upsell_ux_treatment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.upsell_ux_treatment, Unset):
            upsell_ux_treatment = self.upsell_ux_treatment.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if playability_status is not UNSET:
            field_dict["playabilityStatus"] = playability_status
        if is_playable is not UNSET:
            field_dict["isPlayable"] = is_playable
        if universe_id is not UNSET:
            field_dict["universeId"] = universe_id
        if unplayable_display_text is not UNSET:
            field_dict["unplayableDisplayText"] = unplayable_display_text
        if playable_ux_treatment is not UNSET:
            field_dict["playableUxTreatment"] = playable_ux_treatment
        if upsell_ux_treatment is not UNSET:
            field_dict["upsellUxTreatment"] = upsell_ux_treatment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_games_api_models_response_playable_ux_treatment import (
            RobloxGamesApiModelsResponsePlayableUxTreatment,
        )
        from ..models.roblox_games_api_models_response_upsell_ux_treatment import (
            RobloxGamesApiModelsResponseUpsellUxTreatment,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _playability_status = d.pop("playabilityStatus", UNSET)
        playability_status: RobloxGamesApiModelsResponsePlayabilityStatusResponsePlayabilityStatus | Unset
        if isinstance(_playability_status, Unset):
            playability_status = UNSET
        else:
            playability_status = RobloxGamesApiModelsResponsePlayabilityStatusResponsePlayabilityStatus(
                _playability_status
            )

        is_playable = d.pop("isPlayable", UNSET)

        universe_id = d.pop("universeId", UNSET)

        unplayable_display_text = d.pop("unplayableDisplayText", UNSET)

        _playable_ux_treatment = d.pop("playableUxTreatment", UNSET)
        playable_ux_treatment: RobloxGamesApiModelsResponsePlayableUxTreatment | Unset
        if isinstance(_playable_ux_treatment, Unset):
            playable_ux_treatment = UNSET
        else:
            playable_ux_treatment = RobloxGamesApiModelsResponsePlayableUxTreatment.from_dict(_playable_ux_treatment)

        _upsell_ux_treatment = d.pop("upsellUxTreatment", UNSET)
        upsell_ux_treatment: RobloxGamesApiModelsResponseUpsellUxTreatment | Unset
        if isinstance(_upsell_ux_treatment, Unset):
            upsell_ux_treatment = UNSET
        else:
            upsell_ux_treatment = RobloxGamesApiModelsResponseUpsellUxTreatment.from_dict(_upsell_ux_treatment)

        roblox_games_api_models_response_playability_status_response = cls(
            playability_status=playability_status,
            is_playable=is_playable,
            universe_id=universe_id,
            unplayable_display_text=unplayable_display_text,
            playable_ux_treatment=playable_ux_treatment,
            upsell_ux_treatment=upsell_ux_treatment,
        )

        return roblox_games_api_models_response_playability_status_response
