from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_private_messages_api_models_message_details_response import (
        RobloxPrivateMessagesApiModelsMessageDetailsResponse,
    )


T = TypeVar("T", bound="RobloxPrivateMessagesApiModelsGetMessagesResponse")


@_attrs_define
class RobloxPrivateMessagesApiModelsGetMessagesResponse:
    """
    Attributes:
        collection (list[RobloxPrivateMessagesApiModelsMessageDetailsResponse] | Unset):
        total_collection_size (int | Unset):
        total_pages (int | Unset):
        page_number (int | Unset):
    """

    collection: list[RobloxPrivateMessagesApiModelsMessageDetailsResponse] | Unset = UNSET
    total_collection_size: int | Unset = UNSET
    total_pages: int | Unset = UNSET
    page_number: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        collection: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.collection, Unset):
            collection = []
            for collection_item_data in self.collection:
                collection_item = collection_item_data.to_dict()
                collection.append(collection_item)

        total_collection_size = self.total_collection_size

        total_pages = self.total_pages

        page_number = self.page_number

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if collection is not UNSET:
            field_dict["collection"] = collection
        if total_collection_size is not UNSET:
            field_dict["totalCollectionSize"] = total_collection_size
        if total_pages is not UNSET:
            field_dict["totalPages"] = total_pages
        if page_number is not UNSET:
            field_dict["pageNumber"] = page_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_private_messages_api_models_message_details_response import (
            RobloxPrivateMessagesApiModelsMessageDetailsResponse,
        )

        d = dict(src_dict)
        _collection = d.pop("collection", UNSET)
        collection: list[RobloxPrivateMessagesApiModelsMessageDetailsResponse] | Unset = UNSET
        if _collection is not UNSET:
            collection = []
            for collection_item_data in _collection:
                collection_item = RobloxPrivateMessagesApiModelsMessageDetailsResponse.from_dict(collection_item_data)

                collection.append(collection_item)

        total_collection_size = d.pop("totalCollectionSize", UNSET)

        total_pages = d.pop("totalPages", UNSET)

        page_number = d.pop("pageNumber", UNSET)

        roblox_private_messages_api_models_get_messages_response = cls(
            collection=collection,
            total_collection_size=total_collection_size,
            total_pages=total_pages,
            page_number=page_number,
        )

        return roblox_private_messages_api_models_get_messages_response
