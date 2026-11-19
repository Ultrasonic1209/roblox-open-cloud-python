from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.roblox_private_messages_api_models_message_details_response import (
        RobloxPrivateMessagesApiModelsMessageDetailsResponse,
    )
    from ..models.roblox_private_messages_api_models_message_page_entry import (
        RobloxPrivateMessagesApiModelsMessagePageEntry,
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
        page_window (list[RobloxPrivateMessagesApiModelsMessagePageEntry] | Unset): Numbered page window centered on the
            current page. Populated only in cursor mode. Each entry
            carries an opaque Roblox.PrivateMessages.Api.Models.MessagePageEntry.PageToken the client echoes back to
            navigate.
        first_page_token (str | Unset): Opaque token for the first page. Populated only in cursor mode; backs the "first
            page" control.
        has_more (bool | Unset): Whether a next page exists. Populated only in cursor mode.
    """

    collection: list[RobloxPrivateMessagesApiModelsMessageDetailsResponse] | Unset = UNSET
    total_collection_size: int | Unset = UNSET
    total_pages: int | Unset = UNSET
    page_number: int | Unset = UNSET
    page_window: list[RobloxPrivateMessagesApiModelsMessagePageEntry] | Unset = UNSET
    first_page_token: str | Unset = UNSET
    has_more: bool | Unset = UNSET

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

        page_window: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.page_window, Unset):
            page_window = []
            for page_window_item_data in self.page_window:
                page_window_item = page_window_item_data.to_dict()
                page_window.append(page_window_item)

        first_page_token = self.first_page_token

        has_more = self.has_more

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
        if page_window is not UNSET:
            field_dict["pageWindow"] = page_window
        if first_page_token is not UNSET:
            field_dict["firstPageToken"] = first_page_token
        if has_more is not UNSET:
            field_dict["hasMore"] = has_more

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roblox_private_messages_api_models_message_details_response import (
            RobloxPrivateMessagesApiModelsMessageDetailsResponse,  # noqa: PLC0415
        )
        from ..models.roblox_private_messages_api_models_message_page_entry import (
            RobloxPrivateMessagesApiModelsMessagePageEntry,  # noqa: PLC0415
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

        _page_window = d.pop("pageWindow", UNSET)
        page_window: list[RobloxPrivateMessagesApiModelsMessagePageEntry] | Unset = UNSET
        if _page_window is not UNSET:
            page_window = []
            for page_window_item_data in _page_window:
                page_window_item = RobloxPrivateMessagesApiModelsMessagePageEntry.from_dict(page_window_item_data)

                page_window.append(page_window_item)

        first_page_token = d.pop("firstPageToken", UNSET)

        has_more = d.pop("hasMore", UNSET)

        roblox_private_messages_api_models_get_messages_response = cls(
            collection=collection,
            total_collection_size=total_collection_size,
            total_pages=total_pages,
            page_number=page_number,
            page_window=page_window,
            first_page_token=first_page_token,
            has_more=has_more,
        )

        return roblox_private_messages_api_models_get_messages_response
