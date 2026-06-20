from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_publish_api_asset_quota import RobloxPublishApiAssetQuota


T = TypeVar("T", bound="RobloxPublishApiAssetQuotasResponse")


@_attrs_define
class RobloxPublishApiAssetQuotasResponse:
    """Response model for asset quotas.

    Attributes:
        quotas (list[RobloxPublishApiAssetQuota] | Unset): A list of quotas.
    """

    quotas: list[RobloxPublishApiAssetQuota] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        quotas: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.quotas, Unset):
            quotas = []
            for quotas_item_data in self.quotas:
                quotas_item = quotas_item_data.to_dict()
                quotas.append(quotas_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if quotas is not UNSET:
            field_dict["quotas"] = quotas

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_publish_api_asset_quota import RobloxPublishApiAssetQuota

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _quotas = d.pop("quotas", UNSET)
        quotas: list[RobloxPublishApiAssetQuota] | Unset = UNSET
        if _quotas is not UNSET:
            quotas = []
            for quotas_item_data in _quotas:
                quotas_item = RobloxPublishApiAssetQuota.from_dict(quotas_item_data)

                quotas.append(quotas_item)

        roblox_publish_api_asset_quotas_response = cls(
            quotas=quotas,
        )

        return roblox_publish_api_asset_quotas_response
