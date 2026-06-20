from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RobloxPrivateMessagesApiModelsAnnouncementsMetadataResponse")


@_attrs_define
class RobloxPrivateMessagesApiModelsAnnouncementsMetadataResponse:
    """A message details response.

    Attributes:
        num_of_announcements (int | Unset): Number of incoming news
    """

    num_of_announcements: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        num_of_announcements = self.num_of_announcements

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if num_of_announcements is not UNSET:
            field_dict["numOfAnnouncements"] = num_of_announcements

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict) if isinstance(src_dict, Mapping) else {}
        num_of_announcements = d.pop("numOfAnnouncements", UNSET)

        roblox_private_messages_api_models_announcements_metadata_response = cls(
            num_of_announcements=num_of_announcements,
        )

        return roblox_private_messages_api_models_announcements_metadata_response
