from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_economy_api_models_user_group_payout_eligibility_response_model_users_group_payout_eligibility import (
        RobloxEconomyApiModelsUserGroupPayoutEligibilityResponseModelUsersGroupPayoutEligibility,
    )


T = TypeVar("T", bound="RobloxEconomyApiModelsUserGroupPayoutEligibilityResponseModel")


@_attrs_define
class RobloxEconomyApiModelsUserGroupPayoutEligibilityResponseModel:
    """The response model for M:Roblox.Economy.Api.Controllers.V1.GroupPayoutsController.GetUserGroupPayoutEligibility(Syst
    em.Int64,System.Collections.Generic.ICollection{System.Int64},System.Threading.CancellationToken)

        Attributes:
            users_group_payout_eligibility
                (RobloxEconomyApiModelsUserGroupPayoutEligibilityResponseModelUsersGroupPayoutEligibility | Unset): Gets the
                dictionary of (userId, groupPayoutEligibility) mapping.
    """

    users_group_payout_eligibility: (
        RobloxEconomyApiModelsUserGroupPayoutEligibilityResponseModelUsersGroupPayoutEligibility | Unset
    ) = UNSET

    def to_dict(self) -> dict[str, Any]:
        users_group_payout_eligibility: dict[str, Any] | Unset = UNSET
        if not isinstance(self.users_group_payout_eligibility, Unset):
            users_group_payout_eligibility = self.users_group_payout_eligibility.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if users_group_payout_eligibility is not UNSET:
            field_dict["usersGroupPayoutEligibility"] = users_group_payout_eligibility

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_economy_api_models_user_group_payout_eligibility_response_model_users_group_payout_eligibility import (
            RobloxEconomyApiModelsUserGroupPayoutEligibilityResponseModelUsersGroupPayoutEligibility,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _users_group_payout_eligibility = d.pop("usersGroupPayoutEligibility", UNSET)
        users_group_payout_eligibility: (
            RobloxEconomyApiModelsUserGroupPayoutEligibilityResponseModelUsersGroupPayoutEligibility | Unset
        )
        if isinstance(_users_group_payout_eligibility, Unset):
            users_group_payout_eligibility = UNSET
        else:
            users_group_payout_eligibility = (
                RobloxEconomyApiModelsUserGroupPayoutEligibilityResponseModelUsersGroupPayoutEligibility.from_dict(
                    _users_group_payout_eligibility
                )
            )

        roblox_economy_api_models_user_group_payout_eligibility_response_model = cls(
            users_group_payout_eligibility=users_group_payout_eligibility,
        )

        return roblox_economy_api_models_user_group_payout_eligibility_response_model
