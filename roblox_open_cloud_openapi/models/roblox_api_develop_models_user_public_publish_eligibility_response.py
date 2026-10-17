from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_api_develop_models_user_public_publish_eligibility_response_has_devex import (
    RobloxApiDevelopModelsUserPublicPublishEligibilityResponseHasDevex,
)
from ..models.roblox_api_develop_models_user_public_publish_eligibility_response_has_transactions import (
    RobloxApiDevelopModelsUserPublicPublishEligibilityResponseHasTransactions,
)
from ..models.roblox_api_develop_models_user_public_publish_eligibility_response_id_verified import (
    RobloxApiDevelopModelsUserPublicPublishEligibilityResponseIdVerified,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxApiDevelopModelsUserPublicPublishEligibilityResponse")


@_attrs_define
class RobloxApiDevelopModelsUserPublicPublishEligibilityResponse:
    """The result of various checks for a user's eligibility to publish a public universe.

    Attributes:
        is_eligible (bool | Unset): The overall result of eligibility.
        has_transactions (RobloxApiDevelopModelsUserPublicPublishEligibilityResponseHasTransactions | Unset): Whether
            user has spent any Robux since 1/1/25, including gift cards. ['Incomplete' = 0, 'NotRequired' = 1, 'Completed' =
            2]
        id_verified (RobloxApiDevelopModelsUserPublicPublishEligibilityResponseIdVerified | Unset): Whether user has
            completed ID Verification or not. ['Incomplete' = 0, 'NotRequired' = 1, 'Completed' = 2]
        has_devex (RobloxApiDevelopModelsUserPublicPublishEligibilityResponseHasDevex | Unset): Whether user is eligible
            for the developer exchange program. ['Incomplete' = 0, 'NotRequired' = 1, 'Completed' = 2]
    """

    is_eligible: bool | Unset = UNSET
    has_transactions: RobloxApiDevelopModelsUserPublicPublishEligibilityResponseHasTransactions | Unset = UNSET
    id_verified: RobloxApiDevelopModelsUserPublicPublishEligibilityResponseIdVerified | Unset = UNSET
    has_devex: RobloxApiDevelopModelsUserPublicPublishEligibilityResponseHasDevex | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        is_eligible = self.is_eligible

        has_transactions: int | Unset = UNSET
        if not isinstance(self.has_transactions, Unset):
            has_transactions = self.has_transactions.value

        id_verified: int | Unset = UNSET
        if not isinstance(self.id_verified, Unset):
            id_verified = self.id_verified.value

        has_devex: int | Unset = UNSET
        if not isinstance(self.has_devex, Unset):
            has_devex = self.has_devex.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if is_eligible is not UNSET:
            field_dict["isEligible"] = is_eligible
        if has_transactions is not UNSET:
            field_dict["hasTransactions"] = has_transactions
        if id_verified is not UNSET:
            field_dict["idVerified"] = id_verified
        if has_devex is not UNSET:
            field_dict["hasDevex"] = has_devex

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_eligible = d.pop("isEligible", UNSET)

        _has_transactions = d.pop("hasTransactions", UNSET)
        has_transactions: RobloxApiDevelopModelsUserPublicPublishEligibilityResponseHasTransactions | Unset
        if isinstance(_has_transactions, Unset):
            has_transactions = UNSET
        else:
            has_transactions = RobloxApiDevelopModelsUserPublicPublishEligibilityResponseHasTransactions(
                _has_transactions
            )

        _id_verified = d.pop("idVerified", UNSET)
        id_verified: RobloxApiDevelopModelsUserPublicPublishEligibilityResponseIdVerified | Unset
        if isinstance(_id_verified, Unset):
            id_verified = UNSET
        else:
            id_verified = RobloxApiDevelopModelsUserPublicPublishEligibilityResponseIdVerified(_id_verified)

        _has_devex = d.pop("hasDevex", UNSET)
        has_devex: RobloxApiDevelopModelsUserPublicPublishEligibilityResponseHasDevex | Unset
        if isinstance(_has_devex, Unset):
            has_devex = UNSET
        else:
            has_devex = RobloxApiDevelopModelsUserPublicPublishEligibilityResponseHasDevex(_has_devex)

        roblox_api_develop_models_user_public_publish_eligibility_response = cls(
            is_eligible=is_eligible,
            has_transactions=has_transactions,
            id_verified=id_verified,
            has_devex=has_devex,
        )

        return roblox_api_develop_models_user_public_publish_eligibility_response
