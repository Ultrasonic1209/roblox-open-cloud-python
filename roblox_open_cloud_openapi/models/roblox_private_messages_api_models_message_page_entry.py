from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxPrivateMessagesApiModelsMessagePageEntry")


@_attrs_define
class RobloxPrivateMessagesApiModelsMessagePageEntry:
    """A single numbered page in the cursor-mode page window. Roblox.PrivateMessages.Api.Models.MessagePageEntry.PageToken
    is an opaque
    token that fetches that page; clients echo it back as the `pageToken` query param.

        Attributes:
            page_number (int | Unset):
            page_token (str | Unset):
    """

    page_number: int | Unset = UNSET
    page_token: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        page_number = self.page_number

        page_token = self.page_token

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if page_number is not UNSET:
            field_dict["pageNumber"] = page_number
        if page_token is not UNSET:
            field_dict["pageToken"] = page_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        page_number = d.pop("pageNumber", UNSET)

        page_token = d.pop("pageToken", UNSET)

        roblox_private_messages_api_models_message_page_entry = cls(
            page_number=page_number,
            page_token=page_token,
        )

        return roblox_private_messages_api_models_message_page_entry
