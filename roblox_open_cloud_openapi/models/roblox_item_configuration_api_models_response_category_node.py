from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxItemConfigurationApiModelsResponseCategoryNode")


@_attrs_define
class RobloxItemConfigurationApiModelsResponseCategoryNode:
    """A single node in the category hierarchy returned by
    Roblox.ItemConfiguration.Api.Models.Response.GetCategoriesResponse.

        Attributes:
            web_stable_id (str | Unset): The public, tree-stable identifier for the node.
                Callers pass this back as the category filter; it is expanded to leaf uuids server-side.
            id (str | Unset): The internal taxonomy node identifier (Synapse branch id or leaf label id).
            name (str | Unset): The canonical (English) display name of the category.
            is_publishable (bool | Unset): Whether the category is publishable by UGC creators.
            asset_type_ids (list[int] | Unset): Default asset type ids backing this node.
            bundle_type_ids (list[int] | Unset): Default bundle type ids backing this node.
            children (list[RobloxItemConfigurationApiModelsResponseCategoryNode] | Unset): Child category nodes; empty for
                leaves.
    """

    web_stable_id: str | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    is_publishable: bool | Unset = UNSET
    asset_type_ids: list[int] | Unset = UNSET
    bundle_type_ids: list[int] | Unset = UNSET
    children: list[RobloxItemConfigurationApiModelsResponseCategoryNode] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        web_stable_id = self.web_stable_id

        id = self.id

        name = self.name

        is_publishable = self.is_publishable

        asset_type_ids: list[int] | Unset = UNSET
        if not isinstance(self.asset_type_ids, Unset):
            asset_type_ids = self.asset_type_ids

        bundle_type_ids: list[int] | Unset = UNSET
        if not isinstance(self.bundle_type_ids, Unset):
            bundle_type_ids = self.bundle_type_ids

        children: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.children, Unset):
            children = []
            for children_item_data in self.children:
                children_item = children_item_data.to_dict()
                children.append(children_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if web_stable_id is not UNSET:
            field_dict["webStableId"] = web_stable_id
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if is_publishable is not UNSET:
            field_dict["isPublishable"] = is_publishable
        if asset_type_ids is not UNSET:
            field_dict["assetTypeIds"] = asset_type_ids
        if bundle_type_ids is not UNSET:
            field_dict["bundleTypeIds"] = bundle_type_ids
        if children is not UNSET:
            field_dict["children"] = children

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        web_stable_id = d.pop("webStableId", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        is_publishable = d.pop("isPublishable", UNSET)

        asset_type_ids = cast(list[int], d.pop("assetTypeIds", UNSET))

        bundle_type_ids = cast(list[int], d.pop("bundleTypeIds", UNSET))

        _children = d.pop("children", UNSET)
        children: list[RobloxItemConfigurationApiModelsResponseCategoryNode] | Unset = UNSET
        if _children is not UNSET:
            children = []
            for children_item_data in _children:
                children_item = RobloxItemConfigurationApiModelsResponseCategoryNode.from_dict(children_item_data)

                children.append(children_item)

        roblox_item_configuration_api_models_response_category_node = cls(
            web_stable_id=web_stable_id,
            id=id,
            name=name,
            is_publishable=is_publishable,
            asset_type_ids=asset_type_ids,
            bundle_type_ids=bundle_type_ids,
            children=children,
        )

        return roblox_item_configuration_api_models_response_category_node
