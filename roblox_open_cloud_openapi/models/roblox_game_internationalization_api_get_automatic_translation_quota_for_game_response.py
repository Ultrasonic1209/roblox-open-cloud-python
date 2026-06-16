from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_game_internationalization_api_monthly_quota_model import (
        RobloxGameInternationalizationApiMonthlyQuotaModel,
    )
    from ..models.roblox_game_internationalization_api_quota_model import RobloxGameInternationalizationApiQuotaModel


T = TypeVar("T", bound="RobloxGameInternationalizationApiGetAutomaticTranslationQuotaForGameResponse")


@_attrs_define
class RobloxGameInternationalizationApiGetAutomaticTranslationQuotaForGameResponse:
    """A response model for getting the automatic translation quota info of a game.

    Attributes:
        monthly_quota (RobloxGameInternationalizationApiMonthlyQuotaModel | Unset):
        bank_quota (RobloxGameInternationalizationApiQuotaModel | Unset):
    """

    monthly_quota: RobloxGameInternationalizationApiMonthlyQuotaModel | Unset = UNSET
    bank_quota: RobloxGameInternationalizationApiQuotaModel | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        monthly_quota: dict[str, Any] | Unset = UNSET
        if not isinstance(self.monthly_quota, Unset):
            monthly_quota = self.monthly_quota.to_dict()

        bank_quota: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bank_quota, Unset):
            bank_quota = self.bank_quota.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if monthly_quota is not UNSET:
            field_dict["monthlyQuota"] = monthly_quota
        if bank_quota is not UNSET:
            field_dict["bankQuota"] = bank_quota

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_game_internationalization_api_monthly_quota_model import (
            RobloxGameInternationalizationApiMonthlyQuotaModel,
        )
        from ..models.roblox_game_internationalization_api_quota_model import (
            RobloxGameInternationalizationApiQuotaModel,
        )

        d = dict(src_dict)
        _monthly_quota = d.pop("monthlyQuota", UNSET)
        monthly_quota: RobloxGameInternationalizationApiMonthlyQuotaModel | Unset
        if isinstance(_monthly_quota, Unset):
            monthly_quota = UNSET
        else:
            monthly_quota = RobloxGameInternationalizationApiMonthlyQuotaModel.from_dict(_monthly_quota)

        _bank_quota = d.pop("bankQuota", UNSET)
        bank_quota: RobloxGameInternationalizationApiQuotaModel | Unset
        if isinstance(_bank_quota, Unset):
            bank_quota = UNSET
        else:
            bank_quota = RobloxGameInternationalizationApiQuotaModel.from_dict(_bank_quota)

        roblox_game_internationalization_api_get_automatic_translation_quota_for_game_response = cls(
            monthly_quota=monthly_quota,
            bank_quota=bank_quota,
        )

        return roblox_game_internationalization_api_get_automatic_translation_quota_for_game_response
