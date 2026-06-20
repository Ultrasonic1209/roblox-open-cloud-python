from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.roblox_catalog_api_topic_request_model_gender_type import RobloxCatalogApiTopicRequestModelGenderType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_marketplace_topic_discovery_topic_discovery_service_v1_beta_1_avatar_item import (
        RobloxMarketplaceTopicDiscoveryTopicDiscoveryServiceV1Beta1AvatarItem,
    )


T = TypeVar("T", bound="RobloxCatalogApiTopicRequestModel")


@_attrs_define
class RobloxCatalogApiTopicRequestModel:
    """
    Attributes:
        items (list[RobloxMarketplaceTopicDiscoveryTopicDiscoveryServiceV1Beta1AvatarItem] | Unset):
        select_topics (list[str] | Unset):
        input_query (str | Unset):
        max_result (int | Unset): Maximum number of topic results returned from the server.
        gender_type (RobloxCatalogApiTopicRequestModelGenderType | Unset):  ['Unknown' = 1, 'Male' = 2, 'Female' = 3]
    """

    items: list[RobloxMarketplaceTopicDiscoveryTopicDiscoveryServiceV1Beta1AvatarItem] | Unset = UNSET
    select_topics: list[str] | Unset = UNSET
    input_query: str | Unset = UNSET
    max_result: int | Unset = UNSET
    gender_type: RobloxCatalogApiTopicRequestModelGenderType | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        select_topics: list[str] | Unset = UNSET
        if not isinstance(self.select_topics, Unset):
            select_topics = self.select_topics

        input_query = self.input_query

        max_result = self.max_result

        gender_type: int | Unset = UNSET
        if not isinstance(self.gender_type, Unset):
            gender_type = self.gender_type.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if items is not UNSET:
            field_dict["items"] = items
        if select_topics is not UNSET:
            field_dict["selectTopics"] = select_topics
        if input_query is not UNSET:
            field_dict["inputQuery"] = input_query
        if max_result is not UNSET:
            field_dict["maxResult"] = max_result
        if gender_type is not UNSET:
            field_dict["genderType"] = gender_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_marketplace_topic_discovery_topic_discovery_service_v1_beta_1_avatar_item import (
            RobloxMarketplaceTopicDiscoveryTopicDiscoveryServiceV1Beta1AvatarItem,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _items = d.pop("items", UNSET)
        items: list[RobloxMarketplaceTopicDiscoveryTopicDiscoveryServiceV1Beta1AvatarItem] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = RobloxMarketplaceTopicDiscoveryTopicDiscoveryServiceV1Beta1AvatarItem.from_dict(
                    items_item_data
                )

                items.append(items_item)

        select_topics = cast(list[str], d.pop("selectTopics", UNSET))

        input_query = d.pop("inputQuery", UNSET)

        max_result = d.pop("maxResult", UNSET)

        _gender_type = d.pop("genderType", UNSET)
        gender_type: RobloxCatalogApiTopicRequestModelGenderType | Unset
        if isinstance(_gender_type, Unset):
            gender_type = UNSET
        else:
            gender_type = RobloxCatalogApiTopicRequestModelGenderType(_gender_type)

        roblox_catalog_api_topic_request_model = cls(
            items=items,
            select_topics=select_topics,
            input_query=input_query,
            max_result=max_result,
            gender_type=gender_type,
        )

        return roblox_catalog_api_topic_request_model
