from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_private_messages_api_models_announcements_details_response import (
        RobloxPrivateMessagesApiModelsAnnouncementsDetailsResponse,
    )


T = TypeVar("T", bound="RobloxPrivateMessagesApiModelsGetAnnouncementsResponse")


@_attrs_define
class RobloxPrivateMessagesApiModelsGetAnnouncementsResponse:
    """
    Attributes:
        collection (list[RobloxPrivateMessagesApiModelsAnnouncementsDetailsResponse] | Unset):
        total_collection_size (int | Unset):
    """

    collection: list[RobloxPrivateMessagesApiModelsAnnouncementsDetailsResponse] | Unset = UNSET
    total_collection_size: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        collection: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.collection, Unset):
            collection = []
            for collection_item_data in self.collection:
                collection_item = collection_item_data.to_dict()
                collection.append(collection_item)

        total_collection_size = self.total_collection_size

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if collection is not UNSET:
            field_dict["collection"] = collection
        if total_collection_size is not UNSET:
            field_dict["totalCollectionSize"] = total_collection_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_private_messages_api_models_announcements_details_response import (
            RobloxPrivateMessagesApiModelsAnnouncementsDetailsResponse,
        )

        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        _collection = d.pop("collection", UNSET)
        collection: list[RobloxPrivateMessagesApiModelsAnnouncementsDetailsResponse] | Unset = UNSET
        if _collection is not UNSET:
            collection = []
            for collection_item_data in _collection:
                collection_item = RobloxPrivateMessagesApiModelsAnnouncementsDetailsResponse.from_dict(
                    collection_item_data
                )

                collection.append(collection_item)

        total_collection_size = d.pop("totalCollectionSize", UNSET)

        roblox_private_messages_api_models_get_announcements_response = cls(
            collection=collection,
            total_collection_size=total_collection_size,
        )

        return roblox_private_messages_api_models_get_announcements_response
