from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_item_configuration_api_models_response_category_node import (
        RobloxItemConfigurationApiModelsResponseCategoryNode,
    )


T = TypeVar("T", bound="RobloxItemConfigurationApiModelsResponseGetCategoriesResponse")


@_attrs_define
class RobloxItemConfigurationApiModelsResponseGetCategoriesResponse:
    """Defines the response model for GET v1/items/categories.

    Attributes:
        categories_version_id (str | Unset): The version id of the tree the categories were resolved from.
        categories (list[RobloxItemConfigurationApiModelsResponseCategoryNode] | Unset): The root category nodes of the
            hierarchy.
    """

    categories_version_id: str | Unset = UNSET
    categories: list[RobloxItemConfigurationApiModelsResponseCategoryNode] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        categories_version_id = self.categories_version_id

        categories: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.categories, Unset):
            categories = []
            for categories_item_data in self.categories:
                categories_item = categories_item_data.to_dict()
                categories.append(categories_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if categories_version_id is not UNSET:
            field_dict["categoriesVersionId"] = categories_version_id
        if categories is not UNSET:
            field_dict["categories"] = categories

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_item_configuration_api_models_response_category_node import (
            RobloxItemConfigurationApiModelsResponseCategoryNode,  # noqa: PLC0415
        )

        d = dict(src_dict)
        categories_version_id = d.pop("categoriesVersionId", UNSET)

        _categories = d.pop("categories", UNSET)
        categories: list[RobloxItemConfigurationApiModelsResponseCategoryNode] | Unset = UNSET
        if _categories is not UNSET:
            categories = []
            for categories_item_data in _categories:
                categories_item = RobloxItemConfigurationApiModelsResponseCategoryNode.from_dict(categories_item_data)

                categories.append(categories_item)

        roblox_item_configuration_api_models_response_get_categories_response = cls(
            categories_version_id=categories_version_id,
            categories=categories,
        )

        return roblox_item_configuration_api_models_response_get_categories_response
