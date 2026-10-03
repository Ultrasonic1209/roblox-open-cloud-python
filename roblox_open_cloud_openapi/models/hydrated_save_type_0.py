from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.creator_store_asset_type_0 import CreatorStoreAssetType0


T = TypeVar("T", bound="HydratedSaveType0")


@_attrs_define
class HydratedSaveType0:
    """A save record, hydrated with the asset details.

    Attributes:
        owned (bool): Whether the asset is owned by the user.
        date_saved (datetime.datetime): Date the save was added.
        creator_store_asset (CreatorStoreAssetType0 | None): The asset that was saved.
    """

    owned: bool
    date_saved: datetime.datetime
    creator_store_asset: CreatorStoreAssetType0 | None

    def to_dict(self) -> dict[str, Any]:
        from ..models.creator_store_asset_type_0 import CreatorStoreAssetType0

        owned = self.owned

        date_saved = self.date_saved.isoformat()

        creator_store_asset: dict[str, Any] | None
        if isinstance(self.creator_store_asset, CreatorStoreAssetType0):
            creator_store_asset = self.creator_store_asset.to_dict()
        else:
            creator_store_asset = self.creator_store_asset

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "owned": owned,
                "dateSaved": date_saved,
                "creatorStoreAsset": creator_store_asset,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.creator_store_asset_type_0 import CreatorStoreAssetType0

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        owned = d.pop("owned")

        date_saved = datetime.datetime.fromisoformat(d.pop("dateSaved"))

        def _parse_creator_store_asset(data: object) -> CreatorStoreAssetType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_creator_store_asset_type_0 = CreatorStoreAssetType0.from_dict(data)

                return componentsschemas_creator_store_asset_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreatorStoreAssetType0 | None, data)

        creator_store_asset = _parse_creator_store_asset(d.pop("creatorStoreAsset"))

        hydrated_save_type_0 = cls(
            owned=owned,
            date_saved=date_saved,
            creator_store_asset=creator_store_asset,
        )

        return hydrated_save_type_0
