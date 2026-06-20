from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxCatalogApiElasticsearchDebugInfo")


@_attrs_define
class RobloxCatalogApiElasticsearchDebugInfo:
    """
    Attributes:
        elasticsearch_query (str | Unset): Gets or sets the nest query that resulted from the operation.
        is_from_cache (bool | Unset): Gets or sets if the results were returned from cache.
        index_name (str | Unset): Gets or sets the index name.
        is_terminated_early (bool | Unset): Gets or sets if the query was Terminated Early.
        is_force_termination_enabled_by_request (bool | Unset): Gets or sets if Force Termination was Enabled in the
            Request.
        search_result_data_source (str | Unset): Gets or sets the search result data source.
        search_result_relevance_score (str | Unset): Gets or sets the search result relevance score.
        search_result_engagement_score (str | Unset): Gets or sets the search result engagement score.
    """

    elasticsearch_query: str | Unset = UNSET
    is_from_cache: bool | Unset = UNSET
    index_name: str | Unset = UNSET
    is_terminated_early: bool | Unset = UNSET
    is_force_termination_enabled_by_request: bool | Unset = UNSET
    search_result_data_source: str | Unset = UNSET
    search_result_relevance_score: str | Unset = UNSET
    search_result_engagement_score: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        elasticsearch_query = self.elasticsearch_query

        is_from_cache = self.is_from_cache

        index_name = self.index_name

        is_terminated_early = self.is_terminated_early

        is_force_termination_enabled_by_request = self.is_force_termination_enabled_by_request

        search_result_data_source = self.search_result_data_source

        search_result_relevance_score = self.search_result_relevance_score

        search_result_engagement_score = self.search_result_engagement_score

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if elasticsearch_query is not UNSET:
            field_dict["elasticsearchQuery"] = elasticsearch_query
        if is_from_cache is not UNSET:
            field_dict["isFromCache"] = is_from_cache
        if index_name is not UNSET:
            field_dict["indexName"] = index_name
        if is_terminated_early is not UNSET:
            field_dict["isTerminatedEarly"] = is_terminated_early
        if is_force_termination_enabled_by_request is not UNSET:
            field_dict["isForceTerminationEnabledByRequest"] = is_force_termination_enabled_by_request
        if search_result_data_source is not UNSET:
            field_dict["searchResultDataSource"] = search_result_data_source
        if search_result_relevance_score is not UNSET:
            field_dict["searchResultRelevanceScore"] = search_result_relevance_score
        if search_result_engagement_score is not UNSET:
            field_dict["searchResultEngagementScore"] = search_result_engagement_score

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        elasticsearch_query = d.pop("elasticsearchQuery", UNSET)

        is_from_cache = d.pop("isFromCache", UNSET)

        index_name = d.pop("indexName", UNSET)

        is_terminated_early = d.pop("isTerminatedEarly", UNSET)

        is_force_termination_enabled_by_request = d.pop("isForceTerminationEnabledByRequest", UNSET)

        search_result_data_source = d.pop("searchResultDataSource", UNSET)

        search_result_relevance_score = d.pop("searchResultRelevanceScore", UNSET)

        search_result_engagement_score = d.pop("searchResultEngagementScore", UNSET)

        roblox_catalog_api_elasticsearch_debug_info = cls(
            elasticsearch_query=elasticsearch_query,
            is_from_cache=is_from_cache,
            index_name=index_name,
            is_terminated_early=is_terminated_early,
            is_force_termination_enabled_by_request=is_force_termination_enabled_by_request,
            search_result_data_source=search_result_data_source,
            search_result_relevance_score=search_result_relevance_score,
            search_result_engagement_score=search_result_engagement_score,
        )

        return roblox_catalog_api_elasticsearch_debug_info
