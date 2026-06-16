from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.roblox_api_develop_models_universe_moderation_policy_status_region import (
    RobloxApiDevelopModelsUniverseModerationPolicyStatusRegion,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxApiDevelopModelsUniverseModerationPolicyStatus")


@_attrs_define
class RobloxApiDevelopModelsUniverseModerationPolicyStatus:
    """Represents a universe moderation policy status

    Attributes:
        region (RobloxApiDevelopModelsUniverseModerationPolicyStatusRegion | Unset): The region policy label ['Unknown'
            = 0, 'China' = 1]
        status (str | Unset): The status of the universe
    """

    region: RobloxApiDevelopModelsUniverseModerationPolicyStatusRegion | Unset = UNSET
    status: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        region: int | Unset = UNSET
        if not isinstance(self.region, Unset):
            region = self.region.value

        status = self.status

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if region is not UNSET:
            field_dict["region"] = region
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _region = d.pop("region", UNSET)
        region: RobloxApiDevelopModelsUniverseModerationPolicyStatusRegion | Unset
        if isinstance(_region, Unset):
            region = UNSET
        else:
            region = RobloxApiDevelopModelsUniverseModerationPolicyStatusRegion(_region)

        status = d.pop("status", UNSET)

        roblox_api_develop_models_universe_moderation_policy_status = cls(
            region=region,
            status=status,
        )

        return roblox_api_develop_models_universe_moderation_policy_status
