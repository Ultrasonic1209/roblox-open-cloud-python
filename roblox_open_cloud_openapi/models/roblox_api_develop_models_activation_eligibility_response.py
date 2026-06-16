from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_api_develop_models_activation_eligibility_response_allowed_audiences_item import (
    RobloxApiDevelopModelsActivationEligibilityResponseAllowedAudiencesItem,
)
from ..models.roblox_api_develop_models_activation_eligibility_response_creator_tier import (
    RobloxApiDevelopModelsActivationEligibilityResponseCreatorTier,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxApiDevelopModelsActivationEligibilityResponse")


@_attrs_define
class RobloxApiDevelopModelsActivationEligibilityResponse:
    """The result of various checks for a user's eligibility to activate a given universe from private to public.

    Attributes:
        is_eligible (bool | Unset):
        maturity_rated (bool | Unset): Whether the place has an active content maturity rating or not.
        is_user_eligible_for_public_publish (bool | Unset): isUserEligibleForPublicPublish
        remaining_public_publish_count (int | Unset): How many public publishes are remaining for the given user /
            group.
        is_public_publish (bool | Unset): Whether the universe is publicly published or not.
        is_publish_to_existing_universe (bool | Unset): Whether the universeId is within the tracked list of distinct
            allowed published universes.
        is_universe_select (bool | Unset): Whether the universe is in the "Select" program.
        creator_tier (RobloxApiDevelopModelsActivationEligibilityResponseCreatorTier | Unset): The creator tier of the
            universe owner. ['Invalid' = 0, 'Blocked' = 1, 'Private' = 2, 'Trusted' = 3, 'Everyone' = 4]
        allowed_audiences (list[RobloxApiDevelopModelsActivationEligibilityResponseAllowedAudiencesItem] | Unset):
            Audiences the universe is allowed to be published to.
    """

    is_eligible: bool | Unset = UNSET
    maturity_rated: bool | Unset = UNSET
    is_user_eligible_for_public_publish: bool | Unset = UNSET
    remaining_public_publish_count: int | Unset = UNSET
    is_public_publish: bool | Unset = UNSET
    is_publish_to_existing_universe: bool | Unset = UNSET
    is_universe_select: bool | Unset = UNSET
    creator_tier: RobloxApiDevelopModelsActivationEligibilityResponseCreatorTier | Unset = UNSET
    allowed_audiences: list[RobloxApiDevelopModelsActivationEligibilityResponseAllowedAudiencesItem] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        is_eligible = self.is_eligible

        maturity_rated = self.maturity_rated

        is_user_eligible_for_public_publish = self.is_user_eligible_for_public_publish

        remaining_public_publish_count = self.remaining_public_publish_count

        is_public_publish = self.is_public_publish

        is_publish_to_existing_universe = self.is_publish_to_existing_universe

        is_universe_select = self.is_universe_select

        creator_tier: int | Unset = UNSET
        if not isinstance(self.creator_tier, Unset):
            creator_tier = self.creator_tier.value

        allowed_audiences: list[int] | Unset = UNSET
        if not isinstance(self.allowed_audiences, Unset):
            allowed_audiences = []
            for allowed_audiences_item_data in self.allowed_audiences:
                allowed_audiences_item = allowed_audiences_item_data.value
                allowed_audiences.append(allowed_audiences_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if is_eligible is not UNSET:
            field_dict["isEligible"] = is_eligible
        if maturity_rated is not UNSET:
            field_dict["maturityRated"] = maturity_rated
        if is_user_eligible_for_public_publish is not UNSET:
            field_dict["isUserEligibleForPublicPublish"] = is_user_eligible_for_public_publish
        if remaining_public_publish_count is not UNSET:
            field_dict["remainingPublicPublishCount"] = remaining_public_publish_count
        if is_public_publish is not UNSET:
            field_dict["isPublicPublish"] = is_public_publish
        if is_publish_to_existing_universe is not UNSET:
            field_dict["isPublishToExistingUniverse"] = is_publish_to_existing_universe
        if is_universe_select is not UNSET:
            field_dict["isUniverseSelect"] = is_universe_select
        if creator_tier is not UNSET:
            field_dict["creatorTier"] = creator_tier
        if allowed_audiences is not UNSET:
            field_dict["allowedAudiences"] = allowed_audiences

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_eligible = d.pop("isEligible", UNSET)

        maturity_rated = d.pop("maturityRated", UNSET)

        is_user_eligible_for_public_publish = d.pop("isUserEligibleForPublicPublish", UNSET)

        remaining_public_publish_count = d.pop("remainingPublicPublishCount", UNSET)

        is_public_publish = d.pop("isPublicPublish", UNSET)

        is_publish_to_existing_universe = d.pop("isPublishToExistingUniverse", UNSET)

        is_universe_select = d.pop("isUniverseSelect", UNSET)

        _creator_tier = d.pop("creatorTier", UNSET)
        creator_tier: RobloxApiDevelopModelsActivationEligibilityResponseCreatorTier | Unset
        if isinstance(_creator_tier, Unset):
            creator_tier = UNSET
        else:
            creator_tier = RobloxApiDevelopModelsActivationEligibilityResponseCreatorTier(_creator_tier)

        _allowed_audiences = d.pop("allowedAudiences", UNSET)
        allowed_audiences: list[RobloxApiDevelopModelsActivationEligibilityResponseAllowedAudiencesItem] | Unset = UNSET
        if _allowed_audiences is not UNSET:
            allowed_audiences = []
            for allowed_audiences_item_data in _allowed_audiences:
                allowed_audiences_item = RobloxApiDevelopModelsActivationEligibilityResponseAllowedAudiencesItem(
                    allowed_audiences_item_data
                )

                allowed_audiences.append(allowed_audiences_item)

        roblox_api_develop_models_activation_eligibility_response = cls(
            is_eligible=is_eligible,
            maturity_rated=maturity_rated,
            is_user_eligible_for_public_publish=is_user_eligible_for_public_publish,
            remaining_public_publish_count=remaining_public_publish_count,
            is_public_publish=is_public_publish,
            is_publish_to_existing_universe=is_publish_to_existing_universe,
            is_universe_select=is_universe_select,
            creator_tier=creator_tier,
            allowed_audiences=allowed_audiences,
        )

        return roblox_api_develop_models_activation_eligibility_response
