from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxApiDevelopModelsPlaytesterEligibility")


@_attrs_define
class RobloxApiDevelopModelsPlaytesterEligibility:
    """Whether one candidate user can currently be added as a private playtester.

    Attributes:
        user_id (int | Unset): The candidate user id.
        is_eligible (bool | Unset): Whether the candidate is eligible.
    """

    user_id: int | Unset = UNSET
    is_eligible: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        is_eligible = self.is_eligible

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if is_eligible is not UNSET:
            field_dict["isEligible"] = is_eligible

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        user_id = d.pop("userId", UNSET)

        is_eligible = d.pop("isEligible", UNSET)

        roblox_api_develop_models_playtester_eligibility = cls(
            user_id=user_id,
            is_eligible=is_eligible,
        )

        return roblox_api_develop_models_playtester_eligibility
