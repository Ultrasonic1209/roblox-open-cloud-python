from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asset_version import AssetVersion


T = TypeVar("T", bound="ListAssetVersionsResponse")


@_attrs_define
class ListAssetVersionsResponse:
    """A list of AssetVersions in the parent collection.

    Attributes:
        asset_versions (list[AssetVersion] | None | Unset): The asset versions on this page. May be omitted when empty.
        next_page_token (None | str | Unset): Pass this token as `pageToken` to retrieve the next page. If omitted,
            there are no subsequent pages.
    """

    asset_versions: list[AssetVersion] | None | Unset = UNSET
    next_page_token: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        asset_versions: list[dict[str, Any]] | None | Unset
        if isinstance(self.asset_versions, Unset):
            asset_versions = UNSET
        elif isinstance(self.asset_versions, list):
            asset_versions = []
            for asset_versions_type_0_item_data in self.asset_versions:
                asset_versions_type_0_item = asset_versions_type_0_item_data.to_dict()
                asset_versions.append(asset_versions_type_0_item)

        else:
            asset_versions = self.asset_versions

        next_page_token: None | str | Unset
        if isinstance(self.next_page_token, Unset):
            next_page_token = UNSET
        else:
            next_page_token = self.next_page_token

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if asset_versions is not UNSET:
            field_dict["assetVersions"] = asset_versions
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.asset_version import AssetVersion  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_asset_versions(data: object) -> list[AssetVersion] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                asset_versions_type_0 = []
                _asset_versions_type_0 = data
                for asset_versions_type_0_item_data in _asset_versions_type_0:
                    asset_versions_type_0_item = AssetVersion.from_dict(asset_versions_type_0_item_data)

                    asset_versions_type_0.append(asset_versions_type_0_item)

                return asset_versions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AssetVersion] | None | Unset, data)

        asset_versions = _parse_asset_versions(d.pop("assetVersions", UNSET))

        def _parse_next_page_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_page_token = _parse_next_page_token(d.pop("nextPageToken", UNSET))

        list_asset_versions_response = cls(
            asset_versions=asset_versions,
            next_page_token=next_page_token,
        )

        return list_asset_versions_response
