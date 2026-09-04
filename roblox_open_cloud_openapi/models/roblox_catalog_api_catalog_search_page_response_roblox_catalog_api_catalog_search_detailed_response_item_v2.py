from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_catalog_api_catalog_search_detailed_response_item_v2 import (
        RobloxCatalogApiCatalogSearchDetailedResponseItemV2,
    )
    from ..models.roblox_catalog_api_elasticsearch_debug_info import RobloxCatalogApiElasticsearchDebugInfo


T = TypeVar("T", bound="RobloxCatalogApiCatalogSearchPageResponseRobloxCatalogApiCatalogSearchDetailedResponseItemV2")


@_attrs_define
class RobloxCatalogApiCatalogSearchPageResponseRobloxCatalogApiCatalogSearchDetailedResponseItemV2:
    """ApiPageResponse for catalog search.

    Attributes:
        keyword (str | Unset): Keyword used for search query.
        elasticsearch_debug_info (RobloxCatalogApiElasticsearchDebugInfo | Unset):
        previous_page_cursor (str | Unset):
        next_page_cursor (str | Unset):
        data (list[RobloxCatalogApiCatalogSearchDetailedResponseItemV2] | Unset):
    """

    keyword: str | Unset = UNSET
    elasticsearch_debug_info: RobloxCatalogApiElasticsearchDebugInfo | Unset = UNSET
    previous_page_cursor: str | Unset = UNSET
    next_page_cursor: str | Unset = UNSET
    data: list[RobloxCatalogApiCatalogSearchDetailedResponseItemV2] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        keyword = self.keyword

        elasticsearch_debug_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.elasticsearch_debug_info, Unset):
            elasticsearch_debug_info = self.elasticsearch_debug_info.to_dict()

        previous_page_cursor = self.previous_page_cursor

        next_page_cursor = self.next_page_cursor

        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if keyword is not UNSET:
            field_dict["keyword"] = keyword
        if elasticsearch_debug_info is not UNSET:
            field_dict["elasticsearchDebugInfo"] = elasticsearch_debug_info
        if previous_page_cursor is not UNSET:
            field_dict["previousPageCursor"] = previous_page_cursor
        if next_page_cursor is not UNSET:
            field_dict["nextPageCursor"] = next_page_cursor
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_catalog_api_catalog_search_detailed_response_item_v2 import (
            RobloxCatalogApiCatalogSearchDetailedResponseItemV2,
        )
        from ..models.roblox_catalog_api_elasticsearch_debug_info import RobloxCatalogApiElasticsearchDebugInfo

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        keyword = d.pop("keyword", UNSET)

        _elasticsearch_debug_info = d.pop("elasticsearchDebugInfo", UNSET)
        elasticsearch_debug_info: RobloxCatalogApiElasticsearchDebugInfo | Unset
        if isinstance(_elasticsearch_debug_info, Unset):
            elasticsearch_debug_info = UNSET
        else:
            elasticsearch_debug_info = RobloxCatalogApiElasticsearchDebugInfo.from_dict(_elasticsearch_debug_info)

        previous_page_cursor = d.pop("previousPageCursor", UNSET)

        next_page_cursor = d.pop("nextPageCursor", UNSET)

        _data = d.pop("data", UNSET)
        data: list[RobloxCatalogApiCatalogSearchDetailedResponseItemV2] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = RobloxCatalogApiCatalogSearchDetailedResponseItemV2.from_dict(data_item_data)

                data.append(data_item)

        roblox_catalog_api_catalog_search_page_response_roblox_catalog_api_catalog_search_detailed_response_item_v2 = (
            cls(
                keyword=keyword,
                elasticsearch_debug_info=elasticsearch_debug_info,
                previous_page_cursor=previous_page_cursor,
                next_page_cursor=next_page_cursor,
                data=data,
            )
        )

        return (
            roblox_catalog_api_catalog_search_page_response_roblox_catalog_api_catalog_search_detailed_response_item_v2
        )
