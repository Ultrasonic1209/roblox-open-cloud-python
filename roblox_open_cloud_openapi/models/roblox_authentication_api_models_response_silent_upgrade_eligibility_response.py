from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxAuthenticationApiModelsResponseSilentUpgradeEligibilityResponse")


@_attrs_define
class RobloxAuthenticationApiModelsResponseSilentUpgradeEligibilityResponse:
    """
    Attributes:
        su_eligibility (bool | Unset):
    """

    su_eligibility: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        su_eligibility = self.su_eligibility

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if su_eligibility is not UNSET:
            field_dict["suEligibility"] = su_eligibility

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        su_eligibility = d.pop("suEligibility", UNSET)

        roblox_authentication_api_models_response_silent_upgrade_eligibility_response = cls(
            su_eligibility=su_eligibility,
        )

        return roblox_authentication_api_models_response_silent_upgrade_eligibility_response
