from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asset_quota import AssetQuota


T = TypeVar("T", bound="ListAssetQuotasResponse")


@_attrs_define
class ListAssetQuotasResponse:
    """A list of AssetQuotas in the parent collection.

    Attributes:
        asset_quotas (list[AssetQuota] | None | Unset): The AssetQuotas from the specified User.
        next_page_token (None | str | Unset): A token that you can send as a `pageToken` parameter to retrieve the next
            page. If this field is omitted, there are no subsequent pages.
    """

    asset_quotas: list[AssetQuota] | None | Unset = UNSET
    next_page_token: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        asset_quotas: list[dict[str, Any]] | None | Unset
        if isinstance(self.asset_quotas, Unset):
            asset_quotas = UNSET
        elif isinstance(self.asset_quotas, list):
            asset_quotas = []
            for asset_quotas_type_0_item_data in self.asset_quotas:
                asset_quotas_type_0_item = asset_quotas_type_0_item_data.to_dict()
                asset_quotas.append(asset_quotas_type_0_item)

        else:
            asset_quotas = self.asset_quotas

        next_page_token: None | str | Unset
        if isinstance(self.next_page_token, Unset):
            next_page_token = UNSET
        else:
            next_page_token = self.next_page_token

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if asset_quotas is not UNSET:
            field_dict["assetQuotas"] = asset_quotas
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.asset_quota import AssetQuota  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_asset_quotas(data: object) -> list[AssetQuota] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                asset_quotas_type_0 = []
                _asset_quotas_type_0 = data
                for asset_quotas_type_0_item_data in _asset_quotas_type_0:
                    asset_quotas_type_0_item = AssetQuota.from_dict(asset_quotas_type_0_item_data)

                    asset_quotas_type_0.append(asset_quotas_type_0_item)

                return asset_quotas_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AssetQuota] | None | Unset, data)

        asset_quotas = _parse_asset_quotas(d.pop("assetQuotas", UNSET))

        def _parse_next_page_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_page_token = _parse_next_page_token(d.pop("nextPageToken", UNSET))

        list_asset_quotas_response = cls(
            asset_quotas=asset_quotas,
            next_page_token=next_page_token,
        )

        return list_asset_quotas_response
