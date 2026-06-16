from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.preview_assets_model_type_0 import PreviewAssetsModelType0
    from ..models.social_link_model_type_0 import SocialLinkModelType0


T = TypeVar("T", bound="ToolboxServiceAssetType0")


@_attrs_define
class ToolboxServiceAssetType0:
    """Representation of an asset.

    Attributes:
        id (int | Unset): The unique identifier of the asset.
        name (None | str | Unset): The name of the asset.
        description (None | str | Unset): The description of the asset.
        asset_type_id (int | None | Unset): The type that the asset belongs to.
        social_links (list[None | SocialLinkModelType0] | None | Unset): The social links associated with the asset.
        preview_assets (None | PreviewAssetsModelType0 | Unset): The asset's preview asset ids grouped by asset type.
        create_time (datetime.datetime | None | Unset): The time the asset was created.
        update_time (datetime.datetime | None | Unset): The time the asset was last updated.
        creating_universe_id (int | None | Unset): Universe ID if the asset was created within a specific universe.
        category_path (None | str | Unset): Category Path of the asset, if it exists.
            e.g. "3d__characters"
    """

    id: int | Unset = UNSET
    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    asset_type_id: int | None | Unset = UNSET
    social_links: list[None | SocialLinkModelType0] | None | Unset = UNSET
    preview_assets: None | PreviewAssetsModelType0 | Unset = UNSET
    create_time: datetime.datetime | None | Unset = UNSET
    update_time: datetime.datetime | None | Unset = UNSET
    creating_universe_id: int | None | Unset = UNSET
    category_path: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.preview_assets_model_type_0 import PreviewAssetsModelType0
        from ..models.social_link_model_type_0 import SocialLinkModelType0

        id = self.id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        asset_type_id: int | None | Unset
        if isinstance(self.asset_type_id, Unset):
            asset_type_id = UNSET
        else:
            asset_type_id = self.asset_type_id

        social_links: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.social_links, Unset):
            social_links = UNSET
        elif isinstance(self.social_links, list):
            social_links = []
            for social_links_type_0_item_data in self.social_links:
                social_links_type_0_item: dict[str, Any] | None
                if isinstance(social_links_type_0_item_data, SocialLinkModelType0):
                    social_links_type_0_item = social_links_type_0_item_data.to_dict()
                else:
                    social_links_type_0_item = social_links_type_0_item_data
                social_links.append(social_links_type_0_item)

        else:
            social_links = self.social_links

        preview_assets: dict[str, Any] | None | Unset
        if isinstance(self.preview_assets, Unset):
            preview_assets = UNSET
        elif isinstance(self.preview_assets, PreviewAssetsModelType0):
            preview_assets = self.preview_assets.to_dict()
        else:
            preview_assets = self.preview_assets

        create_time: None | str | Unset
        if isinstance(self.create_time, Unset):
            create_time = UNSET
        elif isinstance(self.create_time, datetime.datetime):
            create_time = self.create_time.isoformat()
        else:
            create_time = self.create_time

        update_time: None | str | Unset
        if isinstance(self.update_time, Unset):
            update_time = UNSET
        elif isinstance(self.update_time, datetime.datetime):
            update_time = self.update_time.isoformat()
        else:
            update_time = self.update_time

        creating_universe_id: int | None | Unset
        if isinstance(self.creating_universe_id, Unset):
            creating_universe_id = UNSET
        else:
            creating_universe_id = self.creating_universe_id

        category_path: None | str | Unset
        if isinstance(self.category_path, Unset):
            category_path = UNSET
        else:
            category_path = self.category_path

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if asset_type_id is not UNSET:
            field_dict["assetTypeId"] = asset_type_id
        if social_links is not UNSET:
            field_dict["socialLinks"] = social_links
        if preview_assets is not UNSET:
            field_dict["previewAssets"] = preview_assets
        if create_time is not UNSET:
            field_dict["createTime"] = create_time
        if update_time is not UNSET:
            field_dict["updateTime"] = update_time
        if creating_universe_id is not UNSET:
            field_dict["creatingUniverseId"] = creating_universe_id
        if category_path is not UNSET:
            field_dict["categoryPath"] = category_path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.preview_assets_model_type_0 import PreviewAssetsModelType0
        from ..models.social_link_model_type_0 import SocialLinkModelType0

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_asset_type_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        asset_type_id = _parse_asset_type_id(d.pop("assetTypeId", UNSET))

        def _parse_social_links(data: object) -> list[None | SocialLinkModelType0] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                social_links_type_0 = []
                _social_links_type_0 = data
                for social_links_type_0_item_data in _social_links_type_0:

                    def _parse_social_links_type_0_item(data: object) -> None | SocialLinkModelType0:
                        if data is None:
                            return data
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_social_link_model_type_0 = SocialLinkModelType0.from_dict(data)

                            return componentsschemas_social_link_model_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(None | SocialLinkModelType0, data)

                    social_links_type_0_item = _parse_social_links_type_0_item(social_links_type_0_item_data)

                    social_links_type_0.append(social_links_type_0_item)

                return social_links_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[None | SocialLinkModelType0] | None | Unset, data)

        social_links = _parse_social_links(d.pop("socialLinks", UNSET))

        def _parse_preview_assets(data: object) -> None | PreviewAssetsModelType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_preview_assets_model_type_0 = PreviewAssetsModelType0.from_dict(data)

                return componentsschemas_preview_assets_model_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PreviewAssetsModelType0 | Unset, data)

        preview_assets = _parse_preview_assets(d.pop("previewAssets", UNSET))

        def _parse_create_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                create_time_type_0 = datetime.datetime.fromisoformat(data)

                return create_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        create_time = _parse_create_time(d.pop("createTime", UNSET))

        def _parse_update_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                update_time_type_0 = datetime.datetime.fromisoformat(data)

                return update_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        update_time = _parse_update_time(d.pop("updateTime", UNSET))

        def _parse_creating_universe_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        creating_universe_id = _parse_creating_universe_id(d.pop("creatingUniverseId", UNSET))

        def _parse_category_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category_path = _parse_category_path(d.pop("categoryPath", UNSET))

        toolbox_service_asset_type_0 = cls(
            id=id,
            name=name,
            description=description,
            asset_type_id=asset_type_id,
            social_links=social_links,
            preview_assets=preview_assets,
            create_time=create_time,
            update_time=update_time,
            creating_universe_id=creating_universe_id,
            category_path=category_path,
        )

        return toolbox_service_asset_type_0
