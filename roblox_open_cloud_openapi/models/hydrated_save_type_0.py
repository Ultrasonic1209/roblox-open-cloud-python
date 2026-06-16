from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.creator_store_asset_type_0 import CreatorStoreAssetType0


T = TypeVar("T", bound="HydratedSaveType0")


@_attrs_define
class HydratedSaveType0:
    """A save record, hydrated with the asset details.

    Attributes:
        owned (bool | Unset): Whether the asset is owned by the user.
        date_saved (datetime.datetime | Unset): Date the save was added.
        creator_store_asset (CreatorStoreAssetType0 | None | Unset): The asset that was saved.
    """

    owned: bool | Unset = UNSET
    date_saved: datetime.datetime | Unset = UNSET
    creator_store_asset: CreatorStoreAssetType0 | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.creator_store_asset_type_0 import CreatorStoreAssetType0

        owned = self.owned

        date_saved: str | Unset = UNSET
        if not isinstance(self.date_saved, Unset):
            date_saved = self.date_saved.isoformat()

        creator_store_asset: dict[str, Any] | None | Unset
        if isinstance(self.creator_store_asset, Unset):
            creator_store_asset = UNSET
        elif isinstance(self.creator_store_asset, CreatorStoreAssetType0):
            creator_store_asset = self.creator_store_asset.to_dict()
        else:
            creator_store_asset = self.creator_store_asset

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if owned is not UNSET:
            field_dict["owned"] = owned
        if date_saved is not UNSET:
            field_dict["dateSaved"] = date_saved
        if creator_store_asset is not UNSET:
            field_dict["creatorStoreAsset"] = creator_store_asset

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.creator_store_asset_type_0 import CreatorStoreAssetType0

        d = dict(src_dict)
        owned = d.pop("owned", UNSET)

        _date_saved = d.pop("dateSaved", UNSET)
        date_saved: datetime.datetime | Unset
        if isinstance(_date_saved, Unset):
            date_saved = UNSET
        else:
            date_saved = datetime.datetime.fromisoformat(_date_saved)

        def _parse_creator_store_asset(data: object) -> CreatorStoreAssetType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_creator_store_asset_type_0 = CreatorStoreAssetType0.from_dict(data)

                return componentsschemas_creator_store_asset_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreatorStoreAssetType0 | None | Unset, data)

        creator_store_asset = _parse_creator_store_asset(d.pop("creatorStoreAsset", UNSET))

        hydrated_save_type_0 = cls(
            owned=owned,
            date_saved=date_saved,
            creator_store_asset=creator_store_asset,
        )

        return hydrated_save_type_0
