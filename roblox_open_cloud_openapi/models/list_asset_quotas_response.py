from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asset_quota import AssetQuota


T = TypeVar("T", bound="ListAssetQuotasResponse")


@_attrs_define
class ListAssetQuotasResponse:
    """A list of AssetQuotas in the parent collection.

    Attributes:
        asset_quotas (list[AssetQuota] | Unset): The AssetQuotas from the specified User.
        next_page_token (str | Unset): A token that you can send as a `pageToken` parameter to retrieve the next
            page. If this field is omitted, there are no subsequent pages.
    """

    asset_quotas: list[AssetQuota] | Unset = UNSET
    next_page_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_quotas: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.asset_quotas, Unset):
            asset_quotas = []
            for asset_quotas_item_data in self.asset_quotas:
                asset_quotas_item = asset_quotas_item_data.to_dict()
                asset_quotas.append(asset_quotas_item)

        next_page_token = self.next_page_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asset_quotas is not UNSET:
            field_dict["assetQuotas"] = asset_quotas
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.asset_quota import AssetQuota

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _asset_quotas = d.pop("assetQuotas", UNSET)
        asset_quotas: list[AssetQuota] | Unset = UNSET
        if _asset_quotas is not UNSET:
            asset_quotas = []
            for asset_quotas_item_data in _asset_quotas:
                asset_quotas_item = AssetQuota.from_dict(asset_quotas_item_data)

                asset_quotas.append(asset_quotas_item)

        next_page_token = d.pop("nextPageToken", UNSET)

        list_asset_quotas_response = cls(
            asset_quotas=asset_quotas,
            next_page_token=next_page_token,
        )

        list_asset_quotas_response.additional_properties = d
        return list_asset_quotas_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
