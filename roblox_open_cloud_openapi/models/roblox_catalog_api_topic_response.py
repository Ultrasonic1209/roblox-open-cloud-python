from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_catalog_api_topic_model import RobloxCatalogApiTopicModel
    from ..models.roblox_marketplace_topic_discovery_topic_discovery_service_v1_beta_1_error import (
        RobloxMarketplaceTopicDiscoveryTopicDiscoveryServiceV1Beta1Error,
    )


T = TypeVar("T", bound="RobloxCatalogApiTopicResponse")


@_attrs_define
class RobloxCatalogApiTopicResponse:
    """
    Attributes:
        topics (list[RobloxCatalogApiTopicModel] | Unset):
        error (RobloxMarketplaceTopicDiscoveryTopicDiscoveryServiceV1Beta1Error | Unset):
    """

    topics: list[RobloxCatalogApiTopicModel] | Unset = UNSET
    error: RobloxMarketplaceTopicDiscoveryTopicDiscoveryServiceV1Beta1Error | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        topics: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.topics, Unset):
            topics = []
            for topics_item_data in self.topics:
                topics_item = topics_item_data.to_dict()
                topics.append(topics_item)

        error: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if topics is not UNSET:
            field_dict["topics"] = topics
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_catalog_api_topic_model import RobloxCatalogApiTopicModel
        from ..models.roblox_marketplace_topic_discovery_topic_discovery_service_v1_beta_1_error import (
            RobloxMarketplaceTopicDiscoveryTopicDiscoveryServiceV1Beta1Error,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _topics = d.pop("topics", UNSET)
        topics: list[RobloxCatalogApiTopicModel] | Unset = UNSET
        if _topics is not UNSET:
            topics = []
            for topics_item_data in _topics:
                topics_item = RobloxCatalogApiTopicModel.from_dict(topics_item_data)

                topics.append(topics_item)

        _error = d.pop("error", UNSET)
        error: RobloxMarketplaceTopicDiscoveryTopicDiscoveryServiceV1Beta1Error | Unset
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = RobloxMarketplaceTopicDiscoveryTopicDiscoveryServiceV1Beta1Error.from_dict(_error)

        roblox_catalog_api_topic_response = cls(
            topics=topics,
            error=error,
        )

        return roblox_catalog_api_topic_response
